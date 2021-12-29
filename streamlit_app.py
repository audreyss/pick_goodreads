import pandas as pd
import streamlit as st

from src.utils import get_unique_shelves, get_books_from_shelf

st.set_page_config(
    page_title="Goodreads random picker",
    page_icon=":books:",
    menu_items={
        'About': "# Super cool random picker for goodreads!\nBy mamdrey aka audreyss"
    }
)

st.title('Random pick on Goodreads')
st.write('Get a random pick from one of your goodreads shelves.')

with st.expander("How to get the export file from Goodreads"):
    st.write("""
         Go on Goodreads website, click on 'My Books' and select 'Tools' > 'Import and export' in the left column.\n
         Then, you can click on 'Export Library'. Wait until the export is complete and click on the link
         'Your export ...' to download it.
     """)

uploaded_file = st.file_uploader('Upload the export file from Goodreads.', type='.csv',
                                 help='Select your export library file')
st.caption('sorry, goodreads doesn\'t allow new API developers so I need this file :(')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    shelves, excl_shelves = get_unique_shelves(df)
    shelf = st.selectbox('From which shelf do you want to pick a book ?', shelves)

    selected_books = get_books_from_shelf(df, shelf, excl_shelves)
    random_row = selected_books.sample().iloc[0]

    st.write("The winning book from the shelf %s is:" % shelf)
    st.write("%s by %s" % (random_row['Title'], random_row['Author']))
    st.balloons()
