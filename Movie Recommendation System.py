import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')

# Importing the data
credits = pd.read_csv(r"H:\Downloads\tmdb_5000_credits.csv")
movies = pd.read_csv(r"H:\Downloads\tmdb_5000_movies.csv")
movies.head()


credits.head()


# merging the datasets
movies = movies.merge(credits, on='title')


# Checking the shape of merged dataset
movies.shape



movies.head(2)


# #### Selecting useful fetures :
# - genres
# - id 
# - keywords
# - title
# - overview
# - cast 
# - crew

# In[ ]:


movies = movies[['movie_id','title','overview','genres', 'keywords','cast','crew']]


# In[ ]:


movies.head()


# In[ ]:


movies.shape


# ### Preprocessing

# In[ ]:


# Checking for missing values
movies.isnull().sum()


# In[ ]:


# Dropping the missing values
movies.dropna(inplace=True)


# In[ ]:


movies.isnull().sum()


# In[ ]:


# Checking for duplicate values
movies.duplicated().sum()


# In[ ]:


# Checking the genres column of our data
movies.iloc[0].genres


# In[ ]:


#'[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]
# ['Action', 'Adventure', 'Fantasy', 'SciFi']'
# So this is in the form of list of dictionaries but we want it in the form of list


# In[ ]:


# Converting the dictionary into list format of genres
import ast
ast.literal_eval('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')


# ##### Function to extract useful data from the genres, keywords column.

# In[ ]:


def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name']) 
    return L


# In[ ]:


movies['genres'] = movies['genres'].apply(convert)
movies.head()


# #### Using the same function for keywords column

# In[ ]:


movies['keywords'] = movies['keywords'].apply(convert)
movies.head()


# In[ ]:


# Checking the cast colummn
movies['cast'][0]


# #### Function to extract first 3 actor name from the cast

# In[ ]:


def convert3(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
        counter+=1
    return L 


# In[ ]:


movies['cast'] = movies['cast'].apply(convert3)
movies.head()


# In[ ]:


# Checking the crew column
movies['crew'][0]


# #### Function to extract director's name from the crew.

# In[ ]:


def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L 


# In[ ]:


movies['crew'] = movies['crew'].apply(fetch_director)
movies.head()


# In[ ]:


# Removing the space between a single entity and converting it into one name
movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ", "")for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ", "")for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ", "")for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ", "")for i in x])


# In[ ]:


movies.head()


# In[ ]:


# Converting the overview column to list
movies['overview'] = movies['overview'].apply(lambda x:x.split())


# In[ ]:


movies.head()


# In[ ]:


movies['tags'] = movies['overview'] + movies['genres']+movies['keywords']+movies['cast']+movies['crew']


# In[ ]:


movies.head()


# In[ ]:


# Storing the required coulumns in new_df
new_df = movies[['movie_id', 'title', 'tags']]


# In[ ]:


new_df


# In[ ]:


# Joining the each words 
new_df['tags'] = new_df['tags'].apply(lambda x:" ".join(x))


# In[ ]:


new_df.head()


# In[ ]:


new_df['tags'][0]


# In[ ]:


# Converting upper case into lower cases
new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())


# In[ ]:


new_df.head()


# ### Model Building 

# In[ ]:


from sklearn.feature_extraction.text import CountVectorizer

# Create a CountVectorizer object
cv = CountVectorizer(max_features=5000, stop_words='english')

# Assuming you have a list of text documents called 'documents'
documents = ["This is the first document.", "This document is the second document.", ...]

# Fit the CountVectorizer to your data and transform it into a bag-of-words matrix
X = cv.fit_transform(documents)

# Get the feature names (words) corresponding to the columns in the matrix
feature_names = cv.get_feature_names_out()

# Print the first few feature names
print(feature_names[:10])


# In[ ]:





# #### Stemming words in tags column to avoid repeatation

# In[ ]:


import nltk
from nltk.stem.porter import PorterStemmer


# In[ ]:


ps = PorterStemmer()


# In[ ]:


# Example
['love', 'loved', 'loving']
['love', 'love', 'love']


# In[ ]:


ps.stem('loving')


# In[ ]:


def stem(text):
  L = []
  for i in text.split():
    L.append(ps.stem(i))
  return " ".join(L)


# In[ ]:


new_df['tags'] = new_df['tags'].apply(stem)


# In[ ]:


new_df.head()


# #### Applying text vectorization - Bag of Words(BoW) Term Frequency

# In[ ]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')


# In[ ]:


# Converting our tags into an array
vectors = cv.fit_transform(new_df['tags']).toarray()


# In[ ]:


vectors


# #### Calculating cosine similarities between every pair of movies

# In[ ]:


from sklearn.metrics.pairwise import cosine_similarity


# In[ ]:


similarity = cosine_similarity(vectors)


# In[ ]:


similarity.shape


# In[ ]:


similarity[0]


# #### Building the recommend function

# In[ ]:


# Fetching the index of movie
new_df[new_df['title'] == 'Batman Begins'].index[0]


# In[ ]:


# Sorting the first 5 most similar movies 
sorted(list(enumerate(similarity[1])), reverse=True,key=lambda x:x[1])[1:6]


# In[ ]:


# Creating a function to get similar movies on the basis of their similarity score
def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    for i in movies_list:
        print(new_df.iloc[i[0]].title)


# ### Evaluating our model

# In[ ]:


recommend('batman')


# In[ ]:


recommend('The Rock')


# In[ ]:


import pickle


pickle.dump(new_df, open('movies.pkl', 'wb'))




pickle.dump(new_df.to_dict(),open('movie_dict.pkl','wb'))



pickle.dump(similarity,open('similarity.pkl', 'wb'))



# ANOTHER CODE


# import streamlit as st
# import boto3
# import json

# # Connect to SageMaker
# sagemaker_client = boto3.client('sagemaker', region_name='your_region')
# sagemaker_endpoint = 'your_sagemaker_endpoint_name'

# # Create user interface to collect user preferences/behavior
# user_behavior = st.text_input("Enter user behavior or preferences")

# # Send user input to SageMaker endpoint
# if st.button("Get Recommendations"):
#     response = sagemaker_client.invoke_endpoint(
#         EndpointName=sagemaker_endpoint,
#         Body=json.dumps({"user_behavior": user_behavior}),
#         ContentType='application/json'
#     )
#     recommendations = json.loads(response['Body'].read().decode())

#     st.write("Recommended Content:")
#     for content in recommendations:
#         st.write(content)

# st.write("Modify the Streamlit app to collect user data and display recommendations.")
