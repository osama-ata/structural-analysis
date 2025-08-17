# Adding New Theories

!!! tip "Step-by-Step Theory Implementation Guide"
    This guide walks through the complete process of adding a new structural analysis theory to the library.

## Before You Start

### 1. Check the Roadmap

Review the [development roadmap](roadmap.md) to ensure your theory is planned and prioritized. If not listed, consider opening a GitHub issue to discuss adding it.

### 2. Research the Theory

Thoroughly understand the mathematical background:

- **Governing equations**: Differential equations, formulas
- **Assumptions**: Key limitations and assumptions
- **Applications**: Where the theory is most applicable
- **Limitations**: Known constraints and accuracy limits
- **Test cases**: Analytical solutions for verification

### 3. Study Existing Code

Review existing implementations to understand patterns:

- **Method signatures**: Parameter naming and type annotations
- **Input validation**: Error checking patterns
- **Return structures**: Output format consistency
- **Test approaches**: Analytical verification methods

## Implementation Process

### Step 1: Method Signature Design

Design a clear, consistent method signature:

```python
def theory_name(
    self,
    # Required geometric parameters
    length: float,
    width: float,
    
    # Required material properties
    E: float,
    poisson_ratio: float,
    
    # Load parameters with type constraints
    load_type: Literal["point", "distributed", "moment"],
    load_magnitude: float,
    
    # Optional parameters with defaults
    boundary_conditions: Literal["simply_supported", "clamped"] = "simply_supported",
    num_points: int = 100,
) -> Dict[str, Union[np.ndarray, float]]:
    """
    Brief theory description.
    
    Detailed explanation of the theory, its assumptions, and applications.
    Include key governing equations and limitations.
    
    Args:
        length: Length description with units (m)
        width: Width description with units (m)
        E: Elastic modulus (Pa)
        load_type: Type of applied load
        ...
        
    Returns:
        Dictionary containing arrays and scalar values for analysis results.
        
    Raises:
        ValueError: Description of validation errors
        
    Examples:
        >>> theory = TheoryClass()
        >>> result = theory.theory_name(...)
        >>> print(f"Max response: {result['max_response']:.6f}")
        
    References:
        - Author, "Book Title", Year
        - Journal paper citations
    """
```

### Step 2: Input Validation

Implement comprehensive validation:

```python
def theory_name(self, length: float, E: float, ...):
    """Theory implementation with validation."""
    
    # Type checking (handled by type annotations)
    
    # Physical validation
    if length <= 0:
        raise ValueError("Length must be positive")
    if E <= 0:
        raise ValueError("Elastic modulus must be positive")
    if not 0 < poisson_ratio < 0.5:
        raise ValueError("Poisson's ratio must be between 0 and 0.5")
    
    # Engineering validation  
    if length > 1000:  # Warn for very large structures
        import warnings
        warnings.warn("Large length detected - verify units are correct")
        
    # Load validation
    valid_load_types = ["point", "distributed", "moment"]
    if load_type not in valid_load_types:
        raise ValueError(f"load_type must be one of {valid_load_types}")
    
    # Boundary condition validation
    valid_bc = ["simply_supported", "clamped", "free"]
    if boundary_conditions not in valid_bc:
        raise ValueError(f"boundary_conditions must be one of {valid_bc}")
```

### Step 3: Core Implementation

Implement the theoretical calculations:

```python
def theory_name(self, ...):
    """Theory implementation."""
    
    # Validation (from Step 2)
    ...
    
    # Generate analysis points
    x = np.linspace(0, length, num_points)
    
    # Initialize result arrays
    response = np.zeros_like(x)
    moment = np.zeros_like(x)
    shear = np.zeros_like(x)
    
    # Apply theory equations
    if load_type == "point":
        response = self._point_load_solution(x, length, E, I, load_magnitude, ...)
        moment = self._moment_from_deflection(x, response, E, I)
        shear = self._shear_from_moment(x, moment)
    elif load_type == "distributed":
        response = self._distributed_load_solution(x, length, E, I, load_magnitude, ...)
        # ... calculate moment and shear
    
    # Calculate summary statistics
    max_response = float(np.max(np.abs(response)))
    max_moment = float(np.max(np.abs(moment)))
    max_shear = float(np.max(np.abs(shear)))
    
    # Return structured result
    return {
        'x': x,
        'response': response,           # Primary response (deflection, stress, etc.)
        'moment': moment,
        'shear': shear,
        'max_response': max_response,
        'max_moment': max_moment,
        'max_shear': max_shear,
    }
```

### Step 4: Helper Methods

Implement private helper methods for clarity:

```python
def _point_load_solution(self, x: np.ndarray, L: float, E: float, I: float, 
                        P: float, a: float) -> np.ndarray:
    """Calculate deflection for point load at position a."""
    
    deflection = np.zeros_like(x)
    
    # Left side of load (0 ≤ x ≤ a)
    mask_left = x <= a
    x_left = x[mask_left]
    deflection[mask_left] = (P * x_left * (L**2 - x_left**2) * (L - a)) / (6 * E * I * L)
    
    # Right side of load (a < x ≤ L)  
    mask_right = x > a
    x_right = x[mask_right]
    deflection[mask_right] = (P * a * (2*L*x_right - x_right**2 - a**2)) / (6 * E * I)
    
    return deflection

def _apply_boundary_conditions(self, x: np.ndarray, deflection: np.ndarray, 
                              boundary_conditions: str) -> np.ndarray:
    """Apply boundary conditions to solution."""
    
    if boundary_conditions == "simply_supported":
        # Deflection is zero at ends (already satisfied by equations)
        pass
    elif boundary_conditions == "clamped":
        # Both deflection and slope are zero at ends
        # Apply corrections if needed
        pass
    
    return deflection
```

