import streamlit as st
import pandas as pd
import psycopg2

# Function to establish a connection to PostgreSQL database
def connect_to_database():
    return psycopg2.connect(
        database="DMQL Project",
        user="postgres",
        password="Sujith@6740",
        host="localhost",
        port="5433"
    )

# Function to execute SQL queries
def execute_query(query, params=None):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Function to execute SQL queries that modify data
def execute_update(query, params=None):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()

# Function to load recommendations
def load_recommendations():
    recommendations_query = '''
        SELECT "Movies"."Title", "Movies"."Genre"
        FROM "Movies Database"."Movies"
        ORDER BY RANDOM() LIMIT 5;
    '''
    return execute_query(recommendations_query)

# Function to load top-rated movies
def load_top_rated():
    top_rated_query = '''
        SELECT "Movies"."Title", ROUND(AVG("Ratings"."Ratings"), 2) AS "AverageRating"
        FROM "Movies Database"."Movies"
        JOIN "Movies Database"."Ratings" ON "Movies"."MovieID" = "Ratings"."MovieID"
        GROUP BY "Movies"."Title"
        ORDER BY "AverageRating" DESC
        LIMIT 10;
    '''
    top_rated = execute_query(top_rated_query)
    
    # Convert the AverageRating to float and format with two decimal places
    top_rated_formatted = [(title, f"{average:.2f}") for title, average in top_rated]
    
    return top_rated_formatted

# Function to load low-rated movies
def load_low_rated():
    low_rated_query = '''
        SELECT "Movies"."Title", ROUND(AVG("Ratings"."Ratings"), 2) AS "AverageRating"
        FROM "Movies Database"."Movies"
        JOIN "Movies Database"."Ratings" ON "Movies"."MovieID" = "Ratings"."MovieID"
        GROUP BY "Movies"."Title"
        HAVING AVG("Ratings"."Ratings") <= 2.5
        ORDER BY "AverageRating" ASC
        LIMIT 10;
    '''
    return execute_query(low_rated_query)

# Function to load movies by genre
def load_genre_movies(selected_genre):
    genre_movies_query = f'''
        SELECT "Movies"."Title", "Genres"."GenreName"
        FROM "Movies Database"."Movies"
        JOIN "Movies Database"."Movies_Genres" ON "Movies"."MovieID" = "Movies_Genres"."MovieID"
        JOIN "Movies Database"."Genres" ON "Movies_Genres"."GenreID" = "Genres"."GenreID"
        WHERE "Genres"."GenreName" = '{selected_genre}'
        LIMIT 10;
    '''
    return execute_query(genre_movies_query)

# Function to load user ratings count
def load_user_stats():
    user_stats_query = '''
        SELECT "Users"."UserName", COUNT("Ratings"."RatingId") AS "RatingsCount"
        FROM "Movies Database"."Users"
        LEFT JOIN "Movies Database"."Ratings" ON "Users"."UserID" = "Ratings"."UserID"
        GROUP BY "Users"."UserName"
        ORDER BY "RatingsCount" DESC
        LIMIT 5;
    '''
    return execute_query(user_stats_query)

# Function to retrieve user ratings
def get_user_ratings(user_id):
    user_ratings_query = '''
        SELECT "Movies"."Title", "Ratings"."Ratings"
        FROM "Movies Database"."Movies"
        JOIN "Movies Database"."Ratings" ON "Movies"."MovieID" = "Ratings"."MovieID"
        WHERE "Ratings"."UserID" = %s;
    '''
    return execute_query(user_ratings_query, (user_id,))

# Function to load sample user IDs
def load_sample_user_ids():
    sample_user_ids_query = '''
        SELECT DISTINCT "UserID"
        FROM "Movies Database"."Users"
        LIMIT 5;
    '''
    return execute_query(sample_user_ids_query)

# Function to register a new user
def register_user(user_id, user_name, age, gender):
    try:
        conn = connect_to_database()
        cursor = conn.cursor()

        # Insert new user into the "Users" table with the provided user ID
        cursor.execute('''
            INSERT INTO "Movies Database"."Users" ("UserID", "UserName", "Age", "Gender")
            VALUES (%s, %s, %s, %s)
            RETURNING "UserID";
        ''', (user_id, user_name, age, gender))

        conn.commit()
        cursor.close()
        conn.close()

        return user_id

    except (psycopg2.Error) as e:
        return None

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://previews.123rf.com/images/pilvitus/pilvitus1902/pilvitus190200045/125301341-abstract-background-with-white-film-strip-frame-cinema-festival-poster-or-flyer-template-for-your.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Streamlit app

