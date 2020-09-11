CREATE TABLE author (
  id INT PRIMARY KEY NOT NULL,
  fname TEXT,
  lname TEXT
);



CREATE TABLE users (
  id INT PRIMARY KEY NOT NULL,
   fname TEXT,
  lname TEXT
);


CREATE TABLE user_ratings (
  id INT PRIMARY KEY NOT NULL,
  ratings int
);


CREATE TABLE book_details (
  id INT PRIMARY KEY NOT NULL,
  name int,
  price decimal
);


CREATE TABLE book_details_user_ratings_users_mapping (
  book_details_id INT references book_details(ID),
  user_ratings_id INT references user_ratings(ID),
  users_id INT references users(ID),
  description TEXT
);

CREATE TABLE AUTHOR_BOOK_DETAIL_MAPPING (
  book_details_id INT references book_details(ID),
  author_id INT references author(ID)
);