### Step 5: Write Tests

Create comprehensive test suite:

```python
import pytest
import numpy as np
from structural_analysis.theory_module import TheoryClass

class TestTheoryName:
    """Test suite for new theory implementation."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.theory = TheoryClass()
        
    def test_theory_analytical_case_1(self):
        """Test against known analytical solution - Case 1."""
        
        # Test parameters
        L, E, I, P = 4.0, 200e9, 8.33e-6, 10000
        
        # Library calculation
        result = self.theory.theory_name(
            length=L, E=E, second_moment=I,
            load_type="point", load_magnitude=P,
            boundary_conditions="simply_supported"
        )
        
        # Analytical solution (from textbook/reference)
        expected_max = analytical_formula(L, E, I, P)
        
        # Verify within tolerance
        relative_error = abs(result['max_response'] - expected_max) / expected_max
        assert relative_error < 0.01, f"Error {relative_error:.3%} exceeds 1% tolerance"
        
    def test_theory_analytical_case_2(self):
        """Test against known analytical solution - Case 2."""
        # Additional test case with different parameters
        ...
        
    def test_input_validation(self):
        """Test input validation and error handling."""
        
        valid_params = {
            'length': 4.0, 'E': 200e9, 'second_moment': 8.33e-6,
            'load_type': 'point', 'load_magnitude': 1000
        }
        
        # Test invalid length
        with pytest.raises(ValueError, match="Length must be positive"):
            params = valid_params.copy()
            params['length'] = -1.0
            self.theory.theory_name(**params)
            
        # Test invalid elastic modulus
        with pytest.raises(ValueError, match="Elastic modulus must be positive"):
            params = valid_params.copy()
            params['E'] = -200e9
            self.theory.theory_name(**params)
            
        # Test invalid boundary conditions
        with pytest.raises(ValueError, match="boundary_conditions must be"):
            params = valid_params.copy()
            params['boundary_conditions'] = 'invalid'
            self.theory.theory_name(**params)
            
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        
        # Test very small loads
        result = self.theory.theory_name(
            length=4.0, E=200e9, second_moment=8.33e-6,
            load_type="point", load_magnitude=1e-6  # Very small load
        )
        assert result['max_response'] > 0  # Should still have response
        
        # Test very stiff beam (large E*I)
        result = self.theory.theory_name(
            length=4.0, E=500e9, second_moment=1e-3,  # Very stiff
            load_type="point", load_magnitude=10000
        )
        assert result['max_response'] < 1e-6  # Should be very small deflection
```

### Step 6: Integration

Add the new theory to the appropriate module:

```python
# In theory_module.py
class TheoryModuleClass:
    """Theory module class containing related methods."""
    
    def existing_method(self, ...):
        """Existing method in module."""
        ...
        
    def new_theory_name(self, ...):
        """Your new theory implementation."""
        ...
```

Update the main facade class if needed:

```python
# In __init__.py
class StructuralAnalysis:
    """Main facade class."""
    
    def __init__(self):
        self.beam_theory = BeamTheory()
        self.column_theory = ColumnTheory()
        # Add new module if it's a new category
        self.new_theory_module = NewTheoryModule()
```

### Step 7: Documentation

Create theory documentation page:

```markdown
# New Theory Name

## Mathematical Background

Detailed explanation of the theory including:
- Governing equations
- Key assumptions  
- Derivation steps (if helpful)

## Implementation

::: module_name.ClassName.method_name

## Applications

Where this theory is most useful:
- Application 1
- Application 2

## Limitations

- Limitation 1
- Limitation 2

## Examples

Practical usage examples

## References

- Academic sources
- Textbook references
```

## Quality Checklist

Before submitting your implementation:

### Code Quality

- [ ] **Follows naming conventions**: Descriptive parameter names
- [ ] **Complete type annotations**: All parameters and return values
- [ ] **Input validation**: Comprehensive error checking
- [ ] **Clear docstring**: Theory background, examples, references
- [ ] **Helper methods**: Complex logic broken into smaller functions

### Testing

- [ ] **Analytical verification**: Tested against known solutions
- [ ] **Multiple test cases**: At least 3 different scenarios  
- [ ] **Edge case testing**: Boundary conditions and limits
- [ ] **Error condition testing**: Invalid inputs handled properly
- [ ] **95%+ code coverage**: All logic paths tested

### Documentation

- [ ] **Theory page**: Mathematical background and limitations
- [ ] **Usage examples**: Practical engineering applications
- [ ] **API documentation**: Auto-generated from docstrings
- [ ] **Updated roadmap**: Mark theory as implemented

### Integration

- [ ] **Follows patterns**: Consistent with existing implementations
- [ ] **No regressions**: All existing tests still pass
- [ ] **Performance**: Reasonable computational efficiency
- [ ] **Backwards compatibility**: Doesn't break existing API

## Getting Help

- **Study existing implementations**: Best learning resource
- **GitHub discussions**: Ask questions about approach
- **Engineering references**: Verify mathematical correctness
- **Code review process**: Iterative improvement through feedback

Following this guide ensures your theory implementation will be robust, well-tested, and consistent with the library's engineering focus.
