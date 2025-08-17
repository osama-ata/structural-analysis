You use UV for package and project management.
You use Ruff for linting and formatting.

## Structural Analysis Library Context

### 1. Project Goal

The primary goal of this project is to create a Python library that implements various structural analysis theories based on the `structural_analysis_theories_comprehensive.csv` file. The library should be well-structured, tested, and easy to use.

### 2. Codebase Structure

The project uses a `src` layout.

- The main user-facing class is `StructuralAnalysis` located in `src/structural_analysis/__init__.py`.
- Each category of theory from the CSV (e.g., "Beam Theory", "Column Theory") has its own module in `src/structural_analysis/` (e.g., `beam_theory.py`).
- Each theory is a method within its corresponding category class.

### 3. Key Concepts from the CSV

The library is directly generated from a CSV with the following columns:

- **Category**: The group the theory belongs to (e.g., `Beam Theory`). This maps to a Python module.
- **Theory Name**: The specific theory (e.g., `Euler-Bernoulli`). This maps to a method name.
- **Description**: High-level explanation of the theory.
- **Key Assumptions**: Important assumptions for the theory's validity.
- **Primary Applications**: Where the theory is commonly used.

This context will help Copilot understand the relationships between your modules and provide more relevant suggestions as your library grows.
