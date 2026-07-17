import pandas as pd
import streamlit as st
import pickle

# Title
st.title("Movie Recommender System")

# Load data
df = pd.read_csv("cleaned_data.csv")
similarity = pickle.load(open("similarity.pkl", "rb"))

# Movie list for dropdown
movies = df["title"].tolist()

# Select movie
name = st.selectbox("Select a movie", movies)

# Get movie name from index
def get_name_by_index(i):
    if 0 <= i < len(df):
        return df.loc[i, "title"]
    return ""

# Get movie index from name
def get_index_from_name(name):
    clean_user_name = name.strip().lower().replace(" ", "").replace("-", "")

    match = df[
        df["title"]
        .str.lower()
        .str.replace(" ", "", regex=False)
        .str.replace("-", "", regex=False)
        == clean_user_name
    ]

    if not match.empty:
        return match.index[0]

    return -1

# Recommend button
if st.button("Recommend"):
    index = get_index_from_name(name)

    if index == -1:
        st.write("Movie not found.")
    else:
        similarity_indexes = list(enumerate(similarity[index]))

        similarity_indexes = sorted(
            similarity_indexes,
            key=lambda x: x[1],
            reverse=True
        )

        st.subheader("Recommended Movies")

        count = 0
        for movie in similarity_indexes:
            movie_index = movie[0]

            # Skip selected movie itself
            if movie_index != index:
                st.write(get_name_by_index(movie_index))
                count += 1

            # Show only 5 recommendations
            if count == 5:
                break
