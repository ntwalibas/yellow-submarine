# Yellow Submarine - 4x4 weighted matrices

## Overview

In this experiment we examine the performance of the circuit on 4x4 weighted matrices.

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

Without the presence of non-Gaussian gates, the simulation starts converging at about 50 steps.

### Kerr gate is used

- The Kerr gate doesn't seem to participate in the computation of the final result.
- The simulation doesn't converge faster towards the result with the presence of the Kerr gate.

### Cubic phase gate is used

- The cubic phase gates actively participates in the computation of the final result.
- The simulation doesn't converge faster towards the result with the presence of the cubic phase gate.
- The presence of the cubic phase gates results in instabilities in the during the computation.

## Conclusions

The simulation performs without the presence of non-Gaussian gates.
The instabilities during the simulation with cubic phase gate maybe solved with minor adjustments in learning parameters but considering the speed of computation is not affected by the presence of this gate, this effort may be wasted.
