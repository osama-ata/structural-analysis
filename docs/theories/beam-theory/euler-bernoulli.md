# Euler-Bernoulli Beam Theory

!!! info "Classical Beam Bending Theory"
    The Euler-Bernoulli beam theory is the foundation of structural beam analysis, providing solutions for deflection, moment, and shear in beams under various loading conditions.

## Mathematical Background

The Euler-Bernoulli beam theory is based on the fundamental differential equation:

$$\frac{d^4v}{dx^4} = \frac{q(x)}{EI}$$

Where:

- $v(x)$ = deflection at position $x$
- $q(x)$ = distributed load
- $E$ = elastic modulus
- $I$ = second moment of area

## Key Assumptions

1. **Small deflections**: Deflections are small compared to beam dimensions
2. **Plane sections remain plane**: Cross-sections perpendicular to the neutral axis remain plane after bending
3. **Linear elastic material**: Material follows Hooke's law
4. **No shear deformation**: Shear effects are neglected (valid for slender beams)

## Implementation

::: structural_analysis.beam_theory.BeamTheory.euler_bernoulli

## Boundary Conditions

The implementation supports various boundary conditions:

### Simply Supported

- Both ends pinned (rotation allowed, translation constrained)
- Typical for bridge girders and floor beams

### Cantilever

- One end fixed (no rotation or translation)
- Free end (no constraints)
- Common in balconies and overhangs

## Load Types

### Point Loads

Concentrated forces applied at specific locations along the beam.

### Distributed Loads

Forces distributed over a length of the beam (uniform or varying).

### Moment Loads

Concentrated moments applied at specific points.

## Applications

- **Building design**: Floor beams, roof trusses
- **Bridge engineering**: Girder analysis
- **Mechanical systems**: Machine frames, support structures
- **Academic teaching**: Fundamental structural analysis

## Limitations

- **Thick beams**: Inaccurate for beams with length-to-depth ratios < 10
- **Large deflections**: Theory breaks down for deflections > span/250
- **Shear effects**: Neglects shear deformation (use Timoshenko theory instead)
- **Dynamic loads**: Static analysis only

## Related Theories

- [**Timoshenko Beam Theory**](timoshenko.md): Includes shear deformation
- [**Column Buckling**](../column-theory/euler-buckling.md): For compression members

## Examples

See practical applications in:

- [**Beam Analysis Examples**](../../examples/beam-analysis.md)
- [**Case Studies**](../../examples/case-studies.md)
