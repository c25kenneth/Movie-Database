#All MySQL commands used. 
CREATE DATABASE movies

CREATE TABLE Movie(id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, release_year INT, PRIMARY KEY(id)
INSERT INTO Movie (name, release_year) VALUES (%s, %s)

SELECT * FROM Movie

SELECT * FROM Movie ORDER BY release_year desc
SELECT * FROM Movie ORDER BY name ASC
SELECT * FROM Movie WHERE id=

DELETE FROM Movie WHERE id=

INSERT INTO Movie (name, release_year) VALUES (%s, %s)