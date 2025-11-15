=================================================
Flowcharts Classify Quadrilateral by Sides
=================================================

| The pseudocode below checks to see if a quadrilateral has all sides equal, or just opposite sides equal, and classifies it accordingly.

.. code-block:: none

    ALGORITHM classifyQuadrilateralBySides()

    BEGIN
        INPUT sidesEqual, oppositeSidesEqual
        IF sidesEqual = TRUE THEN
            PRINT "Rhombus"
        ELSEIF oppositeSidesEqual = TRUE THEN
            PRINT "Parallelogram"
        ELSE
            PRINT "Other quadrilateral"
        ENDIF
    END


|
|


.. admonition:: Tasks

    #. On the flowchart, fill in the shapes with text to represent the pseudocode above.

        .. image:: drawio_files/selection/quadrilaterals_by_sides_st.png
            :scale: 60 %
            :align: center

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                On the flowchart, fill in the shapes with text to represent the pseudocode above.

                .. image:: drawio_files/selection/quadrilaterals_by_sides.png
                    :scale: 60 %
                    :align: center
