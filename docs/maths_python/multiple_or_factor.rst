=======================
Multiple or factor
=======================

| VC2M5N10: level 5:  Follow a mathematical algorithm involving branching and repetition (iteration); create and use algorithms involving a sequence of steps and decisions and digital tools to experiment with factors, multiples and divisibility; identify, interpret and describe emerging patterns

* creating algorithms that use multiplication and division facts to determine if a number is a multiple or factor of another number; for example, using a flow chart that determines whether numbers are factors or multiples of other numbers using branching, such as yes/no decisions

----

Pseudocode
------------------------------------------------

| The pseudocode to determine if one number is a factor or multiple of a second number.

.. code-block:: pseudocode

    FUNCTION is_multiple_or_factor(a, b)
        IF a = 0 OR b = 0 THEN
            RETURN "Do not use 0 for a or b"
        ENDIF

        IF b % a = 0 THEN
            RETURN a + " is a factor of " + b
        ELSEIF a % b = 0 THEN
            RETURN a + " is a multiple of " + b
        ELSE
            RETURN a + " is neither factor nor multiple of " + b
        ENDIF
    END FUNCTION

----

Multiple or factor code
------------------------------------------------

| The python to determine if one number is a factor or multiple of a second number.

.. literalinclude:: files/multiple_or_factor.py
    :linenos:

