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

#Data fetch from data base using key
DETA_KEY = st.secrets["data_key"]
deta = Deta(DETA_KEY)
db = deta.Base("data")
#Header area
st.caption("👆👈 Click the arrow at the top-left corner to select a category.")
st.title("⇝ TrendSpoter 📰🚀")
st.header("Search")
#Search bar
select = st.text_input("", placeholder="Enter your search term here ")
st.write("")  

col1, col2, col3 = st.columns([2, 1, 1]) #button align 
with col2:
    submit = st.button("Search 🔍", key="search_button")

if submit:
    # Ensure the search term is not empty
    if select.strip():
        # Query the database for news containing the search term
        res = db.fetch(query={"news?discription": select})
        data = res.items

        if not data:
            st.write("No news found matching the search term 😕.")
        else:
            # Display the news that match the search term
            for news in data:
                display_news(news)
    else:
        st.write("Please enter a search term.")
st.markdown("---")

# Sidebar menu options
with st.sidebar:
    st.header("Select category")
    selected_option = option_menu(
        menu_title=None,
        options=["Latest", "Business 📊", "Sports", "South", "Science", "Crime", "Global", "Political", "Food", "Music", "Entertainment", "Technology"],
        default_index=0,
        menu_icon="cast",
        orientation="vertical",
    )

# Fetch and display news based on the selected category
if selected_option:
    if selected_option == "Latest":
        res = db.fetch(query={"category?discription": "latest"})
    elif selected_option == "Business 📊":
        res = db.fetch(query={"category?discription": "business"})
    elif selected_option == "Sports":
        res = db.fetch(query={"category?discription": "Sports"})
    elif selected_option == "South":
        res = db.fetch(query={"category?discription": "south"})
    elif selected_option == "Science":
        res = db.fetch(query={"category?discription": "science"})
    elif selected_option == "Crime":
        res = db.fetch(query={"category?discription": "crime"})
    elif selected_option == "Global":
        res = db.fetch(query={"news?discription": "global"})
    elif selected_option == "Political":
        res = db.fetch(query={"news?discription": "political"})
    elif selected_option == "Food":
        res = db.fetch(query={"category?contains": "food"})
    elif selected_option == "Music":
        res = db.fetch(query={"category?discription": "music"})
    elif selected_option == "Entertainment":
        res = db.fetch(query={"category?discription": "entertainment"})
    elif selected_option == "Technology":
        res = db.fetch(query={"category?discription": "technology"})
    #function calling
    if res:
        data = res.items
        for news in data:
            display_news(news)
