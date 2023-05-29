import pytest
import time
import shutil

from flashcards import Flashcards
from card import Card


# Variables
filename = "test_data.csv"
filename_restore = "test_data_restore.csv"
expected_users = ["Anna", "Bill", "Carl", "Dave"]
expected_topics = ["IN3050 - Machine Learning", "IN3240 - Software testing"]

def restore_test_data():
    """Helper function to restore test data to original state to avoid errors propagating."""
    shutil.copyfile(filename_restore, filename)
    time.sleep(0.1)

def test_import_of_data():
    restore_test_data()
    fc = Flashcards(filename=filename)


def test_import_of_data_includes_expected_users():
    restore_test_data()
    fc = Flashcards(filename=filename)
    for user in expected_users:
        assert user in fc.all_users


def test_import_of_data_includes_expected_topics():
    restore_test_data()
    fc = Flashcards(filename=filename)
    for topic in expected_topics:
        assert topic in fc.all_topics


def test_update_from_file():
    restore_test_data()
    fc = Flashcards(filename=filename)
    fc.update_from_file()
    assert fc.all_users == expected_users
    assert fc.all_topics == expected_topics


def test_remove_active_users():
    restore_test_data()
    fc = Flashcards(filename=filename)
    fc.remove_active_users("Anna")
    expected_active_users_after_removal = ["Bill", "Carl", "Dave"]
    assert fc.active_users == expected_active_users_after_removal


def test_remove_active_user_already_removed():
    restore_test_data()
    fc = Flashcards(filename=filename)
    fc.remove_active_users("Anna")
    fc.remove_active_users("Anna")
    expected_active_users_after_removal = ["Bill", "Carl", "Dave"]
    assert fc.active_users == expected_active_users_after_removal


def test_add_active_users():
    restore_test_data()
    fc = Flashcards(filename=filename)
    fc.remove_active_users("Anna")
    fc.add_active_users("Anna")
    expected_active_users_after_add = ["Bill", "Carl", "Dave", "Anna"]
    assert fc.active_users == expected_active_users_after_add


def test_add_active_user_already_added():
    restore_test_data()
    fc = Flashcards(filename=filename)
    fc.add_active_users("Anna")
    expected_active_users_after_add = ["Anna", "Bill", "Carl", "Dave"]
    assert fc.active_users == expected_active_users_after_add


def test_remove_active_topic():
    restore_test_data()
    fc = Flashcards(filename=filename)
    fc.remove_active_topic("IN3240 - Software testing")
    expected = ["IN3050 - Machine Learning"]
    assert fc.active_topics == expected


def test_remove_active_topic_already_removed():
    restore_test_data()
    fc = Flashcards(filename=filename)
    fc.remove_active_topic("IN3240 - Software testing")
    fc.remove_active_topic("IN3240 - Software testing")
    expected = ["IN3050 - Machine Learning"]
    assert fc.active_topics == expected


def test_add_active_topic():
    restore_test_data()
    fc = Flashcards(filename=filename)
    fc.remove_active_topic("IN3240 - Software testing")
    fc.add_active_topic("IN3240 - Software testing")
    expected = ["IN3050 - Machine Learning", "IN3240 - Software testing"]
    assert fc.active_topics == expected


def test_add_active_topic_adready_added():
    restore_test_data()
    fc = Flashcards(filename=filename)
    fc.add_active_topic("IN3240 - Software testing")
    expected = ["IN3050 - Machine Learning", "IN3240 - Software testing"]
    assert fc.active_topics == expected


def test_draw_card():
    restore_test_data()
    fc = Flashcards(filename=filename)
    fc.draw_card(seed=1)
    expected = fc.all_cards[0]
    assert fc.current_card == expected


def test_check_if_valid_username_normal():
    restore_test_data()
    fc = Flashcards(filename=filename)
    username = "Eric"
    expected = True
    assert fc.check_if_valid_username(username) is expected


def test_check_if_valid_username_too_long():
    restore_test_data()
    fc = Flashcards(filename=filename)
    username = "Abcdefghijklmnopqrstuvwxyz"
    expected = False
    assert fc.check_if_valid_username(username) is expected


