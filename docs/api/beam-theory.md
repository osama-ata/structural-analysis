# API Reference - Beam Theory

Complete API documentation for beam analysis methods.

## BeamTheory Class

::: structural_analysis.beam_theory.BeamTheory

## Method Documentation

### euler_bernoulli

::: structural_analysis.beam_theory.BeamTheory.euler_bernoulli
    options:
      show_source: true

## Usage Examples

### Basic Point Load Analysis

```python
from structural_analysis.beam_theory import BeamTheory

beam = BeamTheory()
result = beam.euler_bernoulli(
    length=4.0,
    E=200e9,
    second_moment=8.33e-6,
    load_type="point",
    load_magnitude=10000,
    load_position=2.0,
    boundary_conditions="simply_supported"
)
```

### Distributed Load Analysis

```python
result = beam.euler_bernoulli(
    length=6.0,
    E=200e9,
    second_moment=1.2e-5,
    load_type="distributed",
    load_magnitude=5000,  # N/m
    boundary_conditions="simply_supported",
    num_points=200  # Higher resolution for smooth curves
)
```

### Cantilever Beam

```python
result = beam.euler_bernoulli(
    length=3.0,
    E=200e9,
    second_moment=5.4e-6,
    load_type="point",
    load_magnitude=8000,
    load_position=3.0,  # At free end
    boundary_conditions="cantilever"
)
```

## Return Values

All beam analysis methods return a dictionary with the following structure:

| Key | Type | Description | Units |
|-----|------|-------------|-------|
| `x` | `np.ndarray` | Position along beam | m |
| `deflection` | `np.ndarray` | Vertical deflection | m |
| `moment` | `np.ndarray` | Bending moment | N⋅m |
| `shear` | `np.ndarray` | Shear force | N |
| `max_deflection` | `float` | Maximum deflection | m |
| `max_moment` | `float` | Maximum moment | N⋅m |
| `max_shear` | `float` | Maximum shear | N |

## Parameter Validation

The library performs comprehensive input validation:

### Length Parameters

- Must be positive values
- Typical range: 0.1 m to 100 m

### Material Properties

- Elastic modulus `E`: Must be positive (typical steel: 200 GPa)
- Second moment `second_moment`: Must be positive

### Load Parameters

- Load magnitude: Must be positive
- Load position: Must be within beam span (0 ≤ position ≤ length)

### Boundary Conditions

- `"simply_supported"`: Pinned at both ends
- `"cantilever"`: Fixed at left end, free at right end

## Engineering Notes

### Euler-Bernoulli Theory Assumptions

!!! theory "Key Assumptions"
    1. **Small deflections**: δ << L (deflection much smaller than span)
    2. **Plane sections remain plane**: No warping of cross-sections
    3. **Linear elastic material**: Stress proportional to strain
    4. **Homogeneous material**: Uniform properties throughout
    5. **Prismatic beam**: Constant cross-section along length

### Applicability Limits

- **Slenderness ratio**: L/h > 10 (length-to-height ratio)
- **Deflection limit**: δ/L < 1/250 for accuracy
- **Material limit**: Below yield stress

### Common Section Properties

| Section Type | Second Moment Formula |
|--------------|----------------------|
| Rectangular | \\(I = \frac{bh^3}{12}\\) |
| Circular | \\(I = \frac{\pi d^4}{64}\\) |
| I-Beam | See steel design tables |

## Error Handling

The library raises informative exceptions for invalid inputs:

```python
try:
    result = beam.euler_bernoulli(
        length=-1.0,  # Invalid: negative length
        E=200e9,
        second_moment=8.33e-6,
        load_type="point",
        load_magnitude=10000,
        load_position=2.0,
        boundary_conditions="simply_supported"
    )
except ValueError as e:
    print(f"Input error: {e}")
```

Common errors:

- `ValueError`: Invalid parameter values (negative lengths, invalid positions)
- `TypeError`: Wrong parameter types (string instead of float)
- `KeyError`: Invalid load type or boundary condition
