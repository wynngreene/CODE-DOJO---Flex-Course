-- Query: Create 5 different users: Jane Amsden, Emily Dixon, Theodore Dostoevsky, William Shapiro, Lao Xiu
INSERT INTO books_schema.users
(first_name, last_name, created_at, updated_at)
VALUES
("Jane", "Amsden","2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Emily", "Dixon", "2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Theodore", "Dostoevsky", "2023-09-30 00:00:00","2023-09-30 00:00:00"),
("William", "Shapiro","2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Lao", "Xiu","2023-09-30 00:00:00","2023-09-30 00:00:00");

-- Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
INSERT INTO books_schema.books
(title, num_of_pages, created_at, updated_at)
VALUES
("C Sharp", 544, "2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Java", 465, "2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Python", 234, "2023-09-30 00:00:00","2023-09-30 00:00:00"),
("PHP", 321, "2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Ruby", 245, "2023-09-30 00:00:00","2023-09-30 00:00:00");

-- Query: Change the name of the C Sharp book to C#
UPDATE books_schema.books
SET title = "C#"
WHERE id = 1;

-- Query: Change the first name of the 4th user to Bill
UPDATE books_schema.users
SET first_name = "Bill"
WHERE id = 4;

-- Query: Have the first user favorite the first 2 books
INSERT INTO books_schema.favorites
(user_id, book_id)
VALUES
(1,1),
(1,2);

-- Query: Have the second user favorite the first 3 books
INSERT INTO books_schema.favorites
(user_id, book_id)
VALUES
(2,1),
(2,2),
(2,3);

-- Query: Have the third user favorite the first 4 books
INSERT INTO books_schema.favorites
(user_id, book_id)
VALUES
(3,1),
(3,2),
(3,3),
(3,4);

-- Query: Have the fourth user favorite all the books
INSERT INTO books_schema.favorites
(user_id, book_id)
VALUES
(4,1),
(4,2),
(4,3),
(4,4),
(4,5);

-- Query: Retrieve all the users who favorited the 3rd book 
SELECT * FROM users
JOIN favorites ON users.id = favorites.user_id
JOIN  books ON books.id = favorites.book_id
WHERE book_id = 3;

-- Query: Remove the first user of the 3rd book's favorites
DELETE from books_schema.favorites
WHERE user_id = 2 AND book_id = 3;

-- Query: Have the 5th user favorite the 2nd book
INSERT INTO books_schema.favorites
(user_id, book_id)
VALUES
(5,2)

-- Find all the books that the 3rd user favorited
SELECT * FROM users
JOIN favorites ON users.id = favorites.user_id
JOIN  books ON books.id = favorites.book_id
WHERE user_id = 3;

-- Query: Find all the users that favorited to the 5th book

SELECT * FROM users
JOIN favorites ON users.id = favorites.user_id
JOIN  books ON books.id = favorites.book_id
WHERE book_id = 5;