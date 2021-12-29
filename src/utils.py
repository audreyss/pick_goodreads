def get_unique_shelves(bookshelves_df):
    unique_values = bookshelves_df['Bookshelves'].unique()
    list_shelves = [s.split(', ') if type(s) == str else s for s in unique_values if str(s) != 'nan']
    shelves = [shelf for sublist in list_shelves for shelf in sublist]

    excl_shelves = bookshelves_df['Exclusive Shelf'].unique()
    shelves.extend(excl_shelves)

    return sorted(set(shelves)), excl_shelves


def get_books_from_shelf(bookshelves_df, shelf, excl_shelves):
    if shelf in excl_shelves:
        return bookshelves_df[bookshelves_df['Exclusive Shelf'] == shelf]

    bookshelves_df = bookshelves_df[bookshelves_df['Bookshelves'].notnull()]
    return bookshelves_df[bookshelves_df['Bookshelves'].apply(lambda x: x.find(shelf)) != -1]
