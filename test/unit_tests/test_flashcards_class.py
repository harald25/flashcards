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
    assert fc.all_users == expected_users
    assert fc.all_topics == expected_topics


def test_remove_active_users():
    fc = Flashcards(filename=filename)
    fc.remove_active_users("Anna")
    expected_active_users_after_removal = ["Bill", "Carl", "Dave"]
    assert fc.active_users == expected_active_users_after_removal

def test_remove_active_user_already_removed():
    fc = Flashcards(filename=filename)
    fc.remove_active_users("Anna")
    fc.remove_active_users("Anna")
    expected_active_users_after_removal = ["Bill", "Carl", "Dave"]
    assert fc.active_users == expected_active_users_after_removal

def test_add_active_users():
    fc = Flashcards(filename=filename)
    fc.remove_active_users("Anna")
    fc.add_active_users("Anna")
    expected_active_users_after_add = ["Bill", "Carl", "Dave", "Anna"]
    assert fc.active_users == expected_active_users_after_add

def test_add_active_user_already_added():
    fc = Flashcards(filename=filename)
    fc.add_active_users("Anna")
    expected_active_users_after_add = ["Anna", "Bill", "Carl", "Dave"]
    assert fc.active_users == expected_active_users_after_add

def test_remove_active_topic():
    fc = Flashcards(filename=filename)
    fc.remove_active_topic("IN3240 - Software testing")
    expected = ["IN3050 - Machine Learning"]
    assert fc.active_topics == expected

def test_remove_active_topic_already_removed():
    fc = Flashcards(filename=filename)
    fc.remove_active_topic("IN3240 - Software testing")
    fc.remove_active_topic("IN3240 - Software testing")
    expected = ["IN3050 - Machine Learning"]
    assert fc.active_topics == expected

def test_add_active_topic():
    fc = Flashcards(filename=filename)
    fc.remove_active_topic("IN3240 - Software testing")
    fc.add_active_topic("IN3240 - Software testing")
    expected = ["IN3050 - Machine Learning", "IN3240 - Software testing"]
    assert fc.active_topics == expected

def test_add_active_topic_adready_added():
    fc = Flashcards(filename=filename)
    fc.add_active_topic("IN3240 - Software testing")
    expected = ["IN3050 - Machine Learning", "IN3240 - Software testing"]
    assert fc.active_topics == expected




# TODO: Add user, then update from file
# TODO: Add cards, then update from file

