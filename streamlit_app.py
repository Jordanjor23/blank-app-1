
import streamlit as st
import streamlit as st
import pandas as pd
import plotly.express as px 





#Sidebar


page = st.sidebar.selectbox("Select a page", ['Home', "Data Overview", "EDA","Final Thoughts"])

#Display Pages

if page == "Home":
    st.title("📊 Starbucks Data Analysis Project")
    st.write("The Starbucks dataset provides nuturiontal information about the famous Starbucks menu. It contains 240 rows of Starbucks menu items ranging from (Frappuccino® Blended Coffee, Tazo® Tea Drinks, and  Classic Espresso Drinks). For each drink on the menu, the dataset includes nutritional information like calories, vitamin count, and cafeine level.")
# st.image('./photo_1.jpg', caption="Starbucks Drinks") 
   

elif page == "Data Overview":
   
    st.title("Data Overview")
    st.write("Welcome to the Home Page of my steamlit. The focus of this app is to complete a data analysis of a Starbucks dataset that covers nutritional information. Enjoy!")
   
    
elif page =="EDA":
        st.title("Exploratory Data Analysis (EDA)")
        st.write("This page provides elements of the Exploratory Data Analysis (EDA) for the Starbucks data project.")
      

elif page =="Final Thoughts":
        st.title("Final Thoughts")
        st.write("This page will discuss Final Thoughts about the Starbucks Data Analysis project.")
    
if page == "Data Overview":


    tab1, tab2, tab3 = st.tabs(["Quick Overview of the Data","Describing the Data", "Shape of the Data"])
    starbucks = pd.read_csv('./Copy_of_cleaned_starbucks.csv')
    with tab1:
        st.title("Quick View of the Data ")
        head = pd.DataFrame(starbucks.head(30))
        st.dataframe(head)
    with tab2:
        st.title("Describing the Data ")
        describe = pd.DataFrame(starbucks.describe())
        st.dataframe(describe)

    with tab3:  
        st.title("Shape of the Data ")
        shape_starbucks = pd.DataFrame(starbucks.shape)
        st.dataframe(shape_starbucks)
        st.write("This view of the data provides a breadown of the shape of the data.")

if page == "EDA":
    st.subheader("Select the type of visualization you'd like to explore:")
    eda_type = st.multiselect("Visualization Options", ['Histograms', 'Box Plots', 'Scatterplots', 'Bar Charts'])
    starbucks = pd.read_csv ("./Copy_of_cleaned_starbucks.csv") 
    obj_cols = starbucks.select_dtypes(include='object').columns.tolist()
    num_cols = starbucks.select_dtypes(include='number').columns.tolist()
    if 'Histograms' in eda_type:
        st.subheader("Histograms - Visualizing the Data by Beverage Category")
        st.plotly_chart(px.histogram(starbucks, x= 'Beverage_category', color= 'Beverage_category'))

    if 'Box Plots' in eda_type:
        st.subheader("Box Plots - Visualizing Numerical Distributions")
        st.plotly_chart(px.box(starbucks, x= 'Beverage_category', y= 'Caffeine (mg)', color= 'Beverage_category'))

    if 'Scatterplots' in eda_type:
        st.subheader("Scatterplots - Visualizing Relationships")
        st.plotly_chart(px.scatter(starbucks, x= 'Calories', y= 'Total Fat (g)', color= 'Beverage_category'))

    if 'Bar Charts' in eda_type:
        st.subheader("Scatterplots - Visualizing Relationships")
        st.plotly_chart(px.bar(starbucks, x= 'Beverage_category', y= 'Calories', color= 'Beverage_category')) 

if page == "Final Thoughts":
     
    st.subheader("Starbucks Coffee is Made for Everyone")
    st.write("This analysis provided insight into one of the most popular coffee shops in the wolrd, Starbucks. In the analysis we looked at key data points located in the '.csv' file which included beverage category, calories, and other relvant nutrional facts. Throughout the analysis, it became clear why Starbucks drinks are so popular. Starbuck's menu is versatile and has yummy, sweet, caffeinated, or uncaffeinated options, which makes it a good choice for everyone. In the EDA, I created visuals of how different beverages compared by calories, total fat, and caffeine levels. As a consistent Starbucks customer, I found these categories matter most the consumer because people want a drink that not only taste good, but is good for them. Overall, cool topic for an analysis. I hope you all enjoyed this. Feel free to DM me on Disco if you have any questions.")
 #   st.image('./photo_2.jpg')


