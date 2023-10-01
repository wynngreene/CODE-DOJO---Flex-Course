-- Query: Create 3 new users

INSERT INTO users_schema.users
(first_name, last_name, email, created_at, updated_at)
VALUES
("Bilbo", "Baggins", "ring_bearer@email.com", "2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Spongebob", "Sqaurepants", "pineapple@email.com", "2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Mario", "Plumberman", "mushroom_eats@email.com", "2023-09-30 00:00:00","2023-09-30 00:00:00")


-- Query: Retrieve all the users
SELECT * FROM users;

-- Query: Retrieve the first user using their email address
SELECT * FROM users
WHERE email = "ring_bearer@email.com";

-- Query: Retrieve the last user using their id
SELECT * FROM users
WHERE id = 13;

-- Query: Change the user with id=3 so their last name is Pancakes
UPDATE users_schema.users
SET last_name = "Pancakes"
WHERE id = 3;

-- Query: Delete the user with id=2 from the database
DELETE from users_schema.users
WHERE id = 2;

-- Query: Get all the users, sorted by their first name
SELECT first_name
FROM users
ORDER BY first_name;

-- BONUS Query: Get all the users, sorted by their first name in descending order
SELECT first_name
FROM users
ORDER BY first_name DESC;