def test_check_if_valid_username_max_length():
    restore_test_data()
    fc = Flashcards(filename=filename)
    username = "Abcdefghijklmnopqrstuvwxy"
    expected = True
    assert fc.check_if_valid_username(username) is expected


def test_check_if_valid_username_not_alphanumerical_beacuse_of_space():
    restore_test_data()
    fc = Flashcards(filename=filename)
    username = "John is Cool"
    expected = False
    assert fc.check_if_valid_username(username) is expected


def test_check_if_valid_username_not_alphanumerical_beacuse_of_empty_string():
    restore_test_data()
    fc = Flashcards(filename=filename)
    username = ""
    expected = False
    assert fc.check_if_valid_username(username) is expected


def test_check_if_valid_username_already_in_use():
    restore_test_data()
    fc = Flashcards(filename=filename)
    username = "Anna"
    expected = False
    assert fc.check_if_valid_username(username) is expected


def test_add_user():
    restore_test_data()
    fc = Flashcards(filename=filename)
    username = "Eric"
    expected = ["Anna", "Bill", "Carl", "Dave", "Eric"]
    fc.add_user(username)
    assert fc.all_users == expected
    fc_2 = Flashcards(filename=filename)
    assert fc_2.all_users == expected


def test_add_user_already_added():
    restore_test_data()
    fc = Flashcards(filename=filename)
    username = "Bill"
    expected = ["Anna", "Bill", "Carl", "Dave"]
    fc.add_user(username)
    assert fc.all_users == expected
    fc_2 = Flashcards(filename=filename)
    assert fc_2.all_users == expected


def test_remove_user():
    restore_test_data()
    fc = Flashcards(filename=filename)
    username = "Eric"
    expected = ["Anna", "Bill", "Carl", "Dave"]
    fc.remove_user(username)
    assert fc.all_users == expected
    fc_2 = Flashcards(filename=filename)
    assert fc_2.all_users == expected


def test_remove_user_not_existing():
    restore_test_data()
    fc = Flashcards(filename=filename)
    username = "Eric"
    expected = ["Anna", "Bill", "Carl", "Dave"]
    fc.remove_user(username)
    assert fc.all_users == expected
    fc_2 = Flashcards(filename=filename)
    assert fc_2.all_users == expected


def test_edit_username():
    restore_test_data()
    fc = Flashcards(filename=filename)
    old_username = "Carl"
    new_username = "Cruz"
    expected = ["Anna", "Bill", "Cruz", "Dave"]
    fc.edit_username(old_username, new_username)
    assert fc.all_users == expected
    # Change back
    fc.edit_username(new_username, old_username)


def test_get_list_of_card_texts():
    restore_test_data()
    fc = Flashcards(filename=filename)
    expected = ["What is a genetic algorithm?", "How does the weights in a multi layer perceptron (MLP) get updated?",
                "What are the seven test principles?", "What is unit testing?"]
    assert fc.get_list_of_card_texts() == expected


def test_edit_card():
    restore_test_data()
    fc = Flashcards(filename=filename)
    old_card_text = "What is a genetic algorithm?"
    new_card_text = "What is bit-flip mutation?"
    fc.edit_card(old_card_text, new_card_text)
    expected = "What is bit-flip mutation?"
    assert fc.get_list_of_card_texts()[0] == expected
    # Change back
    fc.edit_card(new_card_text, old_card_text)


def test_add_card():
    restore_test_data()
    fc = Flashcards(filename=filename)
    new_card_topic = "IN3050 - Machine Learning"
    new_card_text = "What is inverse mutation?"
    assert fc.add_card(new_card_topic, new_card_text)
    assert fc.get_list_of_card_texts()[-1] == new_card_text


def test_remove_card():
    restore_test_data()
    fc = Flashcards(filename=filename)
    card_to_be_removed_text = 'What is unit testing?'
    assert fc.remove_card(card_to_be_removed_text)
    expected = "What are the seven test principles?"
    assert fc.get_list_of_card_texts()[-1] == expected


def test_remove_card_not_existing():
    restore_test_data()
    fc = Flashcards(filename=filename)
    card_to_be_removed_text = "Where is santa?"
    assert not fc.remove_card(card_to_be_removed_text)
    expected = 'What is unit testing?'
    assert fc.get_list_of_card_texts()[-1] == expected


