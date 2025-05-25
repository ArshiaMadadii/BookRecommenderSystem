import pickle
import streamlit as st
import numpy as np

# --- Page Header ---
st.header("📚 Book Recommender System")

# --- Load Artifacts ---
model = pickle.load(open('D:/GIT/BookRecommenderSystem-/Artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('D:/GIT/BookRecommenderSystem-/Artifacts/books_name.pkl', 'rb'))
final_rating = pickle.load(open('D:/GIT/BookRecommenderSystem-/Artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('D:/GIT/BookRecommenderSystem-/Artifacts/book_pivot.pkl', 'rb'))


# --- Helper Functions ---
def fetch_posters(suggestions):
    poster_urls = []
    for book_id in suggestions[0]:
        book_title = book_pivot.index[book_id]
        idx = np.where(final_rating['Title'] == book_title)[0][0]
        image_url = final_rating.iloc[idx]['Image_URL']
        poster_urls.append(image_url)
    return poster_urls


def recommend_books(selected_book):
    book_index = np.where(book_pivot.index == selected_book)[0][0]
    _, suggestions = model.kneighbors(
        book_pivot.iloc[book_index, :].values.reshape(1, -1),
        n_neighbors=6
    )
    recommended_titles = [book_pivot.index[i] for i in suggestions[0]]
    poster_urls = fetch_posters(suggestions)
    return recommended_titles, poster_urls


# --- UI: Book Selection ---
selected_book = st.selectbox(
    "Looking for a good read? Start typing or choose a favorite!",
    books_name
)

# --- UI: Recommendation Result ---
if st.button("Suggest Me a Book"):
    recommended_books, poster_urls = recommend_books(selected_book)

    st.subheader("📖 Recommended Books for You")
    cols = st.columns(6)
    for i in range(6):
        with cols[i]:
            st.image(poster_urls[i])
            st.caption(recommended_books[i])


# --- Footer: GitHub Link with Icon ---
st.markdown("---", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center;'>
        <a href='https://github.com/ArshiaMadadii/BookRecommenderSystem-' target='_blank' style='text-decoration: none; font-size: 18px;'>
            <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' width='30' style='vertical-align: middle; margin-right: 8px;'/>
            View this project on GitHub
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

