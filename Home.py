import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('James Gill')
    content = """I have started on my journey to becomes a software developer. I have created this showcase page to
    demonstrate my knowledge in Python amongst other skills. I graduated with a degree in Business Management in 
    2010 and entered a career in sales, but i found that this is not a subject that is testing and i found myself 
    seeking a new challenge. I am looking forward to moving into a career in tech and am looking at progressing down
    the DevOps route. 
    """
    st.info(content)

st.subheader("Below you can find some of the apps i have built in Python, Feel free to contact me!")

col3, colgap, col4 = st.columns([1.5, 0.5, 1.5])


df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source Code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source Code]({row["url"]})')