class StringIncrementer:

    def __init__(self, text):
        self.text = text
        if self.is_int(self.text[-1]):
            self.text += str(int(self.text[-1]) + 1)
        else:
            self.text += "1"

    @staticmethod
    def is_int(last_char):
        try:
            int(last_char)
            return True
        except ValueError:
            return False

    def return_string(self):
        return self.text

