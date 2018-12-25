import sys
import time
import csv
import numpy as np
import texttable as tt

from functools import wraps
from scipy.sparse.lil import lil_matrix
from sklearn.feature_extraction.text import TfidfTransformer


def profile_execution_time(func):
    '''
    This decorator helps identify slow code sections by
    profile the execution time of the decorated function.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        sys.stdout.write('"%s" (%s secs)\n' % (func.__name__, elapsed_time))
        return result
    return wrapper


class DocumentList(object):
    '''
    This is a convenience class for modelling
    collections of documents extracted for a csv
    file.
    '''
    @profile_execution_time
    def __init__(self, csv_file_path):
        with open(csv_file_path) as csv_file:
            lines = csv.reader(csv_file, delimiter=',')
            tmp = list(lines)
        self.schema = tmp[0]
        self.documents = tmp[1:]

    def dict(self, doc):
        return {field: doc[i] for i, field in enumerate(self.schema)}

    def __iter__(self):
        for doc in self.documents:
            yield self.dict(doc)

    def __getitem__(self, index):
        return self.dict(self.documents[index])

    def __len__(self):
        return len(self.documents)


@profile_execution_time
def sparse_vsm(books, tags, book_tags):
    '''
    Constructs a sparce vector-space-model based on books,
    tags, and book_tags document lists.
    '''
    book_id_to_index = {book['book_id']: ith for ith, book in enumerate(books)}
    shape = (len(books), len(tags))
    X = lil_matrix(shape, dtype=np.int64)
    for book_tag in book_tags:
        book_id = book_tag['goodreads_book_id']
        book_index = book_id_to_index[book_id]
        tag_index = int(book_tag['tag_id'])
        count = int(book_tag['count'])
        X[book_index, tag_index] = count
    return X


@profile_execution_time
def tfidf_normalize(X):
    '''
    Applies tf-idf normalization the vector space model X.
    '''
    tfidf_xformer = TfidfTransformer()
    tfidf_xformer.fit(X)
    Y = tfidf_xformer.transform(X, copy=True)
    return Y


@profile_execution_time
def closest_documents(Y, x, num_docs=10):
    '''
    Finds the nearst documents to x using the cosine distance based
    on the tf-idf model Y.
    '''
    base = x.T
    distances = [(1 - y.dot(base)[0, 0], i) for i, y in enumerate(Y)]
    distances.sort()
    matches = distances[:num_docs + 1]
    return matches


@profile_execution_time
def search_field_text(documents, field, field_text):
    '''
    Returns the first document whose field contains field_text,
    otherwise None is returned.
    '''
    result = None
    for d in documents:
        if field_text in d[field]:
            result = d
    return result


if __name__ == '__main__':
    sys.stdout.write('Question 3:\n\n')

    # load all documents from csv input
    books = DocumentList('./data/books.csv')
    tags = DocumentList('./data/tags.csv')
    books_tags = DocumentList('./data/book_tags.csv')

    # embed documents into vector space model
    X = sparse_vsm(books, tags, books_tags)
    Y = tfidf_normalize(X)

    # compute closest 10 matches to given book
    base_doc = search_field_text(books, 'title', 'The Golden Compass')
    x = Y[int(base_doc['id']) - 1]
    matches = closest_documents(Y, x)

    # report closest matches
    table = tt.Texttable()
    headings = ['Number', 'Distance', 'Title', 'Authors', 'Isbn', 'Publication Year']
    table.header(headings)
    table.set_cols_width([10, 10, 35, 35, 10, 15])
    for ith, (distance, book_id) in enumerate(matches):
        book = books[book_id]
        table.add_row((ith, distance, book['title'], book['authors'],
                       book['isbn'], book['original_publication_year']))
    s = table.draw()
    sys.stdout.write(s + '\n')

    sys.stdout.write('\n\nDone.\n')


# end of file
