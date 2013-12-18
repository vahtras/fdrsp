gen_findif_all.py
*****************

* Generate unit tests of finite difference tests of analytical response functions

* In all applications ``X`` is a singlet symmetric operator which is added to the one-electron Hamiltonian
    .. math::
        H = H_0 + \epsilon_x X

    This test is obtained in the Dalton input with e.g. ::

    **WAVE FUNCTION
    *HAMILTON
    .FIELD
    XLABEL
    .0005
    
* The following test cases are produced
    * Expectation value
        .. math::

           \langle\!\langle X\rangle\!\rangle = \frac{d}{dx}\langle H \rangle
        * closed-shell
        * open-shell

    * Linear response
        .. math::

           \langle\!\langle A; X\rangle\!\rangle = \frac{d}{dx}\langle A \rangle

        * closed-shell, A singlet
        * open-shell, A singlet
        * open-shell, A triplet
    * Quadratic response
        * closed-shell, A, B singlet
        * closed-shell, A, B singlet

.. literalinclude:: ../gen_findif_all.py

