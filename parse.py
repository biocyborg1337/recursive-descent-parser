'''
parse.py
Programmer: YOUR NAME
Class: CSCI 4200, Spring 2025
Purpose:
    A parser, which implements the following grammar:
    1. <assign>    → id = <expr>
    2. <expr>      → <term> {(+ | -) <term>}
    3. <term>      → <factor> {(* | /) <factor>}
    4. <factor>    → id | int_constant | ( <expr> )
'''

import sys

# Global declarations
char_class = None
lexeme = []
next_char = ''
lex_len = 0
next_token = None
next_token_code = None
current_line = ''
char_idx = 0
input_lines = []

# Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99
EOF = -1

# Token codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

# Token names
TOKEN_NAMES = {
    10: "INT_LIT",
    11: "IDENT",
    20: "ASSIGN_OP",
    21: "ADD_OP",
    22: "SUB_OP",
    23: "MULT_OP",
    24: "DIV_OP",
    25: "LEFT_PAREN",
    26: "RIGHT_PAREN",
    -1: "EOF"
}

def error(msg="****** ERROR ******"):
    print(f"****** ERROR: {msg} ******")

def add_char():
    # Adds the current character to the lexeme list if length allows
    global lexeme, next_char, lex_len
    if lex_len <= 98:
        lexeme.append(next_char)
        lex_len += 1
    else:
        print("Error - lexeme is too long")

def get_char():
    # Reads the next character from the current line and classifies it
    global next_char, char_class, current_line, char_idx
    if char_idx < len(current_line):
        next_char = current_line[char_idx]
        char_idx += 1
        if next_char.isalpha():
            char_class = LETTER
        elif next_char.isdigit():
            char_class = DIGIT
        else:
            char_class = UNKNOWN
    else:
        char_class = EOF

def get_non_blank():
    # Skips whitespace characters
    global next_char
    while next_char.isspace():
        get_char()

def lookup(ch):
    # Looks up and returns the token code for an operator or delimiter
    global next_token_code
    if ch == '(':
        add_char()
        next_token_code = LEFT_PAREN
    elif ch == ')':
        add_char()
        next_token_code = RIGHT_PAREN
    elif ch == '+':
        add_char()
        next_token_code = ADD_OP
    elif ch == '-':
        add_char()
        next_token_code = SUB_OP
    elif ch == '*':
        add_char()
        next_token_code = MULT_OP
    elif ch == '/':
        add_char()
        next_token_code = DIV_OP
    elif ch == '=':
        add_char()
        next_token_code = ASSIGN_OP
    else:
        add_char()
        next_token_code = EOF
    return next_token_code

def lex():
    # Lexical analyzer function – returns the next token from input
    global lex_len, next_token, next_token_code, char_class, lexeme, next_char, char_idx
    lexeme = []
    lex_len = 0
    get_non_blank()
    if char_class == LETTER:
        add_char()
        get_char()
        while char_class in [LETTER, DIGIT]:
            add_char()
            get_char()
        next_token_code = IDENT
    elif char_class == DIGIT:
        add_char()
        get_char()
        while char_class == DIGIT:
            add_char()
            get_char()
        next_token_code = INT_LIT
    elif char_class == UNKNOWN:
        next_token_code = lookup(next_char)
        get_char()
    elif char_class == EOF:
        next_token_code = EOF
        lexeme[:] = ['E', 'O', 'F']

    next_token = TOKEN_NAMES.get(next_token_code)
    print(f"Next token is: {next_token}, Next lexeme is {''.join(lexeme)}")
    return next_token

# === Recursive Descent Parser ===
def assign():
    # <assign> → id = <expr>
    print("Enter <assign>")
    global next_token
    if next_token == "IDENT":
        lex()
        if next_token == "ASSIGN_OP":
            lex()
            expr()
            if next_token != "EOF":
                error("Problem Parsing the Whole Line")
        else:
            error("ASSIGN_OP Expected")
    else:
        error("IDENT Expected")
    print("Exit <assign>")

def expr():
    # <expr> → <term> {(+ | -) <term>}
    print("Enter <expr>")
    term()
    while next_token == "ADD_OP" or next_token == "SUB_OP":
        lex()
        term()
    print("Exit <expr>")

def term():
    # <term> → <factor> {(* | /) <factor>}
    print("Enter <term>")
    factor()
    while next_token == "MULT_OP" or next_token == "DIV_OP":
        lex()
        factor()
    print("Exit <term>")

def factor():
    # <factor> → id | int_constant | ( <expr> )
    print("Enter <factor>")
    global next_token
    if next_token == "IDENT" or next_token == "INT_LIT":
        lex()
    elif next_token == "LEFT_PAREN":
        lex()
        expr()
        if next_token == "RIGHT_PAREN":
            lex()
        else:
            error("RIGHT_PAREN Expected")
    else:
        error("IDENT, INT_LIT, or LEFT_PAREN Expected")
    print("Exit <factor>")

# === Main Driver ===
try:
    sys.stdout = open('front_out.txt', 'w')  # Redirect output to file

    print("\nClark, CSCI 4200, Spring 2025, Parser")
    print("*" * 55)

    with open("front_in.txt", "r") as in_fp:
        input_lines = in_fp.readlines()

    for current_line in input_lines:
        print()
        current_line = current_line.strip()
        if not current_line:
            continue  # Skip empty lines
        print(f"Input line: {current_line}")
        char_idx = 0
        get_char()
        lex()
        assign()

    print("\nParsing the program is complete!")

except FileNotFoundError:
    print("ERROR - cannot open front_in.txt")
    sys.exit()

finally:
    sys.stdout.close()
