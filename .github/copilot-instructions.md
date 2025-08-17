# Structural Analysis Library - Copilot Instructions

## Project Architecture

This is a **CSV-driven structural analysis library** that implements engineering theories from `structural_analysis_theories_comprehensive.csv`. The core pattern:

- Each CSV **Category** becomes a Python module (e.g., "Beam Theory" → `beam_theory.py`)
- Each **Theory Name** becomes a method (e.g., "Euler-Bernoulli" → `euler_bernoulli()`)
- Main facade class `StructuralAnalysis` exposes all theory modules via properties

## Critical Development Patterns

### Parameter Naming Convention

- Use descriptive names over engineering notation: `second_moment` instead of `I`
- Exception: Helper methods may use domain notation for clarity
- This addresses ruff E741 linting while maintaining engineering readability

### Theory Implementation Template

```python
def theory_name(
    self,
    # Geometric parameters first
    length: float,
    # Material properties
    E: float,
    # Load parameters with typed literals
    load_type: Literal["point", "distributed", "moment"],
    # Optional parameters with defaults
    boundary_conditions: Literal["simply_supported", "cantilever"] = "simply_supported",
    num_points: int = 100,
) -> Dict[str, Union[np.ndarray, float]]:
    """
    Include CSV theory description, assumptions, and applications in docstring.

    Returns:
        Dictionary with arrays (x, deflection, moment, shear) and scalars (max_*)
    """
```

### Essential Testing Pattern

Each theory requires analytical verification tests:

```python
def test_theory_analytical_case(self):
    """Test against known analytical solution."""
    result = self.theory.method(**params)
    expected = analytical_formula(**params)
    assert abs(result["max_deflection"] - expected) / expected < 0.01  # 1% tolerance
```

## Development Workflow Commands

**Environment Setup:**

```bash
uv sync  # Install dependencies
```

**Quality Assurance (critical sequence):**

```bash
ruff format .        # Format first
ruff check . --fix   # Then lint with auto-fixes
uv run pytest tests/test_beam_theory.py -v  # Test specific module
```

**Testing Individual Theories:**

```python
# Quick verification pattern used in development
python -c "
import sys; sys.path.append('src')
from structural_analysis.beam_theory import BeamTheory
beam = BeamTheory()
result = beam.euler_bernoulli(length=4.0, E=200e9, second_moment=8.33e-6, ...)
print(f'Max deflection: {result[\"max_deflection\"]:.6f} m')
"
```

## Data Flow Architecture

1. **CSV Theory Database** → defines all methods and their engineering context
2. **Theory Module Classes** → implement computational methods with numpy
3. **StructuralAnalysis Facade** → provides unified access to all theories
4. **Test Suite** → validates against analytical solutions (not just unit tests)

## Integration Points

- **UV Package Manager**: All dependency management, replaces pip/poetry
- **Ruff**: Single tool for formatting + linting (replaces black + flake8)
- **NumPy**: Core numerical engine - all computations return numpy arrays
- **Pytest**: Testing with analytical verification emphasis

## Engineering-Specific Considerations

- Return format consistency: Always `Dict[str, Union[np.ndarray, float]]`
- Include max values for engineering review: `max_deflection`, `max_moment`, etc.
- Validation patterns check for physical constraints (positive lengths, non-zero loads)
- Docstrings must include theory assumptions and applications from CSV data
