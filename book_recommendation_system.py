# -*- coding: utf-8 -*-
"""Book Recommendation System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eC-LhtmRd1uWJopMaW6YE-i7tgFCyEll
"""

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""Data Collection and Pre-Processing"""

books = pd.read_csv('/content/Books_Database.csv')

#printing the first five rows of the dataframe
books.head()

books.shape

selected_features = ['title', 'genre','author','publisher']
print(selected_features)

#replacing the null values string
for feature in selected_features: 
  books[feature] = books[feature].fillna('')

#combining all the selected features
combined_features = books['title']+' '+books['author']+' '+books['genre']+' '+books['publisher']
print(combined_features)

#converting text data to feature vectors(Basically converting tring to numerical value)

vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(combined_features)
print(feature_vectors)

"""**COSINE SIMILARITY**"""

#getting the similarity score using cosine similarity
similarity = cosine_similarity(feature_vectors)
print(similarity)

print(similarity.shape)

#getting the book name from the user
book_name = input("Enter the name of the book youre intrested in:")

#creating a list with all the books given in the dataset
list_of_all_titles = books['title'].tolist()
print(list_of_all_titles)

#finding the close match to the given output
find_close_match = difflib.get_close_matches(book_name, list_of_all_titles)
print(find_close_match)

close_match = find_close_match[0]
print(close_match)

#finding the index of the book with title
index_of_the_book = books[books.title == close_match]['id'].values[0]
print(index_of_the_book)

#getting a list of similar movies
#enumerate is loop in the list
similarity_score = list(enumerate(similarity[index_of_the_book]))
print(similarity_score)

len(similarity_score)

#sorting the books based on their similarity score
#( Basically sorting the books in reverse order usinf lambda function where x[1] is the second term in the similarity score)
sorted_similar_books = sorted(similarity_score, key = lambda x:x[1], reverse = True)
print(sorted_similar_books)

#printing the title of the books

print("BOKS WE WOULD LIKE TO SUGGEST YOU <3")
i = 1

for book in sorted_similar_books:
  index = book[0]
  title_from_index = books[books.index == index]['title'].values[0]
  if(i<=30):
    print(i, '-', title_from_index)
    i+=1

"""BOOK RECOMMENDATION SYSTEM"""

book_name = input("Enter the name of the book youre intrested in:")
list_of_all_titles = books['title'].tolist()

find_close_match = difflib.get_close_matches(book_name, list_of_all_titles)

close_match = find_close_match[0]

index_of_the_book = books[books.title == close_match]['id'].values[0]

sorted_similar_books = sorted(similarity_score, key = lambda x:x[1], reverse = True)

print("BOKS WE WOULD LIKE TO SUGGEST YOU <3")
i = 1

for book in sorted_similar_books:
  index = book[0]
  title_from_index = books[books.index == index]['title'].values[0]
  if(i<=30):
    print(i, '-', title_from_index)
    i+=1