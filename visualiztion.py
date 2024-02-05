import pandas as pd 
import numpy as np 
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

# step 1:
df=pd.read_csv('data_set1.csv')
st.title("Covid-19 Cases Data_Visualization")
# df=df.drop(columns=Unnamed:)
st.write(df.sample(10))

# step 2
# df.dtypes

df.describe()
df.head()
df.tail()
df.info()
df['Province'].unique()
#step 3
spelling_correction={"khyber Pakhtunkhwa": "Khyber Pakhtunkhwa",
    "islamabad Capital Territory": "Islamabad Capital Territory"}
df['Province']=df['Province'].replace(spelling_correction)
replacing={'Federal Administration Tribal Area':'Khyber Pakhtunkhwa'}
df['Province']=df['Province'].replace(replacing)
df['Province'].unique()
df['Province'].value_counts()
# Step 4
# Getting Inside of data 
st.header("Pair Plot of given data on the base of province which help use under the correlation")
a=sns.pairplot(df,hue='Province')
st.pyplot(a)
# showing number of cases in each province
st.subheader("Showing the number of cases in province with the help of swarmplot and barplot")
fig, ax = plt.subplots(nrows=2,ncols=1,figsize=(10,8))
sns.swarmplot(data=df,x="Cases",y="Province",palette='deep',ax=ax[0])
sns.barplot(df,y=df['Cases'],x=df['Province'],palette='pastel',ax=ax[1])
plt.xticks(rotation=90)
st.pyplot(fig)
# grouping data on the base of province
st.subheader("Data Groupby on the base of Provinces")
province_data=df.groupby('Province').sum()
province_data=province_data.drop(columns={'Date','Travel_history','City'})
province_data
# Number of cases in each Province
st.header("Number of cases in each Provinces")
fig, ax = plt.subplots()
province_data['Cases'].plot(kind='pie',
                            figsize = (18, 8),
                            autopct = '%1.1f%%', #The autopct='%1.1f%%' parameter formats the percentage labels on the pie chart with one decimal place.
                            startangle = 0, #The startangle=90 parameter rotates the pie chart such that the first wedge starts at the top.
                            labels = df['Province'].unique(),# showing not labels as showing in hue
                            textprops = dict(color='black', fontsize=16), # text percentage showing in pie plot 
                            explode = [0,0.01,0.02,0.03,0.04,0,0.01] #explode mean yani jitni percentage ha 7 equal part may ha divided ha un ka appas may kitna distance ha
                           ,ax=ax)
st.pyplot(fig)
plt.axis('equal') #The plt.axis('equal') line ensures that the pie chart is drawn as a circle.
plt.show()

# number of recover cases in each provinces
st.header("Number of Recovered in each Provinces")
fig, ax = plt.subplots()
province_data['Recovered'].plot(kind='pie',
                            figsize = (18, 8),
                            autopct = '%1.1f%%', #The autopct='%1.1f%%' parameter formats the percentage labels on the pie chart with one decimal place.
                            startangle = 0, #The startangle=90 parameter rotates the pie chart such that the first wedge starts at the top.
                            labels = df['Province'].unique(), # showing not labels as showing in hue
                            textprops = dict(color='black', fontsize=16), # text percentage showing in pie plot 
                            explode = [0,0.01,0.02,0.03,0.04,0,0.01] #explode mean yani jitni percentage ha 7 equal part may ha divided ha un ka appas may kitna distance ha
                           ,ax=ax)
st.pyplot(fig)
plt.axis('equal') #The plt.axis('equal') line ensures that the pie chart is drawn as a circle.
plt.show()
# Correlation matrix for all variables
st.header("Correlation Matrix For All Variables")
corrMatrix=province_data.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corrMatrix, annot=True, cmap="coolwarm", fmt=".2f",ax=ax)
st.pyplot(fig)
# Scatter plot between two variable
df['Date'] = pd.to_datetime(df['Date'])
var1=st.selectbox("Select Variable to be plotted on x-axis: ",list(province_data.columns))
var2=st.selectbox("Select Variable to be plotted on y-axis: ",list(province_data.columns))
if st.button("Show Plot"):  
# Create an animated scatter plot using plotly express
    fig = px.scatter(x=var1, y=var2,data_frame=df,
    title='COVID Cases vs Deaths Over Time',
    labels={'Cases': 'Total Cases', 'Deaths': 'Total Deaths'},
    size='Cases', color='Province',
    size_max=50)

# Update layout for better visualization
    fig.update_layout(
                    
                xaxis=dict(title='Total Cases'),
                yaxis=dict(title='Total Deaths'),
                showlegend=True,
                title_text=f"COVID {var1} vs {var2} Over Time",
                autosize=True,
                margin=dict(l=0, r=0, t=40, b=0)
#l=0: It sets the left margin of the plot to 0 pixels. This means that there will be no empty space on the left side of the plot.
#r=0: It sets the right margin of the plot to 0 pixels. Similarly, there will be no empty space on the right side of the plot.
#t=40: It sets the top margin of the plot to 40 pixels. This adds a bit of empty space at the top of the plot.
#b=0: It sets the bottom margin of the plot to 0 pixels. There will be no empty space at the bottom of the plot.
                )
    st.plotly_chart(fig)
else:
    pass
    
