import sys

sys.stdin = open('sample_input.txt', 'r')

exp = input()

op_bracket_stack = []
post = []

priority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}


def is_operator(e):
    return e in ['+', '-', '*', '/']


for e in exp:
    if is_operator(e):
        if len(op_bracket_stack) == 0:
            op_bracket_stack.append(e)
            continue
        while (len(op_bracket_stack) > 0 and
                op_bracket_stack[-1] != '(' and
                priority[op_bracket_stack[-1]] >= priority[e]):
            post.append(op_bracket_stack.pop())
        op_bracket_stack.append(e)
    elif e == '(':
        op_bracket_stack.append('(')
    elif e == ')':
        while (len(op_bracket_stack) > 0 and
                op_bracket_stack[-1] != '('):  # 여는 괄호 전까지
            post.append(op_bracket_stack.pop())  # 연산자 post에 다 넣기
        op_bracket_stack.pop()  # 여는 괄호 제거하기
    else:
        post.append(e)

while len(op_bracket_stack) > 0:
    post.append(op_bracket_stack.pop())

print(''.join(post))
