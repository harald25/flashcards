import pytest
from flashcards import Flashcards


# Variables
filename = "test_data.csv"
expected_users = ["Anna", "Bill", "Carl", "Dave"]
expected_topics = ["IN3050 - Machine Learning", "IN3240 - Software testing"]


def test_import_of_data():
    fc = Flashcards(filename=filename)

def test_import_of_data_includes_expected_users():
    fc = Flashcards(filename=filename)
    for user in expected_users:
        assert user in fc.all_users

def test_import_of_data_includes_expected_topics():
    fc = Flashcards(filename=filename)
    for topic in expected_topics:
        assert topic in fc.all_topics

def test_update_from_file():
    fc = Flashcards(filename=filename)
    fc.update_from_file()
    for user in expected_users:
        assert user in fc.all_users
    for topic in expected_topics:
        assert topic in fc.all_topics

def test_remove_participant():
    fc = Flashcards(filename=filename)
    fc.remove_participant("Anna")
    expected_participants_after_removal = ["Bill", "Carl", "Dave"]
    assert fc.participating_users == expected_participants_after_removal

def test_add_participant():
    fc = Flashcards(filename=filename)
    fc.remove_participant("Anna")
    fc.add_participant("Anna")
    expected_participants_after_removal = ["Bill", "Carl", "Dave", "Anna"]
    assert fc.participating_users == expected_participants_after_removal




# TODO: Add user, then update from file
# TODO: Add cards, then update from file

