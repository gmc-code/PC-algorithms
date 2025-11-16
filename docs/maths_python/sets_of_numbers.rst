=======================
Sets of numbers
=======================

| VC2M5N10: level 5: Follow a mathematical algorithm involving branching and repetition (iteration); create and use algorithms involving a sequence of steps and decisions and digital tools to experiment with factors, multiples and divisibility; identify, interpret and describe emerging patterns

* manipulating sets of numbers using a given rule, for example, if a number is even, halve it; or if a number is odd, subtract 1 then halve it

----

Simple rule
------------------------

| Return a set of numbers using the rule: if a number is even, halve it; if a number is odd, subtract 1 then halve it.

.. code-block:: pseudocode

    FUNCTION manipulate_numbers(numbers)
        result ← EMPTY SET

        FOR EACH number IN numbers DO
            IF number MOD 2 = 0 THEN
                new_value ← number ÷ 2
            ELSE
                new_value ← (number - 1) ÷ 2
            ENDIF
            ADD new_value TO result
        ENDFOR

        RETURN result
    ENDFUNCTION


    BEGIN
        INPUTS:
            numbers ← SET OF INTEGERS FROM 1 TO 10

        PROCESS:
            manipulated_numbers ← CALL manipulate_numbers(numbers)

        OUTPUT:
            PRINT("Manipulated numbers are ", manipulated_numbers)
    END



.. literalinclude:: files/sets_of_numbers.py
    :linenos:

----

Even numbers
------------------------

| Return a set of even numbers.

.. code-block:: pseudocode

    FUNCTION get_even_numbers(numbers)
        even_numbers ← EMPTY SET

        FOR EACH number IN numbers DO
            IF number MOD 2 = 0 THEN
                ADD number TO even_numbers
            ENDIF
        ENDFOR

        RETURN even_numbers
    ENDFUNCTION


    BEGIN
        INPUTS:
            numbers ← SET OF INTEGERS FROM 1 TO 10

        PROCESS:
            even_numbers ← CALL get_even_numbers(numbers)

        OUTPUT:
            PRINT("Even numbers are ", even_numbers)
    END


.. literalinclude:: files/sets_of_numbers_even.py
    :linenos:

----

Sum numbers in sequence
------------------------

| Return a list of numbers that are a running total as each member of the set is added to the running total.

.. code-block:: pseudocode

    FUNCTION sum_numbers_in_sequence(numbers)
        running_totals ← EMPTY LIST
        total ← 0

        FOR EACH number IN numbers DO
            total ← total + number
            APPEND total TO running_totals
        ENDFOR

        RETURN running_totals
    ENDFUNCTION


    BEGIN
        INPUTS:
            numbers ← SET OF INTEGERS FROM 1 TO 10

        PROCESS:
            running_totals ← CALL sum_numbers_in_sequence(numbers)

        OUTPUT:
            PRINT("Running totals are ", running_totals)
    END


.. literalinclude:: files/sets_of_numbers_sum.py
    :linenos:
