-- Table: Movies Database.Genres

-- DROP TABLE IF EXISTS "Movies Database"."Genres";

CREATE TABLE IF NOT EXISTS "Movies Database"."Genres"
(
    "GenreID" integer NOT NULL,
    "GenreName" character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Genres_pkey" PRIMARY KEY ("GenreID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "Movies Database"."Genres"
    OWNER to postgres;


-- Table: Movies Database.Movies

-- DROP TABLE IF EXISTS "Movies Database"."Movies";

CREATE TABLE IF NOT EXISTS "Movies Database"."Movies"
(
    "MovieID" integer NOT NULL,
    "Title" character varying(255) COLLATE pg_catalog."default" NOT NULL,
    "Release Year" integer NOT NULL,
    "Genre" character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Movies_pkey" PRIMARY KEY ("MovieID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "Movies Database"."Movies"
    OWNER to postgres;


-- Index: idx_movie_movieid
-- DROP INDEX IF EXISTS "Movies Database".idx_movie_movieid;

CREATE INDEX IF NOT EXISTS idx_movie_movieid
    ON "Movies Database"."Movies" USING btree
    ("MovieID" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: idx_movies_movieid

-- DROP INDEX IF EXISTS "Movies Database".idx_movies_movieid;

CREATE INDEX IF NOT EXISTS idx_movies_movieid
    ON "Movies Database"."Movies" USING btree
    ("MovieID" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: idx_on_movies_movieid

-- DROP INDEX IF EXISTS "Movies Database".idx_on_movies_movieid;

CREATE INDEX IF NOT EXISTS idx_on_movies_movieid
    ON "Movies Database"."Movies" USING btree
    ("MovieID" ASC NULLS LAST)
    TABLESPACE pg_default;

-- Table: Movies Database.Movies_Genres

-- DROP TABLE IF EXISTS "Movies Database"."Movies_Genres";

CREATE TABLE IF NOT EXISTS "Movies Database"."Movies_Genres"
(
    "MovieID" integer NOT NULL,
    "GenreID" integer NOT NULL,
    CONSTRAINT "Movies_Genres_pkey" PRIMARY KEY ("MovieID", "GenreID"),
    CONSTRAINT "GenreID" FOREIGN KEY ("GenreID")
        REFERENCES "Movies Database"."Genres" ("GenreID") MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT "MovieID" FOREIGN KEY ("MovieID")
        REFERENCES "Movies Database"."Movies" ("MovieID") MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "Movies Database"."Movies_Genres"
    OWNER to postgres;


-- Table: Movies Database.Ratings

-- DROP TABLE IF EXISTS "Movies Database"."Ratings";

CREATE TABLE IF NOT EXISTS "Movies Database"."Ratings"
(
    "RatingId" integer NOT NULL,
    "UserID" integer,
    "MovieID" integer,
    "Ratings" numeric(2,1) NOT NULL,
    "TimeStamp" timestamp without time zone,
    CONSTRAINT "Ratings_pkey" PRIMARY KEY ("RatingId"),
    CONSTRAINT "MovieID" FOREIGN KEY ("MovieID")
        REFERENCES "Movies Database"."Movies" ("MovieID") MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT "UserID" FOREIGN KEY ("UserID")
        REFERENCES "Movies Database"."Users" ("UserID") MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "Movies Database"."Ratings"
    OWNER to postgres;


-- Index: idx_on_ratings_movieid

-- DROP INDEX IF EXISTS "Movies Database".idx_on_ratings_movieid;

CREATE INDEX IF NOT EXISTS idx_on_ratings_movieid
    ON "Movies Database"."Ratings" USING btree
    ("MovieID" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: idx_rating_movieid

-- DROP INDEX IF EXISTS "Movies Database".idx_rating_movieid;

CREATE INDEX IF NOT EXISTS idx_rating_movieid
    ON "Movies Database"."Ratings" USING btree
    ("MovieID" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: idx_ratings_movieid

-- DROP INDEX IF EXISTS "Movies Database".idx_ratings_movieid;

CREATE INDEX IF NOT EXISTS idx_ratings_movieid
    ON "Movies Database"."Ratings" USING btree
    ("MovieID" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: idx_ratingson_movieid

-- DROP INDEX IF EXISTS "Movies Database".idx_ratingson_movieid;

CREATE INDEX IF NOT EXISTS idx_ratingson_movieid
    ON "Movies Database"."Ratings" USING btree
    ("MovieID" ASC NULLS LAST)
    TABLESPACE pg_default;

-- Table: Movies Database.Users

-- DROP TABLE IF EXISTS "Movies Database"."Users";

CREATE TABLE IF NOT EXISTS "Movies Database"."Users"
(
    "UserID" integer NOT NULL,
    "UserName" character varying(256) COLLATE pg_catalog."default" NOT NULL,
    "Age" integer,
    "Gender" character varying(10) COLLATE pg_catalog."default",
    CONSTRAINT "Users_pkey" PRIMARY KEY ("UserID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "Movies Database"."Users"
    OWNER to postgres;

