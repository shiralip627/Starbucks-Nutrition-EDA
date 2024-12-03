# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sidebar Navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "Overview", "Exploratory Data Analysis"])

# Load dataset
data = pd.read_csv("data/cleaned_starbucks.csv")

# Home Page
if page == "Home":
    st.title("Welcome to the Starbucks EDA App! ☕️")
    st.write("Explore insights derived from Starbucks nutrition information. Dive into the data, discover trends, and visualize key metrics.")
    st.image("starbucks.jpg")

# Overview of the Data
if page == "Overview":
    st.header("Overview of the Data")
    st.write("This dataset contains information about nutrition information for Starbucks menu items.")

    tab1, tab2, tab3 = st.tabs(["Data Dictionary", "Data Types", "Sample Data"])
    with tab1:
        st.write("### Data Dictionary:")
        st.write("- `Beverage_category`: classifies the type of beverage.")
        st.write("- `Beverage_prep`: details the preparation method of the beverage.")
        st.write("- `Calories`: lists the total caloric content of each beverage.")
        st.write("- `Total Fat (g)`: the number of fat grams per serving.")
        st.write("- `Trans Fat (g)`: the number of trans fat grams per serving.")
        st.write("- `Saturated Fat (g)`: the number of saturated fat grams per serving.")
        st.write("- `Sodium`: indicates the amount of sodium in each beverage.")
        st.write("- `Total Carbohydrates (g)`: provides the total carbohydrate content.")
        st.write("- `Cholesterol (mg)`: lists the amount of cholesterol in each beverage.")
    with tab2:
        st.write("### Data Types:")
        st.write(data.dtypes)
    with tab3:
        st.write("### Sample Data:")
        st.write(data.head())

# EDA Page
if page == "Exploratory Data Analysis":
    st.header("Exploratory Data Analysis (EDA)")

    # Histogram
    st.subheader("Distribution of Calories")
    plt.figure(figsize = (10, 5))
    sns.histplot(data['Calories'], bins = 20, kde = True, color = "green")
    plt.title("Calorie Distribution")
    st.pyplot(plt)

    # Scatter Plot
    st.subheader("Relationship between Total Carbohydrates and Cholesterol")
    plt.figure(figsize = (10, 5))
    beverage_categories = data["Beverage_category"].unique()
    palette = sns.light_palette("green", n_colors = len(beverage_categories))
    sns.scatterplot(x = "Total Carbohydrates (g)", y = "Cholesterol (mg)", data = data, hue = "Beverage_category",  palette = palette)
    plt.title("Total Carbohydrates vs Cholesterol")
    plt.legend(title = "Beverage Categories", bbox_to_anchor = (1.05, 1), loc = "upper left")
    st.pyplot(plt)

    # Box Plot
    st.subheader("Caffeine by Beverage Preparation")
    median_caffeine = data.groupby("Beverage_prep")["Caffeine (mg)"].median().sort_values()
    sorted_categories = median_caffeine.index
    plt.figure(figsize = (10, 5))
    num_categories = len(sorted_categories)
    colors = sns.light_palette("green", n_colors = num_categories)
    sns.boxplot(x = "Beverage_prep", y = "Caffeine (mg)", data = data, order = sorted_categories, palette = colors)
    plt.title("Caffeine Distribution by Beverage Preparation")
    plt.xticks(rotation = 45)
    st.pyplot(plt)

    # Bar Chart
    st.subheader("Total Fat by Beverage Category")
    num_categories = data["Beverage_category"].nunique()
    colors = sns.light_palette("green", n_colors = num_categories)
    plt.figure(figsize = (10, 5))
    sns.barplot(x = "Beverage_category", y = "Total Fat (g)", data = data, palette = colors)
    plt.title("Total Fat by Beverage Category")
    plt.xticks(rotation = 45)
    st.pyplot(plt)

    st.write("Feel free to explore the data further! Use the sidebar to navigate between sections.")
