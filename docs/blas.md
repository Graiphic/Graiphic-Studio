# BLAS — vecteurs et matrices DBL/CDB

Les 35 fonctions se trouvent dans **Mathematics → Linear Algebra → BLAS**.
Matrix et les fonctions Linear Algebra restent distincts. Vecteurs = Arrays de
rang 1 ; matrices = Arrays de rang 2 du modèle Matrix existant. Les préfixes `d`
sont réels DBL, les préfixes `z` complexes CDB ; les autres fonctions choisissent
leur instance dans les domaines indiqués. Les promotions numériques autorisées
sont explicites. Aucun port réel ne supprime une partie imaginaire. Les entiers
64 bits peuvent s’arrondir en DBL ; cette palette n’annonce pas un calcul entier
exact. Les sorties sont des valeurs indépendantes des autres branches.

## Paramètres communs

| Paramètre | Valeurs enregistrées | Défaut |
| --- | --- | --- |
| operation, operation_a, operation_b | 0 Direct ; 1 Conjugated & Transposed ; 2 Transposed | 0 |
| matrix_a_type, matrix_c_type | 2 Lower ; 3 Upper | 3 |
| side | 0 Right ; 1 Left | 1 |
| diagonal | 0 Non-unit ; 1 Unit | 0 |
| alpha, beta | Domaine indiqué ; HERK alpha/beta réels, HER2K beta réel | 1 |
| x_inc, y_inc | Pas d’accès BLAS1 ; zéro refusé | 1 |

Les codes sont ceux du contrat GS/NI, pas les valeurs CBLAS. En complexe,
SYRK/SYR2K refusent H ; HERK/HER2K refusent T : leurs adaptations NI ne sont pas
établies, donc aucune conversion silencieuse T↔H n’est effectuée.

Le triangle non choisi et les cellules hors bloc restent intacts. Unit ignore
la diagonale stockée. Une résolution utilise une substitution triangulaire ;
une diagonale utilisée non-unit exactement nulle produit un diagnostic.
`error` est une sortie **I32**, pas un cluster ni une popup automatique.
Les valeurs non finies actives produisent un diagnostic ; les cellules ignorées
ne sont pas lues et restent intactes.

## Conventions GS explicites

- BLAS1 : nombre sélectionné `L==0 ? 0 : 1+floor((L-1)/abs(inc))`.
  Indices positifs `j*inc` ; négatifs `L-1-j*abs(inc)`.
  DDOT/ZDOTU/ZDOTC exigent les mêmes longueurs physiques et nombres sélectionnés.
  COPY/AXPY exigent assez de positions sélectionnées dans y et conservent toute
  sa longueur. SWAP/ROT/DROTM exigent les mêmes nombres sélectionnés, avec des
  longueurs physiques éventuellement différentes. Aucun minimum silencieux.
  La déduction précise NI des strides n’est pas certifiée.
  ASUM/IAMAX/IAMIN exigent un pas strictement positif.
- IAMAX/IAMIN : indice **physique à base zéro dans x**, premier ex æquo dans le
  parcours. Vide : −1 et avertissement +9601. Base et conventions NI non
  certifiées. Une valeur non finie active ne produit pas un extremum réussi.
- ROTG complexe : c réel, r/s/z complexes ; z conserve y initial, selon le B
  inchangé Netlib. NI montre ce port mais ne définit pas sa convention.
  ROT utilise ZDROT et exige c/s réels ; s complexe n’est pas tronqué en réel.
- DROTM : matrice H 2×2 et flag I32 séparé. DROTMG fournit H complète et son
  flag ; PARAM de l’ABI reste interne.
- Un accumulateur facultatif **non câblé** est matérialisé à zéro à la forme
  dérivée. Ce n’est pas une règle générale remplaçant tout tableau vide câblé.
  GEMM/SYRK/SYR2K exigent C. ZHER exige A couvrant N×N ; les cellules extérieures
  sont conservées (la documentation NI entrée/sortie est contradictoire sur ce point).

## Fonctions et ports

