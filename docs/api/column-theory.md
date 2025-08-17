# Column Theory API

!!! info "Column Stability Analysis Methods"
    This page documents all methods in the `ColumnTheory` class for analyzing column stability and buckling behavior.

## ColumnTheory Class

::: structural_analysis.column_theory.ColumnTheory

## Methods

### euler_buckling

::: structural_analysis.column_theory.ColumnTheory.euler_buckling

#### Usage Example

```python
from structural_analysis.column_theory import ColumnTheory

# Initialize column theory
column = ColumnTheory()

# Analyze a pinned-pinned column
result = column.euler_buckling(
    length=3.0,                    # 3m column
    E=200e9,                       # Steel (200 GPa)
    second_moment=8.33e-6,         # Second moment of area
    end_conditions="pinned"        # Both ends pinned
)

# Access results
critical_load = result['critical_load']        # N
effective_length = result['effective_length']  # m
slenderness = result['slenderness_ratio']      # dimensionless

print(f"Critical load: {critical_load:.0f} N")
print(f"Slenderness ratio: {slenderness:.1f}")
```

#### End Conditions

The method supports four standard end conditions:

| Condition | K Factor | Description | Application |
|-----------|----------|-------------|-------------|
| `"pinned"` | 1.0 | Both ends pinned | Simple column connections |
| `"fixed"` | 0.5 | Both ends fixed | Rigid frame columns |
| `"fixed_free"` | 2.0 | Fixed base, free top | Flagpoles, towers |
| `"fixed_pinned"` | 0.7 | Fixed base, pinned top | Typical building columns |

#### Return Values

The method returns a `EulerBucklingResult` TypedDict with:

```python
{
    'critical_load': float,        # Critical buckling load (N)
    'effective_length': float,     # Effective length KL (m)  
    'slenderness_ratio': float,    # KL/r ratio
    'k_factor': float             # Effective length factor K
}
```

#### Validation

The method performs comprehensive input validation:

- **Positive values**: `length`, `E`, `second_moment` must be > 0
- **Valid end conditions**: Must be one of the four supported types
- **Physical limits**: Checks for reasonable slenderness ratios
- **Material properties**: Validates elastic modulus range

#### Theory Background

Based on Euler's elastic buckling formula:

$$P_{cr} = \frac{\pi^2 EI}{(KL)^2}$$

The slenderness ratio is calculated as:

$$\lambda = \frac{KL}{r} = \frac{KL}{\sqrt{I/A}}$$

For the radius of gyration calculation, a typical area is estimated from the second moment of area.

#### Limitations

- **Elastic analysis only**: Valid for slender columns (λ > 100)
- **Perfect columns**: Assumes no initial imperfections
- **Linear material**: Material remains elastic throughout
- **Static loading**: No dynamic or time-dependent effects

## Usage Patterns

### Direct Usage

```python
from structural_analysis.column_theory import ColumnTheory

column = ColumnTheory()
result = column.euler_buckling(...)
```

### Via Main Class

```python
from structural_analysis import StructuralAnalysis

analysis = StructuralAnalysis()
result = analysis.column_theory.euler_buckling(...)
```

### Multiple Columns

```python
# Analyze multiple columns efficiently
columns_data = [
    {'length': 3.0, 'I': 8.33e-6, 'end': 'pinned'},
    {'length': 4.0, 'I': 1.67e-5, 'end': 'fixed'},
    {'length': 5.0, 'I': 2.50e-5, 'end': 'fixed_pinned'},
]

results = []
for col in columns_data:
    result = column.euler_buckling(
        length=col['length'],
        E=200e9,
        second_moment=col['I'],
        end_conditions=col['end']
    )
    results.append(result)
```

## Error Handling

The method raises specific exceptions for common errors:

- `ValueError`: Invalid input parameters or end conditions
- `TypeError`: Incorrect parameter types
- `AssertionError`: Failed validation checks

Example error handling:

```python
try:
    result = column.euler_buckling(
        length=-1.0,  # Invalid negative length
        E=200e9,
        second_moment=8.33e-6,
        end_conditions="pinned"
    )
except ValueError as e:
    print(f"Input error: {e}")
```

## Related Documentation

- [**Euler Buckling Theory**](../theories/column-theory/euler-buckling.md): Mathematical background
- [**Column Design Examples**](../examples/column-design.md): Practical applications  
- [**Advanced Column Methods**](../theories/column-theory/advanced.md): Additional theories
- [**Core Classes**](core.md): Main library interface
