# Lesson Relational Database

## Set Theory Concepts
    Union 
    Intersection
    
 Link to the [slides](https://docs.google.com/presentation/d/1r6tIBJCv00DU7KZ1B86kCu0ohOAnrqXwakb-xIAtifE/edit?usp=sharing)  from discussion
 
## Working Example

### PostgreSQL to practise - https://sqliteonline.com/ 


### Create 2 tables which have 1-to-many relationship. An address(1) can be linked to many users in the users table; therefore, 1-to-many relationship between tables.

#### Addresses Table
    CREATE TABLE addresses (
      id INT PRIMARY KEY NOT NULL,
      street TEXT,
      city TEXT,
      state TEXT
    );
    
#### Users Table
    CREATE TABLE users (
      id INT PRIMARY KEY NOT NULL,
      addresses_id INT references addresses(ID),
      username TEXT
    );
    
#### Let's add data to addresses table
    INSERT INTO addresses (id,street,city,state) VALUES (
      '100',
      '40 Elizabeth Court, 1 Palgrave Gardens',
      'London, NW1 6EJ',
      'London'
    );
    INSERT INTO addresses (id,street,city,state) VALUES (
      '101',
      '502 Tower B1, Pasavnath Exotica',
      'Gurgaon, 122002',
      'Haryana'
    );

#### Let's add data to users table
    INSERT INTO users (id,addresses_id,username) VALUES (
      '41',
      '101',
      'sainidevika@gmail.com'
    );
    
    INSERT INTO users (id,addresses_id,username) VALUES (
      '42',
      '100',
      'bensaini7@gmail.com'
    ); 	
    
    INSERT INTO users (id,addresses_id,username) VALUES (
      '43',
      '101',
      'stutisaini@gmail.com'
    );
    
    
#### Let's use the INNER JOIN to show username and address for a user
    SELECT U.username, A.street, A.city
    FROM users U 
    INNER JOIN addresses A
    On u.addresses_id = A.id
    WHERE U.username = 'bensaini7@gmail.com'