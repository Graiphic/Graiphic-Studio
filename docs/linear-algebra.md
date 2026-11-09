# Linear Algebra — conventions Graiphic Studio

The Linear Algebra palette contains 38 operations. Matrix is the existing shared Matrix folder; BLAS is a navigable folder with no invented operations. Transpose reuses the existing Matrix adjoint operation and its saved identity.

Matrices are numeric Arrays of rank 2; vectors are rank 1. The calculation profile uses DBL/CDB, with explicit promotion from supported narrower numeric representations. Integer values above 2^53 can round during DBL conversion. No dimensional broadcasting, hidden transposition or private Matrix reinterpretation is performed.

Every newly added operation has an I32 `error` output. Dimensions, singularity, nonconvergence and provider resource failures are distinct from file corruption. Connect the diagnostic explicitly to the application error-handling path; mathematics does not open a dialog automatically. The reused Transpose keeps its existing two-port signature.

The tables below describe the GS projection. NI references support documented mathematics and instance contracts; they do not certify every GS enum, default, algorithm choice or numerical result. QZ `s` and `t` are GS extensions. Test Matrix Type and Condition Number code mappings, automatic negative tolerances, and size=1 preview of Create Special Matrix are explicit GS decisions. GSVD uses the common factor through the adjoint (`R^H`); the prime in the NI complex formula is otherwise ambiguous.

Detailed Help routes are exported through the existing reviewed documentation registry. This local documentation does not itself publish a website release.

## Create Special Matrix

Constructs identity, diagonal, Toeplitz and descending-power Vandermonde matrices. Modes 0..3; Toeplitz uses x for its first column and y for its first row with x[0] priority. Identity alone uses matrix_size. GS preview default size is 1; x/y default empty. Type models never add data. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.special_matrix`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `x` | input | `array<T:numeric,rank=1>` | `[]` |
| `y` | input | `array<T:numeric,rank=1>` | `[]` |
| `matrix_type` | input | `i32` | `0` |
| `matrix_size` | input | `i32` | `1` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/create-special-real-matrix-vi.html).

## Create Real Matrix From Eigenvalues

Builds a real companion matrix from a monic polynomial with the supplied roots: unit superdiagonal and final row of negated ascending coefficients. Non-real roots require conjugate partners with preserved multiplicities. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.real_matrix_from_eigenvalues`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `eigenvalues` | input | `array<c64,rank=1>` | `required` |
| `result` | output | `array<f64,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/create-real-matrix-from-eigenvalues-vi.html).

## Solve Linear Eqs

Solves A*X=B with vector or matrix right-hand sides and preserved output rank. General mode 0 uses a rank-revealing least-squares/minimum-norm solve; mode 1 uses the positive-definite system, 2/3 lower/upper triangular. No inverse(A)*B substitution or silent method change. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.solve_linear_equations`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `b` | input | `T:any` | `required` |
| `matrix_type` | input | `i32` | `0` |
| `result` | output | `T:any` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/solve-linear-equations-single-right-hand-vi.html).

## Dot Product

Computes sum(x[i]*conj(y[i])). The SECOND operand is conjugated. Equal nonzero vector lengths are required; returns a scalar and numerical error code. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.dot_product`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `x` | input | `array<T:numeric,rank=1>` | `required` |
| `y` | input | `array<T:numeric,rank=1>` | `required` |
| `result` | output | `T:numeric` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/baseanly-llb/real-dot-product-vi.html).

## Outer Product

Computes x*y^T WITHOUT conjugation, with output dimensions len(x) by len(y). Empty vectors produce the corresponding empty matrix. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.outer_product`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `x` | input | `array<T:numeric,rank=1>` | `required` |
| `y` | input | `array<T:numeric,rank=1>` | `required` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/baseanly-llb/real-outer-product-vi.html).

## A x B

