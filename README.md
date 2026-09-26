# 📱 SMS Spam Detection Using NLP and Machine Learning

## 📌 Project Overview

This project is an SMS spam detection system that uses Natural Language Processing (NLP) and machine learning to classify SMS messages as either **Ham (not spam)** or **Spam**.

The project demonstrates a complete NLP workflow, from text preprocessing and feature extraction to model training, evaluation, and deployment as a web application.

---

## 🎯 Objective

The main objective is to build a machine learning model that can automatically identify unwanted or fraudulent SMS messages.

The project covers:

* Text preprocessing
* Tokenization
* Train/test splitting
* TF-IDF feature extraction
* Machine learning classification
* Model evaluation
* Error analysis
* Testing on new messages
* Model saving
* Web application development
* Deployment

---

## 📊 Dataset

The project uses the **SMS Spam Collection Dataset**, containing labeled SMS messages classified as:

* `ham` — legitimate message
* `spam` — unwanted message

The dataset was obtained from Kaggle.

---

## 🔄 NLP Pipeline

The project follows this pipeline:

```text
SMS Messages
     ↓
Data Cleaning
     ↓
Text Preprocessing
     ↓
Tokenization
     ↓
Train/Test Split
     ↓
TF-IDF Feature Extraction
     ↓
Logistic Regression
     ↓
Prediction
     ↓
Evaluation
     ↓
Streamlit Application
```

---

## 🧹 Text Preprocessing

The messages were cleaned before training the model.

The preprocessing steps included:

1. Converting text to lowercase
2. Removing URLs
3. Removing non-alphabetic characters
4. Removing extra spaces
5. Tokenizing the cleaned text into individual words

---

## 🔢 Feature Extraction

Since machine learning models cannot directly work with raw text, the messages were converted into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

The vectorizer was configured with:

* Maximum features: `5000`
* N-gram range: `(1, 2)`

This allowed the model to use both individual words and two-word combinations.

---

## 🤖 Machine Learning Model

A **Logistic Regression** classifier was used for binary classification.

The model predicts:

```text
0 → Ham
1 → Spam
```

The dataset was divided into:

* 80% training data
* 20% testing data

Stratified splitting was used to maintain the class distribution.

---

## 📈 Model Performance

The model achieved the following results on the test set:

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **96.32%** |
| Precision | **98.95%** |
| Recall    | **71.76%** |
| F1-score  | **83.19%** |

### Confusion Matrix

```text
                Predicted
              Ham     Spam

Actual Ham    902       1
Actual Spam    37      94
```

The model correctly classified most legitimate messages and achieved high precision for spam predictions.

However, 37 spam messages were classified as ham. This shows that some spam messages were difficult for the model to distinguish from legitimate messages.

---

## 🔍 Error Analysis

The model made **38 incorrect predictions**:

* 1 ham message was classified as spam
* 37 spam messages were classified as ham

Some missed spam messages used conversational language, abbreviations, service notifications, or promotional wording that resembled legitimate SMS messages.

This indicates that the model can still be improved, particularly in identifying more varied forms of spam.

---

## 🧪 Testing New Messages

The trained model was also tested on new SMS messages.

Examples included:

```text
Congratulations! You have won a free prize. Call now!
```

Prediction:

```text
SPAM
```

and:

```text
Hey, are we still meeting at 3pm?
```

Prediction:

```text
HAM
```

The model successfully classified the test examples according to their content patterns.

---

## 🌐 Web Application

A Streamlit application was developed to allow users to enter an SMS message and receive a prediction.

The application:

1. Accepts an SMS message
2. Converts it into TF-IDF features
3. Uses the trained Logistic Regression model
4. Predicts Ham or Spam
5. Displays the prediction confidence

### Application

**Live Demo:** https://nlpspamdetection-dzqdcggkfyq4pr8b8pyqex.streamlit.app/

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF
* Logistic Regression
* Joblib
* Streamlit
* Git
* GitHub
* Kaggle

---

## 📁 Project Structure

```text
NLP_Spam_Detection/
│
├── models/
│   ├── spam_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Running the Application Locally

Clone the repository:

```bash
git clone https://github.com/Hoga30/NLP_Spam_Detection.git
```

Move into the project directory:

```bash
cd NLP_Spam_Detection
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 📚 Learning Outcomes

Through this project, I learned how to:

* Work with text classification data
* Clean and preprocess natural language
* Tokenize text
* Convert text into numerical representations using TF-IDF
* Train a classification model
* Evaluate NLP models using multiple metrics
* Analyze model errors
* Save trained machine learning models
* Build a Streamlit application
* Deploy a machine learning application

---

## 🔮 Future Improvements

Possible improvements include:

* Experimenting with additional NLP models
* Improving text preprocessing
* Preserving useful numerical and symbolic spam features
* Handling abbreviations and informal SMS language
* Addressing missed spam messages
* Comparing different classification algorithms
* Expanding the application with additional user features

---

