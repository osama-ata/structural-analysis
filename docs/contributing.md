# Contributing to Structural Analysis Library

Thank you for your interest in contributing! This guide will help you add new structural theories and improve the library.

## Development Setup

### Prerequisites

- Python 3.8+
- UV package manager (recommended) or pip
- Git

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/osama-ata/structural-analysis.git
cd structural-analysis

# Install with development dependencies
uv sync

# Or with pip
pip install -e ".[dev]"
```

### Development Tools

We use modern Python tooling:

- **UV**: Package management and virtual environments
- **Ruff**: Linting and formatting (replaces black + flake8)
- **Pytest**: Testing with analytical verification
- **MkDocs**: Documentation generation

## Code Quality Standards

### Formatting and Linting

Run these commands before submitting any changes:

```bash
# Format code (must run first)
uv run ruff format .

# Check linting and auto-fix issues
uv run ruff check . --fix

# Run tests
uv run pytest tests/ -v
```

### Parameter Naming Convention

Use descriptive names over engineering notation to avoid linting issues:

```python
# ✅ Good - descriptive names
def euler_bernoulli(self, length: float, E: float, second_moment: float):
    pass

# ❌ Avoid - single letter variables (triggers E741)
def euler_bernoulli(self, L: float, E: float, I: float):
    pass
