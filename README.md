# The Overnight Shipping Problem

Ever wonder how companies like FedEx manage to get packages from one side of the US to the other in just 24 hours?
What if there is only one package that needs to go from Anchorage, AK to Boston, MA that day? Should FedEx send it on a separate plane, or should they use a longer, more complicated route?

In practice, shipping companies solve these problems with complicated, heuristic-oriented planning algorithms. But in this report we take a step back and frame overnight shipping as a network flow problem. We implement a small simulation to show that we can efficiently solve for the optimal shipping routes across many modes of transportation.

To view the analysis, simply open [report.ipynb](https://github.com/evandez/overnight-shipping/blob/master/report.ipynb)
in your browser. All the cells have already been run.

## Disclaimer

We wrote this report as a final project for CS 524: Introduction to Optimization at UW-Madison. Like most final projects, it is not perfect and makes egregious simplifying assumptions about the problem. Take everything you read with two grains of salt.

## Acknowledgements

Shoutout to Matt DePero for the helpful discussions on the way to work every morning.
