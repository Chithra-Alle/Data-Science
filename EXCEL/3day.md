# Functions and Formulas
Very Important, the most asked questions in Interviews
#### Difference between Functions and FOrmulas
- Function - Repetitive Action / Repetitive Block of Code
- Formula  - Calculation
- Example:
  1. Function --> sum()
  2. Formual --> A1 + B1
#### Types of Function
- pre-defined function
- usr-defined function (VBA) Visual Basic Application
A. PRE - DEFINED FUNCTIONS
1. Mathematical Functions (SUM,MAX,MIN,AVG,RANK,STDDEV etc)
3. Text Functions (UPPER,LOWER,PROPER,LEN,LEFT,RIGHT,MID,CONCAT,REPLACE,SUBSTITUTE etc)
4. Logical Functions(AND,OR)
5. Date Functions (YEAR,MONTH,DATE,DATEDIFF etc)

| Name | Upper | Lower | Proper |
|:......:|:.......:|:....:|:.....:|
| ChiThRa|CHITHRA|chithra|Chithra|

### One character 
#### UPPER 
Converts to Upper case letter UPPER()
#### LOWER
Converts to Lower case letter LOWER()
#### PROPER
Converts to proer text satisfyng english rules
#### Len
Calculates length including spaces

 ### Two character
 #### Left --> Left(Cell , no_of_characters)
 extracting left most characters

 #### Right --> Right(Cell, no_of_characters)
 extracting right most characters

 #### MID --> Mid(Cell, start, how_many_letters)
 extracting any characters in between

 #### CONCATENATE --> Concatenate(cell,cell,...,cell)
 combining texts of more than one number of cell

 #### FIND --> Find("C",cell)
find is case sensitive

 #### SEARCH --> Search("C",cell)
 search is not case sensitive

 #### REPLACE --> Replace(cell, starting_num, how many characater, what to replace?)
 To replace the characters, positional based replacement

 ## SUBSTITUTE --> Substitute(oldtext, newtext,Instance number(if you want to substitute first occurence or any particular number mention it otherwise no need to mention))
 newtext syntax ( "a", "zzz")
 ex: Substitute(cell, "a","zzz",1(optional))

#### Q. Extract middle letter from the name
mid(cell,ceiling(len(cell)/2, 1), 1) --> odd length
mid(cell,len(cell)/2,2) --> even length
 
### Logical Functions
- More than one condition-use AND, OR
- in sql where Telugu>=35 and English>=35 and Hindi>=35
- in excel AND(C1,C2,C3)
- Ex: =AND(B1>=35, C1>=35, D1>=35)
#### EXCEL
- If - IF(Condition, True, False)
- If(B1>=35,"Pass","Fail")
- If(AND(B1>=35, C1>=35, D1>=35),"Pass","Fail")
#### SQL
Case when Condition then True else false end

#### Questions 
|Age|
|:..:|
|34|
|23|
|56|
|78|
Q: Display 'Old' if Age  greater than 45 otherwise display 'Young'
#### SQL
- Case when Age > 45 then 'Old' else 'Young' end
#### EXCEL
- IF(A1>45, 'OLD', 'Young')

|WT|InM|
|:..:|:..:|
|34|45|
|78|90|
|23|89|
Q: Display 'Selected if the candidate scores more than 20 in written test and more than 10 in the interview otherwise "Rejected"
#### SQL
- Case when WT > 20 and InM>10 then 'Selected' else 'Rejected' end
### EXCEL
- IF(AND(A1>20,B1>10),'Selected','Rejected')
100%

|WT1|WT2|
|:..:|:..:|
|34|45|
|78|90|
|23|89|
Q: Display 'Selected if the candidate scores more than 20 in written test1 or more than 20 in the written test 2 otherwise "Rejected"
#### SQL
- Case when WT1 > 20 or WT2>20 then 'Selected' else 'Rejected' end
#### EXCEL
- IF(OR(A1>20,B1>20),'Selected','Rejected')

Q: Display 'Selected if the candidate scores more than 20 in written test1 or more than 20  in the written test 2 and  greater than 10 in interview  otherwise "Rejected"

#### SQL 
- Case when (WT1 > 20 or WT2>20) and Int>10 then 'Selected' else 'Rejected' end
#### EXCEL
- IF(And(OR(A1>20,B1>20) , C1>10),'Selected','Rejected')

  Q: Dispaly Old if the age is greater than 60, dispaly middle if the age is between 40 to 60, display young if the age is less than 40

#### EXCEL
- = IF(A1>60, 'Old', If(B2<40,'Young','Middle'))
- OR
- = IF(A1>60, 'Old', If(And(A1>=40,A1<=60),'Middle','Young))

|Interview|
|:..:|
|25|
|56|
|90|
|67|

Q: Display if 'Selected' if the interview marks greater than 20, 'Hold' if the interview marks between 10 and 20.... Otherwise 'You can leave'

#### SQL
- Select *, Case when Interview>20 then 'Selected' when Interview>=10 and Interview<=20 then 'Hold' else 'Sorry! You can leave"

#### EXCEL
- = IF(A1>20, 'Selected', If(And(A1>=10,A1<=20),'Hold','You can leave'))

  
#### search(B1,A2) or =search(B1,$A$2) fixing the coloumn(freeze)
- if $ symbol is before character--> means coloumn freeze
- if $ symbol is before number --> means row freeze

#### if any function gives error and not lookin good to see
use the below syntax
- if(error(Search(A1,B2)),0)


### Interveiw Question
- Count, CountA, CountBlack
- Count --> Count(A1:8) --> Counts numbers
- countA --> Count(A1:8) --> Counts other than blanks
- CountBlanck --> Count(A1:8) --> Count blanks
