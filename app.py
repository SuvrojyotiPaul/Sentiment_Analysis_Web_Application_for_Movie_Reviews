from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
import re
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
@app.route('/home.html')
def home():
    return render_template('home.html')

# Define the route for processing the review and displaying the result
@app.route('/result.html', methods=['POST'])
def result():
    if request.method == 'POST':
        text = request.form.get('fname')
        sent = re.sub(r'[^\w\s]', '', text)  # remove punctuation
        sent = re.sub(r'\d+', '', sent)  # remove numbers
        sent = sent.lower()  # convert to lowercase
        sent = np.array([sent])
        sent = vect.transform(sent).toarray()
        pred = model.predict(sent)
        if pred == [0]:
            cri = 'Negative'
        else:
            cri = 'Positive'
        
        # Initialize connection and cursor in the same thread as INSERT statement
        conn = sqlite3.connect('reviews.db')
        c = conn.cursor()
        c.execute('INSERT INTO reviews (review, prediction) VALUES (?, ?)', (text, cri))
        conn.commit()
        conn.close()
        
        return render_template('result.html', prediction=cri)

# Define the route for displaying the stored data
@app.route('/data.html')
def data():
    # Initialize connection and cursor in the same thread as SELECT statement
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    data = c.execute('SELECT * FROM reviews')
    return render_template('data.html', data=data)

# Load the pre-trained model and vectorizer
with open('forest.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vect = pickle.load(f)

# Run the app
if __name__ == '__main__':
    app.run("localhost", "9999", debug=True)
