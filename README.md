# Random Math Expressions Generator - Software Engineering
## Overview

This Python script generates random mathematical expressions, evaluates them, and writes the expressions along with their results to a text file. It is a simple tool that can also be used to create practice exercises for educational purposes.
## Functionality
### create_mathformula(n):
Generates a random mathematical expression with n operators.
Uses random numbers (0-100) and operators (+, -, *, /).
### evaluate_mathformula(mathformula)
Evaluates a given mathematical expression using Python's "eval()" function.
Handles exceptions, such as division by zero.
### openfile(exercises, n)
Writes generated mathematical exercises and results to a text file ('result.txt').
Includes student ID and the total number of operations in the file header.
Handles FileNotFoundError if the file cannot be opened.
### main()
Entry point of the program. The user should input the number of operations to be performed. It handles input errors if the input is not a integer number. Generates and evaluates mathematical expressions, then writes the results to a file.

## File Structure
#### main.py: 
Main script for executing the program.
#### result.txt:
Output file containing generated exercises and results.

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.
