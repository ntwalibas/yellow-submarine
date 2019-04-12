# Yellow Submarine - Gaussian vs non-Gaussian gates

## Overview

We seek to determine if the presence of non-Gaussian gates is beneficial to solving the maxcut problem.

## Observations

- Stabilization of the loss and gradient norm/global norm starts at about 100 steps in general.

- The D gate magnitude starts stabilizing at about 100 steps. After stabilization, it converges towards 2 or 3 unique values.

- The phase of the D gate remains constant.

- The S gate magnitude starts stabilizing at about 150 steps. There is no convergence towards unique values as for each simulation,
the magnitude will land on different values in general.

- The phase of the S gate varies very slightly and can be considered constant for our purposes.

- The cubic phase gate participates in the computation actively and its parameters starts stabilizing sooner at about 50 steps.
It doesn't converge towards unique values but different values are yielded for each run.

- We also note that the presence of the cubic phase gate results in spikes in the gradient norm/global norm graph.

- The Kerr gate parameters remains constant for all simulations.

## Conclusion

The presence of the cubic phase gate doesn't yield any performance improvement over its absence.
In fact, because it introduces sudden spikes in the gradient norm/global norm, it might be detrimental to the quality of the result.
The Kerr has no effect on the simulation at all.
One can conclude that Gaussian gates are sufficient to solve the maxcut problem on CV quantum computers.
