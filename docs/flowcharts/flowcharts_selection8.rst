=================================================
Flowcharts Classify Angle Type
=================================================

| The pseudocode below identifies the angle type by size.

.. code-block:: pseudocode

    ALGORITHM angleType()

    BEGIN
        INPUT angle
        -- Outer validation
        IF angle >  0 AND angle <= 360 THEN
            -- First split: 0–180 vs 180–360
            IF angle <= 180 THEN
                -- Subsplit: 0–90 vs 90–180
                IF angle <= 90 THEN
                    IF angle > 0 AND angle < 90 THEN
                        PRINT "Acute angle."
                    ELSE
                        PRINT "Right angle."
                    ENDIF
                ELSE
                    IF angle > 90 AND angle < 180 THEN
                        PRINT "Obtuse angle."
                    ELSE
                        PRINT "Straight angle."
                    ENDIF
                ENDIF
            ELSE
                -- Subsplit: 180–360
                IF angle < 360 THEN
                    PRINT "Reflex angle."
                ELSE
                    PRINT "Revolution angle."
                ENDIF
            ENDIF
        ELSE
            PRINT "Invalid angle."
        ENDIF
    END


|
|


.. admonition:: Tasks

    #. On the flowchart, fill in the shapes with text to represent the pseudocode above.

        .. image:: drawio_files/selection/angle_types_st.png
            :width: 100%
            :align: center

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                On the flowchart, fill in the shapes with text to represent the pseudocode above.

                .. image:: drawio_files/selection/angle_types.png
                    :width: 100%
                    :align: center

