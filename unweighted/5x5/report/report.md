# Yellow Submarine - 5x5 matrices

## Overview

In this experiment we examine the performance of the circuit on 5x5 matrices.

## Code 

The code can be found in the current `src` folder in the parent folder of this file.

### Running the code

You can run the simulation by invoking the `runner.py` file. We used 10 steps in order to generate enough data.

```
./runner.py 10
```

## Description

We run 3 sets of simulations: one without any Gaussian gates, another with the Kerr gate and another with the cubic phase gate. We seek to understand how non-Gaussian gates influence the process and result of the simulation.

Non-Gaussian gates are difficult to implement in practice so if we can produce results without their presence using only Gaussian gates it will be a good thing.

## Results

### Only Gaussian gates are used

Without the presence of non-Gaussian gates, the simulation starts converging at about 100 steps.

### Kerr gate is used

- The Kerr gate doesn't seem to participate in the computation of the final result.
- We also note contrary to 4x4 matrices, the simulation doesn't converge faster with the presence of the Kerr gate.

### Cubic phase gate is used

- The cubic phase gates actively participates in the computation of the final result.
- Similar to the Kerr gate, the simulation doesn't seem to converge faster with the presence of the cubic phase gate.

## Conclusions

The presence of non-Gaussian gates doesn't seem to offer any advantage. We obtain the result no sooner with the exclusive use of Gaussian gates alone.