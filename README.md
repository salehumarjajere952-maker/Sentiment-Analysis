# Sentiment Analysis with Python

This project demonstrates a simple **Sentiment Analysis model** using Python and **Naive Bayes Classification**. The goal is to classify text into **positive** or **negative** sentiment.

## Project Overview

* Built with **scikit-learn** (CountVectorizer & MultinomialNB).
* Uses a small sample dataset of positive and negative sentences.
* Converts text into numerical representation using the **Bag-of-Words** model.
* Trains a Naive Bayes model for sentiment classification.
* Tests the model on new unseen sentences and predicts their sentiment.

## Features

* Classifies text as **positive** or **negative**.
* Easy-to-understand code with clear step-by-step comments.
* Lightweight and runs quickly on any machine.
* Can be expanded with a larger dataset for better performance.

## Technologies Used

* Python
* scikit-learn (Machine Learning Library)

## Example Output

```
Text: I really love this   --> Sentiment: positive
Text: This is terrible     --> Sentiment: negative
Text: I am happy           --> Sentiment: positive
Text: I am angry and sad   --> Sentiment: negative
```

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/sentiment-analysis.git
   cd sentiment-analysis
   ```
2. Install dependencies:

   ```bash
   pip install scikit-learn
   ```
3. Run the program:

   ```bash
   python sentiment_analysis.py
   ```

## Future Improvements

* Add a larger real-world dataset.
* Implement advanced models (e.g., Logistic Regression, Deep Learning).
* Build a simple web interface to test inputs interactively.

## Author

Developed by **Saleh Umar Jajere** as part of AI & Machine Learning practice projects.

