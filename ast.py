# This code is example of 
# constructing AST - abstract syntax tree.
# Abstract syntax tree (AST), or just syntax tree, 
# is a tree representation of the abstract syntactic structure 
# of source code written in a programming language. 
# Each node of the tree denotes a construct occurring in the source code.

# Tree, which is constructed:
# represents expression (2 + 3) * 4 / 5
#       /
#      / \
#     *   5
#    / \
#   +   4
#  / \
# 2   3


# Represents Abstract syntax tree node.
class ASTNode():
    def __init__(self, operation, value, left_n, right_n):
        self.operation = operation
        self.value = value
        self.left_n = left_n
        self.right_n = right_n

# func, which takes root node and recursively evaluates
# all child nodes.
def evaluate(Node):
    if Node.value != None:
        return Node.value

    if Node.operation == '+':
        return evaluate(Node.left_n) + Node.right_n.value
    elif Node.operation == '-':
        return evaluate(Node.left_n) - Node.right_n.value
    elif Node.operation == '*':
        return evaluate(Node.left_n) * Node.right_n.value
    elif Node.operation == '/':
        if Node.right_n.value != 0:
            return evaluate(Node.left_n) / Node.right_n.value
        else:
            raise ZeroDivisionError

# creating a tree.
node_two   = ASTNode(None, 2, None, None)
node_three = ASTNode(None, 3, None, None)
node_plus  = ASTNode('+', None, node_two, node_three)
node_four  = ASTNode(None, 4, None, None)
node_mul   = ASTNode('*', None, node_plus, node_four)
node_five  = ASTNode(None, 5, None, None)
node_div   = ASTNode('/', None, node_mul, node_five) #root

# printing the result of expression (2 + 3) * 4 / 5
print(evaluate(node_div))

