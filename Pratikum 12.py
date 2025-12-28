import streamlit as st

st.write("Hello World")
import streamlit as st
import pandas as pd
 
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})) 
import streamlit as st 
 
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)
import streamlit as st
 
st.title('Belajar Analisis Data')
import streamlit as st
 
st.header('Pengembangan Dashboard')

import streamlit as st
 
st.caption('Copyright (c) 2023')
import streamlit as st
 
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')
import streamlit as st
 
st.text('Halo, calon praktisi data masa depan.')
import streamlit as st
 
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")
import pandas as pd
import streamlit as st 
 
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
 
st.dataframe(data=df, width=500, height=150)
import pandas as pd
import streamlit as st 
 
 
 
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)
import streamlit as st
 
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

import streamlit as st
 
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
 
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)
import streamlit as st
 
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)
import streamlit as st
 
text = st.text_area('Feedback')
st.write('Feedback: ', text)
import streamlit as st
 
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

import datetime
import streamlit as st
 
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)
import streamlit as st
import pandas as pd
 
uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

import streamlit as st
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)
    
import streamlit as st
 
if st.button('Say hello'):
    st.write('Hello there')
    import streamlit as st
 
agree = st.checkbox('I agree')

 
if agree:
    st.write('Welcome to MyApp')
import streamlit as st
 
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)
import streamlit as st
 
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)
import streamlit as st
 
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)
