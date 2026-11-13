import streamlit as st
import pandas as pd


st.title("Streamlit Text Input")

name=st.text_input("Enter your name")

age=st.sidebar.slider("Select your age:",0,100,25)

st.write(f"your age is {age}.")

option=['Python','java','c++','js']
choice=st.selectbox("choose your favorite language:",option)
st.write(f"you selected {choice}.")



if name:
    st.write(f"Hello, {name}")

data={
    'Name':['Prajwal','Kiran','chandu','Darshan'],
    'Age':[32,45,23,63],
    'City':['Hassan','Mysuru','Bangloru','Madkeri']
}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose a csv file",type='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)