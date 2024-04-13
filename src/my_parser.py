from lexer import Lexer, TokenType

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
    
    def eat(self, expected_type):
        if self.current_token[0] == expected_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise ValueError(f"Token inesperado: {self.current_token}")

    def factor(self):
        token = self.current_token
        if token[0] == TokenType.CONST_INT:
            self.eat(TokenType.CONST_INT)
            return token[1]
        elif token[0] == TokenType.CONST_FLOAT:
            self.eat(TokenType.CONST_FLOAT)
            return token[1]
        elif token[0] == TokenType.ABRE_PAR:
            self.eat(TokenType.ABRE_PAR)
            result = self.expression()
            self.eat(TokenType.FECHA_PAR)
            return result

    def term(self):
        result = self.factor()
        while self.current_token[0] in (TokenType.OP_MUL, TokenType.OP_DIV):
            if self.current_token[0] == TokenType.OP_MUL:
                self.eat(TokenType.OP_MUL)
                result *= self.factor()
            elif self.current_token[0] == TokenType.OP_DIV:
                self.eat(TokenType.OP_DIV)
                result /= self.factor()
        return result

    def expression(self):
        result = self.term()
        while self.current_token[0] in (TokenType.OP_SUM, TokenType.OP_SUB):
            if self.current_token[0] == TokenType.OP_SUM:
                self.eat(TokenType.OP_SUM)
                result += self.term()
            elif self.current_token[0] == TokenType.OP_SUB:
                self.eat(TokenType.OP_SUB)
                result -= self.term()
        return result
