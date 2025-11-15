=======================
Sets of numbers
=======================

| VC2M5N10: level 5: Follow a mathematical algorithm involving branching and repetition (iteration); create and use algorithms involving a sequence of steps and decisions and digital tools to experiment with factors, multiples and divisibility; identify, interpret and describe emerging patterns

* manipulating sets of numbers using a given rule, for example, if a number is even, halve it; or if a number is odd, subtract 1 then halve it

----

Simple rule
------------------------

| Return a set of numbers using the rule: if a number is even, halve it; if a number is odd, subtract 1 then halve it.

.. code-block:: none

    FUNCTION manipulate_numbers(numbers):
        CREATE empty set result

        FOR each number in numbers:
            IF number is even:
                new_value = number / 2
            ELSE:
                new_value = (number - 1) / 2
            ADD new_value to result

        RETURN result


    MAIN PROGRAM:
        numbers = set of integers from 1 to 10
        manipulated_numbers = CALL manipulate_numbers(numbers)
        PRINT manipulated_numbers


.. literalinclude:: files/sets_of_numbers.py
    :linenos:

----

Even numbers
------------------------

| Return a set of even numbers.

.. code-block:: none

    FUNCTION get_even_numbers(numbers):
        CREATE empty set even_numbers

        FOR each number in numbers:
            IF number is even:
                ADD number to even_numbers

        RETURN even_numbers

    MAIN PROGRAM:
        numbers = set of integers from 1 to 10
        even_numbers = CALL get_even_numbers(numbers)
        PRINT even_numbers

.. literalinclude:: files/sets_of_numbers_even.py
    :linenos:

----

Sum numbers in sequence
------------------------

| Return a list of numbers that are a running total as each member of the set is added to the running total.

.. code-block:: none

    FUNCTION sum_numbers_in_sequence(numbers):
        CREATE empty list running_totals
        total = 0

        FOR each number in numbers:
            total = total + number
            ADD total to running_totals

        RETURN running_totals

    MAIN PROGRAM:
        numbers = set of integers from 1 to 10
        running_totals = CALL sum_numbers_in_sequence(numbers)
        PRINT running_totals

.. literalinclude:: files/sets_of_numbers_sum.py
    :linenos:
