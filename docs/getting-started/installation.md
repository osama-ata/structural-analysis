# Installation

Get started with the Structural Analysis Library in just a few steps.

## Requirements

- Python 3.8 or higher
- NumPy (automatically installed)

## Installation Methods

### Option 1: Using pip (Recommended for Users)

```bash
pip install structural-analysis
```

### Option 2: Using UV (Recommended for Development)

If you're planning to contribute or want the latest features:

```bash
# Install UV first (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install the library
uv add structural-analysis
```

### Option 3: From Source

For developers who want to contribute:

```bash
# Clone the repository
git clone https://github.com/osama-ata/structural-analysis.git
cd structural-analysis

# Install with UV (recommended)
uv sync

# Or install with pip
pip install -e .
```

## Verification

Verify your installation by running a simple test:

```python
from structural_analysis import StructuralAnalysis

# This should work without errors
analysis = StructuralAnalysis()
print("✅ Installation successful!")
print(f"Available modules: {', '.join(dir(analysis))}")
```

## Optional Dependencies

For enhanced functionality, you can install additional packages:

### Development Tools

```bash
# For contributing to the library
uv add --group dev pytest ruff mkdocs-material

# Or with pip
pip install pytest ruff mkdocs-material
```

### Jupyter Notebooks

```bash
# For running example notebooks
pip install jupyter matplotlib
```

## Troubleshooting

### Common Issues

#### ImportError: No module named 'structural_analysis'

**Solution**: Make sure you've activated your virtual environment:

```bash
# If using UV
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# If using standard Python
source venv/bin/activate   # Linux/Mac
# or
venv\Scripts\activate      # Windows
```

#### NumPy Installation Issues

**Solution**: Install NumPy separately first:

```bash
pip install numpy
pip install structural-analysis
```

#### Permission Errors on Windows

**Solution**: Run as administrator or use `--user` flag:

```bash
pip install --user structural-analysis
```

### Getting Help

If you encounter issues:

1. Check the [GitHub Issues](https://github.com/osama-ata/structural-analysis/issues)
2. Search existing issues for solutions
3. Create a new issue with:
   - Your Python version (`python --version`)
   - Your operating system
   - Complete error message
   - Steps to reproduce

## Next Steps

Once installed, continue with:

- [Quick Start Guide](quick-start.md) - Get analyzing structures in 5 minutes
- [Basic Concepts](concepts.md) - Understand the library architecture
- [Examples](../examples/index.md) - See real-world applications
