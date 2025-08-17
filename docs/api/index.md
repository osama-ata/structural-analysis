# API Reference

!!! info "Complete Method Documentation"
    This section provides comprehensive API documentation for all classes and methods in the structural analysis library.

## Core Components

### [StructuralAnalysis](core.md)

Main facade class providing unified access to all structural theories.

### Theory Modules

- [**BeamTheory**](beam-theory.md): Beam bending and deflection analysis
- [**ColumnTheory**](column-theory.md): Column stability and buckling analysis

## Quick Navigation

=== "By Theory Type"

    **Beam Analysis**
    
    - [`euler_bernoulli()`](beam-theory.md#euler_bernoulli): Classical beam bending theory
    - More beam methods coming soon...

    **Column Analysis**
    
    - [`euler_buckling()`](column-theory.md#euler_buckling): Elastic buckling analysis
    - More column methods coming soon...

=== "By Use Case"

    **Static Analysis**
    
    - Beam deflection: [`euler_bernoulli()`](beam-theory.md#euler_bernoulli)
    - Column stability: [`euler_buckling()`](column-theory.md#euler_buckling)

    **Design Verification**
    
    - Deflection limits: [`euler_bernoulli()`](beam-theory.md#euler_bernoulli)
    - Buckling capacity: [`euler_buckling()`](column-theory.md#euler_buckling)

## Usage Patterns

### Basic Usage

```python
from structural_analysis import StructuralAnalysis

# Initialize the library
analysis = StructuralAnalysis()

# Access theory modules
beam_result = analysis.beam_theory.euler_bernoulli(...)
column_result = analysis.column_theory.euler_buckling(...)
```

### Direct Module Access

```python
from structural_analysis.beam_theory import BeamTheory
from structural_analysis.column_theory import ColumnTheory

# Use modules directly
beam = BeamTheory()
column = ColumnTheory()

result = beam.euler_bernoulli(...)
```

## Return Value Patterns

All analysis methods return structured dictionaries with:

- **Arrays**: `x`, `deflection`, `moment`, `shear` for detailed analysis
- **Scalars**: `max_deflection`, `max_moment`, etc. for design verification
- **Engineering units**: Consistent SI units throughout

Example return structure:

```python
{
    'x': np.ndarray,              # Position array (m)
    'deflection': np.ndarray,     # Deflection array (m)
    'moment': np.ndarray,         # Moment array (N⋅m)
    'shear': np.ndarray,          # Shear array (N)
    'max_deflection': float,      # Maximum deflection (m)
    'max_moment': float,          # Maximum moment (N⋅m)
    'max_shear': float,           # Maximum shear (N)
}
```

## Type Safety

The library provides complete type annotations:

- **Input validation**: All parameters are type-checked
- **Return types**: Structured with TypedDict classes
- **IDE support**: Full autocomplete and type checking

## Error Handling

Methods include comprehensive validation:

- **Physical constraints**: Positive lengths, non-zero loads
- **Parameter ranges**: Valid material properties and dimensions
- **Boundary conditions**: Appropriate support conditions

## Development Status

Current implementation includes:

- ✅ **Beam Theory**: Euler-Bernoulli beam analysis
- ✅ **Column Theory**: Euler buckling analysis
- 🚧 **Additional theories**: See [development roadmap](../development/roadmap.md)

## Contributing

API documentation is auto-generated from docstrings. To improve documentation:

1. Update method docstrings in source code
2. Follow Google docstring format
3. Include examples and parameter descriptions
4. Document assumptions and limitations

See our [contributing guide](../contributing.md) for detailed guidelines.
