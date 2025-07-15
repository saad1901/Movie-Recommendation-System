import os
import pickle
import requests
import pandas as pd
from django.shortcuts import render

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load Data
movies_dict = pickle.load(open(os.path.join(BASE_DIR, 'movieapp/data/movie_dict.pkl'), 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open(os.path.join(BASE_DIR, 'movieapp/data/similarity.pkl'), 'rb'))

def fetch_poster(movie_id):
    """
    Fetch movie poster from TMDb using movie_id.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=085e704891ac5afe9a87724a1935831b&language=en-US"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path', '')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500"
    return "https://via.placeholder.com/500"


def get_movie_description(movie_id):
    """
    Get movie description (overview) from TMDb using movie_id.
    """
    api_key = '085e704891ac5afe9a87724a1935831b'
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        description = data.get('overview', 'No description available.')
        return description
    except requests.exceptions.RequestException as e:
        print(f"Error fetching description for movie ID {movie_id}: {e}")
        return 'No description available.'


def recommend(movie):
    """
    Recommend movies similar to the selected movie.
    """
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        print(f"Movie '{movie}' not found in the dataset.")
        return [], [], []  # Return empty recommendations if movie not found

    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_desc = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_desc.append(get_movie_description(movie_id))  # Fetch the description

    return recommended_movie_names, recommended_movie_posters, recommended_movie_desc


def home(request):
    context = {
        'movies': movies['title'].values,
        'recommendations': None,
        'selected_movie': None,
    }

    if request.method == "POST":
        selected_movie = request.POST.get('movie')
        if selected_movie:
            try:
                names, posters, descriptions = recommend(selected_movie)  # Fetch descriptions too
                context.update({
                    'recommendations': zip(names, posters, descriptions),  # Pass names, posters, and descriptions
                    'selected_movie': selected_movie
                })
            except Exception as e:
                print(f"Error recommending movies for '{selected_movie}': {e}")
                context['error'] = "Could not fetch recommendations. Please try again."

    return render(request, 'home.html', context)