Computes the matrix product A*B, never element-wise multiplication. Matrix/matrix, matrix/vector and vector/matrix variants preserve their declared output rank. Inner dimensions must agree; no broadcasting. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.matrix_multiply`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `T:any` | `required` |
| `b` | input | `T:any` | `required` |
| `result` | output | `T:any` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/baseanly-llb/real-a-x-b-vi.html).

## Kronecker Prod

Computes the block Kronecker product A tensor B, dimensions (m*p) by (n*q). Each A coefficient multiplies the complete B matrix; inner dimensions need not agree. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.kronecker_product`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `b` | input | `array<T:numeric,rank=2>` | `required` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-kronecker-product-vi.html).

## Subspaces Angle

Returns the largest principal angle in radians between real column spaces, using orthonormal numerical-rank bases. Vectors are one-column spaces. This NI-compatible profile is real-only; null/rank-difference policy is a GS numerical decision, not a certified NI behavior. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.subspaces_angle`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `T:any` | `required` |
| `b` | input | `T:any` | `required` |
| `result` | output | `f64` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/subspaces-angle-1d-vi.html).

## Determinant

Computes the determinant of a square matrix, preserving pivot parity and complex values. Matrix type 0 general, 1 positive definite, 2 lower triangular, 3 upper triangular. A singular determinant may validly be zero. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.determinant`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `matrix_type` | input | `i32` | `0` |
| `result` | output | `T:numeric` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/baseanly-llb/real-determinant-vi.html).

## Vector Norm

Vector norm with U16 modes 1 one-norm, 2 Euclidean default, 3 maximum modulus, 4 minimum modulus, 5 user exponent p. Complex entries use their modulus. Negative p is a generalized magnitude, not a mathematical norm; p=0 is invalid. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.vector_norm`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `x` | input | `array<T:numeric,rank=1>` | `required` |
| `norm_type` | input | `u16` | `2` |
| `p` | input | `f64` | `-1` |
| `result` | output | `f64` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/algsub-llb/real-vector-norm-vi.html).

## Matrix Norm

Matrix norm modes 0 spectral/two, 1 maximum column sum, 2 Frobenius, 3 maximum row sum. Accepts rectangular real or complex matrices; spectral and Frobenius norms are distinct. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.matrix_norm`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `norm_type` | input | `i32` | `0` |
| `result` | output | `f64` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/algsub-llb/real-matrix-norm-vi.html).

## Matrix Rank

Counts singular values strictly greater than the absolute tolerance. Negative tolerance selects a scale-aware automatic cutoff. GS default is max(m,n)*epsilon*sigma_max; NI does not document that exact automatic formula. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.matrix_rank`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `tolerance` | input | `f64` | `-1` |
| `result` | output | `i32` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/algsub-llb/real-matrix-rank-vi.html).

## Trace

Sums the principal diagonal through min(rows,columns), including rectangular and complex matrices. This is not the sum of all matrix entries. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.trace`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `result` | output | `T:numeric` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/algsub-llb/real-matrix-trace-vi.html).

## Test Matrix Type

Tests a matrix property without conversion. GS explicit codes: 0 diagonal, 1 lower triangular, 2 upper triangular, 3 symmetric, 4 Hermitian, 5 positive definite, 6 positive semidefinite. These codes are GS projection, not certified NI enum codes. Negative relative tolerance selects a scale-aware cutoff. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.test_matrix_type`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `matrix_type` | input | `i32` | `0` |
| `tolerance` | input | `f64` | `-1` |
| `result` | output | `bool` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/algsub-llb/test-real-matrix-type-vi.html).

## Condition Number

Computes the condition number, not its reciprocal. GS mode codes follow Matrix Norm: 0 two-norm, 1 one-norm, 2 Frobenius, 3 infinity. Only two-norm admits rectangular matrices. NI condition-mode codes are not individually certified. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.condition_number`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `norm_type` | input | `i32` | `0` |
| `result` | output | `f64` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/algsub-llb/real-matrix-condition-number-vi.html).

## Inverse Matrix

