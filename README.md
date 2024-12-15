# Kijiji-Rental-
Analyses of rental property for small community all around Canada 
<p align = "center" draggable=”false” ><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8HNB-ex4xb4H3-PXRcywP5zKC_3U8VzQTPA&usqp=CAU" 
     width="200px"
     height="auto"/>
</p>



# Kijiji Rental Price Prediction Project


This project aims to predict rental property prices in Ontario using machine learning models. The project involves Exploratory Data Analysis (EDA), preprocessing, and training multiple models to classify rental prices. Additionally, a Streamlit web application has been deployed to make predictions user-friendly and interactive.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Team Members](#team-members)
3. [Technologies Used](#technologies-used)
4. [Project Structure](#project-structure)
5. [Key Features](#key-features)
6. [How to Run Locally](#how-to-run-locally)
7. [Deployed Application](#deployed-application)

## Project Overview

The project leverages machine learning to classify rental property prices into different categories (e.g., low, medium, high). By preprocessing the data and applying various models like Logistic Regression, Decision Tree, and Random Forest, we evaluate which model performs best. The selected model is then integrated into a Streamlit application for deployment.

## Team Members

- **Vanshnoor Singh Narang**
- **Akashdeep Singh**
- **Alvin Mathew**

## Technologies Used

- **Python**
- **Pandas** and **NumPy** for data manipulation
- **Matplotlib** and **Seaborn** for visualizations
- **Scikit-learn** for machine learning models and preprocessing
- **Streamlit** for building the web application

## Project Structure

```plaintext
┌── data/                  # Contains raw and processed datasets
├── notebooks/             # Jupyter notebooks for EDA and modeling
├── streamlit_app.py      # Streamlit application
├── models/               # Saved machine learning models
├── README.md             # Project documentation
```

## Key Features

- **Data Preprocessing**: Handling missing values, encoding categorical data, and scaling numerical features.
- **Model Training**: Includes Logistic Regression, Decision Tree, and Random Forest models.
- **Evaluation**: Classification reports to compare model performances.
- **Deployment**: A user-friendly Streamlit web app to predict rental prices.

## How to Run Locally

### Prerequisites

- Python 3.8 or above
- Required libraries listed in `requirements.txt`

### Steps

1. Clone this repository:
   ```bash
   git clone <[repository_url](https://github.com/alvin587875/Kijiji-Rental-/edit/main/)>
   cd <Kijiji-Rental>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

4. Open the provided URL in your browser to access the app.

## Deployed Application

The application is deployed using Streamlit and can be accessed via the following link:

[Streamlit App](#)

Feel free to test the features and make predictions on rental property prices.

---

For any issues or suggestions, please open an issue in this repository. Thank you!




[Uchenna Mgbaja](https://www.linkedin.com/in/marianmgbaja/)
