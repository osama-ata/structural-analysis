# Structural Analysis Library

A comprehensive Python library for structural engineering analysis implementing various theoretical frameworks for beams, columns, plates, and other structural elements.

<div class="grid cards" markdown>

- :fontawesome-solid-calculator:{ .lg .middle } __Easy to Use__

    ---

    Simple, intuitive API designed by engineers for engineers. Get started with structural analysis in minutes, not hours.

    [:octicons-arrow-right-24: Getting Started](getting-started/installation.md)

- :fontawesome-solid-book:{ .lg .middle } __Theory-Driven__

    ---

    Built on established structural analysis principles. Every method is grounded in comprehensive engineering theory and analytical verification.

    [:octicons-arrow-right-24: Theory Guide](theories/index.md)

- :fontawesome-solid-code:{ .lg .middle } __Type Safe__

    ---

    Full type annotations and validated inputs ensure reliable calculations. Catch errors before they reach production.

    [:octicons-arrow-right-24: API Reference](api/index.md)

- :fontawesome-solid-flask:{ .lg .middle } __Verified Results__

    ---

    All implementations tested against analytical solutions. Trust your calculations with confidence.

    [:octicons-arrow-right-24: Examples](examples/index.md)

</div>

## Features

- __🎯 Engineering-Focused__: Designed specifically for structural engineers and researchers
- __� Comprehensive Theory Coverage__: Implementation of classical and advanced structural analysis methods
- __🔍 Complete Type Safety__: Full type annotations with runtime validation
- __✅ Analytical Verification__: All methods tested against known solutions
- __🚀 Modern Python__: Built with UV package management and Ruff linting
- __📱 Great Documentation__: Beautiful, searchable docs with mathematical notation

## Quick Example

```python
from structural_analysis import StructuralAnalysis

# Initialize the analysis library
analysis = StructuralAnalysis()

# Analyze a simply supported beam
result = analysis.beam_theory.euler_bernoulli(
    length=4.0,                    # 4 meter beam
    E=200e9,                       # Steel elastic modulus (Pa)
    second_moment=8.33e-6,         # Second moment of area (m⁴)
    load_type="point",             # Point load
    load_magnitude=10000,          # 10 kN load
    load_position=2.0,             # At center
    boundary_conditions="simply_supported"
)

print(f"Max deflection: {result['max_deflection']:.6f} m")
print(f"Max moment: {result['max_moment']:.0f} N·m")
```

## Supported Theories

The library currently implements theories from multiple categories:

| Category | Implemented | Total Available |
|----------|------------|-----------------|
| __Beam Theory__ | 2 | 6 |
| __Column Theory__ | 1 | 4 |
| __Dynamic Analysis__ | 0 | 3 |
| __Plate & Shell__ | 0 | 4 |
| __Advanced Methods__ | 0 | 10 |

!!! info "Continuous Development"
    New theories are continuously added based on the comprehensive CSV database. See our [development roadmap](development/architecture.md) for planned additions.

## Why This Library?

### For Practicing Engineers

- __Reliable__: Every calculation verified against analytical solutions
- __Fast__: Optimized NumPy implementations for production use
- __Documented__: Clear explanations of assumptions and limitations

### For Researchers

- __Extensible__: Easy to add new theories following established patterns
- __Transparent__: Full access to implementation details and theory sources
- __Collaborative__: Open-source development with engineering community

### For Software Developers

- __Type Safe__: Full type annotations prevent runtime errors
- __Modern__: Built with latest Python best practices
- __Tested__: Comprehensive test suite with analytical verification

## Getting Started

Ready to start analyzing structures? Choose your path:

=== "Quick Start"

    Jump right in with our quick start guide:
    
    [:octicons-arrow-right-24: Quick Start Guide](getting-started/quick-start.md)

=== "Learn the Theory"

    Understand the engineering principles behind each method:
    
    [:octicons-arrow-right-24: Theory Guide](theories/index.md)

=== "See Examples"

    Explore real-world engineering examples:
    
    [:octicons-arrow-right-24: Examples](examples/index.md)

=== "API Reference"

    Detailed documentation of all methods and parameters:
    
    [:octicons-arrow-right-24: API Reference](api/index.md)

## Community & Support

- __GitHub__: [Report issues](https://github.com/osama-ata/structural-analysis/issues) or contribute
- __Documentation__: Comprehensive guides and examples
- __License__: MIT - Free for commercial and academic use

---

*Built with ❤️ for the structural engineering community*
