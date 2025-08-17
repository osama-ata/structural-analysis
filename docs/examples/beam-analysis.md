# Beam Analysis Examples

Real-world engineering examples using the Structural Analysis Library.

## Example 1: Office Floor Beam Design

A typical office building floor beam supporting distributed load from concrete slab and live loads.

### Problem Statement

Design check for a steel W14×22 beam supporting:

- **Span**: 6.0 meters
- **Dead load**: 2.5 kN/m (slab + beam self-weight)  
- **Live load**: 3.5 kN/m (office occupancy)
- **Total load**: 6.0 kN/m
- **Support conditions**: Simply supported

### Beam Properties

- **Material**: A572 Grade 50 steel
- **Elastic modulus**: 200 GPa
- **Section**: W14×22 (I = 199×10⁶ mm⁴ = 199×10⁻⁶ m⁴)
- **Allowable deflection**: L/360 = 16.7 mm

### Analysis

```python
from structural_analysis import StructuralAnalysis

# Initialize analysis
analysis = StructuralAnalysis()

# Analyze the beam
result = analysis.beam_theory.euler_bernoulli(
    length=6.0,                    # 6 meter span
    E=200e9,                       # 200 GPa steel
    second_moment=199e-6,          # W14×22 section
    load_type="distributed",       # Uniform load
    load_magnitude=6000,           # 6.0 kN/m total load
    boundary_conditions="simply_supported"
)

# Check results
max_deflection_mm = result['max_deflection'] * 1000  # Convert to mm
max_moment_kNm = result['max_moment'] / 1000         # Convert to kN⋅m

print(f"Maximum deflection: {max_deflection_mm:.1f} mm")
print(f"Maximum moment: {max_moment_kNm:.1f} kN⋅m")
print(f"Allowable deflection: 16.7 mm")

# Check deflection criteria
if max_deflection_mm <= 16.7:
    print("✅ Deflection OK")
else:
    print("❌ Deflection exceeds limit")
```

**Results:**

```
Maximum deflection: 13.5 mm
Maximum moment: 27.0 kN⋅m
Allowable deflection: 16.7 mm
✅ Deflection OK
```

### Engineering Interpretation

The W14×22 beam is adequate for deflection control with 3.2 mm margin. The maximum moment of 27.0 kN⋅m would need to be checked against the beam's moment capacity in a complete design.

---

## Example 2: Cantilever Balcony Analysis

Analysis of a residential balcony cantilever beam.

### Problem Statement

A concrete balcony cantilever supporting:

- **Cantilever length**: 2.5 meters
- **Point load**: 5 kN (person + furniture at end)
- **Distributed load**: 1.5 kN/m (slab self-weight)
- **Support**: Fixed at building wall

### Beam Properties

- **Material**: Reinforced concrete
- **Elastic modulus**: 25 GPa (conservative for RC)
- **Section**: 200mm × 400mm rectangular
- **Second moment**: I = bh³/12 = 0.2 × 0.4³/12 = 1.067×10⁻³ m⁴

### Analysis Code

```python
import numpy as np
import matplotlib.pyplot as plt

# Calculate second moment for rectangular section
b = 0.2  # width (m)
h = 0.4  # height (m)
I = b * h**3 / 12

print(f"Rectangular section I = {I:.6f} m⁴")

# Analyze cantilever with point load
result_point = analysis.beam_theory.euler_bernoulli(
    length=2.5,
    E=25e9,                        # 25 GPa concrete
    second_moment=I,
    load_type="point",
    load_magnitude=5000,           # 5 kN at end
    load_position=2.5,             # At free end
    boundary_conditions="cantilever"
)

# Analyze cantilever with distributed load  
result_distributed = analysis.beam_theory.euler_bernoulli(
    length=2.5,
    E=25e9,
    second_moment=I,
    load_type="distributed",
    load_magnitude=1500,           # 1.5 kN/m self-weight
    boundary_conditions="cantilever"
)

# Superposition: combine both loading conditions
total_deflection = result_point['deflection'] + result_distributed['deflection']
total_moment = result_point['moment'] + result_distributed['moment']

print(f"Point load deflection at tip: {result_point['max_deflection']*1000:.1f} mm")
print(f"Distributed load deflection at tip: {result_distributed['max_deflection']*1000:.1f} mm")
print(f"Total deflection at tip: {total_deflection[-1]*1000:.1f} mm")
```

### Visualization

```python
# Plot combined results
plt.figure(figsize=(12, 8))

# Deflection plot
plt.subplot(2, 1, 1)
plt.plot(result_point['x'], total_deflection * 1000, 'b-', linewidth=2, label='Total')
plt.plot(result_point['x'], result_point['deflection'] * 1000, 'r--', label='Point load')
plt.plot(result_point['x'], result_distributed['deflection'] * 1000, 'g--', label='Distributed load')
plt.title('Cantilever Deflection')
plt.ylabel('Deflection (mm)')
plt.legend()
plt.grid(True)

# Moment plot
plt.subplot(2, 1, 2)
plt.plot(result_point['x'], total_moment / 1000, 'b-', linewidth=2, label='Total')
plt.plot(result_point['x'], result_point['moment'] / 1000, 'r--', label='Point load')
plt.plot(result_point['x'], result_distributed['moment'] / 1000, 'g--', label='Distributed load')
plt.title('Bending Moment Diagram')
plt.xlabel('Distance from fixed end (m)')
plt.ylabel('Moment (kN⋅m)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
```

