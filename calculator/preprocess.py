'''
# This module preprocess user`s input.
# It takes an expression. Example: "2+3*8+123"
# And returns list with separated elements.
# Example: [2, '+', 3, '*', 8, '+', 123].
# Note, that digits have <int> data type and operators <str>.
'''

def error_handler(expression):
    for i in expression:
        if (i.isalpha()):
            print("input error: alphabetic symbols are used")
            return 1
    if len(expression) == 0:
        print("input error: wrong input")
        return 1;
    if expression[len(expression) - 1].isdigit() == False:
        print("input error: wrong input")
        return 1;
    if expression[0].isdigit() == False:
        print("input error: wrong input")
        return 1;

def preprocessing(expression):
    if (error_handler(expression)):
        return -1
    expression_splt = []
    for i in range(len(expression)):
        expression_splt.append(expression[i])
    index = 0
    preprocessed_expression = []
    for i in range(len(expression_splt)):
        if expression_splt[i] in "+-/*()":
            preprocessed_expression.append(expression_splt[i])
            index += 1;
        elif (expression_splt[i].isdigit()):
            if i == 0:
                preprocessed_expression.append(expression_splt[i])
                index += 1
            elif preprocessed_expression[len(preprocessed_expression) - 1] not in "+-/*()":
                preprocessed_expression[len(preprocessed_expression) - 1] += expression_splt[i]
            elif expression_splt[i].isdigit():
                preprocessed_expression.append(expression_splt[i])
    for i in range(len(preprocessed_expression)):
        if (preprocessed_expression[i].isdigit()):
            preprocessed_expression[i] = int(preprocessed_expression[i])
    return preprocessed_expression

