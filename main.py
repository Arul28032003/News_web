from deta import Deta
import streamlit as st
from streamlit_option_menu import option_menu

def display_news(news):
    st.write(news["Date"])
    st.write(news["Country"])
    st.header(news["Headlines"])

    with st.container():
        left, right = st.columns(2)
        with left:
            st.image(news["Image"])
        with right:
            st.write(news["Discription"])
            authors = news.get("authors", "Unknown")
            st.write(f" By - {authors}")

    st.markdown("---")

DETA_KEY = st.secrets["data_key"]
deta = Deta(DETA_KEY)
db = deta.Base("data")

st.caption("👆👈 Click the arrow at the top-left corner to select a category.")
st.title("TrendSpoter 🚀📰")
st.header("Search")

select = st.text_input("", placeholder="Enter your search term here")
st.write("")  

col1, col2, col3 = st.columns([2, 1, 1])
with col2:
    submit = st.button("Search 🔍", key="search_button")

if submit:
    res = db.fetch(query={"Discription?contains": select})
    data = res.items

    for news in data:
        display_news(news)

with st.sidebar:
    st.header("Select Catogary")
    selected_option = option_menu(
        menu_title=None,
        options=["Latest", "Technology", "Business", "Sports", "South", "Science", "Crime", "Global", "Political", "Food", "Music", "Entertainment","Life-style"],
        default_index=0,
        menu_icon="cast",
        orientation="vertical",
    )

if selected_option == "Latest":
    res = db.fetch(query={"Discription?contains": "latest"})
elif selected_option == "Technology":
    res = db.fetch(query={"Catogary?contains": "technology"})
elif selected_option == "Business":
    res = db.fetch(query={"Catogary?contains": "business"})
elif selected_option == "Sports":
    res = db.fetch(query={"Catogary?contains": "Sports"})
elif selected_option == "South":
    res = db.fetch(query={"Catogary?contains": "south"})
elif selected_option == "Science":
    res = db.fetch(query={"Catogary?contains": "science"})
elif selected_option == "Crime":
    res = db.fetch(query={"Catogary?contains": "crime"})
elif selected_option == "Global":
    res = db.fetch(query={"Discription?contains": "global"})
elif selected_option == "Political":
    res = db.fetch(query={"Discription?contains": "political"})
elif selected_option == "Food":
    res = db.fetch(query={"Catogary?contains": "food"})
elif selected_option == "Music":
    res = db.fetch(query={"Catogary?contains": "music"})
elif selected_option == "Entertainment":
    res = db.fetch(query={"Catogary?contains": "entertainment"})
elif selected_option == "Life-style":
    res = db.fetch(query={"Catogary?contains": "life-style"})

if selected_option != "":
    data = res.items
    for news in data:
        display_news(news)
