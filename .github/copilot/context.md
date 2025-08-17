# Structural Analysis Library Context

## 1. Project Goal

The primary goal of this project is to create a Python library that implements various structural analysis theories based on the `structural_analysis_theories_comprehensive.csv` file. The library should be well-structured, tested, and easy to use.

## 2. Codebase Structure

The project uses a `src` layout.

- The main user-facing class is `StructuralAnalysis` located in `src/structural_analysis/__init__.py`.
- Each category of theory from the CSV (e.g., "Beam Theory", "Column Theory") has its own module in `src/structural_analysis/` (e.g., `beam_theory.py`).
- Each theory is a method within its corresponding category class.

## 3. Key Concepts from the CSV

The library is directly generated from a CSV with the following columns:

- **Category**: The group the theory belongs to (e.g., `Beam Theory`). This maps to a Python module.
- **Theory Name**: The specific theory (e.g., `Euler-Bernoulli`). This maps to a method name.
- **Description**: High-level explanation of the theory.
- **Key Assumptions**: Important assumptions for the theory's validity.
- **Primary Applications**: Where the theory is commonly used.

## 4. Development Workflow

### 4.1 Environment Setup

- Use `uv` for dependency management and virtual environment
- Python 3.8+ required
- Dependencies managed in `pyproject.toml`

### 4.2 Code Quality Standards

- **Linting**: Use `ruff` for code linting and formatting
- **Testing**: Use `pytest` for unit testing with comprehensive test coverage
- **Type Hints**: Use type annotations throughout the codebase
- **Parameter Naming**: Use descriptive names (e.g., `second_moment` instead of `I` for moment of inertia)

### 4.3 Implementation Pattern

When implementing new theories:

1. Add method to appropriate category class (e.g., `BeamTheory`, `ColumnTheory`)
2. Include comprehensive docstrings with:
   - Theory description
   - Key assumptions
   - Primary applications
   - Parameter descriptions
   - Return value descriptions
   - Usage examples
3. Implement input validation
4. Add comprehensive unit tests in `tests/`
5. Ensure analytical verification where possible

### 4.4 Testing Strategy

- Each theory method should have corresponding tests
- Tests should verify against known analytical solutions
- Include boundary condition verification
- Test input validation and error handling
- Aim for high test coverage

### 4.5 Code Organization

- Keep theory implementations focused and single-purpose
- Use helper methods for complex calculations
- Maintain consistent return formats (typically dictionaries with arrays and scalars)
- Follow engineering notation conventions where appropriate

This context will help Copilot understand the relationships between your modules and provide more relevant suggestions as your library grows.
