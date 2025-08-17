# Column Design Examples

!!! tip "Practical Column Buckling Analysis"
    This page demonstrates column design using Euler buckling theory with real-world engineering scenarios.

## Example 1: Steel Column Design

### Problem Statement

Design a steel column for a building frame with the following requirements:

- **Height**: 3.5 m (story height)
- **Load**: 150 kN axial compression
- **Material**: Steel (E = 200 GPa)
- **End conditions**: Fixed at base, pinned at top
- **Safety factor**: 2.5

### Given Data

```python
# Column properties
height = 3.5                    # m
axial_load = 150000            # N (150 kN)
E = 200e9                      # Pa (200 GPa steel)
end_conditions = "fixed_pinned" # K = 0.7
safety_factor = 2.5

# Trial section: W200x46 steel section
second_moment = 4.57e-6        # m^4 (from steel tables)
area = 5890e-6                 # m^2
```

### Solution

```python
from structural_analysis import StructuralAnalysis

# Initialize analysis
analysis = StructuralAnalysis()

# Calculate critical buckling load
result = analysis.column_theory.euler_buckling(
    length=height,
    E=E,
    second_moment=second_moment,
    end_conditions=end_conditions
)

# Check capacity
critical_load = result['critical_load']
design_load = axial_load * safety_factor

print(f"Critical buckling load: {critical_load/1000:.0f} kN")
print(f"Required capacity: {design_load/1000:.0f} kN")
print(f"Slenderness ratio: {result['slenderness_ratio']:.1f}")

# Check adequacy
if critical_load > design_load:
    print("✅ Section is adequate for buckling")
    utilization = design_load / critical_load * 100
    print(f"Utilization: {utilization:.1f}%")
else:
    print("❌ Section inadequate - increase size or reduce length")
```

### Expected Results

```
Critical buckling load: 523 kN
Required capacity: 375 kN
Slenderness ratio: 89.2
✅ Section is adequate for buckling
Utilization: 71.7%
```

## Example 2: Optimum Column Selection

### Problem Statement

Select the most economical steel section for a column with:

- **Height**: 4.0 m
- **Load**: 200 kN
- **End conditions**: Pinned both ends
- **Safety factor**: 3.0

### Solution Approach

```python
# Column requirements
height = 4.0
load = 200000  # N
safety_factor = 3.0
required_capacity = load * safety_factor  # 600 kN

# Steel sections database (simplified)
steel_sections = {
    'W150x24': {'I': 1.83e-6, 'mass': 24},
    'W200x27': {'I': 2.81e-6, 'mass': 27}, 
    'W200x46': {'I': 4.57e-6, 'mass': 46},
    'W250x33': {'I': 5.67e-6, 'mass': 33},
}

# Analyze each section
results = {}
for section, props in steel_sections.items():
    result = analysis.column_theory.euler_buckling(
        length=height,
        E=200e9,
        second_moment=props['I'],
        end_conditions="pinned"
    )
    
    critical_load = result['critical_load']
    adequate = critical_load > required_capacity
    
    results[section] = {
        'critical_load_kN': critical_load / 1000,
        'adequate': adequate,
        'mass_per_m': props['mass'],
        'utilization_%': required_capacity / critical_load * 100 if adequate else 'N/A'
    }

# Display results
print("Section Analysis Results:")
print("-" * 60)
for section, data in results.items():
    status = "✅" if data['adequate'] else "❌"
    print(f"{section}: {data['critical_load_kN']:.0f} kN, "
          f"{data['mass_per_m']} kg/m, "
          f"Util: {data['utilization_%']:.1f}% {status}")
```

## Example 3: End Condition Comparison

### Problem Statement

Compare the effect of different end conditions on column capacity:

```python
# Column properties
length = 3.0
E = 200e9
second_moment = 8.33e-6

# Analyze all end conditions
end_conditions = ["pinned", "fixed", "fixed_free", "fixed_pinned"]

print("End Condition Comparison:")
print("-" * 50)

for condition in end_conditions:
    result = analysis.column_theory.euler_buckling(
        length=length,
        E=E,
        second_moment=second_moment,
        end_conditions=condition
    )
    
    k_factor = result['effective_length'] / length
    critical_load = result['critical_load'] / 1000  # Convert to kN
    
    print(f"{condition:12}: K={k_factor:.1f}, Pcr={critical_load:.0f} kN")
```

### Expected Results

```
End Condition Comparison:
--------------------------------------------------
pinned      : K=1.0, Pcr=182 kN
fixed       : K=0.5, Pcr=729 kN  
fixed_free  : K=2.0, Pcr=46 kN
fixed_pinned: K=0.7, Pcr=373 kN
```

## Design Guidelines

### Slenderness Limits

- **Euler buckling valid**: λ > 100
- **Intermediate columns**: 50 < λ < 100 (use Johnson formula)
- **Short columns**: λ < 50 (compression controls)

### Safety Factors

- **Building design**: 2.5 - 3.0
- **Bridge design**: 3.0 - 4.0
- **Critical structures**: 4.0+

### Code Compliance

Always verify results against local building codes:

- AISC (American)
- Eurocode 3 (European)
- CSA S16 (Canadian)
- AS 4100 (Australian)

## Related Topics

- [**Euler Buckling Theory**](../theories/column-theory/euler-buckling.md)
- [**Advanced Column Methods**](../theories/column-theory/advanced.md)
- [**Case Studies**](case-studies.md)
