
A Python-based recursive descent parser for assignment and arithmetic expressions, built for CSCI 4200. Supports lexical analysis, syntax validation, and structured error reporting.
# CSCI 4200 Spring 2025 - Recursive Descent Parser

## Overview

This project is a Python-based parser built for a CSCI 4200 Programming Languages course. It extends a simple expression parser to support assignment statements using a recursive descent parsing strategy. The parser processes arithmetic expressions with variables and constants and validates assignment statement syntax according to a specified grammar.

## Features

- **Grammar Support**: Implements parsing for the following grammar:
<assign> → IDENT ASSIGN_OP <expr>
<expr> → <term> {(+ | -) <term>}
<term> → <factor> {(* | /) <factor>}
<factor> → IDENT | INT_LIT | ( <expr> )
- **Lexical Analysis**: Tokenizes identifiers, integer literals, and operators including `+`, `-`, `*`, `/`, `=`, `(`, `)`.
- **Error Reporting**: Outputs detailed error messages for missing or misplaced tokens.
- **Line-by-Line Parsing**: Processes each line in an input file (`front_in.txt`) and outputs the parser steps and errors.

## Files

## 📁 Files

| File            | Description                                      |
|-----------------|--------------------------------------------------|
| `parse-EXPR.py` | Python implementation of the parser              |
| `front_in.txt`  | Sample input file containing test cases          |
| `front_out.txt` | Output (generated via terminal redirection)      |

## How to Run

1. Ensure Python is installed.
2. Place `parse.py` and `front_in.txt` in the same directory.
3. Run the parser:

 ```bash
 python parse.py > front_out.txt

This redirects the output to front_out.txt.

Sample input (front_in.txt):
average = (num1 +    num2   ) / 2
assignERR 15
= identERR
rightParenERR = (num1 + n
factorERR = *

Sample Output:

Clark, CSCI 4200, Spring 2025, Parser
*******************************************************

Input line: average = (num1 +    num2   ) / 2
Next token is: IDENT, Next lexeme is average
Enter <assign>
Next token is: ASSIGN_OP, Next lexeme is =
Next token is: LEFT_PAREN, Next lexeme is (
Enter <expr>
Enter <term>
Enter <factor>
Next token is: IDENT, Next lexeme is num1
Enter <expr>
Enter <term>
Enter <factor>
Next token is: ADD_OP, Next lexeme is +
Exit <factor>
Exit <term>
Next token is: IDENT, Next lexeme is num2
Enter <term>
Enter <factor>
Next token is: RIGHT_PAREN, Next lexeme is )
Exit <factor>
Exit <term>
Exit <expr>
Next token is: DIV_OP, Next lexeme is /
Exit <factor>
Next token is: INT_LIT, Next lexeme is 2
Enter <factor>
Next token is: EOF, Next lexeme is EOF
Exit <factor>
Exit <term>
Exit <expr>
Exit <assign>

Input line: assignERR 15
Next token is: IDENT, Next lexeme is assignERR
Enter <assign>
Next token is: INT_LIT, Next lexeme is 15
****** ERROR: ASSIGN_OP Expected ******
Exit <assign>

Input line: = identERR
Next token is: ASSIGN_OP, Next lexeme is =
Enter <assign>
****** ERROR: IDENT Expected ******
Exit <assign>

Input line: rightParenERR = (num1 + n
Next token is: IDENT, Next lexeme is rightParenERR
Enter <assign>
Next token is: ASSIGN_OP, Next lexeme is =
Next token is: LEFT_PAREN, Next lexeme is (
Enter <expr>
Enter <term>
Enter <factor>
Next token is: IDENT, Next lexeme is num1
Enter <expr>
Enter <term>
Enter <factor>
Next token is: ADD_OP, Next lexeme is +
Exit <factor>
Exit <term>
Next token is: IDENT, Next lexeme is n
Enter <term>
Enter <factor>
Next token is: EOF, Next lexeme is EOF
Exit <factor>
Exit <term>
Exit <expr>
****** ERROR: RIGHT_PAREN Expected ******
Exit <factor>
Exit <term>
Exit <expr>
Exit <assign>

Input line: factorERR = *
Next token is: IDENT, Next lexeme is factorERR
Enter <assign>
Next token is: ASSIGN_OP, Next lexeme is =
Next token is: MULT_OP, Next lexeme is *
Enter <expr>
Enter <term>
Enter <factor>
****** ERROR: IDENT, INT_LIT, or LEFT_PAREN Expected ******
Exit <factor>
Next token is: EOF, Next lexeme is EOF
Enter <factor>
****** ERROR: IDENT, INT_LIT, or LEFT_PAREN Expected ******
Exit <factor>
Exit <term>
Exit <expr>
Exit <assign>

Parsing the program is complete!

Author:
Clark Neal
CSCI 4200, Spring 2025
University of North Georgia
