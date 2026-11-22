// Export the same typed member descriptors used by Studio's property browser.
#include "frog_native_engine/ApplicationControlSchema.hpp"
#include "frog_native_engine/WidgetCatalog.hpp"
#include <algorithm>
#include <filesystem>
#include <fstream>
#include <set>
#include <stdexcept>

namespace fs = std::filesystem;
using namespace frog::native_engine;

static std::string cell(std::string text) {
    std::string result;
    for (char c : text) {
        if (c == '|') result += "\\|";
        else if (c == '\n' || c == '\r') result += ' ';
        else result += c;
    }
    return result;
}

static std::string typeName(const binding::TypeRef& type) {
    return type.known() ? "`" + cell(type.canonical()) + "`" : "target-dependent";
}

static std::string signature(const ApplicationControlMemberDescriptor& member) {
    if (member.kind == ApplicationControlMemberKind::Property) return typeName(member.type);
    std::string result;
    for (const auto& p : member.parameters) {
        if (!result.empty()) result += ", ";
        result += p.direction == ApplicationControlParameterDirection::In ? "in " :
                  p.direction == ApplicationControlParameterDirection::Out ? "out " : "in/out ";
        result += cell(p.label) + " (`" + cell(p.id) + "`, " + typeName(p.type) + ")";
        if (!p.required) result += " optional";
        if (p.defaultValue) result += " = `" + cell(*p.defaultValue) + "`";
    }
    if (result.empty()) result = "No parameters";
    result += " → ";
    return result + (member.resultType ? typeName(*member.resultType) : "void");
}

int main(int argc, char** argv) {
    if (argc != 2) return 2;
    const fs::path directory(argv[1]);
    fs::create_directories(directory);
    std::ofstream index(directory / "index.md", std::ios::binary);
    index.exceptions(std::ios::failbit | std::ios::badbit);
    index << "# Object references by class\n\n"
          << "Choose the class carried by the reference wire. Each page gives the menu path, saved member ID, "
             "typed connection or method signature, and the actions advertised by the catalog. "
             "The connected object's strict value type specializes Value and related ports. "
             "Array Element follows the configured element template recursively. Use Index Array on the array value to access an individual cell.\n\n"
          << "[Working with references](../using-object-references.md)\n\n"
          << "| Reference class | Properties | Methods |\n| --- | ---: | ---: |\n";
    const auto classes = applicationControlReferenceClasses();
    for (const auto& id : std::set<std::string>(classes.begin(), classes.end())) {
        if (id.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-") != std::string::npos)
            throw std::runtime_error("Invalid catalog class ID");
        const auto* entry = findWidgetCatalogEntryByClassId(id);
        const auto type = entry ? binding::parseType(entry->valueType).type : binding::TypeRef{};
        const auto members = applicationControlMembers(id, type);
        const auto methods = std::count_if(members.begin(), members.end(), [](const auto& m) {
            return m.kind == ApplicationControlMemberKind::Method;
        });
        const auto label = applicationControlClassLabel(id, type);
        index << "| [" << cell(label) << " (`" << id << "`)](" << id << ".md) | " << members.size() - methods
              << " | " << methods << " |\n";
        std::ofstream page(directory / (id + ".md"), std::ios::binary);
        page.exceptions(std::ios::failbit | std::ios::badbit);
        page << "# " << cell(label) << "\n\nReference class `" << id << "`. "
             << "[All classes](index.md) · [How to use Property and Invoke Nodes](../using-object-references.md)\n\n"
             << "Catalog value schema for this listing: " << typeName(type) << ". A strict reference can supply a different schema.\n\n";
        for (const auto kind : {ApplicationControlMemberKind::Property, ApplicationControlMemberKind::Method}) {
            page << (kind == ApplicationControlMemberKind::Property ? "## Properties" : "## Methods") << "\n\n";
            if (std::none_of(members.begin(), members.end(), [=](const auto& m) { return m.kind == kind; })) {
                page << "No entries declared for this class.\n";
                if (kind == ApplicationControlMemberKind::Property) page << '\n';
                continue;
            }
            page << "| Menu path | Saved ID | Connection | Access | Catalog availability |\n| --- | --- | --- | --- | --- |\n";
            for (const auto& m : members) {
                if (m.kind != kind) continue;
                std::string path;
                for (const auto& part : m.menuPath) path += cell(part) + " › ";
                const std::string access = kind == ApplicationControlMemberKind::Method ? "Invoke" :
                    m.readable && m.writable ? "Read / Write" : m.readable ? "Read" : m.writable ? "Write" : "—";
                page << "| " << path << cell(m.label) << " | `" << cell(m.id) << "` | " << signature(m) << " | "
                     << access << " | " << (m.authoringAvailable ? "Editor" : "—");
                if (m.runtimeAvailable) page << " · Run advertised";
                if (!m.unavailableReason.empty()) page << " · " << cell(m.unavailableReason);
                if (!m.help.empty() && m.help != "Private document authoring provider; runtime access is unavailable." &&
                    m.help != "The descriptor configures a typed operation; target capabilities are checked separately. Runtime access requires its own provider." &&
                    m.help != "No runtime or execution side effect is implied by configuring this method.")
                    page << " · " << cell(m.help);
                page << " |\n";
            }
            if (kind == ApplicationControlMemberKind::Property) page << '\n';
        }
    }
}
