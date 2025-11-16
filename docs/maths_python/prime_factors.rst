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

.. code-block:: pseudocode

    FUNCTION get_prime_factors(num)

        prime_factors ← empty list

        WHILE num MOD 2 = 0 DO
            APPEND 2 TO prime_factors
            num ← num ÷ 2
        END WHILE

        FOR factor ← 3 TO sqrt(num) STEP 2 DO
            WHILE num MOD factor = 0 DO
                APPEND factor TO prime_factors
                num ← num ÷ factor
            END WHILE
        END FOR

        IF num > 2 THEN
            APPEND num TO prime_factors
        END IF

        RETURN prime_factors

    END FUNCTION


| The python code implementing the algorithm is shown below:

.. literalinclude:: files/prime_factors.py
    :linenos:

----

Prime factor lists to 100
---------------------------

| The pseudocode for the algorithm is as follows:

.. code-block:: pseudocode

    FUNCTION get_prime_factors(num)

        prime_factors ← empty list

        WHILE num MOD 2 = 0 DO
            prime_factors ← prime_factors APPEND 2
            num ← num ÷ 2
        END WHILE

        FOR factor ← 3 TO sqrt(num) STEP 2 DO
            WHILE num MOD factor = 0 DO
                prime_factors ← prime_factors APPEND factor
                num ← num ÷ factor
            END WHILE
        END FOR

        IF num > 2 THEN
            prime_factors ← prime_factors APPEND num
        END IF

        RETURN prime_factors

    END FUNCTION


    FOR num ← 1 TO 100 DO
        fact ← CALL get_prime_factors(num)
        PRINT num, fact
    END FOR


| The python code implementing the algorithm is shown below:

.. literalinclude:: files/prime_factor_list.py
    :linenos:



