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
## Table A
| ID    |   English  |
|:-----:|:----------:|
| 1     |    30      |
| 2     |    45      |
| 3     | 56         |
| 4     | 56         |

## Table B
| ID    |   Maths    |
|:-----:|:----------:|
| 2     |    36      |
| 2     |    50      |
| 3     | 34         |
| 4     | 65         |
| 5     | 67         |

- Inner Join -- 4
- Left Join  -- 5
- Right Join -- 5
- Full Join  -- 6



## Full Join = (Right Join + Left Join) - Inner Join

![Joins](https://i.pinimg.com/736x/52/71/64/5271644b8c3db314b5830d902db361d9.jpg)

## Example
Table A - 20 records
Table B - 50 records
Common  - 5 records
- Inner  5
- Left   20
- Right  50
- Full Join   65
- Cross Join   1000


## Example 
Table A - 50 records
Table B - 100 records
| Type of Join| MIN  | MAX |
|:-------:|:-------:|:-------:|
| Inner Join| 0 records| 50 records|
|Left Join | 50 records | 50 records |
| Right Join | 100 records | 100 records |
| Full Join |  50 records   | 150 records |
| Cross Join | 1000 | 1000  |

## Example
Table A - m records,  Table B - n records

| Type of Join| MIN  | MAX |
|:-------:|:-------:|:-------:|
| Inner Join| 0 records| min(m,n)|
|Left Join | m | m |
| Right Join | n | n |
| Full Join | (m+n) - min(m,n)   | m+n |
| Cross Join | m*n | m*n |


