--- Data Generation / Data Load
The data used in this project is generated using python code by taking referenced data from Movie Lens Dataset. 
The data was generated in CSV format. The files were then loaded to pgAdmin using the PLSQL tool using the command 

--- Command to import csv

\copy table_name FROM file_path DELIMITER ',' CSV HEADER;


--- Src folder structure
1. Data CSV Files folder - Contains python generated CSV files which are loaded into the respective tables in pgAdmin
2. create.sql - Contains Create Statements / DDL for all the tables of our Movie Database
3. dmqlapp.py - Contains python code that generates Movie Recommendation Web App using Streamlit
4. load.sql - Contains command to import csv for bulk data loading into the tables
5. movielens folder - Contains movie lens data which was referenced in creating the CSV files data

--- Instructions to run and open webapp created by using Streamlit
To launch the Streamlit web app for click fraud prediction, follow these detailed steps:

 1. Install Dependencies:
	Before running the application, make sure you have the required
	dependencies installed.
		- Streamlit

 2. Open a Terminal or Command Prompt:
	Open a terminal or command prompt on your machine.

 3.  Navigate to the Working Directory:
	Navigate to the directory where the Streamlit app files are located.
	Use the cd command:
		cd path/to/project

 4. Execute the Streamlit Command:
 	Execute the following command to run the Streamlit app:
		- streamlit run dmqlapp.py

 5. Access the Web App:
	After running the command, Streamlit will initiate the app, and a local development server will start. Look for the output in the terminal, which will include a local URL (usually starting with http://localhost).

 6. Open a Web Browser:
	Streamlit web app will automatically open up.

--- User Guide: Movie Database Website
1. Home Page:

	Navigation:
	Upon entering the website, you'll find yourself on the Home Page.
	Navigate to other pages using the sidebar on the left.
	Explore "Top Rated Movies," "Low Rated Movies," "Movies by Genre," "User Ratings Count," "Register User," "Rate Movie," and "User Interactions."
	Features:

	Movie Recommendations: See 5 random movie recommendations.
	User Ratings: View a table of all movie titles and their corresponding user ratings.

2. Top Rated Movies Page:

	Navigation:
	Click on "Top Rated Movies" in the sidebar to access this page.

	Features:
	View a table of top-rated movies based on average user ratings.

3. Low Rated Movies Page:

	Navigation:

	Click on "Low Rated Movies" in the sidebar.

	Features:
	See a table of movies with below-average ratings.

4. Movies by Genre Page:

	Navigation:
	Access the "Movies by Genre" page from the sidebar.

	Features:
	Choose a genre from the selection.
	View related movies in a table.

5. Top User Ratings Count Page:

	Navigation:
	Click on "User Ratings Count" in the sidebar.

	Features:
	See a table with user names and their corresponding ratings count.

6. Register User Page:

	Navigation:
	Access the "Register User" page from the sidebar.

	Features:
	Register as a user by entering a unique ID, name, age, and gender.

7. Rate Movie Page:

	Navigation:
	Click on "Rate Movie" in the sidebar.

	Features:
	Rate a movie by entering your ID, movie ID, and a rating.

8. User Interactions Page:

	Navigation:
	Access the "User Interactions" page from the sidebar.

	Features:
	Retrieve rated movies by entering your ID.
	Explore sample user IDs for reference.

9. Refresh Database Button:

	Location:
	Find the "Refresh Database" button on every page.

	Usage:
	Click to refresh the entire database.