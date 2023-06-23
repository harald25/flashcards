import pandas as pd
import random
import shutil

from card import Card
import os
from datetime import datetime

# TODO: Do i need a function to save data to file?


class Flashcards:
    def __init__(self, controller, filename: str="data.csv"):
        # Controller
        self.controller = controller

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

        # Draw the first card
        self.draw_card()

    def import_data_from_file(self):
        """Imports all data from csv-file."""

        df = pd.read_csv(self.filename, sep=";", keep_default_na=False)

        for user in df.head():
            if user not in ["Topic", "Text"]:
                for i in range(len(df[user])):
                    topic = str(df["Topic"][i])
                    text = str(df["Text"][i])
                    if len(text) > 200:
                        text = text[:200]
                    score = str(df[user][i])
                    print(score)
                    card = Card(topic, text, user, score)
                    self.all_cards.append(card)

        for card in self.all_cards:
            if card.user not in self.all_users:
                self.all_users.append(card.user)
            if card.topic not in self.all_topics:
                self.all_topics.append(card.topic)

    def update_from_file(self, update_active=False):
        self.all_cards = []
        self.all_users = []
        self.all_topics = []

        self.import_data_from_file()

        if update_active is True:
            self.active_users = self.all_users
            self.active_topics = self.all_topics



    def remove_active_user(self, participant: str):
        """Removes a user from list of participating users."""
        if participant in self.active_users:
            self.active_users.remove(participant)

    def add_active_user(self, participant: str):
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
        # TODO: Remove current card from pool (in case of only one user)

        # Calculate probabilities for each card
        probability_weights = []
        for card in pool_of_possible_cards:
            probability_weights.append(card.get_probability_weight())

        # Adjusts weights by degree of randomness
        for i in range(len(probability_weights)):
            probability_weights[i] = probability_weights[i] ** ((100 - self.degree_of_randomness) / 100)

        random.seed(seed)
        choices = random.choices(pool_of_possible_cards, probability_weights, k=1)
        choices = list(choices)
        self.current_card = choices[0]

        # TODO: If degree of randomness == 0: draw worst card

    def check_if_valid_username(self, username):
        """Checks if a username is valid. Max length: 25 chars.
        No special characters. Not already existing."""

        # Checks length of username
        if len(username) > 25:
            self.controller.raise_error("E-0102")
            return False

        # Check if username has no special chars
        if not username.isalnum():
            self.controller.raise_error("E-0103")
            return False

        # Check if username not in use.
        if username in self.all_users:
            self.controller.raise_error("E-0104")
            return False
        return True

    def add_user(self, username: str):
        """Adds a user to the system from a string defining the username."""

        # Checks if username is valid
        if self.check_if_valid_username(username) is False:
            # TODO: Remove print
            print("Username not valid")
            return

        # Adds column to datafile
        df = pd.read_csv(self.filename, sep=";", keep_default_na=False)
        length = len(df.index)
        column = ["" for _ in range(length)]
        df[username] = column
        df.to_csv(self.filename, index=False, sep=";")

        # Adds user to active users
        self.active_users.append(username)

        # Updates system
        self.update_from_file()

        for card in self.all_cards:
            print(card.score)
        return True

    def remove_user(self, username: str):
        """Removes a user from the system."""
        if username not in self.all_users:
            self.controller.raise_error("E-0105")
            return

        # Removes user from active users
        if username in self.active_users:
            self.active_users.remove(username)

        # Removes column from datafile
        df = pd.read_csv(self.filename, sep=";", keep_default_na=False)
        df.drop(username, axis=1, inplace=True)
        df.to_csv(self.filename, index=False, sep=";")

        # Updates system
        self.update_from_file()

        # If no active users, make first user active
        if len(self.active_users) == 0:
            self.active_users.append(self.all_users[0])
        return

    def add_attempt_to_card(self, card: Card, correct: bool):
        """Add an attempt to a specific card. Either 1 for correct, or 0 for incorrect answer."""

        # Info from card
        user = card.user
        text = card.text
        new_score = card.score
        if correct:
            new_score += "1"
        else:
            new_score += "0"

        # Updates score in datafile
        df = pd.read_csv(self.filename, sep=";", keep_default_na=False)
        index = df.index[df['Text'] == text].tolist()[0]
        df.at[index, user] = new_score
        df.to_csv(self.filename, index=False, sep=";")

        # Updates system
        self.update_from_file()


    def edit_username(self, old_username, new_username):
        """Changes the name of a user"""

        # Check if old username exists
        if old_username not in self.all_users:
            self.controller.raise_error("E-0105")
            return

        # Checks if new username is valid
        if not self.check_if_valid_username(new_username):
            return

        # Update username
        df = pd.read_csv(self.filename, sep=";", keep_default_na=False)
        df = df.rename({old_username: new_username}, axis=1)
        df.to_csv(self.filename, index=False, sep=";")

        # Updates system
        self.update_from_file()
        if old_username in self.active_users:
            self.active_users.remove(old_username)
        self.active_users.append(new_username)

        return

    def get_list_of_card_texts(self, topic=None):
        """Reutns a list of strings of all the current cards in the deck."""
        df = pd.read_csv(self.filename, sep=";", keep_default_na=False)
        if topic is None:
            return list(df["Text"])
        else:
            card_texts = []
            for card in self.all_cards:
                if card.topic == topic:
                    if card.text not in card_texts:
                        card_texts.append(card.text)
            print(card_texts)
            return card_texts

    def get_dict_of_topics_and_card_texts(self):
        topic_card_dict = {}
        for card in self.all_cards:
            if card.topic not in topic_card_dict:
                topic_card_dict[card.topic] = [card.text]
            else:
                if card.text not in topic_card_dict[card.topic]:
                    topic_card_dict[card.topic].append(card.text)

        # Sort keys alphabetically
        topic_card_dict = dict(sorted(topic_card_dict.items()))

        # Sort values alphabetically
        for key in topic_card_dict:
            topic_card_dict[key] = sorted(topic_card_dict[key])
        return topic_card_dict

    def edit_card(self, old_card_text, new_card_text):
        """Edits the text of a card."""

        # Check if card exists
        if not old_card_text in self.get_list_of_card_texts():
            return False

        # Updates data file
        df = pd.read_csv(self.filename, sep=";", keep_default_na=False)
        df["Text"] = df["Text"].replace(old_card_text, new_card_text)
        df.to_csv(self.filename, index=False, sep=";")

        # Updates system
        self.update_from_file()

        return True

    def add_card(self, new_card_topic, new_card_text):
        """Adds a card to the data file, and updates system."""

        # Check if card exists
        if new_card_text in self.get_list_of_card_texts():
            return False        # TODO: Throw error

        # TODO: Add length limit

        # Updates data file
        df = pd.read_csv(self.filename, sep=";", keep_default_na=False)

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
        df = pd.read_csv(self.filename, sep=";", keep_default_na=False)

        # Remove row
        i = df[df["Text"] == card_text_to_be_removed].index
        df = df.drop(i)

        # Save data to file
        df.to_csv(self.filename, index=False, sep=";")

        # Updates system
        self.update_from_file()

        return True

    def save_backup(self, dir="backups"):
        """Saves the current data-file to the given directory. Filename will be <timestamp>.csv."""
        time_now = int(datetime.now().timestamp())
        filename = f"{time_now}.csv"
        shutil.copyfile("data.csv", f"{dir}/{filename}")

        # Delete the oldest backup if more than 10
        list_of_files = os.listdir("backups")
        # TODO: >= or just > (same in controller)
        while len(list_of_files) > 10:
            for i in range(len(list_of_files)):
                list_of_files[i] = int(list_of_files[i].split(".")[0])
            list_of_files = sorted(list_of_files)
            file_to_be_deleted = f"{list_of_files[0]}.csv"
            os.remove(f"{dir}/{file_to_be_deleted}")
            list_of_files = os.listdir("backups")

    def get_list_of_backups(self, dir="backups"):
        """Returns list of all filenames in given directory."""
        list_of_files = os.listdir(dir)
        # TODO: SHould this be sorted? Is it sorted anywhere else? Should be newest on top.
        return list_of_files

    def restore_from_backup(self, backup):
        """Copies given backup file and overwrites the current data.csv file."""

        # Copy backup file over current data file
        shutil.copyfile(f"backups/{backup}", f"data.csv")

        # Update system from current file. Also update active users and topics.
        self.update_from_file(update_active=True)

    def convert_backup_filename_to_datetime(self, backup: str):
        """Converts name of backup file from timestamp to formated time string."""
        timestamp = float(backup.split(".")[0])
        timestring = datetime.fromtimestamp(timestamp).strftime("%d. %B %Y, %H:%M")
        return timestring

    def delete_backup(self, backup: str):
        os.remove(f"backups/{backup}")



