=======================
Highest common factor
=======================

Euclidean algorithm
---------------------------

See: https://en.wikipedia.org/wiki/Euclidean_algorithm


| The **highest common factor** is known as the greatest common divisor, gcd.
| The Euclidean algorithm is based on the principle that the **highest common factor** of two numbers does not change if the larger number is replaced by its difference with the smaller number.
| For example, 6 is the HCF of 48 and 18 (as 48 = 8 x 6 and 18 = 3 x 6), and the same number 6 is also the HCF of 18 and 30 (obtained by 48 - 18; taking 3 sixes from 8 sixes leaves 5 sixes).
| Since this replacement reduces the larger of the two numbers, repeating this process gives successively smaller pairs of numbers until the two numbers become equal.
| 48 and 18 becomes 30 and 18 which becomes 18 and 12 which becomes 12 and 6 which becomes 6 and 6.
| When that occurs, they are the HCF of the original two numbers.

----

HCF by repeated subtraction (Euclidean algorithm)
---------------------------------------------------

| The code below uses a while loop to repeatedly subtract the smaller number from the larger number until both numbers are equal.

| The pseudocode for the algorithm is as follows:

.. code-block:: pseudocode

    FUNCTION HCF_SUB(a, b):
        WHILE a ≠ b:
            IF a > b:
                a ← a - b
            ELSE:
                b ← b - a
            ENDIF
        ENDWHILE
        RETURN a
    ENDFUNCTION


    MAIN PROGRAM:
        a ← 48
        b ← 18
        result ← HCF_SUB(a, b)
        PRINT "HCF(", a, ",", b, ") IS", result



| The python code implementing the algorithm is shown below:

.. literalinclude:: files/hcf_sub.py
    :linenos:

----

HCF by repeatedly getting remainders from division
---------------------------------------------------

| Instead of repeated subtractions, a division can be used to get the remainder that would occur if all the possible subtractions of that number were be done at once.
| Starting with 48 and 18, instead of subtracting 18 from 48, subtract the largest multiple of 18 that is less than 48.
| 48 - 2*18 = 12. Note that 48//18 gives 2. **//** is floor division, rounding down to an integer.

| The code below runs the while loop until **b** equals 0.
| **b** is stored in **t** so b can be calculated, then **a** is set to **t**.
| An example of **b = a - (a // b) * b** is **b = 48 - (48//19)*18**, which is b = 48 - 36 = 12.

| The pseudocode for the algorithm is as follows:

.. code-block:: pseudocode

    FUNCTION HCF_DIV(a, b):
        WHILE b ≠ 0:
            t ← b
            b ← a - (a // b) * b
            a ← t
        ENDWHILE
        RETURN a
    ENDFUNCTION


    MAIN PROGRAM:
        a ← 48
        b ← 18
        result ← HCF_DIV(a, b)
        PRINT "HCF(", a, ",", b, ") IS", result


| The python code implementing the algorithm is shown below:

.. literalinclude:: files/hcf_div.py
    :linenos:


| The line above, **b = a - (a // b) * b**, can be replaced by **b = a % b**, which finds the remainder from division.


| The pseudocode for the algorithm is as follows:

.. code-block:: pseudocode

    FUNCTION HCF_MOD(a, b):
        WHILE b ≠ 0:
            t ← b
            b ← a % b
            a ← t
        ENDWHILE
        RETURN a
    ENDFUNCTION


    MAIN PROGRAM:
        a ← 48        # Example: 1071
        b ← 18        # Example: 462
        result ← HCF_MOD(a, b)
        PRINT "HCF(", a, ",", b, ") IS", result

| The python code implementing the algorithm is shown below:

.. literalinclude:: files/hcf_mod.py
    :linenos:



