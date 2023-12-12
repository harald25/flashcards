from chatgpt_dialog import ChatGPTPrompt


class Card:
    """Class representing each card in a deck."""

    def __init__(self, topic: str, text: str, user: str, score: str):
        self.topic = topic
        self.text = text
        self.user = user
        self.score = score
        self.hint = ""
        self.gpt_object = None

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
        """Takes into consideration the last 10 attempts on each card. The most recent attempt counts for 10 weight
        points. The second most recent card counts for 9 weight points, and so on. It only counts points for failed
        attempts. This gives cards with more failed attempts a higher probability weight.
        """

        if len(self.score) == 0:
            probability_weight = 100
            return probability_weight

        probability_weight = 0
        n = 10  # Significant attempts. Only looks at the last 10 attempts

        for i in range(n):
            if len(self.score) >= i + 1:
                bit = int(self.score[-(i + 1)])
                if bit == 0:
                    probability_weight += 10 - i

        if probability_weight == 0:
            probability_weight += 1

        return probability_weight

    def add_attempt(self, correct: bool):
        """Adds an attempt to the bit-string representing the score."""
        if correct:
            self.score += "1"
        else:
            self.score += "0"

    def generate_hint(self):
        if self.gpt_object is None:
            self.gpt_object = ChatGPTPrompt(subject="in5200", gpt_model="gpt-4")
        self.hint = self.gpt_object.make_request(question=self.text)
