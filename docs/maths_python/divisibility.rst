=======================
Divisibility
=======================

* testing a number for divisibility

----------------------------------
Prime number divisibility tests
----------------------------------


Divibility by 2
-------------------

| A number is divisible by 2 if the last digit is 0, 2, 4, 6 or 8.
| For example: 234 is divisible by 2, because the last digit is 4.
| The code below checks if the last digit to see if it is divisible by 2.
| To get the last digit, the number is converted to a string, **str(num)**, then string indexing, **str(num)[-1]**, gets the last character.

| The pseudocode for the algorithm is as follows:

.. code-block:: pseudocode

    FUNCTION DIV_BY_2(number):
        endings ← ["0", "2", "4", "6", "8"]
        last_digit ← last character of number (as string)

        IF last_digit IS IN endings:
            RETURN TRUE
        ELSE:
            RETURN FALSE
        ENDIF
    ENDFUNCTION


    MAIN PROGRAM:
        num ← RANDOM INTEGER BETWEEN 10 AND 300
        result ← DIV_BY_2(num)
        PRINT num, result

| The python code implementing the algorithm is shown below:

.. literalinclude:: files/div_test_2.py
    :linenos:

----

Divibility by 3
-------------------

| A number is divisible by 3 if the sum of the digits in the number is divisible by 3.
| For example: 162 is divisible by 3 since the sum of the digits is 9 (1 + 6 + 2 = 9) and 9 is divisible
by 3.
| The code below sums the digits of the number via **sum_digits**, and repeats summing the digits via **repeated_sum_digits** until there is just one digit, then, in **div_by_3**, checks if that sum is 3, 6, or 9.

| The pseudocode for the algorithm is as follows:

.. code-block:: pseudocode

    FUNCTION DIV_BY_3(num):
        sum_of_digits ← REPEATED_SUM_DIGITS(num)

        IF sum_of_digits IS IN [3, 6, 9]:
            RETURN TRUE
        ELSE:
            RETURN FALSE
        ENDIF
    ENDFUNCTION


    FUNCTION SUM_DIGITS(num):
        total ← 0
        FOR each digit IN STRING(num):
            total ← total + INTEGER(digit)
        ENDFOR
        RETURN total
    ENDFUNCTION


    FUNCTION REPEATED_SUM_DIGITS(num):
        sum_of_digits ← SUM_DIGITS(num)

        WHILE sum_of_digits > 10:
            sum_of_digits ← SUM_DIGITS(sum_of_digits)
        ENDWHILE

        RETURN sum_of_digits
    ENDFUNCTION


    MAIN PROGRAM:
        num ← RANDOM INTEGER BETWEEN 12 AND 300
        result ← DIV_BY_3(num)
        PRINT num, result


| The python code implementing the algorithm is shown below:

.. literalinclude:: files/div_test_3.py
    :linenos:

----

Divibility by 5
-------------------

| A number is divisible by 5 if the last digit is either 0 or 5.
| For example: 125 and 120 are both divisible by 5 since their last digits are 5 and 0.
| The code below checks if the last digit is a 5 or 0.
| To get the last digit, the number is converted to a string, **str(num)**, then string indexing, **str(num)[-1]**, gets the last character.

| The pseudocode for the algorithm is as follows:

.. code-block:: pseudocode

    FUNCTION DIV_BY_5(num):
        endings ← ["0", "5"]
        last_digit ← LAST CHARACTER OF STRING(num)

        IF last_digit IS IN endings:
            RETURN TRUE
        ELSE:
            RETURN FALSE
        ENDIF
    ENDFUNCTION


    MAIN PROGRAM:
        num ← RANDOM INTEGER BETWEEN 10 AND 300
        result ← DIV_BY_5(num)
        PRINT num, result

| The python code implementing the algorithm is shown below:

.. literalinclude:: files/div_test_5.py
    :linenos:

----

Divisibility by 7
------------------

| The process for divisibility by 7 requires a few steps. Follow the steps below to test divisibility by 7, and then work through the example provided.
| 1.	Write down all the digits in the number except the last digit.
| 2.	Take the last digit of the number you're testing and double it.
| 3.	Subtract this number from the rest of the digits in the original number that you wrote down.
| 4.	If this new number is either 0 or a number that's divisible by 7, then the original number is also divisible by 7.
| 5.	If you can't tell yet if the new number is divisible by 7, go back to the first step with this new (smaller) number and repeat.

| The pseudocode for the algorithm is as follows:


.. code-block:: pseudocode


    FUNCTION DIV_BY_7(num):
        diff ← REPEATED_DIFF_FROM_DBL_LAST(num)

        IF diff IS IN [0, 7, -7]:
            RETURN TRUE
        ELSE:
            RETURN FALSE
        ENDIF
    ENDFUNCTION


    FUNCTION DIFF_FROM_DBL_LAST(num):
        last ← INTEGER(LAST CHARACTER OF STRING(num))
        all_but_last ← INTEGER(STRING(num) WITHOUT LAST CHARACTER)
        RETURN all_but_last - 2 * last
    ENDFUNCTION


    FUNCTION REPEATED_DIFF_FROM_DBL_LAST(num):
        diff ← DIFF_FROM_DBL_LAST(num)

        WHILE diff > 10:
            diff ← DIFF_FROM_DBL_LAST(diff)
        ENDWHILE

        RETURN diff
    ENDFUNCTION


    MAIN PROGRAM:
        num ← RANDOM INTEGER BETWEEN 12 AND 300
        result ← DIV_BY_7(num)
        PRINT num, result

| The python code implementing the algorithm is shown below:

.. literalinclude:: files/div_test_7.py
    :linenos:
