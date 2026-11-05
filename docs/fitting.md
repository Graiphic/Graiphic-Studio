# Fitting — ajustements réels et intervalles

Mathematics → Fitting contient13 fonctions ; Advanced Curve Fitting en contient15.
Une fonction de palette peut avoir plusieurs variantes aux signatures distinctes.
Le choix enregistré détermine les ports et l’opération native ; aucun modèle ne
remplace silencieusement un autre. Les vecteurs sont des Arrays DBL de rang1,
les matrices des Arrays de rang2. Les promotions réelles sont explicites ; aucune
partie imaginaire n’est supprimée et aucun cluster n’est transformé en texte.
Les modèles, bornes, contraintes et erreurs conservent leurs structures.

## Conventions de calcul GS et limites de compatibilité NI

- Méthodes0 LS,1 LAR,2 Bisquare. LAR utilise une réévaluation IRLS absolue ;
  Bisquare utilise Tukey4.685 et MAD/0.67448975. Ces constantes sont des choix GS,
  pas une identité d’implémentation interne NI certifiée.
- Poids négatifs : valeur absolue. Les poids individuels nuls sont admis ; un
  ensemble sans poids positif est refusé. Les familles classiques demandent les
  longueurs contractuelles ; non linéaire : poids courts complétés par1, longs
  tronqués. Le résidu LS est Σ|w|r²/N, LAR Σ|w||r|/N, N longueur physique de Y.
- Covariance publiée : courbure inv(JᵀWJ), sans multiplication par la variance.
  Paramètres fixés réinsérés avec covariance nulle. General Linear selector0
  calcule,1 omet (matrice vide) : codes et défaut GS, pas certifiés NI.
- Intervalles : courbure × SSE/(nombre de poids positifs−p), variance appliquée
  une seule fois. Quantile Student dépendant des degrés de liberté, pas1.96 fixe.
  Prediction ajoute une variance future unitaire ; Confidence seule produit les
  deltas de paramètres. Hypothèses locales LS, modèle identifiable, paramètres
  libres et absence de contrainte active : pas de bande simultanée universelle.
- Algorithmes linéaires0 SVD strict,1 Givens colonnes,2 Givens lignes,
  3 Householder,4 équations normales LU,5 équations normales Cholesky,
  6 SVD à norme minimale. Une option indisponible doit être refusée, pas ignorée.
- Spline cubique naturelle : pΣw(f−Y)²+(1−p)∫smoothness(f″)² ; p0 droite LS,
  p1 interpolation. Choix auto GS :1/(1+mean(ΔX)³). B-spline : nœuds uniformes
  clampés, bases Cox/de Boor et paramétrisation0 uniforme,1 corde,2 centripète.
  Ce choix ne certifie pas les détails algorithmiques NI.
- Termination par défaut GS : max_iteration500, tolerance1e−8. Une limite atteinte
  doit rester un diagnostic, pas un succès silencieux. Les estimations initiales
  NaN et limites infinies sont des valeurs typées explicites, pas des observations
  non finies acceptées généralement.

## Modèles et structures

`model_description = cluster<model:string,parameters:array<string>,x:string>`.
Les noms de paramètres sont ordonnés ; le champ NI « Parameters » est mappé au
champ GS stable `parameters`. La puissance d’une formule s’écrit `^`.
`termination = cluster<max_iteration:i32,tolerance:f64>`.
Les contraintes polynomiales sont un tableau de
`cluster<order:i32,coefficient:f64>`, jamais une chaîne.
Les erreurs non linéaires sont `cluster<status:bool,code:i32,source:string>`.
Les autres diagnostics I32 ne deviennent pas artificiellement ce cluster.

Le modèle fonction est une référence stricte vers un FROG natif préparé :

```
ref<connectivity.document.strict,cluster<
  in_x:f64,in_parameters:array<f64>,in_data:variant,
  out_value:f64,out_gradient:array<f64>,
  out_diagnostic:cluster<status:bool,code:i32,source:string>>>
```

Une référence n’est pas une formule et ne passe pas par un interprète historique.
Le raccordement, l’admission et l’exécution native de ce callback doivent être
qualifiés séparément ; une signature déclarée n’est pas une preuve d’exécution.

## Inventaire des28 fonctions

| # | Fonction / ID | Variantes | Opération |
| --- | --- | --- | --- |
| F01 | **Linear Fit** `math.fitting.linear_fit` | default | Ajuste une droite a·x+b avec poids, méthodes LS/LAR/Bisquare et bornes réelles. |
| F02 | **Exp Fit** `math.fitting.exponential_fit` | default | Ajuste a·exp(b·x)+c ; l’offset est fixé à zéro par défaut. b est le coefficient exponentiel. |
| F03 | **Power Fit** `math.fitting.power_fit` | default | Ajuste a·xᵇ+c ; l’offset est fixé à zéro par défaut. Le domaine réel est vérifié sans remplacer X par \|X\|. |
| F04 | **Gauss Peak Fit** `math.fitting.gaussian_peak_fit` | default | Ajuste un pic gaussien : amplitude, centre, écart-type et offset. NaN dans l’estimation initiale demande une initialisation automatique. |
| F05 | **Logarithm Fit** `math.fitting.logarithm_fit` | default | Ajuste amplitude·log_base(scale·x), avec scale multiplicatif et base e par défaut. |
| F06 | **Polynomial Fit** `math.fitting.polynomial_fit` | default | Ajuste les coefficients en puissances croissantes, avec contraintes et algorithme réellement sélectionné. |
| F07 | **Gen. Linear Fit** `math.fitting.general_linear_fit` | default | Ajuste Y≈H·c sans ajouter de colonne constante ; conserve coefficients, covariance et poids robustes. |
| F08 | **Cubic Spline Fit** `math.fitting.cubic_spline_fit` | default | Spline cubique lissante : balance0 donne une droite LS ; balance1 interpole ; smoothness agit par intervalle. |
| F09 | **B-Spline Fit** `math.fitting.b_spline_fit` | xy, nd | B-spline paramétrique XY ou nD ; les points nD sont les lignes [n,D] et les deux coordonnées XY peuvent changer. |
| F10 | **Fit on a Sphere** `math.fitting.fitting_on_sphere` | default | Ajuste une sphère3D ; centre = un vecteur DBL de trois composantes, rayon DBL. Les nuages non identifiables sont diagnostiqués. |
| F11 | **Nonlinear Curve Fit** `math.fitting.nonlinear_curve_fit` | function, formula | Ajustement LM par véritable référence de modèle FROG natif ou par formule structurée ; les signatures sont distinctes. |
| F12 | **Constrained Nonlinear Curve Fit** `math.fitting.constrained_nonlinear_curve_fit` | lm, trdl | Ajustement borné LM ou dogleg trust-region ; les bornes agissent pendant l’optimisation. |
| F13 | **Curve Fit** `math.fitting.curve_fit` | linear, quadratic, spline, polynomial, general_linear, nonlinear | Nœud configurable : linéaire, quadratique, spline, polynôme, linéaire général ou formule non linéaire. La variante sauvegardée définit les terminaux. |
| A01 | **Remove Outlier** `math.fitting.remove_outliers` | range, index | Retire les observations désignées par plage ou indices, en conservant les associations X/Y/poids. |
| A02 | **Goodness of Fit** `math.fitting.goodness_of_fit` | default | Mesure SSE, R² et RMSE à partir des prédictions fournies, sans réajuster les paramètres. |
| A03 | **Nonlinear Curve Fit Intervals** `math.fitting.nonlinear_curve_fit_intervals` | function | Intervalles de confiance à paramètres fournis, par modèle FROG natif ; aucun nouvel ajustement caché. |
| A04 | **Linear Fit Intvl** `math.fitting.linear_fit_intervals` | confidence, prediction | Intervalles de confiance ou prédiction de la droite fournie ; seuls ceux de confiance retournent les deltas de paramètres. |
| A05 | **Exp Fit Intvl** `math.fitting.exponential_fit_intervals` | confidence, prediction | Intervalles de a·exp(bx) à paramètres fournis, sans offset ; confiance et prédiction distinctes. |
| A06 | **Power Fit Intvl** `math.fitting.power_fit_intervals` | confidence, prediction | Intervalles de a·xᵇ à paramètres fournis, sans offset ; confiance et prédiction distinctes. |
| A07 | **Gauss Fit Intvl** `math.fitting.gaussian_fit_intervals` | confidence, prediction | Intervalles du pic gaussien sans offset, à amplitude/centre/écart-type fournis. |
| A08 | **Log Fit Intvl** `math.fitting.logarithm_fit_intervals` | confidence, prediction | Intervalles de amplitude·log_base(scale·x), sans confondre scale et intercept. |
| A09 | **Poly Fit Intvl** `math.fitting.polynomial_fit_intervals` | confidence, prediction | Intervalles du polynôme fourni en coefficients croissants ; aucun réajustement. |
| A10 | **Linear Fit Coef** `math.fitting.linear_fit_coefficients` | default | Estime uniquement pente et intercept ; ni courbe, ni résidu, ni bornes supplémentaires. |
| A11 | **Exp Fit Coef** `math.fitting.exponential_fit_coefficients` | default | Estime amplitude/damping ; refine=false utilise l’espace logarithmique, refine=true affine dans l’espace Y. |
| A12 | **Power Fit Coef** `math.fitting.power_fit_coefficients` | default | Estime amplitude/puissance sans offset ni option refine inventée. |
| A13 | **Gauss Fit Coef** `math.fitting.gaussian_fit_coefficients` | default | Estime amplitude/centre/écart-type ; estimation initiale exactement à trois champs, sans offset. |
| A14 | **Log Fit Coef** `math.fitting.logarithm_fit_coefficients` | default | Estime amplitude et scale multiplicatif du logarithme ; base e par défaut. |
| A15 | **Poly Fit Coef** `math.fitting.polynomial_fit_coefficients` | default | Estime uniquement les coefficients croissants avec contraintes et algorithme effectifs. |

## Connecteurs par variante

Les entrées requises sont en gras. Les valeurs dimensionnelles automatiques ne
s’appliquent qu’à un port non câblé. Un tableau vide câblé n’est pas universellement
une demande de défaut. Le contrat mathématique vérifie valeurs et dimensions.

### Linear Fit

Fits a*x+b with weighted LS, LAR or Bisquare and actual parameter bounds; equal bounds fix a parameter. Residue is weighted mean squared error for LS/Bisquare and mean absolute residual for LAR.

**default** — `frog.studio.math.fitting.linear_fit.owned.v1`

Entrées : **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`, `parameter_bounds: cluster<slope_min:f64,slope_max:f64,intercept_min:f64,intercept_max:f64>`.

Sorties : `best_fit: array<f64>`, `slope: f64`, `intercept: f64`, `error: i32`, `residue: f64`.

Défauts non câblés : `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`; `parameter_bounds={"slope_min":"-Infinity","slope_max":"Infinity","intercept_min":"-Infinity","intercept_max":"Infinity"} (NI_fixed_model_bounds_or_GS_empty_nonlinear_limits)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/linear-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Exp Fit

