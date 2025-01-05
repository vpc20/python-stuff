import sys

single_char_tokens = {'(': 'LEFT_PAREN',
                      ')': 'RIGHT_PAREN',
                      '{': 'LEFT_BRACE',
                      '}': 'RIGHT_BRACE',
                      '*': 'STAR',
                      '.': 'DOT',
                      ',': 'COMMA',
                      '+': 'PLUS',
                      '-': 'MINUS',
                      ';': 'SEMICOLON'}
slash_token = {'/': 'SLASH'}
other_single_char_tokens = {'<': 'LESS',
                            '>': 'GREATER',
                            '=': 'EQUAL',
                            '!': 'BANG'}
double_char_tokens = {'==': 'EQUAL_EQUAL',
                      '!=': 'BANG_EQUAL',
                      '<=': 'LESS_EQUAL',
                      '>=': 'GREATER_EQUAL'}


def lexer(file):
    exit_code = 0
    line_num = 1
    other_single_char = None
    slash_char = None
    double_slash_found = False

    while True:
        char = file.read(1)

        if not char:
            break

        if double_slash_found:
            if char == '\n':
                line_num += 1
                double_slash_found = False
            continue

        if slash_char:
            if char == '/':
                double_slash_found = True
                continue
            else:
                print(f'{slash_token[slash_char]} {slash_char} null')
                slash_char = None

        if other_single_char:
            if char == '=':  # double char
                print(f'{double_char_tokens[other_single_char + char]} {other_single_char + char} null')
                other_single_char = None
                continue
            else:  # not double char, so print previously read char
                print(f'{other_single_char_tokens[other_single_char]} {other_single_char} null')
                other_single_char = None

        if char == '\n':
            line_num += 1
        elif char in single_char_tokens:
            print(f'{single_char_tokens[char]} {char} null')
        elif char in other_single_char_tokens:
            other_single_char = char
        elif char == '/':
            slash_char = char
        elif char in ['$', '#', '@', '%']:
            print(f'[line {line_num}] Error: Unexpected character: {char}', file=sys.stderr)
            exit_code = 65

    print('EOF  null')
    exit(exit_code)


def main():
    file = open('test.lox')
    lexer(file)
    file.close()


if __name__ == "__main__":
    main()
