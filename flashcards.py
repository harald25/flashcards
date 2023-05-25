import pandas as pd
import random
from card import Card
import os
from datetime import datetime, timezone


"""
TODO: Save card should be here
"""

class Flashcards:
    def __init__(self, filename: str="data.csv"):
        # Variables to keep track fo the deck
        self.all_cards = []
        self.all_users = []
        self.all_topics = []
        self.degree_of_randomness = 50
        self.filename = filename

        # Importing all data from csv-file
        self.import_data_from_file()

        # Variables for gameplay
        self.participating_users = self.all_users
        self.available_topics = self.all_topics
        self.current_card = None

        # Draw the first card
        self.draw_card()

    def import_data_from_file(self):
        """Imports all data from csv-file."""

        df = pd.read_csv(self.filename, sep=";")

        for user in df.head():
            if user not in ["Deck", "Card"]:
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


    def add_participant(self, participant: str):
        """Adds a user to the list of participating users."""
        if participant not in self.participating_users:
            self.participating_users.append(participant)

    def remove_participant(self, participant: str):
        """Removes a user from list of participating users."""
        if participant in self.participating_users:
            self.participating_users.remove(participant)

    def add_available_topic(self, topic: str):
        """Adds a user to the list of participating users."""
        if topic not in self.available_topics:
            self.available_topics.append(topic)

    def remove_available_topic(self, topic: str):
        """Removes a topic from the list of available topics."""
        if topic in self.available_topics:
            self.available_topics.remove(topic)

    def draw_card(self, topics=None, user=None):
        pass

    def backup_data(self):
        df = pd.read_csv('data.csv', sep=";")
        df.to_csv("data_backup.csv", index=False, sep=";")

    def get_time_last_backup(self, filename="data_backup.csv"):
        statbuf = os.stat(filename)
        print("Modification time: {}".format(statbuf.st_mtime))

        modified = datetime.fromtimestamp(statbuf.st_mtime, tz=timezone.utc).strftime("%d. %B %Y, %H:%M")
        return modified

    def restore_from_backup(self, filename="data_backup.csv"):
        df = pd.read_csv(filename, sep=";")
        df.to_csv("data.csv", index=False, sep=";")

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
        df = pd.read_csv('data.csv', sep=";")
        length = len(df.index)
        column = ["0/0" for _ in range(length)]
        df[username] = column
        df.to_csv("data.csv", index=False, sep=";")

        # Updates system
        self.update_from_file()
        return True

    def remove_user(self, username: str):
        """Removes a user from the system."""
        if username not in self.all_users:
            return False

        # Removes column from datafile
        df = pd.read_csv('data.csv', sep=";")
        df.drop(username, axis=1, inplace=True)
        df.to_csv("data.csv", index=False, sep=";")

        # Updates system
        self.update_from_file()
        return True

    def edit_user_name(self, old_username, new_username):
        """Changes the name of a user"""

        # Check if old username exists
        if old_username not in self.all_users:
            return False

        # Checks if new username is valid
        if not self.check_if_valid_username(new_username):
            return False

        # Update username
        df = pd.read_csv('data.csv', sep=";")
        df = df.rename({old_username: new_username}, axis=1)
        df.to_csv("data.csv", index=False, sep=";")

        # Updates system
        self.update_from_file()

        return True



    def get_list_of_card_texts(self):
        """Reutns a list of strings of all the current cards in the deck."""
        df = pd.read_csv('data.csv', sep=";")
        return list(df["Card"])


    def edit_card(self, old_card_text, new_card_text):
        """Edits the text of a card."""

        # Check if card exists
        if not old_card_text in self.get_list_of_card_texts():
            return False

        # Updates data file
        df = pd.read_csv('data.csv', sep=";")
        df["Card"] = df["Card"].replace(old_card_text, new_card_text)
        df.to_csv("data.csv", index=False, sep=";")

        # Updates system
        self.update_from_file()

        return True

    def add_card(self, new_card_topic, new_card_text):
        """Adds a card to the data file, and updates system."""

        # Check if card exists
        if new_card_text in self.get_list_of_card_texts():
            return False

        # Updates data file
        df = pd.read_csv('data.csv', sep=";")

        # Add new row
        length = len(df.columns)
        new_row = ["0/0" for _ in range(length)]
        new_row[0] = new_card_topic
        new_row[1] = new_card_text
        df.loc[len(df.index)] = new_row

        # Save data to file
        df.to_csv("data.csv", index=False, sep=";")

        # Updates system
        self.update_from_file()

        return True

    def remove_card(self, card_to_be_removed):
        """Adds a card to the data file, and updates system."""

        # Check if card exists
        if not card_to_be_removed in self.get_list_of_card_texts():
            return False

        # Import data file
        df = pd.read_csv('data.csv', sep=";")

        # Remove row
        df = df[df["Card"].str.contains(card_to_be_removed) == False]

        # Save data to file
        df.to_csv("data.csv", index=False, sep=";")

        # Updates system
        self.update_from_file()

        return True