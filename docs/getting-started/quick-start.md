# Quick Start Guide

Get up and running with structural analysis in just 5 minutes!

## Your First Analysis

Let's analyze a simple steel beam under a point load:

```python
from structural_analysis import StructuralAnalysis

# Initialize the library
analysis = StructuralAnalysis()

# Define our beam properties
beam_result = analysis.beam_theory.euler_bernoulli(
    length=4.0,                    # 4 meter span
    E=200e9,                       # Steel modulus (200 GPa)
    second_moment=8.33e-6,         # I-beam second moment (m⁴)
    load_type="point",             # Point load
    load_magnitude=10000,          # 10 kN load
    load_position=2.0,             # At midspan
    boundary_conditions="simply_supported"
)

# Check the results
print(f"Maximum deflection: {beam_result['max_deflection']:.4f} m")
print(f"Maximum moment: {beam_result['max_moment']/1000:.1f} kN⋅m")
```

**Expected Output:**

```
Maximum deflection: 0.0032 m
Maximum moment: 10.0 kN⋅m
```

!!! success "Analysis Complete!"
    You've just performed your first structural analysis! The beam deflects 3.2 mm under the 10 kN load.

## Column Buckling Analysis

Now let's check if a column can support a compressive load:

```python
# Analyze column stability
column_result = analysis.column_theory.euler_buckling(
    length=3.0,                    # 3 meter height
    E=200e9,                       # Steel modulus
    second_moment=8.33e-6,         # Same I-beam section
    end_conditions="pinned"        # Pinned at both ends
)

applied_load = 50000  # 50 kN applied load

print(f"Critical buckling load: {column_result['critical_load']/1000:.1f} kN")
print(f"Applied load: {applied_load/1000:.1f} kN")
print(f"Safety factor: {column_result['critical_load']/applied_load:.2f}")

if column_result['critical_load'] > applied_load:
    print("✅ Column is safe against buckling")
else:
    print("❌ Column will buckle - increase section or reduce load")
```

## Understanding the Results

Every analysis returns a dictionary with comprehensive results:

### Beam Analysis Results

```python
{
    'x': array([...]),              # Position along beam (m)
    'deflection': array([...]),     # Deflection at each point (m)
    'moment': array([...]),         # Bending moment (N⋅m)
    'shear': array([...]),          # Shear force (N)
    'max_deflection': float,        # Maximum deflection (m)
    'max_moment': float,            # Maximum moment (N⋅m)
    'max_shear': float             # Maximum shear (N)
}
```

### Column Analysis Results

```python
{
    'critical_load': float,         # Euler buckling load (N)
    'slenderness_ratio': float,     # L/r ratio
    'effective_length': float,      # Effective length (m)
    'end_condition_factor': float   # K factor for end conditions
}
```

## Working with Arrays

The library returns NumPy arrays for plotting and further analysis:

```python
import matplotlib.pyplot as plt

# Get beam analysis results
result = analysis.beam_theory.euler_bernoulli(
    length=4.0, E=200e9, second_moment=8.33e-6,
    load_type="point", load_magnitude=10000, load_position=2.0,
    boundary_conditions="simply_supported"
)

# Plot deflection curve
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(result['x'], result['deflection'] * 1000)  # Convert to mm
plt.title('Beam Deflection')
plt.ylabel('Deflection (mm)')
plt.grid(True)

# Plot moment diagram
plt.subplot(2, 1, 2)
plt.plot(result['x'], result['moment'] / 1000)  # Convert to kN⋅m
plt.title('Bending Moment Diagram')
plt.xlabel('Position (m)')
plt.ylabel('Moment (kN⋅m)')
plt.grid(True)

plt.tight_layout()
plt.show()
```

## Different Load Types

The library supports various loading conditions:

### Point Load

```python
result = analysis.beam_theory.euler_bernoulli(
    length=4.0, E=200e9, second_moment=8.33e-6,
    load_type="point",
    load_magnitude=10000,      # Load magnitude (N)
    load_position=1.5,         # Position from left end (m)
    boundary_conditions="simply_supported"
)
```

### Distributed Load

```python
result = analysis.beam_theory.euler_bernoulli(
    length=4.0, E=200e9, second_moment=8.33e-6,
    load_type="distributed",
    load_magnitude=5000,       # Load per unit length (N/m)
    boundary_conditions="simply_supported"
)
```

### Applied Moment

```python
result = analysis.beam_theory.euler_bernoulli(
    length=4.0, E=200e9, second_moment=8.33e-6,
    load_type="moment",
    load_magnitude=15000,      # Applied moment (N⋅m)
    load_position=2.0,         # Position of moment (m)
    boundary_conditions="simply_supported"
)
```

## Boundary Conditions

### Simply Supported

```python
boundary_conditions="simply_supported"
```

- Pinned at both ends
- Can rotate but cannot translate
- Most common for beam analysis

### Cantilever

```python
boundary_conditions="cantilever"
```

- Fixed at one end, free at the other
- Common for overhangs and balconies

## Engineering Units

The library uses SI units consistently:

| Quantity | Unit | Symbol |
|----------|------|---------|
| Length | meters | m |
| Force | Newtons | N |
| Moment | Newton⋅meters | N⋅m |
| Stress | Pascals | Pa |
| Elastic Modulus | Pascals | Pa |
| Second Moment | meters⁴ | m⁴ |

!!! tip "Unit Conversions"
    - 1 kN = 1,000 N
    - 1 GPa = 1×10⁹ Pa
    - 1 mm = 0.001 m
    - 1 kN⋅m = 1,000 N⋅m

## Next Steps

Now that you've mastered the basics:

- **[Theory Guide](../theories/index.md)** - Understand the engineering behind each method
- **[Examples](../examples/index.md)** - See real-world engineering applications  
- **[API Reference](../api/index.md)** - Detailed documentation of all parameters
- **[Basic Concepts](concepts.md)** - Learn about the library architecture

Ready to dive deeper? Let's explore some [engineering examples](../examples/index.md)!
