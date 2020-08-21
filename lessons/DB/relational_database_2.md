# Lesson Relational Database

## Relational Database Concepts
    
    Normalization
    
    Primary Key and Composite Primary Key
    
    Index
    
 Link to the [slides](https://docs.google.com/presentation/d/1r6tIBJCv00DU7KZ1B86kCu0ohOAnrqXwakb-xIAtifE/edit?usp=sharing)  from discussion
 
## Working Example

### PostgreSQL to practise - https://sqliteonline.com/ 

## Concepts' Notes

#### Normalization
    When a table with repated data is broken down to distribute data into different but related 
    tables, it is called normalizing data or the database. New tables are related to each other 
    using foreign keys. This design also makes searching and updates faster.

#### Indexing
    Process by which a Database creates map[key-value] data structure for each record using the 
    value of the column on which indexing is applied. Databases select an algorithm for indexing 
    based on the type assigned to the said column. Indexing speeds up the search when the column
    is often searched upon
    
    Duplicate values in an indexed column will negatively affect the speed with search results
    are fetched. Indexing should only be created on columns when a search on the said column is 
    required to be processed quickly. Adding index constraints to a column slows the time it takes 
    to insert a new record to the table because before a record can be saved indexing algorithm 
    has to finish calculating and updating hash value for the said column.
#### Primary Key
    It is a column in a table which is indexed by default and must 
    have not null uniuqe values for each record.
    
#### Composite Primary Key
    When 2 or more columns are combine to form a primary key constraint.
    
