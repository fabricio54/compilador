from enum import Enum, auto

class TokenType(Enum):
    CONST_INT = auto()
    CONST_FLOAT = auto()
    OP_SUM = auto()
    OP_SUB = auto()
    OP_MUL = auto()
    OP_DIV = auto()
    ABRE_PAR = auto()
    FECHA_PAR = auto()
    PONTO_VIRGULA = auto()
    COMMENT = auto()
    EOF = auto()

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.keywords = ['+', '-', '*', '/', '(', ')']

    def get_next_token(self):
        while self.pos < len(self.text):
            # Ignora espaços em branco
            if self.text[self.pos].isspace():
                self.pos += 1
                continue

            # Verifica se é um número inteiro ou float
            if self.text[self.pos].isdigit():
                num_str = ''
                while self.pos < len(self.text) and (self.text[self.pos].isdigit() or self.text[self.pos] == '.'):
                    num_str += self.text[self.pos]
                    self.pos += 1
                if '.' in num_str:
                    return (TokenType.CONST_FLOAT, float(num_str))
                else:
                    return (TokenType.CONST_INT, int(num_str))

            # Verifica se é um caractere válido
            if self.text[self.pos] in self.keywords:
                token_type = {
                    '+': TokenType.OP_SUM,
                    '-': TokenType.OP_SUB,
                    '*': TokenType.OP_MUL,
                    '/': TokenType.OP_DIV,
                    '(': TokenType.ABRE_PAR,
                    ')': TokenType.FECHA_PAR,
                }[self.text[self.pos]]
                token = (token_type, self.text[self.pos])
                self.pos += 1
                return token

            # Se não for nenhum dos casos acima, retorna erro
            raise ValueError(f"Caractere inválido: {self.text[self.pos]}")

        # Se chegou ao final do texto, retorna token de fim de arquivo
        return (TokenType.EOF, None)
