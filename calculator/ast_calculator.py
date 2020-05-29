from preprocess import *

'''
# This is implementation of simple calculator.
# It was written in order to demonstrate working with ast - abstract syntax tree.
# Supported operators: + (plus), - (subtraction), * (muliplication), / (division).
# Braces are not supported! NOT SUPPORTED: (x + y) * z
'''

# Represents Abstract syntax tree node.
class ASTNode():
    def __init__(self, operation, value, left_n, right_n):
        self.operation = operation
        self.value = value
        self.left_n = left_n
        self.right_n = right_n

# Function, which evaluate expression from abstract syntax tree.
def evaluate(Node):
    if Node.value != None:
        return Node.value

    try:
        if Node.operation == '+':
            return evaluate(Node.right_n) + Node.left_n.value
        elif Node.operation == '-':
            return evaluate(Node.right_n) - Node.left_n.value
        elif Node.operation == '*':
            return evaluate(Node.right_n) * Node.left_n.value
        elif Node.operation == '/':
            if Node.right_n.value != 0:
                return evaluate(Node.right_n) / Node.left_n.value
            else:
                raise ZeroDivisionError
    except:
        if Node.operation == '+':
            return evaluate(Node.left_n) + Node.right_n.value
        elif Node.operation == '-':
            return evaluate(Node.left_n) - Node.right_n.value
        elif Node.operation == '*':
            return evaluate(Node.left_n) * Node.right_n.value
        elif Node.operation == '/':
            if Node.left_n.value != 0:
                return evaluate(Node.left_n) / Node.right_n.value
            else:
                raise ZeroDivisionError

'''
# Recursive function, which creates abstract syntax tree.
# Takes list with expression.
# Example of expression: [2, '+', 2, '*', 3, '+', 1]
'''
def ast_creation(expression_list):
    # Check on leaf.
    if (len(expression_list) == 1):
        try:
            test = int(expression_list[0])
            return ASTNode(None, expression_list[0], None, None)
        except:
            print("input error")
            exit(1)

    operators_priority = {1: "+-", 2: "*/"}
    priority = 1
    ast = None
    while(priority < 3):
        for i in range(len(expression_list)):
            try:
                test = int(expression_list[i])
            except:
                if expression_list[i] in operators_priority[priority]:
                    ast = ASTNode(expression_list[i], 
                                  None, 
                                  ast_creation(expression_list[0:i]), 
                                  ast_creation(expression_list[i + 1:len(expression_list)]))
                    return ast;
        priority += 1;

def main():
    while(1):
        expression              = input('Write your expression: ')
        preprocessed_expression = preprocessing(expression)
        if (preprocessed_expression == -1):
            continue
        ast = ast_creation(preprocessed_expression)
        print("The result is: ", end="")
        print(evaluate(ast))

if __name__ == "__main__":
    main()

