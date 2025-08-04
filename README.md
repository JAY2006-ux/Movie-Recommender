Movie-Recommender-System.


-App.py                        # Streamlit app script
-movie_dict.pkl                # Pickled movie metadata (you’ll upload this)
-similarity.pkl                # Pickled similarity matrix (you’ll upload this)
-requirements.txt              # List of required Python packages
-README.md                     # Project overview and instructions
-assets/
    - example_output.png        # (Optional) Screenshots of the app
Movie Recommender System
This is a simple web application that recommends movies based on user input. It uses Streamlit, machine learning, and the TMDB API to fetch movie posters.

🔧 Tech Stack
Python
Streamlit
Pandas
Pickle
TMDB API
Dataset
movie_dict.pkl: Contains movie metadata like titles and IDs.
similarity.pkl: Precomputed cosine similarity matrix between movies.
How It Works
User selects a movie from a dropdown.
The app finds 5 most similar movies using a similarity matrix.
TMDB API is used to fetch and display movie posters.
Results are shown in a clean, interactive UI using Streamlit.
Recommendation Logic
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    return movie_list


🌐 TMDB API We use The Movie Database (TMDB) API to get the poster path using the movie ID.

⚠️ Note: You'll need a TMDB API key and internet connection for poster fetching to work. ▶️ Running the App

Install the dependencies:

pip install -r requirements.txt

##Then run the Streamlit app:

streamlit run App.py

-> requirements.txt streamlit pandas requests Pillow

🙌 Author

Jay Girase Built with ❤️ using Python and Streamlit.