Fits a*exp(b*x)+c in observation space with actual bounds. Offset bounds default to zero; free them explicitly for a three-parameter fit. Damping is b, not a time constant.

**default** — `frog.studio.math.fitting.exponential_fit.owned.v1`

Entrées : **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`, `parameter_bounds: cluster<amp_min:f64,amp_max:f64,damping_min:f64,damping_max:f64,offset_min:f64,offset_max:f64>`.

Sorties : `best_fit: array<f64>`, `amplitude: f64`, `damping: f64`, `offset: f64`, `error: i32`, `residue: f64`.

Défauts non câblés : `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`; `parameter_bounds={"amp_min":"-Infinity","amp_max":"Infinity","damping_min":"-Infinity","damping_max":"Infinity","offset_min":0,"offset_max":0} (NI_fixed_model_bounds_or_GS_empty_nonlinear_limits)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/exponential-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Power Fit

Fits a*x^b+c with actual parameter bounds. Offset defaults fixed zero. Real power domain is checked without abs(X) substitution.

**default** — `frog.studio.math.fitting.power_fit.owned.v1`

Entrées : **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`, `parameter_bounds: cluster<amp_min:f64,amp_max:f64,power_min:f64,power_max:f64,offset_min:f64,offset_max:f64>`.

Sorties : `best_fit: array<f64>`, `amplitude: f64`, `power: f64`, `offset: f64`, `error: i32`, `residue: f64`.

Défauts non câblés : `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`; `parameter_bounds={"amp_min":"-Infinity","amp_max":"Infinity","power_min":"-Infinity","power_max":"Infinity","offset_min":0,"offset_max":0} (NI_fixed_model_bounds_or_GS_empty_nonlinear_limits)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/power-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Gauss Peak Fit

Fits a*exp(-(x-center)^2/(2*standard_deviation^2))+offset. Amplitude is peak height, not area. Typed NaN initial guesses request automatic initialization; offset defaults fixed zero.

**default** — `frog.studio.math.fitting.gaussian_peak_fit.owned.v1`

Entrées : `initial_guess: cluster<amplitude:f64,center:f64,standard_deviation:f64,offset:f64>`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`, `parameter_bounds: cluster<amp_min:f64,amp_max:f64,center_min:f64,center_max:f64,deviation_min:f64,deviation_max:f64,offset_min:f64,offset_max:f64>`.

Sorties : `offset: f64`, `best_fit: array<f64>`, `amplitude: f64`, `center: f64`, `standard_deviation: f64`, `error: i32`, `residue: f64`.

Défauts non câblés : `initial_guess={"amplitude":"NaN","center":"NaN","standard_deviation":"NaN","offset":"NaN"} (GS_automatic_using_NI_NaN_semantics)`; `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`; `parameter_bounds={"amp_min":"-Infinity","amp_max":"Infinity","center_min":"-Infinity","center_max":"Infinity","deviation_min":"-Infinity","deviation_max":"Infinity","offset_min":0,"offset_max":0} (NI_fixed_model_bounds_or_GS_empty_nonlinear_limits)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/gaussian-peak-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Logarithm Fit

Fits amplitude*log_base(scale*x), with multiplicative scale and default base e. Scale is not the intercept of a log-linear intermediate model; invalid bases/domains and nonidentifiability are diagnosed.

**default** — `frog.studio.math.fitting.logarithm_fit.owned.v1`

Entrées : `base: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`, `parameter_bounds: cluster<amp_min:f64,amp_max:f64,scale_min:f64,scale_max:f64>`.

Sorties : `best_fit: array<f64>`, `amplitude: f64`, `scale: f64`, `error: i32`, `residue: f64`.

Défauts non câblés : `base=2.718281828459045 (NI)`; `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`; `parameter_bounds={"amp_min":"-Infinity","amp_max":"Infinity","scale_min":"-Infinity","scale_max":"Infinity"} (NI_fixed_model_bounds_or_GS_empty_nonlinear_limits)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/logarithm-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Polynomial Fit

Fits ascending coefficients c0+c1*x+...+cd*x^d with fixed coefficient constraints, weighted criterion and the selected algorithm. Degree defaults2; degree26 has the documented warning result, not silent success.

**default** — `frog.studio.math.fitting.polynomial_fit.owned.v1`

Entrées : `coefficient_constraints: array<cluster<order:i32,coefficient:f64>>`, `polynomial_order: i32`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`, `algorithm: u16`.

Sorties : `best_fit: array<f64>`, `coefficients: array<f64>`, `error: i32`, `residue: f64`.

Défauts non câblés : `coefficient_constraints=[] (GS_empty_no_constraints)`; `polynomial_order=2 (NI)`; `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`; `algorithm=0 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/general-polynomial-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Gen. Linear Fit

Fits Y=H*c, linear in the supplied H columns; no implicit intercept is added. Returns coefficients, fitted observations, optional curvature covariance and actual robust output weights.

**default** — `frog.studio.math.fitting.general_linear_fit.owned.v1`

Entrées : `covariance_selector: u16`, **y: array<f64>**, **h: array<f64,rank=2>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`, `algorithm: u16`.

Sorties : `best_fit: array<f64>`, `coefficients: array<f64>`, `covariance: array<f64,rank=2>`, `weight_out: array<f64>`, `error: i32`, `residue: f64`.

Défauts non câblés : `covariance_selector=0 (GS_0_compute_1_omit_NI_enum_values_not_documented)`; `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`; `algorithm=0 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/general-linear-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Cubic Spline Fit

Fits a natural cubic smoothing spline. Balance0 gives a least-squares line, balance1 interpolation. GS objective is p*sum(w*r^2)+(1-p)*integral(smoothness*(f second derivative)^2). Automatic p=1/(1+mean(deltaX)^3) is a GS choice, not NI-certified.

**default** — `frog.studio.math.fitting.cubic_spline_fit.owned.v1`

Entrées : **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `balance_parameter: f64`, `smoothness: array<f64>`.

Sorties : `best_fit: array<f64>`, `error: i32`.

Défauts non câblés : `weight="ones_length_y" (NI)`; `balance_parameter=-1 (GS_default_auto_NI_auto_outside_range)`; `smoothness="ones_length_n_minus_1" (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/cubic-spline-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### B-Spline Fit

Fits a parametric B-spline, with distinct XY and nD variants. Both fitted coordinates can change. nD observations occupy rows [n,D]. Degree3, control_points10 and centripetal parameterization2 are defaults. GS uses clamped uniform knots and Cox/de Boor bases.

**xy** — `frog.studio.math.fitting.b_spline_fit.xy.owned.v1`

Entrées : `control_points: i32`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `degree: i32`, `parameter_selection: u16`.

Sorties : `best_fit_y: array<f64>`, `best_fit_x: array<f64>`, `error: i32`, `residue: f64`.

Défauts non câblés : `control_points=10 (NI)`; `weight="ones_length_y" (NI)`; `degree=3 (NI)`; `parameter_selection=2 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/1d-b-spline-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**nd** — `frog.studio.math.fitting.b_spline_fit.nd.owned.v1`

Entrées : `control_points: i32`, **data: array<f64,rank=2>**, `weight: array<f64>`, `degree: i32`, `parameter_selection: u16`.

Sorties : `best_fit: array<f64,rank=2>`, `error: i32`, `residue: f64`.

Défauts non câblés : `control_points=10 (NI)`; `weight="ones_length_data_rows" (GS_shape_derived_NI_weight_default)`; `degree=3 (NI)`; `parameter_selection=2 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/nd-b-spline-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Fit on a Sphere

Fits a 3D sphere by the documented algebraic squared-distance objective; center is one DBL vector of length3 and radius is DBL. Coplanar or otherwise nonidentifiable observations are diagnosed; no fabricated residue output.

**default** — `frog.studio.math.fitting.fitting_on_sphere.owned.v1`

Entrées : **x: array<f64>**, **y: array<f64>**, **z: array<f64>**.

Sorties : `center: array<f64>`, `radius: f64`, `error: i32`.

Défauts non câblés : aucun.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/gmath/opti-llb/fitting-on-a-sphere-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Nonlinear Curve Fit

Levenberg-Marquardt fit with distinct native FROG model-reference and structured-formula variants. Formula model contains model String, ordered parameter names and independent-variable name; ^ means power. Only function variant returns number_of_function_calls.

**function** — `frog.studio.math.fitting.nonlinear_curve_fit.function.owned.v1`

Entrées : `data: variant`, **model_reference: ref<connectivity.document.strict,cluster<in_x:f64,in_parameters:array<f64>,in_data:variant,out_value:f64,out_gradient:array<f64>,out_diagnostic:cluster<status:bool,code:i32,source:string>>>**, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **initial_parameters: array<f64>**, `error_in: cluster<status:bool,code:i32,source:string>`, `termination: cluster<max_iteration:i32,tolerance:f64>`.

Sorties : `number_of_function_calls: i32`, `best_fit: array<f64>`, `best_fit_parameters: array<f64>`, `covariance: array<f64,rank=2>`, `error_out: cluster<status:bool,code:i32,source:string>`, `residue: f64`.

Défauts non câblés : `data="empty_variant" (GS)`; `weight="ones_length_y" (NI)`; `error_in={"status":false,"code":0,"source":""} (NI_no_error)`; `termination={"max_iteration":500,"tolerance":1e-08} (GS_defaults_NI_fields_verified_values_not_stated)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/gmath/numericaloptimization/nonlinear-curve-fit-lm-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**formula** — `frog.studio.math.fitting.nonlinear_curve_fit.formula.owned.v1`

Entrées : **initial_parameters: array<f64>**, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **model_description: cluster<model:string,parameters:array<string>,x:string>**, `error_in: cluster<status:bool,code:i32,source:string>`, `termination: cluster<max_iteration:i32,tolerance:f64>`.

Sorties : `best_fit: array<f64>`, `best_fit_parameters: array<f64>`, `covariance: array<f64,rank=2>`, `error_out: cluster<status:bool,code:i32,source:string>`, `residue: f64`.

Défauts non câblés : `weight="ones_length_y" (NI)`; `error_in={"status":false,"code":0,"source":""} (NI_no_error)`; `termination={"max_iteration":500,"tolerance":1e-08} (GS_defaults_NI_fields_verified_values_not_stated)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/gmath/numericaloptimization/nonlinear-curve-fit-lm-formula-string-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Constrained Nonlinear Curve Fit

Bounded nonlinear fit with distinct LM and trust-region dogleg variants. Bounds constrain optimization itself; equal limits fix a parameter. Criterion LS/LAR/Bisquare is independent of the algorithm choice.

**lm** — `frog.studio.math.fitting.constrained_nonlinear_curve_fit.lm.owned.v1`

Entrées : `data: variant`, **model_reference: ref<connectivity.document.strict,cluster<in_x:f64,in_parameters:array<f64>,in_data:variant,out_value:f64,out_gradient:array<f64>,out_diagnostic:cluster<status:bool,code:i32,source:string>>>**, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **initial_parameters: array<f64>**, `error_in: cluster<status:bool,code:i32,source:string>`, `termination: cluster<max_iteration:i32,tolerance:f64>`, `parameter_bounds: cluster<parameter_minimum:array<f64>,parameter_maximum:array<f64>>`, `method: u16`.

Sorties : `number_of_function_calls: i32`, `best_fit: array<f64>`, `best_fit_parameters: array<f64>`, `covariance: array<f64,rank=2>`, `residue: f64`, `error_out: cluster<status:bool,code:i32,source:string>`.

Défauts non câblés : `data="empty_variant" (GS)`; `weight="ones_length_y" (NI)`; `error_in={"status":false,"code":0,"source":""} (NI_no_error)`; `termination={"max_iteration":500,"tolerance":1e-08} (GS_defaults_NI_fields_verified_values_not_stated)`; `parameter_bounds={"parameter_minimum":[],"parameter_maximum":[]} (NI_fixed_model_bounds_or_GS_empty_nonlinear_limits)`; `method=0 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/gmath/numericaloptimization/nonlinear-curve-fit-lm-bound-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**trdl** — `frog.studio.math.fitting.constrained_nonlinear_curve_fit.trdl.owned.v1`

Entrées : `data: variant`, **model_reference: ref<connectivity.document.strict,cluster<in_x:f64,in_parameters:array<f64>,in_data:variant,out_value:f64,out_gradient:array<f64>,out_diagnostic:cluster<status:bool,code:i32,source:string>>>**, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **initial_parameters: array<f64>**, `error_in: cluster<status:bool,code:i32,source:string>`, `termination: cluster<max_iteration:i32,tolerance:f64>`, `parameter_bounds: cluster<parameter_minimum:array<f64>,parameter_maximum:array<f64>>`, `method: u16`.

Sorties : `number_of_function_calls: i32`, `best_fit: array<f64>`, `best_fit_parameters: array<f64>`, `covariance: array<f64,rank=2>`, `residue: f64`, `error_out: cluster<status:bool,code:i32,source:string>`.

Défauts non câblés : `data="empty_variant" (GS)`; `weight="ones_length_y" (NI)`; `error_in={"status":false,"code":0,"source":""} (NI_no_error)`; `termination={"max_iteration":500,"tolerance":1e-08} (GS_defaults_NI_fields_verified_values_not_stated)`; `parameter_bounds={"parameter_minimum":[],"parameter_maximum":[]} (NI_fixed_model_bounds_or_GS_empty_nonlinear_limits)`; `method=0 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/gmath/numericaloptimization/nonlinear-curve-fit-trdl-bound-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Curve Fit

Configurable Curve Fit with six real model variants: linear, quadratic, spline, polynomial, general_linear and nonlinear formula. Reuses specialized numerical services; its connector and native identity follow the saved model. Polynomial defaults order5. Spline has no invented coefficient output.

**linear** — `frog.studio.math.fitting.curve_fit.linear.owned.v1`

Entrées : **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`, `parameter_bounds: cluster<slope_min:f64,slope_max:f64,intercept_min:f64,intercept_max:f64>`, `error_in: cluster<status:bool,code:i32,source:string>`.

Sorties : `best_fit: array<f64>`, `coefficients: array<f64>`, `residue: f64`, `residual: array<f64>`, `error_out: cluster<status:bool,code:i32,source:string>`.

Défauts non câblés : `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`; `parameter_bounds={"slope_min":"-Infinity","slope_max":"Infinity","intercept_min":"-Infinity","intercept_max":"Infinity"} (NI_fixed_model_bounds_or_GS_empty_nonlinear_limits)`; `error_in={"status":false,"code":0,"source":""} (GS_Express_adapter)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/linear-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**quadratic** — `frog.studio.math.fitting.curve_fit.quadratic.owned.v1`

Entrées : `coefficient_constraints: array<cluster<order:i32,coefficient:f64>>`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`, `algorithm: u16`, `error_in: cluster<status:bool,code:i32,source:string>`.

Sorties : `best_fit: array<f64>`, `coefficients: array<f64>`, `residue: f64`, `residual: array<f64>`, `error_out: cluster<status:bool,code:i32,source:string>`.

Défauts non câblés : `coefficient_constraints=[] (GS_empty_no_constraints)`; `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`; `algorithm=0 (NI)`; `error_in={"status":false,"code":0,"source":""} (GS_Express_adapter)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/general-polynomial-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**spline** — `frog.studio.math.fitting.curve_fit.spline.owned.v1`

Entrées : **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `balance_parameter: f64`, `smoothness: array<f64>`, `error_in: cluster<status:bool,code:i32,source:string>`.

Sorties : `best_fit: array<f64>`, `residue: f64`, `residual: array<f64>`, `error_out: cluster<status:bool,code:i32,source:string>`.

Défauts non câblés : `weight="ones_length_y" (NI)`; `balance_parameter=-1 (GS_default_auto_NI_auto_outside_range)`; `smoothness="ones_length_n_minus_1" (NI)`; `error_in={"status":false,"code":0,"source":""} (GS_Express_adapter)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/cubic-spline-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**polynomial** — `frog.studio.math.fitting.curve_fit.polynomial.owned.v1`

Entrées : `coefficient_constraints: array<cluster<order:i32,coefficient:f64>>`, `polynomial_order: i32`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`, `algorithm: u16`, `error_in: cluster<status:bool,code:i32,source:string>`.

Sorties : `best_fit: array<f64>`, `coefficients: array<f64>`, `residue: f64`, `residual: array<f64>`, `error_out: cluster<status:bool,code:i32,source:string>`.

Défauts non câblés : `coefficient_constraints=[] (GS_empty_no_constraints)`; `polynomial_order=5 (NI_Express_default)`; `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`; `algorithm=0 (NI)`; `error_in={"status":false,"code":0,"source":""} (GS_Express_adapter)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/general-polynomial-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**general_linear** — `frog.studio.math.fitting.curve_fit.general_linear.owned.v1`

Entrées : `covariance_selector: u16`, **y: array<f64>**, **h: array<f64,rank=2>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`, `algorithm: u16`, `error_in: cluster<status:bool,code:i32,source:string>`.

Sorties : `best_fit: array<f64>`, `coefficients: array<f64>`, `residue: f64`, `residual: array<f64>`, `error_out: cluster<status:bool,code:i32,source:string>`.

Défauts non câblés : `covariance_selector=0 (GS_0_compute_1_omit_NI_enum_values_not_documented)`; `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`; `algorithm=0 (NI)`; `error_in={"status":false,"code":0,"source":""} (GS_Express_adapter)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/general-linear-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**nonlinear** — `frog.studio.math.fitting.curve_fit.nonlinear.owned.v1`

Entrées : **initial_parameters: array<f64>**, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **model_description: cluster<model:string,parameters:array<string>,x:string>**, `error_in: cluster<status:bool,code:i32,source:string>`, `termination: cluster<max_iteration:i32,tolerance:f64>`.

Sorties : `best_fit: array<f64>`, `coefficients: array<f64>`, `residue: f64`, `residual: array<f64>`, `error_out: cluster<status:bool,code:i32,source:string>`.

Défauts non câblés : `weight="ones_length_y" (NI)`; `error_in={"status":false,"code":0,"source":""} (NI_no_error)`; `termination={"max_iteration":500,"tolerance":1e-08} (GS_defaults_NI_fields_verified_values_not_stated)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/gmath/numericaloptimization/nonlinear-curve-fit-lm-formula-string-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Remove Outlier

Removes designated observations while preserving X/Y/weight association. Range removes boundary and outside points; limits are upper then lower. Index uses explicit zero-based indices. Only Range returns outlier_indices; absent weights remain an empty output.

**range** — `frog.studio.math.fitting.remove_outliers.range.owned.v1`

Entrées : **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **range_type: u16**, **range: array<f64>**.

Sorties : `y_out: array<f64>`, `x_out: array<f64>`, `weight_out: array<f64>`, `outlier_indices: array<i32>`, `error: i32`.

Défauts non câblés : `weight="absent_weights_output_empty" (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/remove-outliers-range-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**index** — `frog.studio.math.fitting.remove_outliers.index.owned.v1`

Entrées : **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **indices: array<i32>**.

Sorties : `y_out: array<f64>`, `x_out: array<f64>`, `weight_out: array<f64>`, `error: i32`.

Défauts non câblés : `weight="absent_weights_output_empty" (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/remove-outliers-index-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Goodness of Fit

Measures supplied predictions without refitting. SSE=sum(abs(w)*r^2); SST uses the unweighted Y mean; R-square=1-SSE/SST, possibly negative. RMSE=sqrt(SSE/DOF), default nonpositive DOF replaced by n-2. Constant observations require a diagnostic.

**default** — `frog.studio.math.fitting.goodness_of_fit.owned.v1`

Entrées : **y: array<f64>**, **best_fit: array<f64>**, `weight: array<f64>`, `degree_of_freedom: i32`.

Sorties : `sse: f64`, `r_square: f64`, `rmse: f64`, `error: i32`.

Défauts non câblés : `weight="ones_length_y" (NI)`; `degree_of_freedom=-1 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/goodness-of-fit-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Nonlinear Curve Fit Intervals

Computes local confidence intervals for supplied model parameters; no hidden new fit. Uses the same strict native model callback, real observations, confidence level and typed error cluster; returns parameter half-widths.

**function** — `frog.studio.math.fitting.nonlinear_curve_fit_intervals.function.owned.v1`

Entrées : `data: variant`, **model_reference: ref<connectivity.document.strict,cluster<in_x:f64,in_parameters:array<f64>,in_data:variant,out_value:f64,out_gradient:array<f64>,out_diagnostic:cluster<status:bool,code:i32,source:string>>>**, `confidence_level: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **best_fit_parameters: array<f64>**, `error_in: cluster<status:bool,code:i32,source:string>`.

Sorties : `upper_bound: array<f64>`, `lower_bound: array<f64>`, `delta_best_fit_parameters: array<f64>`, `error_out: cluster<status:bool,code:i32,source:string>`.

Défauts non câblés : `data="empty_variant" (GS)`; `confidence_level=0.95 (NI)`; `weight="ones_length_y" (NI)`; `error_in={"status":false,"code":0,"source":""} (NI_no_error)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/gmath/numericaloptimization/nonlinear-curve-fit-intervals-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Linear Fit Intvl

Computes confidence or prediction intervals for supplied slope/intercept without refitting. Prediction adds observation variance and has no delta-parameter ports.

**confidence** — `frog.studio.math.fitting.linear_fit_intervals.confidence.owned.v1`

Entrées : `confidence_level: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **slope: f64**, **intercept: f64**.

Sorties : `upper_bound: array<f64>`, `lower_bound: array<f64>`, `delta_slope: f64`, `delta_intercept: f64`, `error: i32`.

Défauts non câblés : `confidence_level=0.95 (NI)`; `weight="ones_length_y" (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/confidence-interval-linear-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**prediction** — `frog.studio.math.fitting.linear_fit_intervals.prediction.owned.v1`

Entrées : `confidence_level: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **slope: f64**, **intercept: f64**.

Sorties : `upper_bound: array<f64>`, `lower_bound: array<f64>`, `error: i32`.

Défauts non câblés : `confidence_level=0.95 (NI)`; `weight="ones_length_y" (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/prediction-interval-linear-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Exp Fit Intvl

Computes confidence or prediction intervals for supplied amplitude/damping in a*exp(b*x), without offset. No hidden refit; Confidence alone has parameter half-widths.

**confidence** — `frog.studio.math.fitting.exponential_fit_intervals.confidence.owned.v1`

Entrées : `confidence_level: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **amplitude: f64**, **damping: f64**.

Sorties : `upper_bound: array<f64>`, `lower_bound: array<f64>`, `delta_amplitude: f64`, `delta_damping: f64`, `error: i32`.

Défauts non câblés : `confidence_level=0.95 (NI)`; `weight="ones_length_y" (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/confidence-interval-exp-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**prediction** — `frog.studio.math.fitting.exponential_fit_intervals.prediction.owned.v1`

Entrées : `confidence_level: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **amplitude: f64**, **damping: f64**.

Sorties : `upper_bound: array<f64>`, `lower_bound: array<f64>`, `error: i32`.

Défauts non câblés : `confidence_level=0.95 (NI)`; `weight="ones_length_y" (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/prediction-interval-exp-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Power Fit Intvl

Computes confidence or prediction intervals for supplied amplitude/power in a*x^b, without offset. Real domains are checked; Confidence alone has parameter half-widths.

**confidence** — `frog.studio.math.fitting.power_fit_intervals.confidence.owned.v1`

Entrées : `confidence_level: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **amplitude: f64**, **power: f64**.

Sorties : `upper_bound: array<f64>`, `lower_bound: array<f64>`, `delta_amplitude: f64`, `delta_power: f64`, `error: i32`.

Défauts non câblés : `confidence_level=0.95 (NI)`; `weight="ones_length_y" (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/confidence-interval-power-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**prediction** — `frog.studio.math.fitting.power_fit_intervals.prediction.owned.v1`

Entrées : `confidence_level: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **amplitude: f64**, **power: f64**.

Sorties : `upper_bound: array<f64>`, `lower_bound: array<f64>`, `error: i32`.

Défauts non câblés : `confidence_level=0.95 (NI)`; `weight="ones_length_y" (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/prediction-interval-power-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Gauss Fit Intvl

Computes confidence or prediction intervals for supplied amplitude/center/standard_deviation, without offset. Standard deviation is not variance or FWHM. Confidence alone returns three parameter half-widths.

**confidence** — `frog.studio.math.fitting.gaussian_fit_intervals.confidence.owned.v1`

Entrées : `confidence_level: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **amplitude: f64**, **center: f64**, **standard_deviation: f64**.

Sorties : `upper_bound: array<f64>`, `lower_bound: array<f64>`, `delta_amplitude: f64`, `delta_center: f64`, `error: i32`, `delta_standard_deviation: f64`.

Défauts non câblés : `confidence_level=0.95 (NI)`; `weight="ones_length_y" (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/confidence-interval-gauss-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**prediction** — `frog.studio.math.fitting.gaussian_fit_intervals.prediction.owned.v1`

Entrées : `confidence_level: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **amplitude: f64**, **center: f64**, **standard_deviation: f64**.

Sorties : `upper_bound: array<f64>`, `lower_bound: array<f64>`, `error: i32`.

Défauts non câblés : `confidence_level=0.95 (NI)`; `weight="ones_length_y" (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/prediction-interval-gauss-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Log Fit Intvl

Computes confidence or prediction intervals for supplied amplitude/scale/base in amplitude*log_base(scale*x). Scale stays multiplicative; Confidence alone returns parameter half-widths.

**confidence** — `frog.studio.math.fitting.logarithm_fit_intervals.confidence.owned.v1`

Entrées : `confidence_level: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **amplitude: f64**, **scale: f64**, `base: f64`.

Sorties : `upper_bound: array<f64>`, `lower_bound: array<f64>`, `delta_amplitude: f64`, `delta_scale: f64`, `error: i32`.

Défauts non câblés : `confidence_level=0.95 (NI)`; `weight="ones_length_y" (NI)`; `base=2.718281828459045 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/confidence-interval-log-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**prediction** — `frog.studio.math.fitting.logarithm_fit_intervals.prediction.owned.v1`

Entrées : `confidence_level: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **amplitude: f64**, **scale: f64**, `base: f64`.

Sorties : `upper_bound: array<f64>`, `lower_bound: array<f64>`, `error: i32`.

Défauts non câblés : `confidence_level=0.95 (NI)`; `weight="ones_length_y" (NI)`; `base=2.718281828459045 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/prediction-interval-log-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Poly Fit Intvl

Computes confidence or prediction intervals from supplied ascending coefficients. Effective free-parameter count controls degrees of freedom; no hidden refit. Confidence alone returns coefficient half-widths.

**confidence** — `frog.studio.math.fitting.polynomial_fit_intervals.confidence.owned.v1`

Entrées : `confidence_level: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **coefficients: array<f64>**.

Sorties : `upper_bound: array<f64>`, `lower_bound: array<f64>`, `delta_coefficients: array<f64>`, `error: i32`.

Défauts non câblés : `confidence_level=0.95 (NI)`; `weight="ones_length_y" (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/confidence-interval-polynomial-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

**prediction** — `frog.studio.math.fitting.polynomial_fit_intervals.prediction.owned.v1`

Entrées : `confidence_level: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, **coefficients: array<f64>**.

Sorties : `upper_bound: array<f64>`, `lower_bound: array<f64>`, `error: i32`.

Défauts non câblés : `confidence_level=0.95 (NI)`; `weight="ones_length_y" (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/prediction-interval-polynomial-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Linear Fit Coef

Estimates slope/intercept only, using the linear weighted/robust criterion. No invented curve, residue or bound ports.

**default** — `frog.studio.math.fitting.linear_fit_coefficients.owned.v1`

Entrées : **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`.

Sorties : `slope: f64`, `intercept: f64`, `error: i32`.

Défauts non câblés : `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/linear-fit-coefficients-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Exp Fit Coef

Estimates amplitude/damping only, with no offset. Refine false uses weighted log-space estimation; Refine true performs observation-space nonlinear refinement. These are distinct calculations; refine defaults false.

**default** — `frog.studio.math.fitting.exponential_fit_coefficients.owned.v1`

Entrées : **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`, `refine: bool`.

Sorties : `amplitude: f64`, `damping: f64`, `error: i32`.

Défauts non câblés : `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`; `refine=false (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/exponential-fit-coefficients-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Power Fit Coef

Estimates amplitude/power in a*x^b, without offset. No refine port is copied from Exponential Fit Coefficients. Domains and weighted criterion are checked.

**default** — `frog.studio.math.fitting.power_fit_coefficients.owned.v1`

Entrées : **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`.

Sorties : `amplitude: f64`, `power: f64`, `error: i32`.

Défauts non câblés : `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/power-fit-coefficients-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Gauss Fit Coef

Estimates amplitude/center/standard_deviation only; initial_guess has exactly these three fields, with typed NaN automatic estimates. No offset, curve or residue output is invented.

**default** — `frog.studio.math.fitting.gaussian_fit_coefficients.owned.v1`

Entrées : `initial_guess: cluster<amplitude:f64,center:f64,standard_deviation:f64>`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`.

Sorties : `amplitude: f64`, `center: f64`, `standard_deviation: f64`, `error: i32`.

Défauts non câblés : `initial_guess={"amplitude":"NaN","center":"NaN","standard_deviation":"NaN"} (GS_automatic_using_NI_NaN_semantics)`; `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/gaussian-peak-fit-coefficients-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Log Fit Coef

Estimates amplitude and multiplicative scale in amplitude*log_base(scale*x), not slope/intercept under different labels. Default base e; nonidentifiable zero amplitude is diagnosed.

**default** — `frog.studio.math.fitting.logarithm_fit_coefficients.owned.v1`

Entrées : `base: f64`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`.

Sorties : `amplitude: f64`, `scale: f64`, `error: i32`.

Défauts non câblés : `base=2.718281828459045 (NI)`; `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/logarithm-fit-coefficients-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

### Poly Fit Coef

Estimates ascending polynomial coefficients only, with actual coefficient constraints and algorithm selection0..6. Negative degree and degree>25 retain their explicit error/warning contracts, never fictitious success.

**default** — `frog.studio.math.fitting.polynomial_fit_coefficients.owned.v1`

Entrées : `coefficient_constraints: array<cluster<order:i32,coefficient:f64>>`, `polynomial_order: i32`, **y: array<f64>**, **x: array<f64>**, `weight: array<f64>`, `tolerance: f64`, `method: u16`, `algorithm: u16`.

Sorties : `coefficients: array<f64>`, `error: i32`.

Défauts non câblés : `coefficient_constraints=[] (GS_empty_no_constraints)`; `polynomial_order=2 (NI)`; `weight="ones_length_y" (NI)`; `tolerance=0.0001 (GS_default_NI_only_nonpositive_fallback_verified)`; `method=0 (NI)`; `algorithm=0 (NI)`.

[Référence NI](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/6fits-llb/general-polynomial-fit-coefficients-vi.html). Les ports de Curve Fit configuré sont une adaptation GS explicite.

## Curve Fit configurable

Les six variantes sont de vraies configurations de Curve Fit : linear, quadratic,
spline, polynomial, general_linear et nonlinear. Elles réutilisent les noyaux
spécialisés, avec identité native propre. Quadratic fixe le degré2 ; Polynomial
choisit5 par défaut. General Linear reçoit H ; Nonlinear reçoit le modèle formule
structuré. Les autres options restent des paramètres câblables selon le modèle.
Coefficients : linéaire [pente,intercept], polynôme en puissances croissantes,
linéaire général dans l’ordre des colonnes H, non linéaire dans l’ordre déclaré.
Spline n’expose pas de coefficients inventés. Reconfiguration et sauvegarde
doivent préserver le modèle et signaler les connexions devenues incompatibles.

Les liens NI identifient les enveloppes et connecteurs. Les conventions GS
signalées ci-dessus restent distinctes. Construction, admission, calcul natif,
contrôles vivants, Highlight, Run après Save/Open et déploiement sont des preuves
séparées ; aucune disponibilité universelle d’un backend n’est inférée ici.
