=================================================
Flowcharts Positive Numbers
=================================================

| Selection is a control structure that allows a program to choose between different actions based on a condition.
| It's represented by IF…THEN…ELSE statements.
| In simple terms: “If something is true, do this. Otherwise, do that.”

| The pseudocode below checks to see whether a number is positive or not.

.. code-block:: pseudocode

    ALGORITHM positiveOrNot()

    BEGIN
        INPUT number
        IF number > 0 THEN
            PRINT number + " is positive."
        ELSE
            PRINT number + " is not positive."
        ENDIF
    END


| The new shape in the flowchart (number > 0?), is for a decision, which tests a condition and answers True (Yes) or False (No).
| These decisions are written on each branch line.

.. image:: drawio_files/selection/positive_or_not.png
    :scale: 60 %
    :align: center

|
|

.. admonition:: Tasks

    #. What shape is used for a decision?
    #. In the pseudocode above, what keywords start and end the line that checks the number?
    #. In the pseudocode above, what keyword starts the code for the NO branch of the flowchart?
    #. In the pseudocode above, what keyword ends the code for the IF block?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                What shape is used for a decision?

                .. code-block:: pseudocode

                    A diamond

            .. tab-item:: Q2

                In the pseudocode above, what keywords start and end the line that checks the number?

                .. code-block:: pseudocode

                    IF and THEN

            .. tab-item:: Q3

                 In the pseudocode above, what keyword starts the code for the NO branch of the flowchart?

                .. code-block:: pseudocode

                    ELSE

            .. tab-item:: Q4

                In the pseudocode above, what keyword ends the code for the IF block?

                .. code-block:: pseudocode

                    ENDIF

