



class Card:
    """Class representing each card in a deck."""
    def __init__(self, topic: str, text: str, user: str, score: str):
        self.topic = topic
        self.text = text
        self.user = user
        self.score = score

    def __repr__(self):
        return f"Topic:  {self.topic}\nText:   {self.text}\nUser:   {self.user}\nScore:  {self.score}"

    def get_correct_attempts(self):
        pass

    def get_total_attempts(self):
        pass

    def get_score_string(self) -> str:
        """Returns a string of the total"""
        correct = 0
        total_attempts = len(self.score)
        for bit in self.score:
            if bit == "1":
                correct += 1
        return f"{correct} / {total_attempts}"

    def calculate_probability_weight(self):
        """Takes into consideration the last 5 attempts on each card. The most recent attempt counts twice as much
        as the second most recent attempt, and so on."""
        return

    def add_attempt(self, correct: bool):
        """Adds an attempt to the bit-string representing the score."""
        if correct:
            self.score += "1"
        else:
            self.score += "0"