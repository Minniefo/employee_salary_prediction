# Employee Salary Prediction System

This project is designed to predict whether an employee's salary is above or below 50,000 based on various features. It uses machine learning models and a web interface to provide predictions.

## Project Overview

This project predicts an employee's salary based on a set of input features such as education level, occupation, and hours worked per week. We employed various machine learning algorithms and selected Random Forest due to its superior performance. The application uses Flask for the backend and HTML, CSS, and Bootstrap for the frontend.

## Features

- Predict whether the salary is above or below 50,000.
- User-friendly web interface to input employee data and view predictions.
- Visual representation of the input features and predictions.
- High accuracy prediction using Random Forest.

## Technologies Used

### Frontend
- **HTML5**
- **CSS3**
- **Bootstrap**: For responsive web design.

### Backend
- **Flask**: Lightweight web framework for Python.

### Machine Learning Libraries
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical operations.
- **Scikit-learn**: Machine learning algorithms.
- **Matplotlib**: Data visualization.

## Machine Learning Models

We tested several machine learning models to find the best one for predicting whether an employee's salary is above or below $50,000. The models we tested include:

- **Linear Regression**: A simple model used to predict continuous outcomes, which performed with moderate accuracy.
- **Decision Tree Classifier**: This model splits the data based on feature importance but can overfit the data.
- **Random Forest Classifier**: An ensemble method combining multiple decision trees for more robust predictions. This model achieved the highest accuracy in our tests.
- **Naive Bayes**: A probabilistic model that assumes independence between features. It provided reasonable predictions but didn't outperform Random Forest.
- **Support Vector Classifier (SVC)**: A model that separates data using hyperplanes. It performed well but was computationally more expensive than Random Forest.

Based on the accuracy scores, **Random Forest** was selected as the final model for this project.

