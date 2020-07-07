

# Lesson Database

2 differet types of Databases
- Relational
- NOsql - JSON(JavaScript Object Notation)


CRUD operations
- C create
- R Read
- U Update
- D Delete

## Example of a Table
- Employees [Table Name]
    - Name  [Column Names]
    - Education
    - Background - Past exprience
    - Address
    - Contact Details

DB resource practise : [https://sqliteonline.com/]






## SELECT to read data from a table

SELECT * FROM demo; //READ

## INSERT to add data to a table
INSERT INTO demo (id, name, hint)
VALUES (8, 'DEVIKA', 'DB Lesson');  //WRITE

INSERT INTO EMPLOYEE (id, name, title)
VALUES (1, 'DEVIKA SAINI', 'Chief Designer'); 

INSERT INTO EMPLOYEE (id, name, title)
VALUES (2, 'Stuti SAINI', 'Quality Control VP'); 

INSERT INTO ADDRESS (id, street_name)
VALUES (19, 'Parsavnath Exotica'); 

INSERT INTO ADDRESS (id, street_name)
VALUES (4, '11 Palace Gate'); 

## UPDATE data in a table
UPDATE TABLE

ALTER TABLE EMPLOYEE
ADD ADDRESS_KEY INTEGER;

ALTER TABLE EMPLOYEE ADD CONSTRAINT fk_address_id 
FOREIGN KEY (ADDRESS_KEY) REFERENCES ADDRESS(ID);

## Remove data/record from a table
DELETE

## Create table to organize data
CREATE TABLE 
CREATE TABLE EMPLOYEE (
    ID INTEGER NOT NULL,
    NAME TEXT,
    TITLE TEXT,
    ADDRESS_KEY INTEGER,
    PRIMARY KEY (ID),
    FOREIGN KEY (ADDRESS_KEY) REFERENCES ADDRESS(ID)
);


CREATE TABLE ADDRESS (
    ID INTEGER NOT NULL,
    street_name TEXT,
    PRIMARY KEY (ID)
);


# Lesson to Practise
INSERT INTO ADDRESS (id, street_name)
VALUES (19, 'Parsavnath Exotica'); 

INSERT INTO ADDRESS (id, street_name)
VALUES (4, '11 Palace Gate'); 

SELECT * FROM employee; 
SELECT * FROM address ORDER by id;


INSERT INTO EMPLOYEE (id, name, title, address_key)
VALUES (1, 'DEVIKA SAINI', 'Chief Designer', 19); */



SELECT * FROM address WHERE ID = (SELECT address_key FROM employee WHERE name = 'DEVIKA SAINI');



## Homework
- Excel price data apply rules on the new excel sheet only
- Practise SQL statments on DB
- Read about Set theory
- Do 2 questions on Python