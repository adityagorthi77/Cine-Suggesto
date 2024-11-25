-- Load data into Movies Database.Genres

COPY "Movies Database"."Genres" ("GenreID", "GenreName") FROM '/path/to/sample_genres.csv' DELIMITER ',' CSV HEADER;

-- Load data into Movies Database.Movies

COPY "Movies Database"."Movies" ("MovieID", "Title", "Release Year", "Genre") FROM '/path/to/sample_movies.csv' DELIMITER ',' CSV HEADER;

-- Load data into Movies Database.Movies_Genres

COPY "Movies Database"."Movies_Genres" ("MovieID", "GenreID") FROM '/path/to/sample_movie_genres.csv' DELIMITER ',' CSV HEADER;

-- Load data into Movies Database.Ratings

COPY "Movies Database"."Ratings" ("RatingId", "UserID", "MovieID", "Ratings", "TimeStamp") FROM '/path/to/sample_ratings.csv' DELIMITER ',' CSV HEADER;

-- Load data into Movies Database.Users

COPY "Movies Database"."Users" ("UserID", "UserName", "Age", "Gender") FROM '/path/to/sample_users.csv' DELIMITER ',' CSV HEADER;
