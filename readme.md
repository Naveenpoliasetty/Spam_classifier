# Email Spam Classifier using Streamlit

This Streamlit application uses a machine learning model to classify whether an input message is spam or not. The model is trained on a dataset and employs text preprocessing techniques for better prediction accuracy.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

1) Install the required Python packages. You can use a virtual environment for this:
pip install -r requirements.txt

2) Make sure to replace requirements.txt with the actual filename if you have one.

Run the Streamlit application:  streamlit run your_app_filename.py

Replace your_app_filename.py with the actual filename of your Streamlit app.

### Usage
Enter a message in the provided text input.

Click the "Predict" button to see the classification result.

If the result is 1, the message is classified as "Spam".
If the result is 0, the message is classified as "Not Spam".
Note: Make sure to run the prediction first before interpreting the result.

Model and Text Preprocessing
The model (model.pkl) and TF-IDF vectorizer (vectorizer.pkl) are used for prediction. They are loaded using the pickle library.

The text preprocessing includes:

Lowercasing
Tokenization
Removing non-alphanumeric characters
Removing stopwords
Applying stemming
Dependencies
Streamlit
Scikit-learn
NLTK


## Author : Naveen Poliasetty


