==========================
Pseudocode
==========================

| Pseudocode is known as Structured English.
| Pseudocode is a way of writing a program that generalizes it for conversion into a programming language.
| Pseudocode represents the steps of the program in natural language and mathematical notation.
| Pseudocode describes the logic of the program or algorithm.

| See: https://www.vcaa.vic.edu.au/curriculum/vce-curriculum/vce-study-designs/pseudocode
| VCAA uses bold lowercase for pseudocode keywords, but in this documentation the common standard is to use UPPERCASE.


----

Python to Pseudocode Summary
----------------------------------

| The keywords below are in UPPERCASE.
| Pseudocode typically starts with **BEGIN** and ends with **END**.
| The table below has the typical pseudocode for common keywords and operators in python.
| The quoted text in the python is not python. It is there to indicate the purpose.

.. list-table:: Pseudocode Summary
	:widths: 125 250
	:header-rows: 1

	* - Python
	  - Pseudocode
	* - ==
	  - =
	* - =
	  - ←
	* - print
	  - OUTPUT or PRINT or DISPLAY
	* - input
	  - INPUT or GET
	* - if
	  - IF ....THEN
	* - elif
	  - ELSEIF   ....THEN
	* - else
	  - ELSE
	* - "end of if"
	  - ENDIF
	* - for
	  - FOR
	* - "end of for"
	  - ENDFOR
	* - while
	  - WHILE
	* - "end of while"
	  - ENDWHILE
	* - def
	  - FUNCTION
	* - "end of def"
	  - ENDFUNCTION
	* - return
	  - RETURN
	* - or
	  - OR
	* - and
	  - AND
	* - not
	  - NOT
	* - True
	  - TRUE
	* - False
	  - FALSE
	* - try
	  - TRY
	* - except
	  - EXCEPT
	* - pass
	  - PASS
	* - class
	  - CLASS
	* - "end of class"
	  - ENDCLASS
	* - import
	  - IMPORT
	* - open "a file"
	  - OPEN
	* - read "a file"
	  - READ
	* - write "to a file"
	  - WRITE

----

Arithmetic Operators
--------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 30 30 20

   * - **Operator**
     - **Symbol**
     - **Meaning**
     - **Example**
     - **Result**
   * - Addition
     - ``+``
     - Adds two values
     - ``5 + 3``
     - ``8``
   * - Subtraction
     - ``-``
     - Subtracts right from left
     - ``5 - 3``
     - ``2``
   * - Multiplication
     - ``×`` or ``*``
     - Multiplies two values
     - ``5 × 3`` or ``5 * 3``
     - ``15``
   * - Division
     - ``÷`` or ``/``
     - Divides left by right
     - ``6 ÷ 3`` or ``6 / 3``
     - ``2``
   * - Integer Division
     - ``DIV``
     - Quotient without remainder
     - ``7 DIV 3``
     - ``2``
   * - Modulus
     - ``MOD`` or ``%``
     - Remainder after division
     - ``7 MOD 3`` or ``7 % 3``
     - ``1``
   * - Exponentiation
     - ``^``
     - Raises to a power
     - ``2 ^ 3``
     - ``8``
   * - Negation
     - ``-``
     - Unary minus (sign change)
     - ``-5``
     - ``-5``

----

Relational and Logical Operators
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 30 30 20

   * - **Operator**
     - **Symbol**
     - **Meaning**
     - **Example**
     - **Result**
   * - Equal
     - ``=``
     - Tests equality
     - ``5 = 5``
     - ``TRUE``
   * - Not Equal
     - ``≠`` or ``<>``
     - Tests inequality
     - ``5 ≠ 3``
     - ``TRUE``
   * - Greater Than
     - ``>``
     - Left greater than right
     - ``7 > 3``
     - ``TRUE``
   * - Less Than
     - ``<``
     - Left less than right
     - ``2 < 5``
     - ``TRUE``
   * - Greater or Equal
     - ``≥`` or ``>=``
     - Left greater or equal to right
     - ``5 ≥ 5``
     - ``TRUE``
   * - Less or Equal
     - ``≤`` or ``<=``
     - Left less or equal to right
     - ``3 ≤ 5``
     - ``TRUE``
   * - AND
     - ``AND``
     - Logical conjunction
     - ``TRUE AND FALSE``
     - ``FALSE``
   * - OR
     - ``OR``
     - Logical disjunction
     - ``TRUE OR FALSE``
     - ``TRUE``
   * - NOT
     - ``NOT``
     - Logical negation
     - ``NOT TRUE``
     - ``FALSE``


----

.. list-table:: Extra Pseudocode Keywords
   :header-rows: 1
   :widths: 25 35

   * - Keyword
     - Meaning / Usage
   * - BEGIN
     - Entry point of the pseudocode program
   * - PROCEDURE
     - Defines a procedure (subroutine)
   * - ENDPROCEDURE / END PROCEDURE
     - Marks the end of a procedure
   * - PROCESS
     - Defines a process (similar to procedure, sometimes used in flowcharts)
   * - ENDPROCESS / END PROCESS
     - Marks the end of a process
   * - CALL
     - Calls a function or procedure
   * - CASE / OF
     - Multi-way branch (like switch/case)
   * - ENDCASE / END CASE
     - Marks the end of a case block
   * - STEP
     - Increment in a FOR loop
   * - LOOP
     - General loop construct
   * - REPEAT / UNTIL
     - Repeat loop until condition is true
   * - END UNTIL
     - Marks the end of a repeat-until loop
   * - DO
     - Loop body keyword (used with WHILE or UNTIL)
   * - EXIT WHEN
     - Exit loop when condition is met
   * - DISPLAY / SHOW / PROMPT / SCAN
     - Variants of output/input operations
   * - WRITE LINE / READ LINE
     - File or console I/O line operations
   * - ARRAY / LIST / RECORD / TABLE / STACK / QUEUE
     - Data structures
   * - DECLARE / CONSTANT / VARIABLE / TYPE / OF TYPE
     - Declarations of variables, constants, or types
   * - SET / SET OF
     - Set data type or assignment
   * - BEGIN / START / END
     - Block delimiters
   * - EXIT / BREAK / CONTINUE
     - Loop control statements
   * - COMMENT
     - Marks a comment
   * - WITH / BY
     - Used in structured statements (e.g. WITH record BY field)
   * - DEFAULT / OTHERWISE
     - Default branch in CASE statements
   * - NULL / EMPTY
     - Null or empty value
   * - IS / IN
     - Membership or comparison operators


