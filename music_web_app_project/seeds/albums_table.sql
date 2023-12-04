-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year int,
    artist_id int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year, artist_id) VALUES ('Asleep in the Back', 2001, 1); -- artist: Elbow
INSERT INTO albums (title, release_year, artist_id) VALUES ('The Balcony', 2014, 2); -- artist: Catfish and the Bottlemen
INSERT INTO albums (title, release_year, artist_id) VALUES ('Nothing But Thieves', 2015, 3); -- artist: Nothing But Thieves
INSERT INTO albums (title, release_year, artist_id) VALUES ('Cast of Thousands', 2003, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('The Ride', 2016, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Moral Panic', 2020, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Leaders of the Free World', 2005, 1);
