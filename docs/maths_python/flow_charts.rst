=======================
Flow charts
=======================

| VCMNA221: level 6: Design algorithms involving branching and iteration to solve specific classes of mathematical problems

* devising flowcharts to represent algorithms for a common processes such as adding two fractions

----

Adding fractions
---------------------

| The flow chart shows the main steps involved in adding 2 fractions.

.. image:: images/flow_chart_add_fractions.png
    :width: 200
    :align: center

|
| The code below carries out these steps for adding two fractions:

1. The `add_fractions` function takes two fractions as input, represented as tuples of the form `(numerator, denominator)`.
2. The function unpacks the fractions to extract the numerators and denominators.
3. The function finds the lowest common denominator (LCD) of the two fractions by calculating the least common multiple (LCM) of the denominators.
4. The function converts each fraction to an equivalent fraction with the LCD as the denominator by multiplying the numerator and denominator by the same factor.
5. The function adds the numerators of the two fractions to calculate the numerator of the sum.
6. The function simplifies the resulting fraction if possible by dividing both the numerator and denominator by their greatest common divisor (GCD).
7. If the resulting fraction is an improper fraction (i.e. if the numerator is greater than the denominator), the function converts it to a mixed number by calculating the whole number and remainder.
8. The function returns the sum of the fractions, either as a proper fraction or as a mixed number.

| The pseudocode for the algorithm is as follows:

.. code-block:: pseudocode

FUNCTION add_fractions(fraction1, fraction2):
    EXTRACT numerator1, denominator1 from fraction1
    EXTRACT numerator2, denominator2 from fraction2

    FIND lcd = (denominator1 * denominator2) / gcd(denominator1, denominator2)

    CONVERT numerator1 = numerator1 * (lcd / denominator1)
    CONVERT numerator2 = numerator2 * (lcd / denominator2)

    numerator_sum = numerator1 + numerator2

    gcd_value = gcd(numerator_sum, lcd)
    result_numerator = numerator_sum / gcd_value
    result_denominator = lcd / gcd_value

    IF result_numerator > result_denominator:
        whole_number = result_numerator / result_denominator
        remainder = result_numerator MOD result_denominator
        RETURN "whole_number remainder/result_denominator"
    ELSE:
        RETURN "result_numerator/result_denominator"


BEGIN:
    fraction1 = (1, 2)
    fraction2 = (2, 3)
    result = CALL add_fractions(fraction1, fraction2)
    PRINT "fraction1 + fraction2 = result"


| The python code implementing the algorithm is shown below:

.. literalinclude:: files/add_fractions.py
    :linenos:

| The output is: 1/2 + 2/3 = 1 1/6

----

Adding fractions using the fractions module
---------------------------------------------

| The fractions module can be used to create fraction objects which allow easy addition.
| Improper fractions results then have to be simplified.

| The pseudocode for the algorithm is as follows:

.. code-block:: pseudocode

    BEGIN:
    fraction1 = 1/3
    fraction2 = 2/3

    result = fraction1 + fraction2
    whole_number = integer part of result

    IF whole_number > 0:
        fraction_part = result - whole_number

        IF fraction_part > 0:
            PRINT "fraction1 + fraction2 = whole_number fraction_part"
            # Example: 1/2 + 2/3 = 1 1/6
        ELSE:
            PRINT "fraction1 + fraction2 = result"
            # Example: 1/3 + 2/3 = 1
    ELSE:
        PRINT "fraction1 + fraction2 = result"
        # Example: 1/6 + 2/3 = 5/6


| The python code implementing the algorithm using the fractions module is shown below:

.. literalinclude:: files/add_fractions_using_fractions.py
    :linenos:

