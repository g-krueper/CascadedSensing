# CascadedSensing

This is the code base used in my cascaded phase sensing simulations. The code implements standard Gaussian state propagation and Fisher information calculations, with a unitary matrix representing the "system" or "sensor." See: G. Adesso, S. Ragy, and A. R. Lee, Open Systems and Information Dynamics 21, 1440001 (2014), and Serafini, A. (2017). Quantum Continuous Variables: A Primer of Theoretical Methods (1st ed.). CRC Press. https://doi.org/10.1201/9781315118727

The code begins in Mathematica to compute and simplify a given unitary matrix representing a sensor. The mathematica expression is then converted to a Python-readable expression and copied into a Python file. The Python file then takes that unitary and some chosen input state to calculate and optimize the multiparameter quantum Cram´er-Rao bound.

Files:
matrix_to_python.nb: Computes and simplifies the unitary matrix for a sensor, and converts the expression to Python
3phase_sequential.py: Example implementation of the Gaussian state calculations and optimizations, yielding results detailed in Appendix D of the paper (under review).
OTDR_2sided.py: Implements equations 22-25 of the paper to calculate and optimize a cascaded phase sensor with any number of discrete phase-sensing regions, granted the simplifying assumptions in the paper.
