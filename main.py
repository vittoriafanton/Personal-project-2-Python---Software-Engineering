from random import randint


def create_mathformula(n):   # to create the final expression that will be evaluated
    operations = ['+', '-', '*', '/']  # possible operators
    mathformula = ""
    for k in range(n-1):
        number1 = randint(0, 100)  # defining a random number between 1 and 100
        number2 = randint(0, 100)
        op = operations[randint(0, 3)]  # defining a random operation between the ones in the array
        mathformula += f"{number1} {op} {number2}"  # obtaining a new part of the expression
    return mathformula


def evaluate_mathformula(mathformula):
    try:
        return eval(mathformula)  # evaluating the expression as a mathematical formula
    except Exception:
        print("ERROR! It could be a division by 0. Generate again random exercises.")
        return 0


def openfile(exercises, n):
    try:
        with open('result.txt', 'w') as file:
            file.write("Student ID: 2256329\n")
            file.write(f"Number of operations performed: {n}\n\n")
            for line in exercises:
                file.write(f"{line}\n")  # write each exercise into the file
    except FileNotFoundError:
        print("Error! File not found")


def main():
    print("My student ID is 2256329")
    n = input("How many operations do we have to perform: ")
    while n.isalpha():  # if the input is not an integer, it will ask to insert another input
        n = input("Not valid number. Please, write how many operations do we have to perform: ")
    n = int(n)
    print("\nThe number of operations to be performed is", n, "\nThe randomly generated operations are shown in the text file.")
    exercises = []  # this array is used to store all the different exercises randomly generated
    for j in range(n):
        nmboperators = randint(3, 5)  # define the number of operators in a line
        line = create_mathformula(nmboperators)
        result = evaluate_mathformula(line)
        totalline = f"{line} = {round(result, 2)}"  # the result is shown rounded to the 2nd decimal number
        exercises.append(totalline)
    openfile(exercises, n)


if __name__ == '__main__':
    main()