Inverts a nonsingular square real/complex matrix by factorized solves. Matrix type codes 0 general, 1 positive definite, 2 lower triangular, 3 upper triangular. Singular input is not replaced by a pseudoinverse. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.inverse_matrix`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `matrix_type` | input | `i32` | `0` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/baseanly-llb/real-inverse-matrix-vi.html).

## PseudoInv

Computes the Moore-Penrose pseudoinverse by SVD, output n by m. Values at or below the absolute tolerance are not inverted. Negative cutoff selects max(m,n)*epsilon*sigma_max (explicit GS automatic policy). Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.pseudoinverse`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `tolerance` | input | `f64` | `-1` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/algsub-llb/real-pseudoinverse-matrix-vi.html).

## Matrix Sqrt

Computes a principal matrix square root, never element-wise roots. Output is statically CDB rank two even for real input; unsolvable/domain/nonconvergence cases produce an error. Retains all imaginary components. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.matrix_sqrt`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `result` | output | `array<c64,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-matrix-square-root-vi.html).

## Matrix Exp

Computes the matrix exponential with scaled matrix algorithms, never element-wise exp. Preserves real or complex element type; dimensions must be square. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.matrix_exp`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-matrix-exp-vi.html).

## Matrix Power

Computes integer matrix powers with signed I32 n, default 1. Zero gives identity; negative exponents require invertibility. Uses exponentiation by squaring, never fractional scalar lifting. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.matrix_power`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `n` | input | `i32` | `1` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-matrix-power-vi.html).

## Matrix Log

Computes a matrix logarithm with statically complex CDB output, never element-wise ln. U16 option 0 general, 1 real-special; singular inputs have no finite logarithm. Branch/scaling outcomes are reported explicitly. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.matrix_log`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `logarithm_option` | input | `u16` | `0` |
| `result` | output | `array<c64,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-matrix-logarithm-vi.html).

## LU

Pivoted factorization P*A=L*U. For m by n input and k=min(m,n), L is m by k, U k by n, and P is an I32 m by m permutation matrix. A singular partial factorization reports its diagnostic. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.lu`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `l` | output | `array<T:numeric,rank=2>` | `recommended` |
| `u` | output | `array<T:numeric,rank=2>` | `recommended` |
| `p` | output | `array<i32,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-lu-factorization-vi.html).

## Cholesky

Upper-triangular Cholesky factor R satisfying A=R^H*R, with positive real diagonal. Only the upper triangle is read; non-positive-definite input produces an error. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.cholesky`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-cholesky-factorization-vi.html).

## Cholesky Update

Updates an existing upper Cholesky factor using x*x^H: method 0 additive update, 1 subtractive downdate. Invalid downdate reports a warning/error with the retained upper factor according to the provider contract. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.cholesky_update`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `r` | input | `array<T:numeric,rank=2>` | `required` |
| `x` | input | `array<T:numeric,rank=1>` | `required` |
| `method` | input | `i32` | `0` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/cholesky-factorization-rank-1-update-dbl-vi.html).

## QR

QR with A*P=Q*R when pivot=true and A=Q*R otherwise. P is an I32 permutation matrix (empty without pivot). U16 q_option 0 complete, 1 reduced, 2 omit Q; all options alter actual computation. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.qr`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `pivot` | input | `bool` | `false` |
| `q_option` | input | `u16` | `0` |
| `q` | output | `array<T:numeric,rank=2>` | `recommended` |
| `r` | output | `array<T:numeric,rank=2>` | `recommended` |
| `p` | output | `array<i32,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-qr-decomposition-vi.html).

## SVD

