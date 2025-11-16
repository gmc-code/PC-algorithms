=======================
Random walks
=======================

| VC2M5N10: level 5: Follow a mathematical algorithm involving branching and repetition (iteration); create and use algorithms involving a sequence of steps and decisions and digital tools to experiment with factors, multiples and divisibility; identify, interpret and describe emerging patterns


* simulating a simple random walk

----

1D walk plot: Walking the plank
---------------------------------

| Simulate walking the plank on a pirate ship.
| Have 9 positions on the plank, from 1 to 9, with position 1 at the start of the plank and 9 at the end.
| Start at position 3.

| The pseudocode to simulate a 1D random walk and plot the results.

.. code-block:: pseudocode

    FUNCTION random_walk_1d(start_position)
        x ← start_position
        positions ← [x]

        WHILE x > 0 AND x < 10 DO
            step ← RANDOM CHOICE FROM [-1, +1]
            IF step = +1 THEN
                x ← x + 1
            ELSE
                x ← x - 1
            ENDIF
            APPEND x TO positions
        ENDWHILE

        RETURN positions
    ENDFUNCTION


    FUNCTION plot_random_walk_1d(positions)
        DRAW LINE GRAPH OF positions
        SET TITLE ← "Random Walk 1D"
        LABEL X-AXIS ← "Step"
        LABEL Y-AXIS ← "Position"
        CALL save_plot(graph, "random_walk_1D.png")
        DISPLAY graph
    ENDFUNCTION


    FUNCTION save_plot(graph, filename)
        filepath ← DIRECTORY OF THIS FILE + filename
        SAVE graph TO filepath WITH HIGH RESOLUTION
    ENDFUNCTION


    BEGIN
        INPUTS:
            start_position ← 3   -- initial position for the walk

        PROCESS:
            positions ← CALL random_walk_1d(start_position)
            CALL plot_random_walk_1d(positions)

        OUTPUT:
            DISPLAY graph of the random walk with labelled axes and title
    END




------------------------

| The python to simulate a 1D random walk and plot the results.

.. literalinclude:: files/random_walk_1D_plot.py
    :linenos:

| Examples 1D walks are below:

.. image:: images/random_walk_1D.png
    :width: 600
    :align: center

.. image:: images/random_walk_1D_multi.png
    :width: 600
    :align: center

----

Walking the plank analysis
---------------------------

| Simulate walking the plank on a pirate ship.
| Have 9 positions on the plank, from 1 to 9, with position 1 at the start of the plank and 9 at the end.

.. literalinclude:: files/random_walk_1D.py
    :linenos:

| The code below simulates a 1D random walk.
| The `random_walk_1d` function takes a starting position as an argument, with a default value of 3.
| The function simulates a random walk by generating random steps using the `random.randint` function.
| If the step is 1, the position is incremented by 1, otherwise it is decremented by 1.
| The new position is then appended to the `x_positions` list.
| This continues until the position reaches either 0 or 10.

| The script then simulates `number_of_walks` walks for each starting position from 1 to 9.
| For each walk, it checks if the final position is 0 and if so, increments the `safe_count` variable.
| Finally, it prints the starting position and the percentage of walks that ended at position 0.

.. image:: images/random_walks_1D.png
    :width: 600
    :align: center

----

2D walk plot
------------------------

| The code below simulates a 2D random walk.

.. literalinclude:: files/random_walk_2D_plot.py
    :linenos:

| Examples 2D walks are below:

.. image:: images/random_walks_2D_10_steps.png
    :width: 600
    :align: center

.. image:: images/random_walks_2D_50_steps.png
    :width: 600
    :align: center

.. image:: images/random_walks_2D_100_steps.png
    :width: 600
    :align: center

.. image:: images/random_walks_2D_1000_steps.png
    :width: 600
    :align: center

----

| The code below simulates a multiple 2D random walks suitable for 2 to 6 walks.

.. literalinclude:: files/random_walk_2D_multiplot.py
    :linenos:

| Examples multi 2D walks are below:

.. image:: images/random_walks_2D_multi_20_steps.png
    :width: 600
    :align: center

.. image:: images/random_walks_2D_multi_50_steps.png
    :width: 600
    :align: center

.. image:: images/random_walks_2D_multi_1000_steps.png
    :width: 600
    :align: center

----

2D walks analysis
------------------------

| The code below simulates a 2D random walk.

.. literalinclude:: files/random_walks_2D.py
    :linenos:

| The `random_walk` function takes an argument `n` which represents the number of steps in the walk.
| The function initializes the starting position at `(0, 0)` and then simulates the walk by generating random steps using the `random.choice` function.
| The step is chosen from a list of possible steps: up, down, left, or right.
| The new position is calculated by adding the step to the current position.

