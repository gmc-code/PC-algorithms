=======================
Prime factors
=======================

Prime factor list
---------------------

| The modulus operator can be used to test for a remainder when division is carried out.
| Steps:
* Check if 2 goes into the number, num, with no remainder.
* While 2 goes into the number exactly, add 2 to the list of prime factors and divide the number by 2.
* For every odd number from 3 up to the square root of the number, check if the odd number goes in exactly.
* While the factor goes in exactly, add it to the prime factors list and divide the number, num, by the factor.
* Return the list of prime factors.

| The pseudocode for the algorithm is as follows:

.. code-block:: none

    FUNCTION get_prime_factors(num):
        CREATE empty list prime_factors
        WHILE num mod 2 == 0:
            ADD 2 to prime_factors
            num = num / 2
        FOR factor from 3 to sqrt(num) step 2:
            WHILE num mod factor == 0:
                ADD factor to prime_factors
                num = num / factor
        IF num > 2:
            ADD num to prime_factors
        RETURN prime_factors

| The python code implementing the algorithm is shown below:

.. literalinclude:: files/prime_factors.py
    :linenos:

----

Prime factor lists to 100
---------------------------

| The pseudocode for the algorithm is as follows:

.. code-block:: none

    FUNCTION get_prime_factors(num):
        CREATE empty list prime_factors
        WHILE num mod 2 == 0:
            ADD 2 to prime_factors
            num = num / 2
        FOR factor from 3 to sqrt(num) step 2:
            WHILE num mod factor == 0:
                ADD factor to prime_factors
                num = num / factor
        IF num > 2:
            ADD num to prime_factors
        RETURN prime_factors

    FOR num from 1 to 100:
        fact  = CALL get_prime_factors(num)
        PRINT num, fact


| The python code implementing the algorithm is shown below:

.. literalinclude:: files/prime_factor_list.py
    :linenos:



