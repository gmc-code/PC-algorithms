=======================
Sums of sequences
=======================

* finding the sum of a set of consecutive numbers using a loop structure

----

------------------------------
Sum of consecutive numbers
------------------------------

Listed numbers
-------------------

| The code below uses a for loop which iterates over the **nums** list.
| Each number, **num**, in the list, **nums**, is added to the **sum**.

.. code-block:: python

    nums = [1, 2, 3, 4, 5]
    sum = 0
    for num in nums:
        sum += num
    print(sum)


| The pseudocode below uses a for each loop to iterate over the nums list.

.. code-block:: pseudocode

    BEGIN
        nums ← [1, 2, 3, 4, 5]
        sum ← 0

        FOR EACH num IN nums DO
            sum ← sum + num
        ENDFOR

        PRINT("Sum is ", sum)
    END



----

Range from 0
-----------------------------------

| The code below uses the range function to provide a list of integers from 0 to 5.

.. code-block:: python

    nums = list(range(6))
    print(nums)
    sum = 0
    for num in nums:
        sum += num
    print(sum)

| The pseudocode below uses a for each loop to iterate over the nums list.

.. code-block:: pseudocode

    BEGIN
        nums ← [0, 1, 2, 3, 4, 5]
        PRINT("Numbers are ", nums)

        sum ← 0

        FOR EACH num IN nums DO
            sum ← sum + num
        ENDFOR

        PRINT("Sum is ", sum)
    END



----

Range: first and last
-----------------------------------

| The code below uses the range function to provide a list of integers from **start_num** to **end_num**.

.. code-block:: python

    start_num = 4
    end_num = 12
    nums = list(range(start_num, end_num + 1))
    print(nums)
    sum = 0
    for num in nums:
        sum += num
    print(sum)

| The pseudocode below uses a for each loop to iterate over the nums list.

.. code-block:: pseudocode

    BEGIN
        start_num ← 4
        end_num ← 12

        nums ← LIST OF INTEGERS FROM start_num TO end_num
        PRINT("Numbers are ", nums)

        sum ← 0

        FOR EACH num IN nums DO
            sum ← sum + num
        ENDFOR

        PRINT("Sum is ", sum)
    END



----

Range: step size
-----------------------------------

| The code below uses the range function to provide a list of integers from **start_num** to **end_num** in steps of **step_size**.

.. code-block:: python

    start_num = 4
    end_num = 12
    step_size = 2
    nums = list(range(start_num, end_num + 1, step_size))
    print(nums)
    sum = 0
    for num in nums:
        sum += num
    print(sum)

| The pseudocode below uses a for each loop to iterate over the nums list.

.. code-block:: pseudocode

    BEGIN
        start_num ← 4
        end_num ← 12
        step_size ← 2

        nums ← LIST OF INTEGERS FROM start_num TO end_num IN STEPS OF step_size
        PRINT("Numbers are ", nums)

        sum ← 0

        FOR EACH num IN nums DO
            sum ← sum + num
        ENDFOR

        PRINT("Sum is ", sum)
    END



----

Arithmetic sequence formula 1
-----------------------------------

| One formula for the sum of a sequence of numbers with the same difference between them is:
| S = n/2[2a + (n-1)d]
| where
| S is the sum
| n is the number of numbers
| a is the start number
| d is the difference between numbers

.. code-block:: python

    a = 4
    n = 5
    d = 2
    sum = (n/2) * (2*a + (n-1)*d)
    print(sum)


| The pseudocode below calculates the sum using this formula.

.. code-block:: pseudocode

    BEGIN
        a ← 4          -- first term
        n ← 5          -- number of terms
        d ← 2          -- common difference

        sum ← (n ÷ 2) * (2 * a + (n - 1) * d)

        PRINT("Sum of arithmetic progression is ", sum)
    END



----

Arithmetic sequence formula 2
-----------------------------------

| Another formula for the sum of a sequence of numbers with the same difference between them is:
| S = n/2[a + l]
| where
| S is the sum
| n is the number of numbers
| a is the start number
| l is the last number

.. code-block:: python

    a = 4
    n = 5
    l = 12
    sum = (n/2) * (a + l)
    print(sum)


| The pseudocode below calculates the sum using this formula.

.. code-block:: pseudocode

    BEGIN
        a ← 4          -- first term
        n ← 5          -- number of terms
        l ← 12         -- last term

        sum ← (n ÷ 2) * (a + l)

        PRINT("Sum of arithmetic progression is ", sum)
    END