R=DBL, Z=CDB ; `t`=scalaire du domaine, `v`=vecteur, `m`=matrice.
Toutes les lignes ont `error:i32`. Les noms sont les identités persistées.
Aucun n, lda, pointeur ou stride BLAS2/3 n’est ajouté aux connecteurs publics.

| # | Fonction / domaine | Entrées (requises en **gras**) | Sorties | Défauts non câblés |
| --- | --- | --- | --- | --- |
| 01 | [ddot](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/ddot-dot-product-dbl-vi.html) R | **x:v**, **y:v**, `x_inc:i32`, `y_inc:i32` | `result:t`, `error:i32` | `x_inc=1`, `y_inc=1` |
| 02 | [zdotu](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/zdotu-dot-product-cdb-vi.html) Z | **x:v**, **y:v**, `x_inc:i32`, `y_inc:i32` | `result:t`, `error:i32` | `x_inc=1`, `y_inc=1` |
| 03 | [zdotc](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/zdotc-dot-product-with-conjugation-cdb-vi.html) Z | **x:v**, **y:v**, `x_inc:i32`, `y_inc:i32` | `result:t`, `error:i32` | `x_inc=1`, `y_inc=1` |
| 04 | [axpy](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/axpy-scalar-vector-product-vi.html) R/Z | **x:v**, `y:v`, `x_inc:i32`, `y_inc:i32`, `alpha:t` | `result:v`, `error:i32` | `y=zero_like_x`, `x_inc=1`, `y_inc=1`, `alpha=1` |
| 05 | [nrm2](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/nrm2-vector-2-norm-vi.html) R/Z | **x:v**, `x_inc:i32` | `result:f64`, `error:i32` | `x_inc=1` |
| 06 | [asum](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/asum-absolute-values-sum-vi.html) R/Z | **x:v**, `x_inc:i32` | `result:f64`, `error:i32` | `x_inc=1` |
| 07 | [copy](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/copy-vector-copy-vi.html) R/Z | **x:v**, `y:v`, `x_inc:i32`, `y_inc:i32` | `result:v`, `error:i32` | `y=zero_like_x`, `x_inc=1`, `y_inc=1` |
| 08 | [swap](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/swap-vector-swap-vi.html) R/Z | **x:v**, **y:v**, `x_inc:i32`, `y_inc:i32` | `x_out:v`, `y_out:v`, `error:i32` | `x_inc=1`, `y_inc=1` |
| 09 | [drotm](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/drotm-fast-givens-rotation-dbl-vi.html) R | **x:v**, **y:v**, **rotation_matrix:m**, **rotation_matrix_flag:i32**, `x_inc:i32`, `y_inc:i32` | `x_out:v`, `y_out:v`, `error:i32` | `x_inc=1`, `y_inc=1` |
| 10 | [drotmg](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/drotmg-fast-givens-rotation-parameters-dbl-vi.html) R | **x:f64**, **y:f64**, **d1_in:f64**, **d2_in:f64** | `r:f64`, `d1_out:f64`, `d2_out:f64`, `rotation_matrix:m`, `rotation_matrix_flag:i32`, `error:i32` | aucun |
| 11 | [rot](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/rot-givens-rotation-vi.html) R/Z | **x:v**, **y:v**, **c:f64**, **s:f64**, `x_inc:i32`, `y_inc:i32` | `x_out:v`, `y_out:v`, `error:i32` | `x_inc=1`, `y_inc=1` |
| 12 | [rotg](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/rotg-givens-rotation-parameters-vi.html) R/Z | **x:t**, **y:t** | `r:t`, `c:f64`, `s:t`, `z:t`, `error:i32` | aucun |
| 13 | [iamax](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/amax-max-element-index-vi.html) R/Z | **x:v**, `x_inc:i32` | `result:i32`, `error:i32` | `x_inc=1` |
| 14 | [iamin](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/amin-min-element-index-vi.html) R/Z | **x:v**, `x_inc:i32` | `result:i32`, `error:i32` | `x_inc=1` |
| 15 | [gemv](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/gemv-general-matrix-vector-product-vi.html) R/Z | **a:m**, **x:v**, `y:v`, `alpha:t`, `beta:t`, `operation_a:i32` | `result:v`, `error:i32` | `y=zero_vector_rows_op_a`, `alpha=1`, `beta=1`, `operation_a=0` |
| 16 | [dsymv](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/dsymv-symmetric-matrix-vector-product-dbl-vi.html) R | **a:m**, **x:v**, `y:v`, `alpha:t`, `beta:t`, `matrix_a_type:i32` | `result:v`, `error:i32` | `y=zero_vector_length_x`, `alpha=1`, `beta=1`, `matrix_a_type=3` |
| 17 | [zhemv](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/zhemv-hermitian-matrix-vector-product-cdb-vi.html) Z | **a:m**, **x:v**, `y:v`, `alpha:t`, `beta:t`, `matrix_a_type:i32` | `result:v`, `error:i32` | `y=zero_vector_length_x`, `alpha=1`, `beta=1`, `matrix_a_type=3` |
| 18 | [trmv](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/trmv-triangle-matrix-vector-product-vi.html) R/Z | **a:m**, **x:v**, `operation_a:i32`, `matrix_a_type:i32`, `diagonal:i32` | `result:v`, `error:i32` | `operation_a=0`, `matrix_a_type=3`, `diagonal=0` |
| 19 | [dsyr](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/dsyr-symmetric-matrix-rank-1-update-dbl-vi.html) R | **x:v**, `a:m`, `alpha:t`, `matrix_a_type:i32` | `result:m`, `error:i32` | `a=zero_square_length_x`, `alpha=1`, `matrix_a_type=3` |
| 20 | [dsyr2](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/dsyr2-symmetric-matrix-rank-2-update-dbl-vi.html) R | **x:v**, **y:v**, `a:m`, `alpha:t`, `matrix_a_type:i32` | `result:m`, `error:i32` | `a=zero_square_length_x`, `alpha=1`, `matrix_a_type=3` |
| 21 | [zher](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/zher-hermitian-matrix-rank-1-update-cdb-vi.html) Z | **x:v**, **a:m**, `alpha:f64`, `matrix_a_type:i32` | `result:m`, `error:i32` | `alpha=1`, `matrix_a_type=3` |
| 22 | [zher2](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/zher2-hermitian-matrix-rank-2-update-cdb-vi.html) Z | **x:v**, **y:v**, `a:m`, `alpha:t`, `matrix_a_type:i32` | `result:m`, `error:i32` | `a=zero_square_length_x`, `alpha=1`, `matrix_a_type=3` |
| 23 | [dger](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/dger-general-matrix-rank-1-update-dbl-vi.html) R | **x:v**, **y:v**, `a:m`, `alpha:t` | `result:m`, `error:i32` | `a=zero_matrix_length_x_by_length_y`, `alpha=1` |
| 24 | [zgeru](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/zgeru-general-matrix-rank-1-update-cdb-vi.html) Z | **x:v**, **y:v**, `a:m`, `alpha:t` | `result:m`, `error:i32` | `a=zero_matrix_length_x_by_length_y`, `alpha=1` |
| 25 | [zgerc](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/zgerc-general-matrix-rank-1-update-with-conjugation-cdb-vi.html) Z | **x:v**, **y:v**, `a:m`, `alpha:t` | `result:m`, `error:i32` | `a=zero_matrix_length_x_by_length_y`, `alpha=1` |
| 26 | [trsv](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/trsv-solve-linear-eqs-triangle-single-vi.html) R/Z | **a:m**, **x:v**, `operation_a:i32`, `matrix_a_type:i32`, `diagonal:i32` | `result:v`, `error:i32` | `operation_a=0`, `matrix_a_type=3`, `diagonal=0` |
| 27 | [gemm](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/gemm-general-matrix-matrix-product-vi.html) R/Z | **a:m**, **b:m**, **c:m**, `alpha:t`, `beta:t`, `operation_a:i32`, `operation_b:i32` | `result:m`, `error:i32` | `alpha=1`, `beta=1`, `operation_a=0`, `operation_b=0` |
| 28 | [symm](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/symm-symmetric-matrix-matrix-product-vi.html) R/Z | **a:m**, **b:m**, `c:m`, `alpha:t`, `beta:t`, `side:i32`, `matrix_a_type:i32` | `result:m`, `error:i32` | `c=zero_matrix_shape_b`, `alpha=1`, `beta=1`, `side=1`, `matrix_a_type=3` |
| 29 | [zhemm](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/zhemm-hermitian-matrix-matrix-product-cdb-vi.html) Z | **a:m**, **b:m**, `c:m`, `alpha:t`, `beta:t`, `side:i32`, `matrix_a_type:i32` | `result:m`, `error:i32` | `c=zero_matrix_shape_b`, `alpha=1`, `beta=1`, `side=1`, `matrix_a_type=3` |
| 30 | [trmm](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/trmm-triangle-matrix-matrix-product-vi.html) R/Z | **a:m**, **b:m**, `alpha:t`, `side:i32`, `operation_a:i32`, `matrix_a_type:i32`, `diagonal:i32` | `result:m`, `error:i32` | `alpha=1`, `side=1`, `operation_a=0`, `matrix_a_type=3`, `diagonal=0` |
| 31 | [syrk](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/syrk-symmetric-matrix-rank-k-update-vi.html) R/Z | **a:m**, **c:m**, `alpha:t`, `beta:t`, `operation_a:i32`, `matrix_c_type:i32` | `result:m`, `error:i32` | `alpha=1`, `beta=1`, `operation_a=0`, `matrix_c_type=3` |
| 32 | [syr2k](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/syr2k-symmetric-matrix-rank-2k-update-vi.html) R/Z | **a:m**, **b:m**, **c:m**, `alpha:t`, `beta:t`, `operation:i32`, `matrix_c_type:i32` | `result:m`, `error:i32` | `alpha=1`, `beta=1`, `operation=0`, `matrix_c_type=3` |
| 33 | [zherk](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/zherk-hermitian-matrix-rank-k-update-cdb-vi.html) Z | **a:m**, `c:m`, `alpha:f64`, `beta:f64`, `operation_a:i32`, `matrix_c_type:i32` | `result:m`, `error:i32` | `c=zero_square_rows_op_a`, `alpha=1`, `beta=1`, `operation_a=0`, `matrix_c_type=3` |
| 34 | [zher2k](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/zher2k-hermitian-matrix-rank-2k-update-cdb-vi.html) Z | **a:m**, **b:m**, `c:m`, `alpha:t`, `beta:f64`, `operation:i32`, `matrix_c_type:i32` | `result:m`, `error:i32` | `c=zero_square_rows_op_a`, `alpha=1`, `beta=1`, `operation=0`, `matrix_c_type=3` |
| 35 | [trsm](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/blas-llb/trsm-solve-linear-eqs-triangle-multiple-vi.html) R/Z | **a:m**, **x:m**, `alpha:t`, `side:i32`, `operation_a:i32`, `matrix_a_type:i32`, `diagonal:i32` | `result:m`, `error:i32` | `alpha=1`, `side=1`, `operation_a=0`, `matrix_a_type=3`, `diagonal=0` |

## Opérations

### ddot

Produit scalaire réel : somme de xᵢyᵢ.

sum(x_i*y_i), DBL.

### zdotu

Produit scalaire complexe sans conjugaison : somme de xᵢyᵢ.

sum(x_i*y_i), with no conjugation.

### zdotc

Produit scalaire complexe : somme de conj(xᵢ)yᵢ ; conjugue x, pas y.

sum(conj(x_i)*y_i); conjugates x, not y.

### axpy

Calcule alpha·x+y et conserve le terme y initial.

y = alpha*x + y; the existing y term is retained.

### nrm2

Norme euclidienne stable ; résultat DBL même pour un vecteur complexe.

Stable Euclidean norm; complex input produces a DBL norm.

### asum

Somme des valeurs absolues BLAS ; en complexe, |Re|+|Im|, pas le module euclidien.

sum(abs(x)) for real data; sum(abs(Re(x))+abs(Im(x))) for complex data.

### copy

Copie les composantes sélectionnées de x dans y en conservant les cases non ciblées.

Copies selected x components into the selected y positions, retaining untouched y components.

### swap

Échange x et y à partir de leurs valeurs initiales ; les deux sorties sont indépendantes.

Returns two independent outputs after exchanging selected x/y components from their original inputs.

### drotm

Applique la transformation de Givens modifiée H : matrice 2×2 et flag I32 séparé.

Applies the modified Givens matrix H to paired components. H is a rank-two 2x2 Array and the flag is a separate I32; provider PARAM[5] stays private.

### drotmg

Construit H, son flag et les facteurs d’échelle mis à jour. Les quatre entrées scalaires sont requises.

Computes the modified Givens transform and updated d1,d2,r. All four scalar inputs are required; H is fully materialized as a 2x2 Array and its flag is preserved.

### rot

Applique x′=c·x+s·y et y′=c·y−s·x. c et s sont réels, y compris pour ZDROT complexe.

x_out=c*x+s*y; y_out=c*y-s*x. The complex instance is ZDROT: both c and s remain DBL real scalars.

### rotg

Calcule r, c, s et z. c reste réel ; en complexe, z conserve y initial selon le choix GS explicite.

Computes r,c,s,z from x,y. The complex instance retains a real c and complex r,s,z. GS complex z copies original y; that convention is not NI-certified.

### iamax

Indice PHYSIQUE à base zéro du premier maximum sélectionné de |Re|+|Im|. Vide : −1 et avertissement +9601.

Returns the zero-based PHYSICAL index in x of the first selected maximum BLAS amplitude; complex amplitude is abs(Re)+abs(Im). Empty selection returns -1 with warning +9601.

### iamin

Indice PHYSIQUE à base zéro du premier minimum sélectionné de |Re|+|Im|. Vide : −1 et avertissement +9601.

Returns the zero-based PHYSICAL index in x of the first selected minimum BLAS amplitude; complex amplitude is abs(Re)+abs(Im). Empty selection returns -1 with warning +9601.

### gemv

Calcule alpha·op(A)·x+beta·y, en conservant la fin de y hors calcul.

y = alpha*op(A)*x + beta*y; updates the leading result block, retains the full y length and untouched tail.

### dsymv

Produit symétrique réel avec accumulation ; seul le triangle choisi est lu.

y = alpha*S(A)*x + beta*y using only the selected triangle; the ignored triangle never contributes.

### zhemv

Produit hermitien avec accumulation ; conjugaison hors diagonale et diagonale réelle.

y = alpha*H(A)*x + beta*y using the selected triangle; off-diagonal completion is conjugated and the diagonal is real.

### trmv

Multiplie par op(U(A)). Unit ignore la diagonale stockée ; ce n’est pas une résolution.

result = op(U(A))*x; multiplication, not a solve. Unit diagonal ignores all stored diagonal entries.

### dsyr

Mise à jour symétrique de rang 1 ; seul le triangle choisi change.

Updates only the chosen triangle of A + alpha*x*x^T; keeps the other triangle and all cells outside the leading block.

### dsyr2

Mise à jour symétrique de rang 2 ; préserve l’autre triangle et les cellules hors bloc.

Updates only the chosen triangle of A + alpha*x*y^T + alpha*y*x^T; keeps the rest of A.

### zher

Mise à jour hermitienne de rang 1 ; alpha réel. A requise couvrant N×N, diagonale calculée réelle.

Updates the chosen triangle of A + alpha*x*x^H, with DBL real alpha and a real computed diagonal. A is required and covers at least the NxN calculated block; the rest is preserved.

### zher2

Mise à jour hermitienne de rang 2 avec alpha puis conj(alpha) ; diagonale calculée réelle.

Updates the chosen triangle of A + alpha*x*y^H + conj(alpha)*y*x^H; computed diagonal is real.

### dger

