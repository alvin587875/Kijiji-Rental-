# Kijiji-Rental-
Analyses of rental property for small community all around Canada 
<p align = "center" draggable=”false” ><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8HNB-ex4xb4H3-PXRcywP5zKC_3U8VzQTPA&usqp=CAU" 
     width="200px"
     height="auto"/>
</p>



# Kijiji Rental Price Prediction Project

This project focuses on analyzing and predicting rental property prices using Kijiji's real estate dataset. By leveraging various machine learning models, this project aims to provide insights into rental price trends and build predictive tools for price estimation.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Key Results](#key-results)
- [Future Enhancements](#future-enhancements)

## Project Overview

Kijiji is a popular platform for buying, selling, and renting goods and services. This project specifically addresses the rental property market by:

- Performing **Exploratory Data Analysis (EDA)** to clean and preprocess the data.
- Using **machine learning algorithms** to predict rental prices based on features like property type, size, and amenities.
- Evaluating and comparing the performance of multiple regression models.
- Identifying key features influencing rental prices.

## Features

- **Price Prediction:** Predict rental property prices based on features such as bedrooms, bathrooms, size, and location.
- **Feature Analysis:** Understand the key drivers of rental prices through feature importance analysis.
- **Model Comparison:** Evaluate models like Linear Regression, Decision Tree, Random Forest, and Gradient Boosting.
- **Categorical Classification (Optional):** Categorize rental properties into price ranges (low, medium, high).

## Dataset

- **Source:** Kijiji real estate dataset.
- **Key Attributes:**
  - `Bedrooms`: Number of bedrooms in the property.
  - `Bathrooms`: Number of bathrooms in the property.
  - `Size`: Size of the property in square feet.
  - `Type`: Type of property (e.g., Apartment, Condo, House).
  - `Utilities`: Availability of Hydro, Heat, and Water.
  - `Price`: Rental price of the property.

## Technologies Used

- **Programming Language:** Python
- **Libraries:**
  - `pandas`, `numpy` for data manipulation and analysis.
  - `scikit-learn` for machine learning algorithms and preprocessing.
  - `matplotlib` for data visualization.
- **Tools:** Jupyter Notebook, Google Colab, GitHub

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/kijiji-price-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd kijiji-price-prediction
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the preprocessing and modeling scripts:
   ```bash
   python eda_ml_work_integrated_02.py
   python modelling_kijiji.py
   ```
5. View results in the output CSV files and generated plots.

## Project Structure

```
.
├── data/                     # Dataset files
├── eda_ml_work_integrated_02.py  # Data cleaning and EDA script
├── modelling_kijiji.py          # Machine learning models
├── requirements.txt          # Dependencies
├── README.md                 # Project description (this file)
```

## Key Results

- **Best Model:** [e.g., Gradient Boosting Regressor]
- **Performance Metrics:**
  - Mean Squared Error (MSE): [Value]
  - R-squared (R²): [Value]
- **Feature Importance:**
  - [Feature 1]: [Importance Value]
  - [Feature 2]: [Importance Value]

## Future Enhancements

- **Hyperparameter Tuning:** Optimize model parameters for better performance.
- **Additional Features:** Incorporate more features like location-based data or proximity to amenities.
- **Classification Models:** Develop models for predicting price categories.
- **Interactive Dashboard:** Create a user-friendly interface for price prediction.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Author:** [Your Name]\
**Contact:** [Your Email]

Thank you



[Uchenna Mgbaja](https://www.linkedin.com/in/marianmgbaja/)