SVD A=U*S*V^H, returning BOTH descending real singular_values vector and diagonal/rectangular S matrix with the input real/complex element representation, plus U and V (not V^H). U16 svd_option 0 thin, 1 full; values_only suppresses unnecessary factor calculation. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.svd`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `values_only` | input | `bool` | `false` |
| `svd_option` | input | `u16` | `0` |
| `singular_values` | output | `array<f64,rank=1>` | `recommended` |
| `u` | output | `array<T:numeric,rank=2>` | `recommended` |
| `s` | output | `array<T:numeric,rank=2>` | `recommended` |
| `v` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-svd-decomposition-vi.html).

## Generalized SVD

Simultaneous generalized SVD of A and B with the same column count. Factors reconstruct A=U*C*R^H and B=V*S*R^H. Returns generalized singular values plus U,V,C,S,R; not two independent SVDs. SVD options and zero beta receive explicit handling. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.generalized_svd`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `b` | input | `array<T:numeric,rank=2>` | `required` |
| `values_only` | input | `bool` | `false` |
| `svd_option` | input | `u16` | `0` |
| `singular_values` | output | `array<f64,rank=1>` | `recommended` |
| `u` | output | `array<T:numeric,rank=2>` | `recommended` |
| `v` | output | `array<T:numeric,rank=2>` | `recommended` |
| `c` | output | `array<f64,rank=2>` | `recommended` |
| `s` | output | `array<f64,rank=2>` | `recommended` |
| `r` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-generalized-svd-decomposition-vi.html).

## Schur

Schur decomposition A=Z*T*Z^H. result is Schur form, vectors are Z, eigenvalues are always complex. compute_vectors defaults false. U16 order 0 unchanged, 1/2 real part ascending/descending, 3/4 modulus ascending/descending; ordering must preserve factor consistency. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.schur`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `compute_vectors` | input | `bool` | `false` |
| `order` | input | `u16` | `0` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `vectors` | output | `array<T:numeric,rank=2>` | `recommended` |
| `eigenvalues` | output | `array<c64,rank=1>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-schur-decomposition-vi.html).

## Hessenberg

Upper Hessenberg reduction A=Q*H*Q^H. result is H, q is Q. index_low/index_high are zero-based inclusive; default -1 selects the full range. Entries below the first subdiagonal vanish by similarity, not truncation. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.hessenberg`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `index_low` | input | `i32` | `-1` |
| `index_high` | input | `i32` | `-1` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `q` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-hessenberg-decomposition-vi.html).

## QZ

Generalized reduction of A/B: decomposition_type 0 generalized Hessenberg, 1 generalized Schur. Returns eigenvectors,Q,Z,complex alpha,beta, and I32 error. Additional GS outputs s/t expose the actual reduced matrix pair for independent reconstruction A=Q*S*Z^H, B=Q*T*Z^H. order 0..4 applies only in Schur mode. No inverse(B)*A shortcut. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.qz`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `b` | input | `array<T:numeric,rank=2>` | `required` |
| `decomposition_type` | input | `i32` | `0` |
| `order` | input | `u16` | `0` |
| `eigenvectors` | output | `array<c64,rank=2>` | `recommended` |
| `q` | output | `array<T:numeric,rank=2>` | `recommended` |
| `z` | output | `array<T:numeric,rank=2>` | `recommended` |
| `alpha` | output | `array<c64,rank=1>` | `recommended` |
| `beta` | output | `T:any` | `recommended` |
| `s` | output | `array<T:numeric,rank=2>` | `recommended` |
| `t` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-qz-decomposition-vi.html).

## Sylvester Eqs

Solves op(A)*X plus/minus X*op(B)=scale*C. operation_a/b U16 0 normal,1 transpose (adjoint for complex); sign 0 plus,1 minus. matrix_type 0 general,3 upper triangular (NI default). Returns X, scale, perturbed, error; residuals must use scale*C. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.sylvester_equations`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `b` | input | `array<T:numeric,rank=2>` | `required` |
| `c` | input | `array<T:numeric,rank=2>` | `required` |
| `operation_a` | input | `u16` | `0` |
| `operation_b` | input | `u16` | `0` |
| `sign` | input | `u16` | `0` |
| `matrix_type` | input | `i32` | `3` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `scale` | output | `f64` | `recommended` |
| `perturbed` | output | `bool` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-sylvester-equations-vi.html).

## Lyapunov Eqs

Solves A*X+X*A^H=scale*B (equation_type 0 continuous) or A*X*A^H-X=scale*B (1 discrete). matrix_type 0 general,3 upper triangular default. Stability is not an arbitrary prerequisite; uniqueness and scaling are diagnosed. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.lyapunov_equations`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `b` | input | `array<T:numeric,rank=2>` | `required` |
| `matrix_type` | input | `i32` | `3` |
| `equation_type` | input | `i32` | `0` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `scale` | output | `f64` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-lyapunov-equations-vi.html).

