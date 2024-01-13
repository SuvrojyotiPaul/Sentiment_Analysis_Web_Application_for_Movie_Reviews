# Sentiment_Analysis_Web_Application_for_Movie_Reviews


## Project Overview

This web application offers an intuitive platform for sentiment analysis on movie reviews, leveraging a machine learning model trained on the IMDB dataset. It's designed with user-friendly navigation and efficient data handling, making it ideal for those interested in natural language processing and sentiment classification.

### Key Features

- **Home Page**: Accessible via ‘/home.html’ and ‘/’, the home page is the gateway to the application. It features:
  - A **Navigation Bar** for easy access to different sections of the web app.
  - A **Header** that sets the context for the application.
  - **Informational Text** providing insights into the app's functionality.
  - An **Input Form** where users can submit movie reviews.
  - A **Submit Button** for review analysis.

- **Sentiment Analysis**: Upon submission, the app employs a `scikit-learn` model to classify the review as either positive or negative. This process includes:
  - **Preprocessing** of the review text, similar to the procedures in the NLP IMDB notebook.
  - Displaying the **Result** on a separate page (‘/result.html’), which indicates whether the sentiment of the review is positive or negative.

- **Result Page**: This page:
  - Echoes the

navigation bar from the home page for consistency.
  - Clearly displays the **Sentiment Analysis Result** of the submitted review, categorizing it as either positive or negative.

- **Data Storage**: All reviews and their corresponding predictions are:
  - Stored in a **SQLite Database**.
  - The database table includes two columns: one for the **Movie Review** and another for the **Prediction** (positive or negative).

- **Data Page**: Located at ‘/data.html’, this page:
  - Lists all user-submitted reviews and their predictions.
  - Maintains the same navigation bar for seamless user experience.

### User Interaction Flow

1. **Submit a Review**: Users enter a movie review on the home page and submit it for analysis.
2. **View Results**: The sentiment (positive or negative) is displayed on the result page.
3. **Review Database**: Users can navigate to the data page to view all submitted reviews and their corresponding sentiment analysis.


This application serves as a practical implementation of sentiment analysis in NLP, demonstrating the power of machine learning in classifying text data. It's a valuable tool for movie enthusiasts, data scientists, and anyone interested in the intersection of AI and film criticism.


![Screenshot 2024-01-13 171006](https://github.com/SuvrojyotiPaul/Sentiment_Analysis_Web_Application_for_Movie_Reviews/assets/122437351/5840e01b-a29c-4d9c-8b75-584b15c1c1db)
![Screenshot 2024-01-13 171201](https://github.com/SuvrojyotiPaul/Sentiment_Analysis_Web_Application_for_Movie_Reviews/assets/122437351/b7de293a-fe26-41b9-a7a1-9478148bc70e)
