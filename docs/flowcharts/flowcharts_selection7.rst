=================================================
Flowcharts Classify Triangles by Angles
=================================================


| The pseudocode below checks to see if a triangle has all angles less than 90 degrees, one angle equal to 90 degrees, or one angle greater than 90 degrees, and classifies it accordingly.

.. code-block:: pseudocode

    ALGORITHM triangleAngleType()

    BEGIN
        INPUT angleA, angleB, angleC

        IF angleA + angleB + angleC ≠ 180 THEN
            PRINT "Not a valid triangle."
        ELSEIF angleA < 90 AND angleB < 90 AND angleC < 90 THEN
            PRINT "Acute triangle."
        ELSEIF angleA = 90 OR angleB = 90 OR angleC = 90 THEN
            PRINT "Right triangle."
        ELSEIF angleA > 90 OR angleB > 90 OR angleC > 90 THEN
            PRINT "Obtuse triangle."
        ENDIF
    END


|


.. admonition:: Tasks

    #. In the pseudocode, why has ``ELSEIF angleA > 90 OR angleB > 90 OR angleC > 90 THEN`` been replaced with just ``ELSE``?
    #. In the flowchart, fill in the missing text.

        .. image:: drawio_files/selection/triangles_by_angles_st.png
            :scale: 60 %
            :align: center


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                In the pseudocode, why has ``ELSEIF angleA > 90 OR angleB > 90 OR angleC > 90 THEN`` been replaced with just ``ELSE``?

                .. code-block:: none

                    All other possibilities have been tested for,
                    so an obtuse triangle is the last possibility,
                    so it doesn't need testing to confirm it.

            .. tab-item:: Q2

                In the flowchart, fill in the missing text.

                .. image:: drawio_files/selection/triangles_by_angles.png
                    :scale: 60 %
                    :align: center

