
# 🎬 Movie Recommendation System

A content-based movie recommendation platform built using **Django** and **Scikit-learn**, leveraging **cosine similarity** to suggest similar movies based on user input. The system fetches dynamic movie metadata from the **TMDB API** and presents it via a clean Bootstrap UI.

---

## 🚀 Live Demo

🌐 [Project Demo Link](#) *(Replace with your deployed URL)*

---

## 🛠️ Tech Stack

- **Backend**: Django, Python, Scikit-learn
- **Frontend**: Bootstrap, HTML5, CSS3
- **Deployment**: PythonAnywhere / Railway / Heroku *(based on what you used)*
- **API Integration**: TMDB (The Movie Database API)

---

## 🎯 Key Features

- 🔍 **Content-Based Filtering** using cosine similarity on movie metadata
- 🎞️ **Dynamic movie data** including posters, overviews, and ratings fetched from TMDB API
- 🧠 Lightweight **ML model** (TF-IDF / CountVectorizer + cosine similarity)
- ⚡ **Fast and responsive UI** powered by Bootstrap
- 🛡️ **Secure backend** with environment-managed secrets for API access

---

## ⚙️ How It Works

1. **Preprocessing**: Movie metadata (genres, keywords, etc.) is vectorized using CountVectorizer.
2. **Similarity Matrix**: Cosine similarity is computed on these vectors.
3. **User Input**: A movie title is selected by the user.
4. **Recommendation Engine**: System returns top-N similar movies using precomputed similarity scores.
5. **API Fetching**: TMDB API is used to display posters and movie details dynamically.

---

## 💻 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/movie-recommendation-django.git
cd movie-recommendation-django
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Your TMDB API Key
Create a `.env` file and add:
```env
TMDB_API_KEY=your_tmdb_api_key_here
```

### 5. Run the Server
```bash
python manage.py migrate
python manage.py runserver
```

---

## 🌐 Deployment (Handled by Me)

- 🐍 Deployed the backend on [PythonAnywhere / Heroku / Railway] using a production-ready Django setup.
- ⚙️ Configured environment variables, static files, and WSGI entry points.
- 🔗 Integrated the TMDB API securely with key rotation in deployment settings.
- 🛠️ Used version control and Git for deployment pipeline (local ➝ remote).

---

## 👤 Team Roles

| Name               | Role                           |
|--------------------|--------------------------------|
| Your Name (You)    | 🔧 Backend Developer & Deployer |
| Teammate A         | 🎨 UI Design & Frontend Logic   |
| Teammate B         | 🤖 ML Logic & Data Engineering  |

---

## 📸 Screenshots

> *(Insert screenshots of the homepage, search results, and recommendation output)*

---

## 🧠 Learnings & Takeaways

- Worked with **content-based filtering** using **cosine similarity**
- Integrated **external APIs (TMDB)** and handled dynamic data rendering
- Learned **secure backend deployment** and environment configuration for production
- Gained experience in **team-based development**, working across frontend, backend, and ML layers

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 📬 Contact

Feel free to reach out if you'd like to collaborate or ask questions!

- 📧 Email: your.email@example.com
- 💼 LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourusername)
- 🔗 Portfolio: [yourportfolio.com](https://yourportfolio.com)

---

