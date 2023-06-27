import lexical
from parser_1 import Parser

# Formula input
input_formula = "123 + 234 - 1.123 x -576"

# Analisis leksikal
output_tokens = lexical.lexical_analyzer(input_formula)
print("Input: ", input_formula)
print("Output (Lexical):", " ".join(str(token) for token in output_tokens))

# Parsing
parser = Parser(output_tokens)
parser.parse()


# Formula input
input_formula = "7.5 : -2.14 ^ 178 |"

# Analisis leksikal
output_tokens = lexical.lexical_analyzer(input_formula)
print("Input: ", input_formula)
print("Output (Lexical):", " ".join(str(token) for token in output_tokens))

# Parsing
parser = Parser(output_tokens)
parser.parse()


# Formula input
input_formula = input_formula = "( -123 x 99.6 ^ 55.4 ) ]"

# Analisis leksikal
output_tokens = lexical.lexical_analyzer(input_formula)
print("Input: ", input_formula)
print("Output (Lexical):", " ".join(str(token) for token in output_tokens))

# Parsing
parser = Parser(output_tokens)
parser.parse()