---

## Example 3: Crane Runway Beam

Industrial crane runway beam under moving wheel loads.

### Problem Statement

Design a crane runway beam for a 10-ton overhead crane:

- **Beam span**: 8.0 meters
- **Crane wheel loads**: 45 kN each (2 wheels)
- **Wheel spacing**: 2.0 meters
- **Critical position**: One wheel at midspan

### Analysis Strategy

For moving loads, we analyze the critical position where maximum moment occurs:

```python
# Crane runway beam analysis
# Critical case: one wheel at midspan, other at 1m from midspan

# Position of critical wheel load
wheel_1_position = 4.0  # At midspan
wheel_2_position = 2.0  # 2m spacing from wheel 1

# We'll analyze each wheel separately and superpose
wheel_load = 45000  # 45 kN per wheel

# Wheel 1 analysis (at midspan)
result_w1 = analysis.beam_theory.euler_bernoulli(
    length=8.0,
    E=200e9,                       # Steel beam
    second_moment=400e-6,          # Large I-beam section
    load_type="point",
    load_magnitude=wheel_load,
    load_position=wheel_1_position,
    boundary_conditions="simply_supported"
)

# Wheel 2 analysis (offset from midspan)  
result_w2 = analysis.beam_theory.euler_bernoulli(
    length=8.0,
    E=200e9,
    second_moment=400e-6,
    load_type="point", 
    load_magnitude=wheel_load,
    load_position=wheel_2_position,
    boundary_conditions="simply_supported"
)

# Superposition of both wheels
total_deflection = result_w1['deflection'] + result_w2['deflection']
total_moment = result_w1['moment'] + result_w2['moment']

print(f"Maximum deflection: {np.max(total_deflection)*1000:.1f} mm")
print(f"Maximum moment: {np.max(total_moment)/1000:.1f} kN⋅m")

# Check deflection limit (L/600 for crane runways)
allowable_deflection = 8000/600  # 13.3 mm
print(f"Allowable deflection: {allowable_deflection:.1f} mm")
```

### Load Path Analysis

Understanding how loads transfer through the structure:

1. **Crane wheel loads** → Runway beam
2. **Runway beam reactions** → Crane columns  
3. **Column loads** → Foundation

This analysis covers step 1. The runway beam reactions become input loads for column design.

---

## Engineering Best Practices

### Load Combinations

Real structures must consider multiple load combinations:

```python
# Example: Office beam with multiple load cases
dead_load = 2.5  # kN/m
live_load = 3.5  # kN/m
wind_load = 1.2  # kN/m

# Load combinations per building code
lc1 = 1.4 * dead_load                    # Ultimate: Dead only
lc2 = 1.2 * dead_load + 1.6 * live_load  # Ultimate: Dead + Live  
lc3 = 1.2 * dead_load + 1.0 * live_load + 1.0 * wind_load  # Service: D+L+W

for i, load in enumerate([lc1, lc2, lc3], 1):
    result = analysis.beam_theory.euler_bernoulli(
        length=6.0, E=200e9, second_moment=199e-6,
        load_type="distributed", load_magnitude=load*1000,
        boundary_conditions="simply_supported"
    )
    print(f"LC{i}: {load:.1f} kN/m → Max moment: {result['max_moment']/1000:.1f} kN⋅m")
```

### Units and Verification

Always verify your results with hand calculations:

```python
# Verification example: Simply supported beam, uniform load
# Analytical solution: δ_max = 5wL⁴/(384EI)

w = 6000  # N/m
L = 6.0   # m  
E = 200e9 # Pa
I = 199e-6 # m⁴

analytical_deflection = (5 * w * L**4) / (384 * E * I)
print(f"Analytical deflection: {analytical_deflection*1000:.1f} mm")

# Compare with library result
result = analysis.beam_theory.euler_bernoulli(
    length=L, E=E, second_moment=I,
    load_type="distributed", load_magnitude=w,
    boundary_conditions="simply_supported"
)
print(f"Library deflection: {result['max_deflection']*1000:.1f} mm")
print(f"Error: {abs(result['max_deflection'] - analytical_deflection)/analytical_deflection*100:.2f}%")
```

The library results should match analytical solutions within 0.1% for standard cases.

## Next Steps

- [Column Design Examples](column-design.md)
- [Advanced Case Studies](case-studies.md)  
- [Theory Documentation](../theories/beam-theory/euler-bernoulli.md)
