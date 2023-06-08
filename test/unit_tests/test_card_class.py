import pytest
from card import Card


# Variables
test_topic_1 = "IN3050 - Machine Learning"
test_text_1 = "What is a genetic algorithm?"
test_user_1 = "Bernd"
test_score_1 = "00010010111"


def test_creation_of_a_card():
    test_card = Card(test_topic_1, test_text_1, test_user_1, test_score_1)

def test_card_repr():
    test_card = Card(test_topic_1, test_text_1, test_user_1, test_score_1)
    assert test_card.__repr__() == \
           "Topic:  IN3050 - Machine Learning\nText:   What is a genetic algorithm?\nUser:   Bernd\nScore:  00010010111"

def test_get_correct_attempts_of_card():
    test_card = Card(test_topic_1, test_text_1, test_user_1, test_score_1)
    assert test_card.get_correct_attempts() == 5

def test_get_total_attempts_of_card():
    test_card = Card(test_topic_1, test_text_1, test_user_1, test_score_1)
    assert test_card.get_total_attempts() == 11

def test_get_score_string_of_card():
    test_card = Card(test_topic_1, test_text_1, test_user_1, test_score_1)
    assert test_card.get_score_string() == "5 / 11"

def test_adding_successful_attempt_to_card():
    test_card = Card(test_topic_1, test_text_1, test_user_1, test_score_1)
    test_card.add_attempt(correct=True)
    assert test_card.score == "000100101111"
    assert test_card.get_correct_attempts() == 6
    assert test_card.get_total_attempts() == 12
    assert test_card.get_score_string() == "6 / 12"

def test_adding_failed_attempt_to_card():
    test_card = Card(test_topic_1, test_text_1, test_user_1, test_score_1)
    test_card.add_attempt(correct=False)
    assert test_card.score == "000100101110"
    assert test_card.get_correct_attempts() == 5
    assert test_card.get_total_attempts() == 12
    assert test_card.get_score_string() == "5 / 12"

def test_calculate_probability_weight_of_card_no_attempts():
    # With exactly 5 attempts
    test_card = Card(test_topic_1, test_text_1, test_user_1, "")
    assert test_card.get_probability_weight() == 100

def test_calculate_probability_weight_of_card_one_failure():
    # With exactly 5 attempts
    test_card = Card(test_topic_1, test_text_1, test_user_1, "010")
    assert test_card.get_probability_weight() == 18

def test_calculate_probability_weight_of_card_ten_falures():
    # With exactly 5 attempts
    test_card = Card(test_topic_1, test_text_1, test_user_1, "0000000000")
    assert test_card.get_probability_weight() == 55

def test_calculate_probability_weight_of_card_more_than_ten_falures():
    # With exactly 5 attempts
    test_card = Card(test_topic_1, test_text_1, test_user_1, "0000000000")
    assert test_card.get_probability_weight() == 55

def test_calculate_probability_weight_of_card_random_score():
    # With exactly 5 attempts
    test_card = Card(test_topic_1, test_text_1, test_user_1, "00101111111010001101")
    assert test_card.get_probability_weight() == 26
