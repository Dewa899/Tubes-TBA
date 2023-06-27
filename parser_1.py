class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.error = False

    def parse(self):
        self.advance()
        self.expression()

        if not self.error and self.current_token is None:
            print("Formula valid.")
        else:
            print("Formula tidak valid.")

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def expression(self):
        self.term()
        while self.current_token in [3, 4]:
            self.advance()
            self.term()

    def term(self):
        self.factor()
        while self.current_token in [5, 6, 7, 8]:
            self.advance()
            self.factor()

    def factor(self):
        if self.current_token in [1, 2]:
            self.advance()
        elif self.current_token == 9:
            self.advance()
            self.expression()
            if self.current_token == 10:
                self.advance()
            else:
                self.error = True
        else:
            self.error = True


# Contoh penggunaan
# input_tokens = [1, 3, 1, 4, 2, 5, 1]
# parser = Parser(input_tokens)
# parser.parse()

# input_tokens = [2, 6, 2, 7, 1, 8]
# parser = Parser(input_tokens)
# parser.parse()

# input_tokens = [9, 1, "error"]
# parser = Parser(input_tokens)
# parser.parse()
