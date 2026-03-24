import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")

vectorizer = CountVectorizer()
genre_vectors = vectorizer.fit_transform(movies["genre"])

similarity_matrix = cosine_similarity(genre_vectors)

def get_recommendations(movie_name):
    movie_name = movie_name.lower()

    if movie_name not in movies["title"].str.lower().values:
        return ["Movie not found"]

    movie_index = movies[movies["title"].str.lower() == movie_name].index[0]

    similarity_scores = similarity_matrix[movie_index]

    similar_movies = sorted(
        list(enumerate(similarity_scores)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommendations = []
    for movie in similar_movies:
        recommendations.append(movies.iloc[movie[0]].title)

    return recommendations


st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommendation System")
st.markdown("### Discover movies you'll love")
st.write("Select a movie and discover similar ones based on genre.")

movie_options = movies["title"].values
selected_movie = st.selectbox("Choose a movie", movie_options)

if st.button("Get Recommendations"):
    results = get_recommendations(selected_movie)

    st.subheader("🎯 Recommended for you:")
    for movie in results:
        st.write("👉", movie)