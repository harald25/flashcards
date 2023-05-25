import pytest
from flashcards import Flashcards


# Variables
filename = "test_data.csv"
expected_users = ["Anna", "Bill", "Carl", "Dave"]
expected_topics = ["IN3050 - Machine Learning", "IN3240 - Software testing"]


def test_import_of_data():
    fc = Flashcards(filename=filename)

    for user in expected_users:
        assert user in fc.all_users

    for topic in expected_topics:
        assert topic in fc.all_topics

