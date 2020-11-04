# problems is a list with computations
# problems = ["31 + 691", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(problems, show_answer=False):
    # if there are to many problems: stop function
    if len(problems) > 5:
        print("Error: Too many problems.")
        return "Error: Too many problems."

    #  variables to store each row
    row1 = []
    row2 = []
    row3 = []
    row4 = []

    for problem in problems:
        # make a list from each problem
        # each problem has three items: [operand, operator, operand]
        problem = problem.split(" ")

        # handle the errors before creating the result:
        # operand is not a digit
        if problem[0].isdigit() is False or problem[2].isdigit() is False:
            print("Error: Numbers must only contain digits.")
            return "Error: Numbers must only contain digits."

        # operator is not + or -
        if not(problem[1] == "+" or problem[1] == "-"):
            print("Error: Operator must be '+' or '-'.")
            return "Error: Operator must be '+' or '-'."

        # operand has too manny digits
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return "Error: Numbers cannot be more than four digits."

        # create the result:
        longest = 0
        stripe = ""

        for i in problem:
            if len(i) > longest:
                longest = len(i)

        # attach the right amount of spaces to each operand
        if len(problem[0]) < longest:
            diff = longest - len(problem[0])
            problem[0] = (diff * " ") + (2 * " ") + problem[0]
            problem[2] = " " + problem[2]
        elif len(problem[2]) < longest:
            diff = longest - len(problem[2])
            problem[0] = (2 * " ") + problem[0]
            problem[2] = (diff * " ") + " " + problem[2]
        else:
            problem[0] = (2 * " ") + problem[0]
            problem[2] = " " + problem[2]

        # make the stripe with the right length
        stripe = (longest * "-") + (2 * "-")

        # create eacht row
        if show_answer is True:
            # solution has to be a string to be able to use the len() function
            solution = str(eval(problem[0] + problem[1] + problem[2]))
            diff = len(stripe) - len(solution)
            row4.append((diff * " ") + solution)

        row1.append(problem[0])
        row2.append(problem[1] + problem[2])
        row3.append(stripe)

    # make a tuple from each row list to be able to use the join() function
    row1[:] = tuple(row1)
    row2[:] = tuple(row2)
    row3[:] = tuple(row3)

    row1 = "    ".join(row1)
    row2 = "    ".join(row2)
    row3 = "    ".join(row3)

    # create the final result (one string)
    result = row1 + "\n" + row2 + "\n" + row3

    if show_answer is True:
        row4 = "    ".join(row4)
        result = result + "\n" + row4

    print(result)
    return result

# arithmetic_arranger(problems, True)