```

**Exception**: Helper methods may use domain notation for clarity when the context is clear.

## Adding New Theories

### Step 1: Plan Your Theory

Review the [development roadmap](roadmap.md) to see planned theories or propose a new one:

- Check if your theory is already listed in `roadmap.csv`
- For new theories, ensure they fit the library's scope and patterns
- Consider the engineering context and practical applications

### Step 2: Implement the Theory

Add the method to the appropriate module (e.g., `beam_theory.py`):

```python
def your_new_theory(
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
    Brief description of the theory.
    
    Include theory assumptions, applications, and engineering context in docstring.
    
    Args:
        length: Beam length in meters
        E: Elastic modulus in Pa
        load_type: Type of applied load
        boundary_conditions: Support conditions
        num_points: Number of points for analysis
        
    Returns:
        Dictionary with arrays (x, deflection, moment, shear) and scalars (max_*)
        
    Raises:
        ValueError: If parameters are invalid
    """
    # Input validation
    if length <= 0:
        raise ValueError("Length must be positive")
    
    # Implementation here
    x = np.linspace(0, length, num_points)
    # ... calculations ...
    
    return {
        "x": x,
        "deflection": deflection_array,
        "moment": moment_array, 
        "shear": shear_array,
        "max_deflection": float(np.max(np.abs(deflection_array))),
        "max_moment": float(np.max(np.abs(moment_array))),
        "max_shear": float(np.max(np.abs(shear_array)))
    }
```

### Step 3: Write Tests

Create comprehensive tests in `tests/test_[module].py`:

```python
def test_your_new_theory_analytical_case(self):
    """Test against known analytical solution."""
    result = self.beam.your_new_theory(
        length=4.0,
        E=200e9,
        # ... other parameters
    )
    
    # Calculate expected result using analytical formula
    expected_deflection = analytical_formula(...)
    
    # Verify within 1% tolerance
    assert abs(result["max_deflection"] - expected_deflection) / expected_deflection < 0.01

def test_your_new_theory_edge_cases(self):
    """Test boundary conditions and edge cases."""
    # Test zero load
    # Test extreme geometry
    # Test different boundary conditions
    pass

def test_your_new_theory_validation(self):
    """Test input validation."""
    with pytest.raises(ValueError):
        self.beam.your_new_theory(length=-1.0, ...)  # Negative length
```

### Step 4: Update Documentation

Add theory documentation to `docs/theories/[category]/[theory-name].md`:

```markdown
# Your New Theory

Brief description and engineering context.

## Theory Background

Mathematical foundation and derivation.

## Implementation

How it's implemented in the library.

## Examples

Practical engineering examples.

## Limitations

Where this theory applies and doesn't apply.
```

## Testing Strategy

### Analytical Verification

Every theory must be tested against analytical solutions:

```python
def test_analytical_verification(self):
    """Compare library results with hand calculations."""
    # Use simple cases with known analytical solutions
    # Verify within engineering tolerance (typically 1%)
    pass
```

### Engineering Validation

Test realistic engineering scenarios:

```python
def test_engineering_scenarios(self):
    """Test typical engineering use cases."""
    # Standard beam sizes and loads
    # Typical material properties
    # Common boundary conditions
    pass
```

### Regression Testing

Ensure new changes don't break existing functionality:

```bash
# Run full test suite
uv run pytest tests/ -v

# Test specific module
uv run pytest tests/test_beam_theory.py -v
```

## Documentation Guidelines

### Code Documentation

- **Docstrings**: Use Google style with clear parameter descriptions
- **Type hints**: Full type annotations for all parameters
- **Examples**: Include usage examples in docstrings

### Theory Documentation

- **Engineering context**: Why and when to use this theory
- **Assumptions**: Clear statement of limitations
- **Mathematical foundation**: Key equations and derivations
- **Examples**: Real-world applications

### API Documentation

Auto-generated from docstrings using mkdocstrings:

```python
def method_name(self, param: float) -> Dict[str, float]:
    """
    Brief description.
    
    Longer description with engineering context from CSV database.
    
    Args:
        param: Description with units
        
    Returns:
        Dictionary with calculation results
        
    Raises:
        ValueError: When input validation fails
        
    Example:
        ```python
        result = analysis.method_name(param=1.0)
        print(f"Result: {result['key']}")
        ```
    """
```

## Pull Request Process

### Before Submitting

1. **Run all quality checks**:

   ```bash
   uv run ruff format .
   uv run ruff check . --fix
   uv run pytest tests/ -v
   ```

2. **Update documentation**:
   - Add theory to docs if new
   - Update API reference
   - Add examples if applicable

3. **Test documentation build**:

   ```bash
   uv run mkdocs serve
   ```

### PR Requirements

- [ ] All tests pass
- [ ] Code formatted with Ruff
- [ ] No linting errors
- [ ] Documentation updated
- [ ] Theory tested against analytical solution
- [ ] CSV database updated if adding new theory

### Review Process

1. **Automated checks**: CI runs tests and linting
2. **Engineering review**: Verify theory implementation and assumptions
3. **Documentation review**: Ensure clear explanations and examples
4. **Integration testing**: Verify compatibility with existing code

## Architecture Guidelines

### Theory-Driven Development

The library follows a systematic theory implementation approach:

1. **Development Roadmap**: `docs/development/roadmap.csv` defines all planned theories
2. **Module Structure**: Each theory category becomes a Python module
3. **Method Mapping**: Each theory becomes a class method
4. **Facade Pattern**: `StructuralAnalysis` class provides unified access

### Return Value Consistency

All methods return dictionaries with consistent structure:

```python
{
    "x": np.ndarray,           # Position arrays
    "result_type": np.ndarray, # Result arrays (deflection, stress, etc.)
    "max_result": float,       # Maximum values for engineering review
    # ... other relevant outputs
}
```

### Error Handling

- **Input Validation**: Check all parameters at method entry
- **Informative Errors**: Clear messages with engineering context
- **Graceful Degradation**: Handle edge cases appropriately

## Getting Help

- **GitHub Issues**: Report bugs or request features
- **Discussions**: Ask questions about implementation
- **Documentation**: Comprehensive guides and examples
- **Code Review**: Submit PRs for feedback

## Recognition

Contributors are recognized in:

- **GitHub Contributors**: Automatic recognition
- **Documentation**: Contributors page
- **Release Notes**: Major contributions highlighted

Thank you for helping make structural analysis more accessible to engineers worldwide!
