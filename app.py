import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Welcome to my brand spanking new app ft Penguin dataset!!")


st.write('**starting** the *build* of the "penguin" app :penguin:')
st.write('Data is taken from [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/)')
st.header('Data')
df = pd.read_csv('penguins_extra.csv')
st.write('Display a sample of 20 datapoints', df.sample(20))

species = st.selectbox(f"Select species", df.species.unique())
st.write(f"Displaying a subdataframe from {species}", df[df['species']== species])

fig,ax = plt.subplots()
ax = sns.scatterplot(data= df, x = 'bill_length_mm', y='flipper_length_mm', 
hue='species')
plt.title('Relationship between bill length and flipper length in penguins')
plt.xlabel('Bill length (mm)')
plt.ylabel('Flipper length (mm)')
st.pyplot(fig)

st.bar_chart(df.groupby('island')['species'].count())

st.map(df)

st.sidebar.file_uploader('Upload a csv file', type=['csv'])
if csv_variable is not None:
    df = pd.read(csv_variable)
    st.write(df)