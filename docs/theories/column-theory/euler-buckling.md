# Euler Buckling Theory

!!! info "Elastic Column Buckling Analysis"
    Euler buckling theory provides the critical load analysis for long, slender columns under axial compression.

## Mathematical Background

The Euler buckling formula determines the critical load at which a column becomes unstable:

$$P_{cr} = \frac{\pi^2 EI}{(KL)^2}$$

Where:

- $P_{cr}$ = critical buckling load
- $E$ = elastic modulus
- $I$ = second moment of area
- $K$ = effective length factor
- $L$ = actual column length

## Effective Length Factors

Different end conditions result in different effective length factors:

| End Condition | K Factor | Description |
|---------------|----------|-------------|
| Pinned-Pinned | 1.0 | Both ends pinned |
| Fixed-Fixed | 0.5 | Both ends fixed |
| Fixed-Free | 2.0 | One end fixed, one free |
| Fixed-Pinned | 0.7 | One end fixed, one pinned |

## Implementation

::: structural_analysis.column_theory.ColumnTheory.euler_buckling

## Key Assumptions

1. **Perfect column**: Straight, homogeneous, no initial imperfections
2. **Elastic material**: Material remains within elastic limit
3. **Axial loading**: Load applied along centroidal axis
4. **Small deflections**: Linear elastic analysis
5. **Long, slender columns**: Length-to-radius ratio > 100

## Slenderness Ratio

The slenderness ratio determines if Euler buckling applies:

$$\lambda = \frac{KL}{r}$$

Where $r = \sqrt{I/A}$ is the radius of gyration.

- $\lambda > 100$: Euler buckling applies
- $\lambda < 100$: Use Johnson formula or other methods

## Applications

- **Building columns**: Steel and concrete column design
- **Bridge piers**: Compression member stability
- **Machine design**: Struts and compression members
- **Aerospace**: Lightweight structure design

## Limitations

- **Short columns**: Inaccurate for stocky columns (use Johnson formula)
- **Imperfections**: Real columns have initial crookedness
- **Material yielding**: Limited to elastic range
- **Dynamic effects**: Static analysis only

## Safety Considerations

In practice, apply safety factors:

- **Load factors**: Increase applied loads
- **Resistance factors**: Reduce critical loads
- **Code compliance**: Follow local building codes

## Related Theories

- [**Advanced Column Methods**](advanced.md): Inelastic buckling analysis
- [**Beam Theory**](../beam-theory/euler-bernoulli.md): Related bending analysis

## Examples

See practical applications in:

- [**Column Design Examples**](../../examples/column-design.md)
- [**Case Studies**](../../examples/case-studies.md)