Ajoute alpha·x·yᵀ au bloc rectangulaire initial de A ; préserve les cellules restantes.

Updates the leading rectangular block of A + alpha*x*y^T, preserving the full shape and untouched cells.

### zgeru

Ajoute alpha·x·yᵀ sans conjugaison.

Updates the leading rectangular block of A + alpha*x*y^T with no conjugation.

### zgerc

Ajoute alpha·x·yᴴ ; conjugue y, pas x.

Updates the leading rectangular block of A + alpha*x*y^H; conjugation is on y, not x.

### trsv

Résout op(U(A))·u=x sans inverse explicite. Diagonale Unit ignorée ; zéro non-unit utilisé diagnostiqué.

Solves op(U(A))*result=x by triangular substitution. Unit ignores stored diagonal; a used zero non-unit diagonal reports a singularity.

### gemm

Calcule alpha·op(A)·op(B)+beta·C. C requise ; sa forme et ses cellules hors bloc restent intactes.

C = alpha*op(A)*op(B) + beta*C. C is required; preserves its full shape and every cell outside the calculated leading block.

### symm

Produit symétrique à gauche ou à droite avec accumulation ; en complexe, symétrique n’implique aucune conjugaison.

C = alpha*S(A)*B + beta*C (Left) or alpha*B*S(A)+beta*C (Right). Complex symmetry is transpose, without conjugation.

### zhemm

Produit hermitien à gauche ou à droite avec accumulation ; seul le triangle choisi est lu.

C = alpha*H(A)*B + beta*C (Left) or alpha*B*H(A)+beta*C (Right), using only the chosen triangle of A.

### trmm

Multiplie B par la matrice triangulaire à gauche ou à droite ; aucun terme beta·C.

B = alpha*op(U(A))*B (Left), or alpha*B*op(U(A)) (Right). No beta or C accumulator; B retains its shape.

### syrk

Mise à jour symétrique de rang k sans conjugaison ; C requise. H complexe refusé.

Updates only the chosen C triangle using alpha*A*A^T + beta*C or alpha*A^T*A + beta*C. No conjugation. C is required; complex H is explicitly rejected.

### syr2k

Mise à jour symétrique de rang 2k sans conjugaison ; C requise. H complexe refusé.

Updates only the chosen C triangle using alpha*A*B^T + alpha*B*A^T + beta*C, or its transposed form. No conjugation. C is required; complex H is rejected.

### zherk

Mise à jour hermitienne de rang k ; alpha et beta réels. N/H admis, T refusé.

Updates only the chosen C triangle using alpha*A*A^H + beta*C or alpha*A^H*A + beta*C. Both alpha and beta are DBL real. N/H supported; T is explicitly rejected.

### zher2k

Mise à jour hermitienne de rang 2k ; alpha complexe, beta réel. N/H admis, T refusé.

Updates only the chosen C triangle using alpha*A*B^H + conj(alpha)*B*A^H + beta*C, or its adjoint form. Alpha CDB, beta DBL. N/H supported; T is rejected.

### trsm

Résout le système triangulaire à gauche ou à droite, avec plusieurs seconds membres x ; sans inverse explicite.

Solves op(U(A))*result=alpha*x (Left), or result*op(U(A))=alpha*x (Right); x is a matrix. No explicit inverse is formed.

## Formes des zéros facultatifs

`zero_like_x` et `zero_vector_length_x` : longueur physique de x.
`zero_vector_rows_op_a` : nombre de lignes de op(A).
`zero_square_length_x` : len(x)×len(x).
`zero_matrix_length_x_by_length_y` : len(x)×len(y).
`zero_matrix_shape_b` : même forme que B.
`zero_square_rows_op_a` : carré d’ordre égal aux lignes de op(A).
Ces règles s’appliquent à l’absence de connexion, pas à tout tableau vide.

Les liens NI documentent les enveloppes correspondantes. Les conventions GS
signalées ne certifient pas leur exécution NI. Fournisseur, admission et preuve
d’exécution restent séparés des signatures. Build/AOT et d’autres cibles ne
sont pas déduits d’un Run natif.