## Eigenvalues and Vectors

Eigenvalues and right eigenvectors in columns: A*V[:,i]=lambda[i]*V[:,i]. Both outputs are statically CDB. matrix_type 0 general,1 symmetric/Hermitian; output_option 0 values only,1 values plus vectors default. Hermitian eigenvalues are ascending. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.eigenvalues_vectors`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `matrix_type` | input | `i32` | `0` |
| `output_option` | input | `i32` | `1` |
| `eigenvalues` | output | `array<c64,rank=1>` | `recommended` |
| `eigenvectors` | output | `array<c64,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-eigenvalues-and-vectors-vi.html).

## Generalized Eigenvalues and Vectors

Generalized right eigenproblem A*v=lambda*B*v with statically CDB values/vectors. output_option 0 values only,1 plus vectors default. Uses a matrix-pair solver, preserving infinite/indeterminate eigenvalue diagnostics without unsafe inverse(B). Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.generalized_eigenvalues_vectors`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `b` | input | `array<T:numeric,rank=2>` | `required` |
| `output_option` | input | `i32` | `1` |
| `eigenvalues` | output | `array<c64,rank=1>` | `recommended` |
| `eigenvectors` | output | `array<c64,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-generalized-eigenvalues-and-vectors-vi.html).

## Matrix Balance

Balances by similarity B=T^-1*A*T. job U16 0 none,1 permutations,2 scaling,3 both default. Returns scale descriptor and zero-based inclusive index_low/high; descriptor must feed Back Transform without changing its meaning. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.matrix_balance`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `job` | input | `u16` | `3` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `index_low` | output | `i32` | `recommended` |
| `index_high` | output | `i32` | `recommended` |
| `scale` | output | `array<f64,rank=1>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-matrix-balance-vi.html).

## Back Transform Eigenvectors

Back-transforms eigenvectors using the Matrix Balance descriptor. job 0..3, side 0 right default,1 left. Right vectors use T; left vectors use T^-H. Index range is zero-based inclusive and dimension-checked. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.back_transform_eigenvectors`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `eigenvectors` | input | `array<T:numeric,rank=2>` | `required` |
| `scale` | input | `array<f64,rank=1>` | `required` |
| `index_low` | input | `i32` | `-1` |
| `index_high` | input | `i32` | `-1` |
| `job` | input | `u16` | `3` |
| `side` | input | `u16` | `0` |
| `result` | output | `array<T:numeric,rank=2>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-back-transform-eigenvectors-vi.html).

## Matrix Characteristic Polynomial

Computes det(lambda*I-A), with n+1 coefficients in ASCENDING powers. The leading coefficient is 1; constant coefficient=(-1)^n*det(A), next-to-leading=-trace(A). Preserves complex coefficients. Inputs calculate in DBL/CDB with explicit numeric promotion; 64-bit integers above 2^53 may round. No broadcasting, no private Matrix reinterpretation. error is I32 and never an automatic dialog.

Stable identity: `frog.studio.math.linear_algebra.characteristic_polynomial`.

| Port ID | Direction | Type contract | Required / default |
| --- | --- | --- | --- |
| `a` | input | `array<T:numeric,rank=2>` | `required` |
| `result` | output | `array<T:numeric,rank=1>` | `recommended` |
| `error` | output | `i32` | `recommended` |

[NI reference](https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/analysis/7linalg-llb/real-characteristic-polynomial-vi.html).
