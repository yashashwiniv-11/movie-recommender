🎬 Movie Recommendation System

This is a simple and interactive movie recommendation system built using Machine Learning and Streamlit.
The application suggests similar movies based on their genre using cosine similarity.

🚀 Features

Recommends movies based on the selected movie
Uses genre-based similarity to find related movies
Clean and easy-to-use interface built with Streamlit
Fast and responsive performance

🛠️ Tech Stack

Python
Pandas
Scikit-learn
Streamlit

📂 Project Structure

movie-recommender/
│── app.py
│── movies.csv
│── README.md

▶️ How to Run

Clone this repository:
git clone  https://github.com/yashashwiniv-11/movie-recommender.git
Go to the project folder:
cd movie-recommender
Install the required libraries:
pip install pandas scikit-learn streamlit
Run the application:
streamlit run app.py

📸 Output

Select a movie from the dropdown
Click on “Get Recommendations”
Instantly see similar movie suggestions

🧠 How It Works

The system converts movie genres into numerical data using CountVectorizer and then calculates similarity between movies using cosine similarity. Based on this, it recommends the most similar movies.

🌟 Future Improvements

Add movie posters
Use a larger dataset
Improve recommendation accuracy
Add search functionality

🙋‍♀️ Author

Yashashwini
B.Tech AIML Student