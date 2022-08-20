# DerivativesPricing - dpf
 
## Description

A library used to review derivatives pricing

Some of available functionalities that dpf offers:

- Analytical formulae for different plain vanilla and exotic options:

    - European Option
    - American Option
    - Asian Option
    - Barrier Option 
    - Knock-in/out option

- Monte-carlo simulation for different stochastic process

    - Arithmetic Brownian Motion
    - Geometric Brownian Motion
    - OU process
    - Vasicek process

## Installation

Clone the respository into your folder and run below command:

```
python setup.py install
```

## Roadmap (to be updated)

- August: Complex Numbers, Analytical pricing engine for Plain Vanilla option pricing
    - Closed form solution for Greeks 
    - Numerical Greeks to calculate the sensitivities of the BSM formula
    - Analytical formulas for American Options
        - Barone-Adesi and Whaley Approximation
        - Bjerksund and Stensland Approximation (1993) (2002)
- September: Local Volatility (Surface calibration, interpolation) 
- October: Stochastic Volatility and Heston model 
- November: Interest rate model
- December: tba



