import streamlit as st
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import folium


# Load the dataset with a specified encoding
data = pd.read_csv('Cleaned_kijiji_55.csv', encoding='latin1')

# Page 1: Dashboard
def dashboard():
    st.image('Logo.PNG', use_column_width=True)
    st.subheader("💡 Abstract:")
    inspiration = '''
The task is to collect accurate and abundant data for small Canadian communities and derive useful insights to support their local initiatives.
    '''
    st.write(inspiration)
    st.subheader("👨🏻‍💻 What our Project Does?")
    what_it_does = '''
Throughout this project, we did collecte, cleaned and find usefull insight from the dataset, which is available from kijiji for the smaller community in canada. Followed by Implimenting and deploing Machine learning model to perdict the price of different rental property.
'''
    st.write(what_it_does)

# Page 2: Exploratory Data Analysis (EDA)
def exploratory_data_analysis():
    st.title("Exploratory Data Analysis")

    # Price Distribution
    fig = px.histogram(data, x='Price', nbins=20, title='Distribution of Rental Prices')
    st.plotly_chart(fig)

    # Boxplot for Price by Property Type
    fig = px.box(data, x='Type', y='Price', title='Price Distribution by Property Type')
    st.plotly_chart(fig)

# Page 3: Machine Learning Modeling
def machine_learning_modeling():
    st.title("Kijiji Rental Price Prediction")
    st.write("Enter the details of the property to predict its rental price:")

    # Input fields for user to enter data
    property_type = st.selectbox("Type of Property", ['Apartment', 'House', 'Condo', 'Townhouse'])
    bedrooms = st.slider("Number of Bedrooms", 1, 5, 2)
    bathrooms = st.slider("Number of Bathrooms", 1, 3, 1)
    size = st.slider("Size (sqft)", 300, 5000, 1000)

    if st.button("Predict"):
        # Load the trained model including preprocessing
        model = joblib.load('model.pkl')

        # Assuming the model_with_preprocessing is a pipeline that ends with your estimator
        # Prepare input data as a DataFrame to match the training data structure
        input_df = pd.DataFrame({
            'Type': [property_type],
            'Bedrooms': [bedrooms],
            'Bathrooms': [bathrooms],
            'Size': [size]

        })


        # Make prediction
        prediction = model.predict(input_df)

        # Display the prediction
        st.success(f"Predicted Rental Price: ${prediction[0]:,.2f}")

# Page 4: Community Mapping
def community_mapping():
    st.title("Small Communities Map")
    geodata = pd.read_csv("smallcomunity_EDA_75.csv")

    # Optional: Set your Mapbox token (if you want to use Mapbox styles)
    # px.set_mapbox_access_token('YOUR_MAPBOX_TOKEN_HERE')

    # Create the map using Plotly Express
    fig = px.scatter_mapbox(geodata,
                            lat='Latitude',
                            lon='Longitude',
                            color='Population',  # Color points by population, or choose another column
                            size='Price',  # Size points by price, or choose another column
                            color_continuous_scale=px.colors.cyclical.IceFire,
                            size_max=15,
                            zoom=10,
                            hover_name='Type',  # Display property type when hovering over points
                            hover_data={'Price': True, 'Population': True, 'Latitude': False, 'Longitude': False},
                            title='Small Communities Map')

    fig.update_layout(mapbox_style="open-street-map")  # Use OpenStreetMap style
    st.plotly_chart(fig)


# Main App Logic
def main():
    st.sidebar.title("Kijiji Community App")
    app_page = st.sidebar.radio("Select a Page", ["Dashboard", "EDA", "ML Modeling", "Community Mapping"])

    if app_page == "Dashboard":
        dashboard()
    elif app_page == "EDA":
        exploratory_data_analysis()
    elif app_page == "ML Modeling":
        machine_learning_modeling()
    elif app_page == "Community Mapping":
        community_mapping()

if __name__ == "__main__":
    main()
