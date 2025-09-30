CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday)
VALUES (1, 'Ororo Munroe','1940-05-30');

INSERT INTO friends (id, name, birthday)
VALUES (2, 'Kassandra Ocampo','2002-10-11');

INSERT INTO friends (id, name, birthday)
VALUES (3, 'Ana Line Ramirez','2004-05-22');

UPDATE friends 
SET name = 'Storm'
WHERE id = 1;

ALTER TABLE friends 
ADD email TEXT;

UPDATE friends 
SET email = 'storm@codecademy.com' 
WHERE id = 1;

UPDATE friends 
SET email = 'kassog12@gmail.com' 
WHERE id = 2;

UPDATE friends 
SET email = 'analine22@gmail.com' 
WHERE id = 3;

DELETE FROM friends 
WHERE id = 1;


SELECT * 
FROM friends;
