# Core Classes

!!! info "Main Library Interface"
    This page documents the core `StructuralAnalysis` class that provides unified access to all structural theories.

## StructuralAnalysis

::: structural_analysis.StructuralAnalysis

The `StructuralAnalysis` class serves as the main entry point to the library, providing access to all theory modules through a unified interface.

### Usage

```python
from structural_analysis import StructuralAnalysis

# Initialize the main analysis class
analysis = StructuralAnalysis()

# Access theory modules
beam_analysis = analysis.beam_theory
column_analysis = analysis.column_theory
```

### Available Properties

| Property | Type | Description |
|----------|------|-------------|
| `beam_theory` | `BeamTheory` | Access to beam analysis methods |
| `column_theory` | `ColumnTheory` | Access to column analysis methods |

### Design Pattern

The class follows the **Facade Pattern**, providing a simplified interface to the complex subsystem of structural analysis theories. This design:

1. **Simplifies usage**: Single import provides access to all theories
2. **Maintains organization**: Each theory category in its own module
3. **Enables extensibility**: New theory modules easily added
4. **Provides consistency**: Uniform access patterns across theories

### Future Extensions

As new theory modules are implemented, they will be accessible through additional properties:

- `plate_theory`: Plate and shell analysis methods
- `dynamic_theory`: Dynamic analysis and vibration methods  
- `nonlinear_theory`: Nonlinear analysis methods
- `material_theory`: Advanced material modeling

### Example Integration

Complete example showing typical usage patterns:

```python
from structural_analysis import StructuralAnalysis

# Initialize once, use throughout application
analysis = StructuralAnalysis()

# Beam analysis
beam_result = analysis.beam_theory.euler_bernoulli(
    length=4.0,
    E=200e9,
    second_moment=8.33e-6,
    load_type="point",
    load_magnitude=10000,
    load_position=2.0,
    boundary_conditions="simply_supported"
)

# Column analysis using same instance
column_result = analysis.column_theory.euler_buckling(
    length=3.0,
    E=200e9,
    second_moment=8.33e-6,
    end_conditions="pinned"
)

# Results are independent and can be processed separately
print(f"Beam max deflection: {beam_result['max_deflection']:.6f} m")
print(f"Column critical load: {column_result['critical_load']:.0f} N")
```

## Related Documentation

- [**BeamTheory API**](beam-theory.md): Detailed beam analysis methods
- [**ColumnTheory API**](column-theory.md): Detailed column analysis methods
- [**Examples**](../examples/index.md): Practical usage examples
- [**Theory Guide**](../theories/index.md): Mathematical background
