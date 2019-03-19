# Reedsy Test


## Summary
This is the Reedsy test solution implementation.


## Installation (Ubuntu)

First make sure that `Python3`, `pip3` and `virtualenv` are all installed and working fine:

    sudo apt-get update
    sudo apt-get dist-upgrade
    sudo apt-get install -y python3-dev virtualenv gcc 

Clone the repository into a destination directory, cd into it then create your virtual env using

    virtualenv -p python3 env
    
and activate it by

    . env/bin/activate
    
Now you can install the requirements by

    pip3 install -r requirements.txt


## Questions

### Question 1

Describe a commercial project in which you set up and analysed tracking data. What actions came out of this work?

#### Answer

Company: et3arraf.com | [view](http://www.et3arraf.com/)

Project: Online Dating Recommender System

This project was aimed at finding reliable recommendations for online daters from both genders. A specialized algorithm based on reciprocal collaborative filtering was used in addition to summary statistics per feature to generate the recommendations. We designed and implemented the whole system including the RESTFUL API service, the actual logic, reporting and dashboard/UI.


### Question 2

List the Top 10 authors by their average rating.

Use any approach you feel comfortable with, but include any scripts with your answer and make sure your working is clear.

What thoughts do you have on the results?


#### Answer

The answer is implemented in script answer_2.py:

    python answer_2.py
    
will produce the following output:


    Answer 2
    --------
    "__init__" (0.10717296600341797 secs)
    "__init__" (1.1132380962371826 secs)
    "get_authors_books" (0.11050987243652344 secs)
    "aggregate_ratings" (9.59074091911316 secs)
    "best_average_ratings" (0.018919944763183594 secs)
    
    +------------+----------------------+----------------------+----------------------+----------------------+
    |   Number   |        Author        |    Average Rating    |  Number of Entries   |   Number of Books    |
    +============+======================+======================+======================+======================+
    | 1          | Lane T. Dennis       | 4.820                | 89                   | 1                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 2          | Hafez                | 4.774                | 93                   | 1                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 3          | Bill Watterson       | 4.712                | 1299                 | 13                   |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 4          | Kelly Jones          | 4.710                | 100                  | 1                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 5          | Daniel Vozzo         | 4.710                | 100                  | 1                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 6          | Lee Loughridge       | 4.710                | 100                  | 1                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 7          | Steve Oliff          | 4.710                | 100                  | 1                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 8          | James E. Talmage     | 4.670                | 100                  | 1                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 9          | BookRags             | 4.660                | 100                  | 1                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 10         | Marc Hempel          | 4.650                | 100                  | 1                    |
    +------------+----------------------+----------------------+----------------------+----------------------+


    Done.


Our thoughts of the results: the results looks reasonable. One thing to note is that almost all the best authors wrote a single high quality book. This suggests that authors with only a single book can be considered as outliers. Running the answer script again but this time filtering outliers:

    python answer_2.py filter-outliers
    
gives:


    Answer 2
    --------
    "__init__" (0.09192085266113281 secs)
    "__init__" (0.9750626087188721 secs)
    "get_authors_books" (0.10425114631652832 secs)
    "aggregate_ratings" (8.317081212997437 secs)
    "best_average_ratings" (0.016385793685913086 secs)
    
    +------------+----------------------+----------------------+----------------------+----------------------+
    |   Number   |        Author        |    Average Rating    |  Number of Entries   |   Number of Books    |
    +============+======================+======================+======================+======================+
    | 1          | Bill Watterson       | 4.712                | 1299                 | 13                   |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 2          | Andrew Williamson    | 4.648                | 182                  | 2                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 3          | Ronald A. Beers      | 4.621                | 190                  | 2                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 4          | Steve Parkhouse      | 4.620                | 200                  | 2                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 5          | Brandon Stanton      | 4.614                | 184                  | 2                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 6          | Michael Zulli        | 4.603                | 400                  | 4                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 7          | Colleen Doran        | 4.570                | 300                  | 3                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 8          | George Pratt         | 4.560                | 200                  | 2                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 9          | Stan Woch            | 4.550                | 200                  | 2                    |
    +------------+----------------------+----------------------+----------------------+----------------------+
    | 10         | Todd Klein           | 4.546                | 1000                 | 10                   |
    +------------+----------------------+----------------------+----------------------+----------------------+
    
    
    Done.


### Question 3

Recommend 10 books similar to "The Golden Compass" by Philip Pullman.

Again, you may use any tools; include scripts and clear workings in your answer.


#### Answer

The answer is implemented in script answer_3.py:

    python answer_3.py
    
will produce the following output:

    Answer 3
    --------
    "__init__" (0.1307697296142578 secs)
    "__init__" (0.05058002471923828 secs)
    "__init__" (1.5501189231872559 secs)
    "sparse_vsm" (7.517226934432983 secs)
    "tfidf_normalize" (0.7128639221191406 secs)
    "search_field_text" (0.04247021675109863 secs)
    "closest_documents" (4.4669811725616455 secs)
    
    +------------+------------+-------------------------------------+-------------------------------------+------------+-----------------+
    |   Number   |  Distance  |                Title                |               Authors               |    Isbn    |   Publication   |
    |            |            |                                     |                                     |            |      Year       |
    +============+============+=====================================+=====================================+============+=================+
    | 0          | 0          | The Golden Compass (His Dark        | Philip Pullman                      | 6.799e+08  | 1995            |
    |            |            | Materials, #1)                      |                                     |            |                 |
    +------------+------------+-------------------------------------+-------------------------------------+------------+-----------------+
    | 1          | 0.001      | Graceling (Graceling Realm, #1)     | Kristin Cashore                     | 015206396X | 2008            |
    +------------+------------+-------------------------------------+-------------------------------------+------------+-----------------+
    | 2          | 0.001      | Magyk (Septimus Heap, #1)           | Angie Sage                          | 60577312   | 2005            |
    +------------+------------+-------------------------------------+-------------------------------------+------------+-----------------+
    | 3          | 0.001      | The Neverending Story               | Michael Ende, Ralph Manheim,        | 5.255e+08  | 1979            |
    |            |            |                                     | Roswitha Quadflieg                  |            |                 |
    +------------+------------+-------------------------------------+-------------------------------------+------------+-----------------+
    | 4          | 0.002      | Leven Thumps and the Gateway to Foo | Obert Skye                          | 1.417e+09  | 2005            |
    |            |            | (Leven Thumps, #1)                  |                                     |            |                 |
    +------------+------------+-------------------------------------+-------------------------------------+------------+-----------------+
    | 5          | 0.002      | The Thief (The Queen's Thief, #1)   | Megan Whalen Turner                 | 60824972   | 1996            |
    +------------+------------+-------------------------------------+-------------------------------------+------------+-----------------+
    | 6          | 0.002      | The Wizard Heir (The Heir           | Cinda Williams Chima                | 1.423e+09  | 2007            |
    |            |            | Chronicles, #2)                     |                                     |            |                 |
    +------------+------------+-------------------------------------+-------------------------------------+------------+-----------------+
    | 7          | 0.002      | The False Prince (The Ascendance    | Jennifer A. Nielsen                 | 5.453e+08  | 2012            |
    |            |            | Trilogy #1)                         |                                     |            |                 |
    +------------+------------+-------------------------------------+-------------------------------------+------------+-----------------+
    | 8          | 0.002      | The Warrior Heir (The Heir          | Cinda Williams Chima                | 7.868e+08  | 2006            |
    |            |            | Chronicles, #1)                     |                                     |            |                 |
    +------------+------------+-------------------------------------+-------------------------------------+------------+-----------------+
    | 9          | 0.002      | Stardust                            | Neil Gaiman                         | 61142026   | 1999            |
    +------------+------------+-------------------------------------+-------------------------------------+------------+-----------------+
    | 10         | 0.002      | The Dragon Heir (The Heir           | Cinda Williams Chima                | 1.423e+09  | 2008            |
    |            |            | Chronicles, #3)                     |                                     |            |                 |
    +------------+------------+-------------------------------------+-------------------------------------+------------+-----------------+
    
    
    Done.

To get the set of similar books, we embeded the data in a normalized vector space model then used cosine similarity to compute the results.

Of course in a real production setting, we could use efficient methods to compute nearst neighbors in a large high-dimenssional data sets
such as:

1. [Locality-sensitive hashing](https://en.wikipedia.org/wiki/Locality-sensitive_hashing)
2. [Scalable Nearest Neighbor Algorithms for High Dimensional Data](http://www.cs.ubc.ca/research/flann/uploads/FLANN/flann_pami2014.pdf) 

(end of README.md)