| The script then simulates `number_of_walks` walks for each walk length from 0 to 30.
| For each walk, it checks if the final position is within (`dist_to_home`) 4 blocks of the origin (using the Manhattan distance) and if it is, increments the `close_to_home` variable.
| Finally, for plotting, it returns the walk length and the percentage of walks that ended within 4 blocks of the origin.

| The Manhattan distance, also known as the taxicab distance or city block distance, is a way to measure the distance between two points in a grid-like space.
| It is calculated as the sum of the absolute differences between the coordinates of the two points.
| For example, if there are two points `P1` and `P2` with coordinates `(x1, y1)` and `(x2, y2)`, respectively, then the Manhattan distance between them is `abs(x1 - x2)` + `abs(y1 - y2)`.
| This distance can be imagined as the length needed to move between two points in a grid where you can only move up, down, left or right.


.. image:: images/random_walks_2D.png
    :width: 600
    :align: center


----

Levy flights
--------------------

| Levy flights are random walks with longer jumps.
| They can simulate animals looking for food.
| The code below creates some longer jumps.


| The pseudocode to simulate a 2D random walk with Levy flights and plot the results.

.. code-block:: pseudocode

    FUNCTION levy_flight(total_steps, levy_interval, min_jump, max_jump)
        x ← 0
        y ← 0
        coords ← [(0, 0)]

        FOR i ← 0 TO total_steps - 1 DO
            IF i MOD levy_interval = 0 THEN
                r ← RANDOM INTEGER BETWEEN min_jump AND max_jump
                theta ← RANDOM ANGLE BETWEEN 0 AND 2π
                dx ← INTEGER PART OF (r * COS(theta))
                dy ← INTEGER PART OF (r * SIN(theta))
            ELSE
                (dx, dy) ← RANDOM CHOICE FROM [(0,1), (0,-1), (1,0), (-1,0)]
            ENDIF

            x ← x + dx
            y ← y + dy
            APPEND (x, y) TO coords
        ENDFOR

        RETURN coords
    ENDFUNCTION


    FUNCTION plot_walk(coords, levy_interval, total_steps)
        x_coords ← EXTRACT X VALUES FROM coords
        y_coords ← EXTRACT Y VALUES FROM coords

        DRAW LINE GRAPH OF (x_coords, y_coords)
        MARK STARTING POINT GREEN
        MARK ENDING POINT RED

        max_coord ← MAXIMUM ABSOLUTE VALUE AMONG ALL COORDINATES

        IF max_coord > 100 THEN
            ticks ← MULTIPLES OF 50 UP TO max_coord
        ELSE IF max_coord > 60 THEN
            ticks ← MULTIPLES OF 20 UP TO max_coord
        ELSE IF max_coord > 30 THEN
            ticks ← MULTIPLES OF 10 UP TO max_coord
        ELSE IF max_coord > 16 THEN
            ticks ← MULTIPLES OF 5 UP TO max_coord
        ELSE IF max_coord > 8 THEN
            ticks ← MULTIPLES OF 2 UP TO max_coord
        ELSE
            ticks ← INTEGERS FROM -max_coord TO +max_coord
        ENDIF

        SET X-AXIS TICKS ← ticks
        SET Y-AXIS TICKS ← ticks
        LIMIT X-AXIS AND Y-AXIS TO [-max_coord, +max_coord]
        ADD LEGEND FOR Start AND End
        SET TITLE ← "Random Walk (" + total_steps + " steps)"
        ADJUST LAYOUT FOR LEGEND
        CALL save_plot(graph, "random_walk_Levy_every_" + levy_interval + "_of_" + total_steps)
        DISPLAY graph
    ENDFUNCTION


    FUNCTION save_plot(graph, filename)
        filepath ← DIRECTORY OF THIS FILE + filename
        SAVE graph TO filepath WITH HIGH RESOLUTION
    ENDFUNCTION


    BEGIN
        INPUTS:
            levy_interval ← 100        -- number of steps between Levy jumps
            total_steps ← 1000         -- total number of steps in the walk
            min_jump ← 10              -- minimum jump size for Levy flight
            max_jump ← 20              -- maximum jump size for Levy flight

        PROCESS:
            coords ← CALL levy_flight(total_steps, levy_interval, min_jump, max_jump)
            CALL plot_walk(coords, levy_interval, total_steps)

        OUTPUT:
            DISPLAY graph of the walk with start and end marked
    END




| The python to simulate a 2D random walk with Levy flights and plot the results.


.. literalinclude:: files/random_walk_2D_plot_Levy.py
    :linenos:


.. image:: images/random_walk_Levy_every_100_of_1000.png
    :width: 600
    :align: center


.. image:: images/random_walk_Levy_every_200_of_1000.png
    :width: 600
    :align: center

