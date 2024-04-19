import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# Load the dataset with a specified encoding
data = pd.read_csv('data_01.csv', encoding='latin1')

# Page 1: Dashboard
def dashboard():
    st.title("Dashboard")
    st.image('Logo.PNG', use_column_width=True)
    st.markdown("### Abstract:")
    inspiration = '''
    The task is to collect accurate and abundant data for small Canadian communities and derive useful insights to support their local initiatives.
    '''
    st.write(inspiration)
    st.markdown("### What our Project Does?")
    what_it_does = '''
    Throughout this project, we collected, cleaned, and found useful insights from the dataset available from Kijiji for smaller communities in Canada. We then implemented and deployed machine learning models to predict the price of different rental properties.
    '''
    st.write(what_it_does)

# Page 2: Exploratory Data Analysis (EDA)
def exploratory_data_analysis():
    st.title("Exploratory Data Analysis")
    st.plotly_chart(px.histogram(data, x='Price', nbins=20, title='Distribution of Rental Prices'))
    st.plotly_chart(px.box(data, x='Type', y='Price', title='Price Distribution by Property Type'))
    type_counts = data['type'].value_counts()
    # Create a pie chart using Plotly
    st.plotly_chart(px.pie(values=type_counts, names=type_counts.index, title='Distribution of Types'))

# Page 3: Machine Learning Modeling
def machine_learning_modeling():
    st.title("Kijiji Rental Price Prediction")
    st.write("Enter the details of the property to predict its rental price:")

    # Input fields for user to enter data
    property_type = st.selectbox("Type of Property", ['Apartment', 'House', 'Condo', 'Townhouse'])
    bedrooms = st.slider("Number of Bedrooms", 1, 5, 2)
    bathrooms = st.slider("Number of Bathrooms", 1, 3, 1)
    size = st.slider("Size (sqft)", 300, 5000, 1000)
    unique_locations = data['CSDNAME'].unique()
    location = st.selectbox("Location", unique_locations)

    if st.button("Predict"):
        # Load the trained model including preprocessing
        model = joblib.load('model.pkl')

        # Assuming the model_with_preprocessing is a pipeline that ends with your estimator
        # Prepare input data as a DataFrame to match the training data structure
        input_df = pd.DataFrame({
            'Type': [property_type],
            'Bedrooms': [bedrooms],
            'Bathrooms': [bathrooms],
            'Size': [size],
            'CSDNAME': [location]
        })
        prediction = model.predict(input_df)
        st.success(f"Predicted Rental Price: ${prediction[0]:,.2f}")

# Page 4: Community Mapping
def community_mapping():
    st.title("Small Communities Map")
    geodata = pd.read_csv("smallcomunity_EDA_75.csv")
    fig = px.scatter_mapbox(geodata,
                            lat='Latitude',
                            lon='Longitude',
                            color='Population',
                            size='Price',
                            color_continuous_scale=px.colors.cyclical.IceFire,
                            size_max=15,
                            zoom=10,
                            hover_name='Type',
                            hover_data={'Price': True, 'Population': True, 'Latitude': False, 'Longitude': False},
                            title='Small Communities Map')
    fig.update_layout(mapbox_style="open-street-map")
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
