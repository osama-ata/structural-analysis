# Structural Analysis Library

A comprehensive Python library for structural engineering analysis implementing various theoretical frameworks for beams, columns, plates, and other structural elements.

## 🚀 Features

- **CSV-Driven Architecture**: Theories automatically generated from comprehensive engineering database
- **Complete Type Safety**: Full type annotations and validated inputs
- **Engineering-Focused**: Designed by engineers, for engineers
- **Analytical Verification**: All implementations tested against known analytical solutions
- **Modern Python**: Built with UV package management and Ruff linting

## 📦 Installation

```bash
# Using pip
pip install structural-analysis

# Using UV (recommended for development)
uv add structural-analysis
```

## 🏗️ Quick Start

```python
from structural_analysis import StructuralAnalysis

# Initialize the analysis library
analysis = StructuralAnalysis()

# Analyze a simply supported beam
beam_result = analysis.beam_theory.euler_bernoulli(
    length=4.0,                    # 4 meter beam
    E=200e9,                       # Steel elastic modulus (Pa)
    second_moment=8.33e-6,         # Second moment of area (m^4)
    load_type="point",             # Point load
    load_magnitude=10000,          # 10 kN load
    load_position=2.0,             # At center
    boundary_conditions="simply_supported"
)

print(f"Max deflection: {beam_result['max_deflection']:.6f} m")
print(f"Max moment: {beam_result['max_moment']:.0f} N·m")

# Analyze column buckling
column_result = analysis.column_theory.euler_buckling(
    length=3.0,                    # 3 meter column
    E=200e9,                       # Steel elastic modulus (Pa)
    second_moment=8.33e-6,         # Second moment of area (m^4)
    end_conditions="pinned",       # Pinned-pinned ends
    safety_factor=2.0              # Design safety factor
)

print(f"Critical load: {column_result['critical_load']/1000:.1f} kN")
print(f"Design load: {column_result['design_load']/1000:.1f} kN")
print(f"Recommendation: {column_result['recommendation']}")
```

## 📚 Available Theories

### Beam Theory

- **Euler-Bernoulli**: Classical beam bending for slender beams
- **Timoshenko**: Includes shear deformation effects (coming soon)
- **Reddy-Bickford**: Higher-order shear theory (coming soon)

### Column Theory

- **Euler Buckling**: ✅ Elastic buckling analysis with multiple end conditions
- **Rankine-Gordon**: Combined buckling-crushing (coming soon)
- **Johnson Parabolic**: Inelastic buckling (coming soon)

### Additional Categories

- **Plate/Shell Theory**: Kirchhoff, Mindlin-Reissner theories
- **Material Theory**: Linear elastic, elastic-plastic, viscoelastic
- **Dynamic Theory**: Natural frequencies, response analysis
- **Energy Methods**: Castigliano's theorem, virtual work
- **And many more...**

## 🔧 Advanced Usage

### Beam Analysis with Different Loading

```python
# Distributed load on cantilever
cantilever_result = analysis.beam_theory.euler_bernoulli(
    length=3.0,
    E=200e9,
    second_moment=5.21e-6,
    load_type="distributed",
    load_magnitude=5000,           # 5 kN/m
    boundary_conditions="cantilever",
    num_points=200                 # High resolution analysis
)

# Applied moment
moment_result = analysis.beam_theory.euler_bernoulli(
    length=4.0,
    E=200e9,
    second_moment=8.33e-6,
    load_type="moment",
    load_magnitude=15000,          # 15 kN·m
    load_position=1.0,             # 1m from left end
    boundary_conditions="simply_supported"
)
```

### Column Analysis with Different End Conditions

```python
# Fixed-fixed column (strongest)
fixed_result = analysis.column_theory.euler_buckling(
    length=4.0,
    E=200e9,
    second_moment=8.33e-6,
    end_conditions="fixed",        # K = 0.5
    safety_factor=2.5
)

# Cantilever column (weakest)
cantilever_result = analysis.column_theory.euler_buckling(
    length=4.0,
    E=200e9,
    second_moment=8.33e-6,
    end_conditions="fixed_free",   # K = 2.0
    safety_factor=3.0
)

print(f"Fixed-fixed critical load: {fixed_result['critical_load']/1000:.1f} kN")
print(f"Cantilever critical load: {cantilever_result['critical_load']/1000:.1f} kN")
print(f"Strength ratio: {fixed_result['critical_load']/cantilever_result['critical_load']:.1f}")
```

## 🎯 Return Value Structure

All analysis methods return structured dictionaries with both arrays and scalars:

```python
{
    # Arrays for plotting and detailed analysis
    'x': np.array([...]),              # Position coordinates
    'deflection': np.array([...]),     # Deflection values
    'moment': np.array([...]),         # Moment values
    'shear': np.array([...]),          # Shear values
    
    # Scalars for engineering review
    'max_deflection': float,           # Maximum deflection
    'max_moment': float,               # Maximum moment
    'max_shear': float,                # Maximum shear
}
```

## 🏛️ Architecture

The library follows a CSV-driven architecture where:

1. **Categories** (e.g., "Beam Theory") → Python modules (`beam_theory.py`)
2. **Theory Names** (e.g., "Euler-Bernoulli") → Class methods (`euler_bernoulli()`)
3. **Main Class** `StructuralAnalysis` → Unified access to all theories

```text
StructuralAnalysis
├── beam_theory (BeamTheory)
│   ├── euler_bernoulli()
│   ├── timoshenko()
│   └── ...
├── column_theory (ColumnTheory)
│   ├── euler_buckling()
│   ├── rankine_gordon()
│   └── ...
└── ... (other theory categories)
```

## 🧪 Testing and Validation

All implementations are validated against analytical solutions:

```bash
# Run all tests
uv run pytest tests/ -v

# Run specific theory tests
uv run pytest tests/test_beam_theory.py -v
uv run pytest tests/test_column_theory.py -v

# Check code quality
ruff format .
ruff check . --fix
```

## 🛠️ Development

### Environment Setup

```bash
# Clone and setup
git clone https://github.com/your-username/structural-analysis.git
cd structural-analysis
uv sync

# Activate environment
uv shell
```

### Adding New Theories

1. Add theory to `structural_analysis_theories_comprehensive.csv`
2. Implement method in appropriate module (e.g., `beam_theory.py`)
3. Add comprehensive tests with analytical verification
4. Run quality checks: `ruff format . && ruff check . --fix`

## 📖 Engineering Background

This library implements classical structural engineering theories with modern software practices:

- **Euler-Bernoulli Beam Theory**: Small deflections, plane sections remain plane
- **Euler Buckling Theory**: Elastic instability of perfect columns
- **Engineering Units**: SI units throughout (N, Pa, m, kg)
- **Safety Factors**: Built-in design load calculations
- **Boundary Conditions**: Complete support for real-world constraints

## 🤝 Contributing

We welcome contributions! Please see our development workflow in `.github/copilot-instructions.md`.

## 📄 License

MIT License - see LICENSE file for details.

## 🔗 References

- Timoshenko, S.P. & Gere, J.M. "Theory of Elastic Stability"
- Hibbeler, R.C. "Structural Analysis"
- Classical structural engineering texts and modern research

---

Built with ❤️ for the structural engineering community
