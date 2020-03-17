# single lowercase char tokens only
# assume valid expression

from string import ascii_lowercase


def infix_to_postfix(infix):
    preced = {'*': 1, '/': 1, '+': 2, '-': 2}
    postfix = ''
    opstack = []
    tokens = [ch for ch in infix if ch != ' ']
    for token in tokens:
        if token in ascii_lowercase:
            postfix += token
        else:
            if opstack:
                while opstack and preced[opstack[-1]] <= preced[token]:
                    postfix += opstack.pop()
            opstack.append(token)
    while opstack:
        postfix += opstack.pop()
    return postfix


def infix_to_prefix(infix):
    return infix_to_postfix(infix[-1::-1])[-1::-1]


print(infix_to_postfix('a +b '))
print(infix_to_postfix('a +b*c '))
print(infix_to_postfix('a +b *c +     d  '))

print(infix_to_prefix('a+b'))
print(infix_to_prefix('a +b*c '))
print(infix_to_prefix('a +b *c +     d  '))
