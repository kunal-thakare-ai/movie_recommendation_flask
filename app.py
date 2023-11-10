from flask import Flask, render_template, request, jsonify, url_for
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

data = pickle.load(open("data.pkl", "rb"))

api_key = os.environ.get("TMDB_KEY")

data = pd.DataFrame(data)

movies = data["title"]

# similarities = pickle.load(open('similarities.pkl', 'rb'))
similiarities_dict = pickle.load(open('similarities_dict.pkl', 'rb'))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    res = requests.get(url)
    res = res.json()
    poster_path = res['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def get_movies(movie_name):
    # movie_index = data[data["title"] == movie_name].index[0]
    # rec = sorted(list(enumerate(similarities[movie_index])), reverse = True, key = lambda x: x[1])[1:6]
    # ls = []
    # path_ls = []
    # for i in rec:
    #     ls.append(data.iloc[i[0]]["title"])
    # for i in rec:
    #     path_ = fetch_poster(data.iloc[i[0]]['id'])
    #     path_ls.append(path_)
    # return ls, path_ls
    res = similiarities_dict[movie_name]
    names, id_ = res['title'], res["id"]
    path_ls = []
    for i in id_: 
        path_ = fetch_poster(i)
        path_ls.append(path_)
    return names, path_ls


@app.route('/')
def index():
    return render_template(
    'index.html',
       movies = movies)
    # )


@app.route('/recommend_movies', methods=['POST'])
def recommend_movies():
    movie_name_ = request.form.get('movie_name')  # Get the movie name from the form
    # Add your movie recommendation logic here and return the recommendations as JSON
    recommended_movies, movie_images = get_movies(movie_name_)
    # recommended_movies = ["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5"]
    # movie_images = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"]

    # Create a dictionary to store the movie names and images
    movies_data = [{'name': name, 'image': image} for name, image in zip(recommended_movies, movie_images)]

    return jsonify({'movies': movies_data})

if __name__ == "__main__":
    app.run()