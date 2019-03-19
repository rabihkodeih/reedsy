import sys
import time
import csv
import texttable as tt

from functools import wraps


def profile_execution_time(func):
    '''
    This decorator helps identify slow code sections by
    profiling the execution time of the decorated function.
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
    collections of documents extracted from a csv
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


def normalize_author(author):
    '''
    Normalizes author_name.
    '''
    return ' '.join(w.strip() for w in author.split())


def authors_from_book(book):
    '''
    Extracts a normalized list of authors from a given book.
    '''
    authors = book['authors'].split(',')
    return [normalize_author(a) for a in authors]


@profile_execution_time
def aggregate_ratings(ratings):
    '''
    Extracts ratings and insert them into authors_ratings dict.
    '''
    authors_ratings = {}
    for r in ratings:
        book_index = int(r['book_id']) - 1
        book = books[book_index]
        authors = authors_from_book(book)
        for a in authors:
            rating = int(r['rating'])
            assert rating >= 1 and rating <= 5
            if a not in authors_ratings:
                authors_ratings[a] = []
            authors_ratings[a].append(rating)
    return authors_ratings


@profile_execution_time
def get_authors_books(books):
    '''
    Get list of books per author.
    '''
    authors_books = {}
    for book in books:
        authors = authors_from_book(book)
        for a in authors:
            title = book['title']
            if a not in authors_books:
                authors_books[a] = []
            authors_books[a].append(title)
    return authors_books


@profile_execution_time
def best_average_ratings(authors_ratings, num_results, authors_books=None):
    '''
    Computes the best average ratings.
    '''
    all_ratings = []
    for author, ratings in authors_ratings.items():
        average_rating = sum(ratings) / len(ratings)
        ratings_count = len(ratings)
        if authors_books is None:
            all_ratings.append((average_rating, author, ratings_count))
        else:
            num_books = len(authors_books[author])
            if num_books > 1:
                all_ratings.append((average_rating, author, ratings_count))

    all_ratings.sort(key=lambda x: x[0], reverse=True)
    return all_ratings[:num_results]


if __name__ == '__main__':
    sys.stdout.write(
        ('\nQuestion 2\n'
         '----------\n'
         'List the Top 10 authors by their average rating.\n'
         'Use any approach you feel comfortable with, but include any '
         'scripts with your answer and make sure your working is clear.\n'
         'What thoughts do you have on the results?\n\n'
         'Answer 2\n'
         '--------\n')
    )

    # check command line option to filter outliers
    if len(sys.argv) > 1 and sys.argv[1] == 'filter-outliers':
        filter_outliers = True
    else:
        filter_outliers = False

    # load all documents from csv input
    books = DocumentList('./data/books.csv')
    ratings = DocumentList('./data/ratings.csv')

    # get authors_books
    authors_books = get_authors_books(books)

    # aggregate ratings
    authors_ratings = aggregate_ratings(ratings)

    # compute best average ratings
    if filter_outliers:
        best_ratings = best_average_ratings(authors_ratings, 10, authors_books)
    else:
        best_ratings = best_average_ratings(authors_ratings, 10)

    # report results
    table = tt.Texttable()
    headings = ['Number', 'Author', 'Average Rating', 'Number of Entries', 'Number of Books']
    table.header(headings)
    table.set_cols_width([10, 20, 20, 20, 20])
    for ith, (average_rating, author, num_entries) in enumerate(best_ratings):
        num_books = len(authors_books[author])
        table.add_row((ith + 1, author, average_rating, num_entries, num_books))
    s = table.draw()
    sys.stdout.write('\n' + s + '\n')

    sys.stdout.write('\n\nDone.\n')


# end of file
