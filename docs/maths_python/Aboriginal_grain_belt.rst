=======================
Aboriginal grain belt
=======================

| VC2M7SP04: level 7: Design algorithms involving a sequence of steps and decisions that will sort and classify sets of shapes according to their attributes, and describe how the algorithms work

* using mathematical modelling to investigate the proportion of land mass/area of Aboriginal Peoples' traditional grain belt compared with Australia's current grain belt

----

Modelling
---------------------

| To use mathematical modelling to investigate the proportion of land mass/area of Aboriginal Peoples' traditional grain belt compared with Australia's current grain belt, estimate the following:

* The total land area of Australia
* The land area of the current wheat belt
* The land area of the Indigenous grain belt


| According to Wikipedia, the total land area of Australia is **7.7 million square kilometres**.
| See: https://www.ga.gov.au/scientific-topics/national-location-information/dimensions/area-of-australia-states-and-territories
| The land area of the current wheat belt is estimated to be **460,000 square kilometres**.
| See: http://www.consortiumland.com/investors/introduction-to-the-australian-wheatbelt/
| It seems that the Indigenous grain belt with native grasses covers a similar or slightly larger area than the current wheat belt, but this is just a guess.


.. image:: https://www.consortiumland.com/wp-content/uploads/2016/06/Wheat-growing-regions-of-the-Australian-Wheatbelt.gif
   :alt: Wheat belt of Australia 2016
   :width: 600
   :align: center

.. image:: https://grdc.com.au/__data/assets/image/0021/437070/aus-map.jpg
   :alt: Wheat belt of Australia 2024
   :width: 600
   :align: center

| According to the RIRDC Report June 2015, the traditional Aboriginal grain belt (Tindale's Arc) covers a large area of southern Australia, including parts of Western Australia, South Australia, New South Wales, Victoria and Tasmania.
| See: https://www.agrifutures.com.au/wp-content/uploads/publications/15-056.pdf

.. image:: https://www.agrifutures.com.au/wp-content/uploads/2015/06/15-056-Figure-1.jpg
   :alt: Tindale's Arc Aboriginal grain belt
   :width: 600
   :align: center

----

Steps for Mathematical Modelling
-------------------------------------

| The **honeycomb tiling** method is efficient for modelling area because hexagons tessellate without gaps and approximate circular regions better than squares.

1. **Define the regions**
   - Obtain maps showing the **traditional Aboriginal grain belt** (where native grains like *microlaena* or *panicum* were cultivated) and the **current Australian grain belt** (primarily wheat and barley regions).
   - Represent each region as a polygon or shape on a coordinate grid.

2. **Overlay a geometric tiling (honeycomb pattern)**
   - Use dynamic geometry software (e.g. GeoGebra) to overlay a **hexagonal grid** across the map.
   - Each hexagon represents a unit of land area.

3. **Count and compare proportions**
   - Count how many hexagons fall within the traditional grain belt.
   - Count how many hexagons fall within the current grain belt.
   - Calculate the proportion:
     \[
     \text{Proportion} = \frac{\text{Hexagons in traditional belt}}{\text{Hexagons in current belt}}
     \]

4. **Interpret the result**
   - Express the proportion as a percentage.
   - Communicate what this means in terms of land use change — e.g. “The traditional grain belt covered about 40% of the area of today’s grain belt.”


----

Using GeoGebra
---------------------

1. **Open GeoGebra Geometry or GeoGebra Classic**
   - Go to [GeoGebra](https://www.geogebra.org/geometry).
   - Import or insert an image of the map you want to study (e.g. Australia’s grain belt regions).

2. **Create a hexagon tile**
   - Use the **Polygon tool** to draw a regular hexagon.
   - Alternatively, type in the input bar:
     ```
     RegularPolygon[(0,0),(1,0),6]
     ```
     This makes a hexagon with side length 1.

3. **Duplicate the hexagon to form a grid**
   - Use the **Translate by Vector tool** to copy the hexagon horizontally and vertically.
   - For a honeycomb effect, shift every second row by half a hexagon width.
   - Repeat until the grid covers the entire map area.

4. **Overlay the grid on the map**
   - Adjust transparency of the hexagons (right-click → Object Properties → Color → Opacity).
   - Position the grid so it covers both the traditional grain belt and the current grain belt.

5. **Count and compare areas**
   - Count how many hexagons fall inside each region.
   - Calculate proportions:
     \[
     \text{Proportion} = \frac{\text{Hexagons in traditional belt}}{\text{Hexagons in current belt}}
     \]
   - Express as a percentage and interpret in context.


