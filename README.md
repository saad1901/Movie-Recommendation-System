# Movie Recommendation System

A sophisticated movie recommendation engine built with React and TypeScript, leveraging matrix factorization techniques and cosine similarity algorithms to provide personalized movie suggestions.

## 🎬 Overview

This application uses advanced machine learning techniques to recommend movies based on user preferences and viewing history. The recommendation system employs collaborative filtering through matrix factorization and cosine vector similarity to identify patterns in user behavior and movie characteristics.

## ✨ Features

- **Personalized Recommendations**: Get movie suggestions tailored to your taste
- **Collaborative Filtering**: Recommendations based on similar users' preferences
- **Content-Based Filtering**: Suggestions based on movie attributes (genre, director, cast)
- **Real-time Updates**: Dynamic recommendations that adapt to new ratings
- **Advanced Search**: Find movies by title, genre, director, or actor
- **User Ratings**: Rate movies and improve recommendation accuracy
- **Movie Details**: Comprehensive information about movies including cast, plot, and ratings
- **Responsive Design**: Optimized for desktop and mobile devices

## 🔬 Technical Approach

### Matrix Factorization
The system uses **Singular Value Decomposition (SVD)** and **Non-negative Matrix Factorization (NMF)** to decompose the user-item interaction matrix into lower-dimensional representations:

```
R ≈ U × Σ × V^T
```

Where:
- `R` is the user-movie ratings matrix
- `U` represents user factors
- `V` represents movie factors
- `Σ` contains singular values

### Cosine Similarity
To find similar users and movies, we calculate cosine similarity between vectors:

```
similarity(A, B) = (A · B) / (||A|| × ||B||)
```

This measures the cosine of the angle between two vectors, providing a value between -1 and 1.

### Hybrid Approach
The system combines multiple recommendation strategies:
1. **Collaborative Filtering**: User-based and item-based recommendations
2. **Content-Based Filtering**: Movie metadata analysis
3. **Matrix Factorization**: Latent factor models
4. **Deep Learning**: Neural collaborative filtering (planned)

## 🚀 Getting Started

### Prerequisites

- Node.js (v18 or higher)
- npm or yarn package manager

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd movie-recommendation-system
```

2. **Install dependencies**
```bash
npm install
```

3. **Start the development server**
```bash
npm run dev
```

4. **Open your browser**
Navigate to `http://localhost:8080`

## 🛠 Technologies Used

### Frontend
- **React 18** - Modern UI library
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **shadcn/ui** - Beautiful and accessible components
- **React Query** - Data fetching and caching
- **React Router** - Client-side routing

### Backend & Data Processing
- **Matrix Operations** - Linear algebra computations
- **Cosine Similarity** - Vector similarity calculations
- **SVD/NMF** - Matrix factorization algorithms
- **Real-time Updates** - Dynamic recommendation updates

### Development Tools
- **Vite** - Fast build tool
- **ESLint** - Code linting
- **TypeScript** - Static type checking

## 📊 Algorithm Details

### User-Based Collaborative Filtering
1. Calculate similarity between users using cosine similarity
2. Find k-nearest neighbors for the target user
3. Predict ratings based on weighted average of neighbors' ratings

### Item-Based Collaborative Filtering
1. Compute similarity matrix between all movie pairs
2. For each user, recommend movies similar to their highly-rated ones
3. Use cosine similarity on movie feature vectors

### Matrix Factorization Process
1. **Data Preprocessing**: Handle missing values and normalize ratings
2. **Decomposition**: Apply SVD to the user-movie matrix
3. **Dimensionality Reduction**: Keep top k singular values
4. **Reconstruction**: Generate predictions from reduced matrices
5. **Optimization**: Use gradient descent to minimize RMSE
