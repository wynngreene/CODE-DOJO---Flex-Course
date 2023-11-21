-- Query: Create 3 new dojos
INSERT INTO dojos_and_ninjas_schema.dojos
(name, created_at, updated_at)
VALUES
("Mortal Combat Dojo","2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Pokemon Shadow Dojo","2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Kamen Rider Dojo","2023-09-30 00:00:00","2023-09-30 00:00:00")

-- Query: Delete the 3 dojos you just created
DELETE from dojos_and_ninjas_schema.dojos
WHERE id = 1;
DELETE from dojos_and_ninjas_schema.dojos
WHERE id = 2;
DELETE from dojos_and_ninjas_schema.dojos
WHERE id = 3;

-- Query: Create 3 more dojos
INSERT INTO dojos_and_ninjas_schema.dojos
(name, created_at, updated_at)
VALUES
("TMNT Dojo","2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Naruto Dojo","2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Power Ranger Dojo","2023-09-30 00:00:00","2023-09-30 00:00:00")


-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO dojos_and_ninjas_schema.ninjas
(first_name,last_name, age, dojo_id, created_at, updated_at)
VALUES
("Leo","Nardo",15,4,"2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Jack","Samurai",100,4,"2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Naruto","Uzumaki",15,4,"2023-09-30 00:00:00","2023-09-30 00:00:00")

-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO dojos_and_ninjas_schema.ninjas
(first_name,last_name, age, dojo_id, created_at, updated_at)
VALUES
("Mikey","Angelo",15,5,"2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Hattori","Hanzo",135,5,"2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Jubei","Kibagami",45,5,"2023-09-30 00:00:00","2023-09-30 00:00:00")

-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO dojos_and_ninjas_schema.ninjas
(first_name,last_name, age, dojo_id, created_at, updated_at)
VALUES
("Mugen","Champloo",23,6,"2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Scorpion","Hasashi",32,6,"2023-09-30 00:00:00","2023-09-30 00:00:00"),
("Kuai","Liang",33,6,"2023-09-30 00:00:00","2023-09-30 00:00:00")

-- Query: Retrieve all the ninjas from the first dojo
SELECT * FROM ninjas
WHERE dojo_id = 4;

-- Query: Retrieve all the ninjas from the last dojo
SELECT * FROM ninjas
WHERE dojo_id = 6;

-- Query: Retrieve the last ninja's dojo
SELECT *
FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 12;

-- Query: Use a JOIN to retrieve the ninja with id 6 as well as the data from its dojo.
-- Be sure to do this in one query using a join statement.
SELECT ninjas.first_name, ninjas.last_name, dojos.name
FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 6

-- Query: Use a JOIN to retrieve all the ninjas as well as that ninja's dojo, note, 
-- you will see repeated data on dojos as a dojo can have many ninjas!
SELECT ninjas.first_name, ninjas.last_name, dojos.name AS "Ninjas Dojo"
FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id


