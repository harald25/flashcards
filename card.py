



class Card:
    """Class representing each card in a deck."""
    def __init__(self, topic: str, text: str, user: str, score: str):
        self.topic = topic
        self.text = text
        self.user = user
        self.score = score
        self.significant_attempts = 5

    def __repr__(self):
        return f"Topic:  {self.topic}\nText:   {self.text}\nUser:   {self.user}\nScore:  {self.score}"

    def get_correct_attempts(self):
        correct = 0
        for bit in self.score:
            if bit == "1":
                correct += 1
        return correct

    def get_total_attempts(self):
        return len(self.score)

    def get_score_string(self) -> str:
        """Returns a string of the total"""
        correct = 0
        total_attempts = len(self.score)
        for bit in self.score:
            if bit == "1":
                correct += 1
        return f"{correct} / {total_attempts}"

    def get_probability_weight(self):
        """Takes into consideration the last 5 attempts on each card. The most recent attempt counts for 10 weight
        points. The second most recent card counts for 4 weight points, and so on. It only counts points for failed
        attempts. This gives cards with more failed attempts a higher probability weight.
        TODO: This calculation is subject for revision."""

        probability_weight = 0
        n = self.significant_attempts

        for i in range(1, n+1):
            if len(self.score) >= i:
                bit = int(self.score[-i])
                if bit == 0:
                    probability_weight += 1 + n - i
            else:
                probability_weight += 1 + n - i

        if probability_weight == 0:
            probability_weight += 1

        return probability_weight


    def add_attempt(self, correct: bool):
        """Adds an attempt to the bit-string representing the score."""
        if correct:
            self.score += "1"
        else:
            self.score += "0"