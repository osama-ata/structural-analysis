# Theory Guide

!!! info "Comprehensive Theory Coverage"
    This section provides detailed explanations of all structural analysis theories implemented in the library.

## Available Theory Categories

### [Beam Theory](beam-theory/euler-bernoulli.md)

Classical and advanced beam analysis methods for various loading and boundary conditions.

- **[Euler-Bernoulli](beam-theory/euler-bernoulli.md)**: Classical beam bending theory
- **[Timoshenko](beam-theory/timoshenko.md)**: Includes shear deformation effects

### [Column Theory](column-theory/euler-buckling.md)

Stability analysis for columns under compression loads.

- **[Euler Buckling](column-theory/euler-buckling.md)**: Elastic buckling analysis
- **[Advanced Methods](column-theory/advanced.md)**: Inelastic and combined failure modes

### [Advanced Theories](advanced.md)

Additional structural analysis methods for specialized applications.

## Theory Implementation Standards

All theories in this library follow consistent patterns:

1. **Clear Assumptions**: Each theory documents its key assumptions and limitations
2. **Analytical Verification**: Methods are tested against known analytical solutions
3. **Engineering Units**: Consistent SI unit usage throughout
4. **Type Safety**: Full type annotations for all parameters
5. **Return Consistency**: Structured dictionaries with arrays and scalar values

## Using the Theories

Each theory page includes:

- **Mathematical Background**: Governing equations and derivations
- **Implementation Details**: How the theory is coded in the library
- **Usage Examples**: Practical engineering applications
- **Limitations**: When to use (and not use) each method
- **References**: Academic and code sources

## Navigation

- [**Examples**](../examples/index.md): See theories applied to real problems
- [**API Reference**](../api/index.md): Complete method documentation
- [**Development**](../development/roadmap.md): Theory roadmap and contributing
