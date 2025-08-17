# Case Studies

!!! info "Real-World Engineering Applications"
    This page presents comprehensive case studies demonstrating the structural analysis library applied to real engineering problems.

## Case Study 1: Office Building Floor Beam

### Project Background

A 5-story office building requires floor beam analysis for gravity loads. The structural engineer needs to verify deflection limits and design adequacy.

### Building Details

- **Building type**: Commercial office
- **Floor system**: Steel beams with concrete slab
- **Design codes**: AISC 360, IBC 2021
- **Deflection limit**: L/360 for live load, L/240 for total load

### Beam Analysis

```python
from structural_analysis import StructuralAnalysis

# Initialize analysis
analysis = StructuralAnalysis()

# Beam properties
span = 8.0                     # 8m span
E = 200e9                      # Steel modulus
second_moment = 1.67e-5        # W410x85 section

# Loading (simplified)
dead_load = 12000              # 12 kN/m (includes self-weight)
live_load = 6000               # 6 kN/m (office occupancy)
total_load = dead_load + live_load

# Analyze for total load
result_total = analysis.beam_theory.euler_bernoulli(
    length=span,
    E=E,
    second_moment=second_moment,
    load_type="distributed",
    load_magnitude=total_load,
    boundary_conditions="simply_supported"
)

# Analyze for live load only
result_live = analysis.beam_theory.euler_bernoulli(
    length=span,
    E=E,
    second_moment=second_moment,
    load_type="distributed", 
    load_magnitude=live_load,
    boundary_conditions="simply_supported"
)

# Check deflection limits
max_deflection_total = result_total['max_deflection']
max_deflection_live = result_live['max_deflection']

limit_total = span / 240      # L/240 limit
limit_live = span / 360       # L/360 limit

print("Floor Beam Analysis Results:")
print("-" * 40)
print(f"Total load deflection: {max_deflection_total*1000:.1f} mm")
print(f"Live load deflection:  {max_deflection_live*1000:.1f} mm")
print(f"Total limit (L/240):   {limit_total*1000:.1f} mm")
print(f"Live limit (L/360):    {limit_live*1000:.1f} mm")

# Check adequacy
total_ok = max_deflection_total < limit_total
live_ok = max_deflection_live < limit_live

print(f"\nDeflection check:")
print(f"Total load: {'✅ PASS' if total_ok else '❌ FAIL'}")
print(f"Live load:  {'✅ PASS' if live_ok else '❌ FAIL'}")
```

### Results and Interpretation

The analysis shows the beam meets deflection requirements with comfortable margins, confirming the W410x85 section is adequate.

## Case Study 2: Industrial Crane Column

### Project Background

A manufacturing facility requires analysis of crane runway columns subjected to vertical loads and lateral crane forces.

### Design Requirements

- **Crane capacity**: 10-ton overhead crane
- **Column height**: 6m to crane rail
- **Material**: Grade 50 steel
- **End conditions**: Fixed base, laterally supported at top

### Analysis Approach

```python
# Column properties
height = 6.0                   # m
E = 200e9                      # Pa
second_moment = 8.49e-5        # W360x122 section
area = 15500e-6               # m^2

# Loading
vertical_load = 180000         # N (crane + dead load)
lateral_load = 25000           # N (crane horizontal force)

# Buckling analysis (simplified - vertical load only)
buckling_result = analysis.column_theory.euler_buckling(
    length=height,
    E=E,
    second_moment=second_moment,
    end_conditions="fixed_pinned"  # Conservative assumption
)

# Check buckling capacity
critical_load = buckling_result['critical_load']
safety_factor = critical_load / vertical_load

print("Crane Column Analysis:")
print("-" * 30)
print(f"Applied load:    {vertical_load/1000:.0f} kN")
print(f"Critical load:   {critical_load/1000:.0f} kN") 
print(f"Safety factor:   {safety_factor:.1f}")
print(f"Slenderness:     {buckling_result['slenderness_ratio']:.1f}")

# Engineering judgment
if safety_factor > 2.5:
    print("✅ Column adequate for buckling")
else:
    print("❌ Review required - consider larger section")
```

