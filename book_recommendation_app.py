import streamlit as st

# Sample book recommendations
books = {
    "Fiction": ["To Kill a Mockingbird by Harper Lee", "1984 by George Orwell", "The Great Gatsby by F. Scott Fitzgerald"],
    "Non-Fiction": ["Sapiens by Yuval Noah Harari", "Educated by Tara Westover", "Becoming by Michelle Obama"],
    "Science Fiction": ["Dune by Frank Herbert", "Neuromancer by William Gibson", "Snow Crash by Neal Stephenson"],
    "Fantasy": ["Harry Potter by J.K. Rowling", "The Hobbit by J.R.R. Tolkien", "The Name of the Wind by Patrick Rothfuss"],
    "Mystery": ["Gone Girl by Gillian Flynn", "The Girl with the Dragon Tattoo by Stieg Larsson", "Big Little Lies by Liane Moriarty"]
}

# Streamlit app
st.title("Book Recommendation App")
st.write("Select a genre to get book recommendations:")

genre = st.selectbox("Choose a genre", list(books.keys()))

if genre:
    st.write(f"### Recommended Books in {genre}")
    for book in books[genre]:
        st.write(f"- {book}")
