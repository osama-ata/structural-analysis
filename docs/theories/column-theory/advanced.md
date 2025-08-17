# Advanced Column Methods

!!! warning "Under Development"
    These advanced column theories are planned for implementation. Check the [development roadmap](../../development/roadmap.md) for current status.

## Overview

Advanced column methods extend beyond Euler buckling to handle:

- **Inelastic buckling**: Material yielding before elastic buckling
- **Combined loading**: Axial load plus bending moments
- **Imperfect columns**: Real-world geometric imperfections
- **Material nonlinearity**: Beyond elastic limit behavior

## Planned Theories

### Rankine-Gordon Formula

Combines crushing and buckling failure modes:

$$\frac{1}{P_{allow}} = \frac{1}{P_c} + \frac{1}{P_{cr}}$$

Where:

- $P_c$ = crushing load
- $P_{cr}$ = Euler buckling load

### Johnson Parabolic Formula

For intermediate slenderness ratios:

$$P_{cr} = A \sigma_y \left(1 - \frac{\sigma_y (KL/r)^2}{4\pi^2 E}\right)$$

Valid when: $KL/r < \sqrt{2\pi^2 E / \sigma_y}$

### Plastic Buckling

Accounts for material yielding in the buckling analysis:

- Tangent modulus theory
- Reduced modulus theory
- Numerical integration methods

## Implementation Status

These theories are in the development pipeline:

- [ ] Rankine-Gordon formula
- [ ] Johnson parabolic formula
- [ ] Plastic buckling analysis
- [ ] Combined axial and bending
- [ ] Imperfection sensitivity analysis

## Applications

- **Building design**: Real-world column behavior
- **Steel structures**: Inelastic buckling of steel columns
- **Concrete design**: Slender concrete column analysis
- **Code compliance**: Building code requirements

## Contributing

Interested in implementing these theories? See our [contributing guide](../../contributing.md) for detailed guidelines.

## Related Topics

- [**Euler Buckling**](euler-buckling.md): Basic elastic buckling
- [**Development Roadmap**](../../development/roadmap.md): Implementation timeline
- [**Contributing**](../../contributing.md): How to add theories
