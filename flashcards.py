import pandas as pd
import random
from card import Card
import os
from datetime import datetime, timezone

# TODO: Save card should be here
# TODO: Do i need backups?


class Flashcards:
    def __init__(self, filename: str="data.csv"):
        # Variables to keep track fo the deck
        self.all_cards = []
        self.all_users = []
        self.all_topics = []
        self.degree_of_randomness = 100
        self.filename = filename

        # Importing all data from csv-file
        self.import_data_from_file()

        # Variables for gameplay
        self.active_users = self.all_users
        self.active_topics = self.all_topics
        self.current_card = None

        # Draw the first card TODO: activate
        # self.draw_card()

    def import_data_from_file(self):
        """Imports all data from csv-file."""

        df = pd.read_csv(self.filename, sep=";")

        for user in df.head():
            if user not in ["Topic", "Text"]:
                for i in range(len(df[user])):
                    topic = df["Topic"][i]
                    text = df["Text"][i]
                    if len(text) > 200:
                        text = text[:200]
                    score = df[user][i]
                    card = Card(topic, text, user, score)
                    self.all_cards.append(card)

        for card in self.all_cards:
            if card.user not in self.all_users:
                self.all_users.append(card.user)
            if card.topic not in self.all_topics:
                self.all_topics.append(card.topic)

    def update_from_file(self):
        # TODO: Also update participating?
        self.all_cards = []
        self.all_users = []
        self.all_topics = []

        self.import_data_from_file()

    def remove_active_users(self, participant: str):
        """Removes a user from list of participating users."""
        if participant in self.active_users:
            self.active_users.remove(participant)

    def add_active_users(self, participant: str):
        """Adds a user to the list of participating users."""
        if participant not in self.active_users:
            self.active_users.append(participant)

    def remove_active_topic(self, topic: str):
        """Removes a topic from the list of available topics."""
        if topic in self.active_topics:
            self.active_topics.remove(topic)

    def add_active_topic(self, topic: str):
        """Adds a user to the list of participating users."""
        if topic not in self.active_topics:
            self.active_topics.append(topic)

    def draw_card(self, seed=None):
        # Picks the first user in the active_users list, and moves him to the back of the list.
        user = self.active_users.pop(0)
        self.active_users.append(user)

        # Adds possible cards to pool of possible cards
        pool_of_possible_cards = []
        for card in self.all_cards:
            if card.topic in self.active_topics and card.user == user:
                pool_of_possible_cards.append(card)

        # Calculate probabilities for each card
        probability_weights = []
        for card in pool_of_possible_cards:
            probability_weights.append(card.get_probability_weight())
        for i in range(len(probability_weights)):
            weight = probability_weights[i]
            weight = weight ** ((100 - self.degree_of_randomness) / 100)
            probability_weights[i] = weight

        random.seed(seed)
        choices = random.choices(pool_of_possible_cards, probability_weights, k=1)
        self.current_card = choices[0]

    def check_if_valid_username(self, username):
        """Checks if a username is valid. Max length: 25 chars.
        No special characters. Not already existing."""

        # Checks length of username
        if len(username) > 25:
            return False

        # Check if username has no special chars
        if not username.isalnum():
            return False

        # Check if username not in use.
        if username in self.all_users:
            return False
        return True

    def add_user(self, username: str):
        """Adds a user to the system from a string defining the username."""

        # Checks if username is valid
        if not self.check_if_valid_username(username):
            return False

        # Adds column to datafile
        df = pd.read_csv(self.filename, sep=";")
        length = len(df.index)
        column = ["" for _ in range(length)]
        df[username] = column
        df.to_csv(self.filename, index=False, sep=";")

        # Updates system
        self.update_from_file()
        return True

    def remove_user(self, username: str):
        """Removes a user from the system."""
        if username not in self.all_users:
            return False

        # Removes column from datafile
        df = pd.read_csv(self.filename, sep=";")
        df.drop(username, axis=1, inplace=True)
        df.to_csv(self.filename, index=False, sep=";")

        # Updates system
        self.update_from_file()
        return True

    def edit_username(self, old_username, new_username):
        """Changes the name of a user"""

        # Check if old username exists
        if old_username not in self.all_users:
            return False

        # Checks if new username is valid
        if not self.check_if_valid_username(new_username):
            return False

        # Update username
        df = pd.read_csv(self.filename, sep=";")
        df = df.rename({old_username: new_username}, axis=1)
        df.to_csv(self.filename, index=False, sep=";")

        # Updates system
        self.update_from_file()

        return True



    def get_list_of_card_texts(self):
        """Reutns a list of strings of all the current cards in the deck."""
        df = pd.read_csv(self.filename, sep=";")
        return list(df["Text"])


    def edit_card(self, old_card_text, new_card_text):
        """Edits the text of a card."""

        # Check if card exists
        if not old_card_text in self.get_list_of_card_texts():
            return False

        # Updates data file
        df = pd.read_csv(self.filename, sep=";")
        df["Text"] = df["Text"].replace(old_card_text, new_card_text)
        df.to_csv(self.filename, index=False, sep=";")

        # Updates system
        self.update_from_file()

        return True

    def add_card(self, new_card_topic, new_card_text):
        """Adds a card to the data file, and updates system."""

        # Check if card exists
        if new_card_text in self.get_list_of_card_texts():
            return False

        # Updates data file
        df = pd.read_csv(self.filename, sep=";")

        # Add new row
        length = len(df.columns)
        new_row = ["" for _ in range(length)]
        new_row[0] = new_card_topic
        new_row[1] = new_card_text
        df.loc[len(df.index)] = new_row

        # Save data to file
        df.to_csv(self.filename, index=False, sep=";")

        # Updates system
        self.update_from_file()

        return True

    def remove_card(self, card_text_to_be_removed):
        """Adds a card to the data file, and updates system."""

        # Check if card exists
        if not card_text_to_be_removed in self.get_list_of_card_texts():
            return False

        # Import data file
        df = pd.read_csv(self.filename, sep=";")

        # Remove row
        df = df[df["Text"].str.contains(card_text_to_be_removed) is False]

        # Save data to file
        df.to_csv(self.filename, index=False, sep=";")

        # Updates system
        self.update_from_file()

        return True