def main():
    st.set_page_config(
        page_title="Movie Recommender App",
        page_icon=":movie_camera:",
        layout="wide"
    )

    set_bg_hack_url()

    st.title("Cine Suggesto : Movie Database App")

    st.sidebar.image("/Users/sujith/Downloads/sample/Cine Suggesto (1).png")
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Home", "Top Rated Movies", "Low Rated Movies", "Movies by Genre", "User Ratings Count", "Register User", "Rate Movie", "User Interactions"])

    if st.button("Refresh Database"):
        # Refresh the entire database
        conn = connect_to_database()

    if page == "Home":
        st.header("Movie Recommendations")
        recommendations = load_recommendations()
        st.table(pd.DataFrame(recommendations, columns=["Title", "Genre"]).style.set_properties(**{'font-size': '20px'}))

        st.header("User Ratings")
        ratings = execute_query('''
            SELECT "Movies"."Title", "Ratings"."Ratings"
            FROM "Movies Database"."Movies"
            JOIN "Movies Database"."Ratings" ON "Movies"."MovieID" = "Ratings"."MovieID";
        ''')
        df_ratings = pd.DataFrame(ratings, columns=["Title", "Rating"])
        df_ratings["Rating"] = df_ratings["Rating"].map("{:.2f}".format)  # Format to two decimal places
        st.table(df_ratings.style.set_properties(**{'font-size': '20px'}))

    elif page == "Top Rated Movies":
        st.header("Top Rated Movies")
        top_rated = load_top_rated()
        st.table(pd.DataFrame(top_rated, columns=["Title", "Average Rating"]).style.set_properties(**{'font-size': '20px'}))

    elif page == "Low Rated Movies":
        st.header("Low Rated Movies")
        low_rated = load_low_rated()
        df_low_rated = pd.DataFrame(low_rated, columns=["Title", "Average Rating"])
        df_low_rated["Average Rating"] = df_low_rated["Average Rating"].map("{:.2f}".format)  # Format to two decimal places
        st.table(df_low_rated.style.set_properties(**{'font-size': '20px'}))

    elif page == "Movies by Genre":
        st.header("Movies by Genre")
        genre_options = ["Action", "Drama", "Comedy", "Sci-Fi"]  # Add more genres as needed
        selected_genre = st.selectbox("Select Genre", genre_options)
        genre_movies = load_genre_movies(selected_genre)
        st.table(pd.DataFrame(genre_movies, columns=["Title", "Genre"]).style.set_properties(**{'font-size': '20px'}))

    elif page == "User Ratings Count":
        st.header("User Ratings Count")
        user_stats = load_user_stats()
        st.table(pd.DataFrame(user_stats, columns=["User Name", "Ratings Count"]).style.set_properties(**{'font-size': '20px'}))
    elif page == "Register User":
        st.header("Register User")

        # User Registration Form
        user_id = st.text_input("Enter User ID:")
        user_name = st.text_input("Enter User Name:")
        age = st.number_input("Enter Age:", min_value=1, max_value=120)
        gender_options = ["Male", "Female", "Other"]
        gender = st.selectbox("Select Gender", gender_options)

        if st.button("Register User"):
            if not user_id:
                st.error("Please enter a User ID.")
            else:
                # Register the new user
                registered_user_id = register_user(user_id, user_name, age, gender)

                if registered_user_id is not None:
                    st.success(f"User {user_name} registered successfully with User ID: {registered_user_id}")
                else:
                    st.error("Error registering user. Please try again.")

    elif page == "Rate Movie":
        st.header("Rate Movie")

        # Movie Rating Form
        user_id = st.text_input("Enter User ID:")
        movie_id = st.text_input("Enter Movie ID:")
        rating_id = st.text_input("Enter Rating ID:")
        rating = st.text_input("Enter Rating:")

        if st.button("Rate Movie"):
            try:
                user_id = int(user_id)
                movie_id = int(movie_id)
                rating_id = int(rating_id) if rating_id else None
                rating = float(rating)

                # Check if the user ID exists in the Users table
                user_exists = execute_query('''
                    SELECT 1
                    FROM "Movies Database"."Users"
                    WHERE "UserID" = %s;
                ''', (user_id,))

                if not user_exists:
                    st.error("User ID does not exist. Please register first.")
                    return

                execute_update('''
                    INSERT INTO "Movies Database"."Ratings" ("RatingId", "UserID", "MovieID", "Ratings", "TimeStamp")
                    VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP);
                ''', (rating_id, user_id, movie_id, rating))
                st.success("Movie rated successfully!")
            except (ValueError, psycopg2.Error) as e:
                st.error(f"Error: {e}")


    elif page == "User Interactions":
        st.header("User Interactions")

        # User ID input
        user_id_input = st.text_input("Enter User ID:")
        if st.button("Retrieve Ratings"):
            try:
                user_id = int(user_id_input)
                user_ratings = get_user_ratings(user_id)

                if user_ratings:
                    # Convert the "Rating" column to float before formatting
                    user_ratings_df = pd.DataFrame(user_ratings, columns=["Title", "Rating"])
                    user_ratings_df["Rating"] = user_ratings_df["Rating"].astype(float)
                    st.table(user_ratings_df.style.format({"Rating": "{:.2f}"}))
                else:
                    st.info(f"No ratings found for User ID {user_id}.")

            except ValueError:
                st.error("Please enter a valid User ID.")

        # Show sample user IDs
        st.subheader("Sample User IDs:")
        sample_user_ids = load_sample_user_ids()
        st.write([user_id[0] for user_id in sample_user_ids])

# Run the app
if __name__ == "__main__":
    main()
