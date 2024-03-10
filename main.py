from deta import Deta
import streamlit as st
from streamlit_option_menu import option_menu

def display_news(news):
    st.write(Discription["Date"])
    st.write(Discription["Country"])
    st.header(Discription["Headlines"])

    with st.container():
        left, right = st.columns(2)
        with left:
            st.image(Discription["Image"])
        with right:
            st.write(Discription["Discription"])
            authors = Discription.get("Author", "Unknown")
            st.write(f" By - {Author}")

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
        res = db.fetch(query={"Discription?contains": select})
        data = res.items

        if not data:
            st.write("No news found matching the search term 😕.")
        else:
            # Display the news that match the search term
            for news in data:
                display_news(discription)
    else:
        st.write("Please enter a search term.")
st.markdown("---")

# Sidebar menu options
with st.sidebar:
    st.header("Select category")
    selected_option = option_menu(
        menu_title=None,
        options=["Latest", "Business 📊", "Sports", "South", "Science", "Crime", "Global", "Political", "Food", "Music", "Entertainment", "Technology","Life style"],
        default_index=0,
        menu_icon="cast",
        orientation="vertical",
    )

# Fetch and display news based on the selected category
if selected_option:
    if selected_option == "Latest":
        res = db.fetch(query={"Category?contains": "latest"})
    elif selected_option == "Business 📊":
        res = db.fetch(query={"Category?contains": "business"})
    elif selected_option == "Sports":
        res = db.fetch(query={"Category?contains": "Sports"})
    elif selected_option == "South":
        res = db.fetch(query={"Category?contains": "south"})
    elif selected_option == "Science":
        res = db.fetch(query={"Category?contains": "science"})
    elif selected_option == "Crime":
        res = db.fetch(query={"Category?contains": "crime"})
    elif selected_option == "Global":
        res = db.fetch(query={"Category?contains": "global"})
    elif selected_option == "Political":
        res = db.fetch(query={"Category?contains": "political"})
    elif selected_option == "Food":
        res = db.fetch(query={"Category?contains": "food"})
    elif selected_option == "Music":
        res = db.fetch(query={"Category?contains": "music"})
    elif selected_option == "Entertainment":
        res = db.fetch(query={"Category?contains": "entertainment"})
    elif selected_option == "Technology":
        res = db.fetch(query={"Category?contains": "technology"})
    elif selected_option == "Life style":
        res = db.fetch(query={"Category?contains": "life-style"})
    #function calling
    if res:
        data = res.items
        for news in data:
            display_news(news)
