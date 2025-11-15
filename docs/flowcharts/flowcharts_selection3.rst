=================================================
Flowcharts Study or not
=================================================

| In flowcharts, these comparison operators are used in decision shapes (diamonds) to test conditions that lead to different branches (Yes/No).

+----------+---------------------------+-----------------------------------------------+
| Operator | Meaning                   | Example Sentence                              |
+==========+===========================+===============================================+
| =        | Equal to                  | If score = 100, print "Perfect!"              |
+----------+---------------------------+-----------------------------------------------+
| !=       | Not equal to              | If color != "red", change to "blue".          |
+----------+---------------------------+-----------------------------------------------+
| >        | Greater than              | If speed > 60, show "Slow down!"              |
+----------+---------------------------+-----------------------------------------------+
| <        | Less than                 | If age < 18, deny access.                     |
+----------+---------------------------+-----------------------------------------------+
| >=       | Greater than or equal to  | If temperature >= 30, turn on fan.            |
+----------+---------------------------+-----------------------------------------------+
| <=       | Less than or equal to     | If hours <= 8, allow break.                   |
+----------+---------------------------+-----------------------------------------------+


| The pseudocode below checks to see whether a it is time to study for an exam or not.

.. code-block:: none

    ALGORITHM studyOrNot ()

    BEGIN
        INPUT examSoon
        IF examSoon = 'yes' THEN
            PRINT "Time to study."
        ELSE
            PRINT "Take a break."
        ENDIF
    END


|
|

.. admonition:: Tasks

    #. In the pseudocode above what is the comparison operator that is used to test equality?
    #. Use the pseudocode to add the missing text to the flowchart.

        .. image:: drawio_files/selection/study_or_not_st.png
            :scale: 60 %
            :align: center

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

               In the pseudocode above what is the comparison operator that is used to test equality?

                .. code-block:: none

                    =

            .. tab-item:: Q2

                Use the pseudocode to add the missing text to the flowchart.

                .. image:: drawio_files/selection/study_or_not.png
                    :scale: 60 %
                    :align: center

