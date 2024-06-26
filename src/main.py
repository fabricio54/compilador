import os
from my_parser import Parser


# Obtendo o caminho absoluto para o arquivo file.txt
file_path = os.path.abspath("../file/file.txt")

# Lendo o conteúdo do arquivo
with open(file_path, "r") as file:
    expression = file.read()

# Testando o analisador com a expressão lida do arquivo
# Testando o analisador com a expressão lida do arquivo
parser = Parser(expression)
tokens = parser.tokenize()  # Obtém os tokens da expressão

# Imprimindo os tokens no formato <type.name, lexema>
for token in tokens:
    print(f"<{token[0]}, {token[1]}>")

if parser.is_infix(expression):
    print("A expressão é infixa.")
elif parser.is_prefix(expression):
    print("A expressão é prefixa.")
else:
    print("A expressão não é nem infixa nem prefixa.")

