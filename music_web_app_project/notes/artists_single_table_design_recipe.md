# Artists: Single Table Design Recipe Template

1. Test-drive a route `GET /artists`, which returns the list of artists:
```
# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone
```

2. Test-drive a route `POST /artists`, which creates a new artist in the
   database. Your test should verify the new artist is returned in the response
   of `GET /artists`.

```
# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
```


## 1. Extract nouns from the user stories or specification

```
Nouns:

artist, name, genre
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties         |
| --------------------- | ------------------ |
| artist                | name, genre        |

Name of the table (always plural): `artists`

Column names: `name`, `genre`

## 3. Decide the column types

```
id: SERIAL
name: text
genre: text
```

## 4. Write the SQL

```sql
-- file: artists_table.sql
CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
  genre text
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 music_web_app_project < artists_table.sql
```