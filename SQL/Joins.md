# Joins  🛩️🛩️
Combining 2 or more tables is known as joins

## Types of Joins
### Inner Join 
  It gives the matching columns from both the tables
### Outer Join
- Left Outer Join / Left Join
   It gives all records from left table and matchin records from right table
- Right outer Join / Right Join
   It gives all records from right table and matchin records from left table
- Full outer Join / Full Join
   A FULL OUTER JOIN returns all records from both tables, combining matching records and filling unmatched ones with NULL.
### Cross Join
   A CROSS JOIN creates a Cartesian product, returning all possible combinations of rows from both tables.
### Self Join
   A SELF JOIN is a join where a table is joined with itself, treating it as two separate tables using aliases.

## Example
##Table A
| ID    |   English  |
|:-----:|:----------:|
| 1     |    30      |
| 2     |    45      |
| 3     | 56         |
| 4     | 56         |

##Table B
| ID    |   Maths    |
|:-----:|:----------:|
| 2     |    36      |
| 2     |    50      |
| 3     | 34         |
| 4     | 65         |
| 5     | 67         |

Inner Join -- 4
Left Join  -- 5
Right Join -- 5
Full Join  -- 6

<div style="border: 2px solid black; padding: 10px; display: inline-block;">
$$
Full Join  = (Right Join  +  Left Join ) - Inner Join
$$
</div>

