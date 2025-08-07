import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import numpy ass np

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=56d4f8e2fbd1b4d36e413df3479a1669&language=en-US"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        image_url = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        image = image.resize((180, 270))  # Resize to fit nicely
        return image
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750.png?text=No+Image"


movies_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movie_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id

        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movie_poster


similarity = np.load("similarity.npy")

st.title('Movie Recommender System')
option = st.selectbox(
    'Select Movie Recommender',
    movies['title'].values
)

if st.button('Recommend'):
   names,posters=recommend(option)

   col1, col2, col3,col4,col5 = st.columns(5)
   with col1:
       st.text(names[0])
       st.image(posters[0])

   with col2:
       st.text(names[1])
       st.image(posters[1])

   with col3:
       st.text(names[2])
       st.image(posters[2])

   with col4:
       st.text(names[3])
       st.image(posters[3])

   with col5:
       st.text(names[4])
       st.image(posters[4])
