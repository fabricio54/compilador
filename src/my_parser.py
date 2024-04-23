from lexer import Lexer
from lexer import TokenType

class Parser:
    def __init__(self, text):
        self.lexer = Lexer(text)
        self.current_token = None

    def tokenize(self):
        tokens = []
        while True:
            token = self.lexer.get_next_token()
            tokens.append((token[0].name, token[1]))
            if token[0] == TokenType.EOF:
                break
        return tokens

    def is_prefix(self, expression):
        def is_valid_prefix(tokens):
            if not tokens:
                return False
            token = tokens.pop(0)
            if token in operators:
                left_valid = is_valid_prefix(tokens)
                right_valid = is_valid_prefix(tokens)
                return left_valid and right_valid
            elif token.isdigit():
                return True
            else:
                return False

        operators = set(['+', '-', '*', '/'])
        tokens = expression.split()

        # A expressão prefixa deve ter mais de um token
        if len(tokens) < 3:
            return False

        # A expressão prefixa deve começar com um operador
        if tokens[0] not in operators:
            return False

        return is_valid_prefix(tokens)

    def is_infix(self, expression):
        def is_valid_infix(tokens):
            operand_expected = True
            for token in tokens:
                if token in operators:
                    if operand_expected:
                        return False
                    operand_expected = True
                elif token.isdigit():
                    if not operand_expected:
                        return False
                    operand_expected = False
                else:
                    return False
            return not operand_expected

        operators = set(['+', '-', '*', '/'])
        tokens = expression.split()

        # A expressão infixa deve ter mais de dois tokens
        if len(tokens) < 3:
            return False

        return is_valid_infix(tokens)