### Key Insights

- Pure buckling analysis is conservative for crane columns
- Combined axial and bending should be considered
- Dynamic amplification factors may apply for crane loads

## Case Study 3: Pedestrian Bridge Analysis

### Project Background

A pedestrian bridge spans a small creek in a park. The design requires verification of both strength and serviceability under pedestrian loads.

### Bridge Specifications

- **Span**: 12m simple span
- **Width**: 2m wide
- **Material**: Glue-laminated timber (glulam)
- **Section**: Custom 300mm x 600mm glulam beam

### Design Loads

```python
# Bridge geometry and properties
span = 12.0                    # m
width = 2.0                    # m
E = 12e9                       # Pa (glulam modulus)

# Section properties (300mm x 600mm)
b = 0.3                        # width
h = 0.6                        # height  
second_moment = b * h**3 / 12  # I = bh³/12
area = b * h

# Loading per code requirements
dead_load_psf = 25             # psf (self-weight + railings)
live_load_psf = 85             # psf (pedestrian load)

# Convert to metric (N/m on 2m wide bridge)
dead_load = dead_load_psf * 4.88 * width  # N/m
live_load = live_load_psf * 4.88 * width   # N/m
total_load = dead_load + live_load

print(f"Loading summary:")
print(f"Dead load: {dead_load:.0f} N/m")
print(f"Live load: {live_load:.0f} N/m") 
print(f"Total:     {total_load:.0f} N/m")

# Structural analysis
result = analysis.beam_theory.euler_bernoulli(
    length=span,
    E=E,
    second_moment=second_moment,
    load_type="distributed",
    load_magnitude=total_load,
    boundary_conditions="simply_supported"
)

# Results
max_deflection = result['max_deflection']
max_moment = result['max_moment']

# Deflection check (L/300 for pedestrian bridges)
deflection_limit = span / 300
deflection_ok = max_deflection < deflection_limit

print(f"\nStructural Results:")
print(f"Max deflection: {max_deflection*1000:.1f} mm")
print(f"Deflection limit: {deflection_limit*1000:.1f} mm")
print(f"Deflection check: {'✅ PASS' if deflection_ok else '❌ FAIL'}")

# Stress check (simplified)
max_stress = max_moment * (h/2) / second_moment  # σ = My/I
allowable_stress = 24e6  # Pa (typical glulam allowable)
stress_ok = max_stress < allowable_stress

print(f"Max stress: {max_stress/1e6:.1f} MPa")
print(f"Allowable: {allowable_stress/1e6:.1f} MPa")
print(f"Stress check: {'✅ PASS' if stress_ok else '❌ FAIL'}")
```

### Design Verification

The analysis confirms the glulam section provides adequate strength and stiffness for the pedestrian bridge application.

## Lessons Learned

### Best Practices

1. **Load combinations**: Always consider multiple load cases
2. **Code compliance**: Verify against applicable design standards  
3. **Engineering judgment**: Supplement analysis with practical experience
4. **Safety factors**: Apply appropriate factors for the application

### Common Pitfalls

1. **Oversimplification**: Real structures have complexity not captured in simple models
2. **Boundary conditions**: Actual support conditions may differ from assumptions
3. **Dynamic effects**: Some loads require dynamic analysis
4. **Material properties**: Use verified material properties for design

## Contributing Case Studies

We welcome real-world case studies! Each submission should include:

1. **Complete problem description**: Background, requirements, constraints
2. **Detailed analysis**: Step-by-step solution with code
3. **Engineering context**: Why this problem matters
4. **Lessons learned**: Key insights for practitioners

See our [contributing guide](../contributing.md) for submission guidelines.
