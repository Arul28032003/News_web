from deta import Deta
import streamlit as st
from streamlit_option_menu import option_menu

def display_news(news):
    st.write(news["Date"])
    st.write(news["country"])
    st.header(news["headlines"])

    with st.container():
        left, right = st.columns(2)
        with left:
            st.image(news["images"])
        with right:
            st.write(news["news"])
            authors = news.get("authors", "Unknown")
            st.write(f" By - {authors}")

    st.markdown("---")

DETA_KEY = "dGAPJHJhu_jSQ57BDygnED8L2HmM8GXHg52Apdwf8X"
deta = Deta(DETA_KEY)
db = deta.Base("news")

st.caption("Click the arrow at the top-left corner to select a category.")
st.title("TrendSpoter")
st.header("Search")

select = st.text_input("", placeholder="Enter your search term here")
st.write("")  

col1, col2, col3 = st.columns([2, 1, 1])
with col2:
    submit = st.button("Search", key="search_button")

if submit:
    res = db.fetch(query={"news?contains": select})
    data = res.items

    for news in data:
        display_news(news)

with st.sidebar:
    st.header("Select category")
    selected_option = option_menu(
        menu_title=None,
        options=["Latest", "Technology", "Business", "Sports", "South", "Science", "Crime", "Global", "Political", "Food", "Music", "Entertainment",],
        default_index=0,
        menu_icon="cast",
        orientation="vertical",
    )

if selected_option == "Latest":
    res = db.fetch(query={"category?contains": "latest"})
elif selected_option == "Technology":
    res = db.fetch(query={"category?contains": "technology"})
elif selected_option == "Business":
    res = db.fetch(query={"category?contains": "business"})
elif selected_option == "Sports":
    res = db.fetch(query={"category?contains": "Sports"})
elif selected_option == "South":
    res = db.fetch(query={"category?contains": "south"})
elif selected_option == "Science":
    res = db.fetch(query={"category?contains": "science"})
elif selected_option == "Crime":
    res = db.fetch(query={"category?contains": "crime"})
elif selected_option == "Global":
    res = db.fetch(query={"news?contains": "global"})
elif selected_option == "Political":
    res = db.fetch(query={"news?contains": "political"})
elif selected_option == "Food":
    res = db.fetch(query={"category?contains": "food"})
elif selected_option == "Music":
    res = db.fetch(query={"category?contains": "music"})
elif selected_option == "Entertainment":
    res = db.fetch(query={"category?contains": "entertainment"})


if selected_option != "":
    data = res.items
    for news in data:
        display_news(news)
