-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre text
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO artists (name, genre) VALUES ('Elbow', 'Indie');
INSERT INTO artists (name, genre) VALUES ('Catfish and the Bottlemen', 'Alternative');
INSERT INTO artists (name, genre) VALUES ('Nothing But Thieves', 'Alt-Rock');