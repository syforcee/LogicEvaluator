#Converts expression to postfix notation

operator_imp = ">"
operator_equal="="
operator_and = "&"
operator_or = "|"
operator_xor="v"
operator_not = "!"
operator_left_paran = "("
operator_right_paran = ")"

operator_precedence = {
    operator_not: 4,
    operator_imp: 2,
    operator_equal:2,
    operator_and: 3,
    operator_xor:2,
    operator_or: 2,
    operator_left_paran: -1,
    operator_right_paran: -1
}

operator_association = {
    operator_imp: "left",
    operator_and: "left",
    operator_or: "left",
    operator_equal:"left",
    operator_xor:"left",
    operator_not: "right"
}

def precedence(op):
    return operator_precedence[op]

def associativity(op):
    return operator_association[op]

def is_left_paran(c):
    return c == operator_left_paran

def is_right_paran(c):
    return c == operator_right_paran

def is_op(c):
    return (c in operator_precedence) and not (is_left_paran(c) or is_right_paran(c))

def convert_postfix(tokens):
    stack = []
    postfix=[]
    for token in tokens:
        if is_op(token):
            while stack and is_op(stack[-1]) and \
                ((associativity(token ) == "left" and precedence(token)<=precedence(stack[-1]))
                or (associativity(token)=="right") and precedence(token) < precedence(stack[-1])):
                postfix.append(stack.pop())
            stack.append(token)
        elif is_left_paran(token):
            stack.append(token)
        elif is_right_paran(token):
            while stack and not is_left_paran(stack[-1]):
                postfix.append(stack.pop())
            if is_left_paran(stack[-1]):
                stack.pop()
        else:
            postfix.append(token)
    while stack:
        if is_right_paran(stack[-1]) or is_left_paran(stack[-1]):
            print("error: mismatched brackets")
        postfix.append(stack.pop())
    return postfix
