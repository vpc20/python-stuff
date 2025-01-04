import os
import subprocess
import sys


# Backslash within double quotes
def file_exists(filename):
    path = os.environ.get('PATH')
    delim = ';' if os.name == 'nt' else ':'
    pathnames = path.split(delim)
    for pathname in pathnames:
        fullname = os.path.join(pathname, filename)
        if os.path.isfile(fullname):
            return fullname
    return None


# parsing of command arguments
def split_args(command_string):
    tokens = []
    current_token = ""
    single_quote_char = None
    double_quote_char = None
    escaped = False

    backslash_in_double_quote = False
    for i, char in enumerate(command_string):
        if escaped:
            current_token += char
            escaped = False
        elif backslash_in_double_quote:
            current_token += char
            backslash_in_double_quote = False
        elif char == '\\':
            if double_quote_char:
                if command_string[i+1] not in ['\\', '$', '"']:
                    current_token += char
                else:
                    backslash_in_double_quote = True
            elif single_quote_char:
                current_token += char
            else:
                escaped = True
        elif single_quote_char:
            if char == single_quote_char:
                single_quote_char = None
            else:
                current_token += char
        elif double_quote_char:
            if char == double_quote_char:
                double_quote_char = None
            else:
                current_token += char
        elif char == "'":
            single_quote_char = char
        elif char == '"':
            double_quote_char = char
        elif char == ' ' and not single_quote_char and not double_quote_char:
            if current_token:
                tokens.append(current_token)
                current_token = ""
        else:
            current_token += char

        # Add the last token if it's not empty
    if current_token:
        tokens.append(current_token)

    return tokens


def write_to_file(filename, stdout):
    f = open(filename, 'w')
    f.write(stdout)
    f.close()


def main():
    builtin_cmds = ['echo', 'exit', 'type', 'pwd', 'cd']

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == '':
            continue
        cmds = command.split()
        cmd = cmds[0]
        if len(cmds) > 1:
            cmd, arg = command.split(' ', maxsplit=1)

        if command.startswith('exit'):
            if len(cmds) == 1:
                return
            if command[5:] != ' ':
                return int(arg)
            else:
                return
        elif command.startswith('echo'):
            # print(' '.join(shlex.split(arg)))
            splitted_args = split_args(arg)
            if len(splitted_args) >= 3 and splitted_args[-2] in ['>', '1>']:
                write_to_file(splitted_args[-1], ' '.join(splitted_args[:-2]) + '\n')
            else:
                print(' '.join(split_args(arg)))
        elif command == 'pwd':
            print(os.getcwd())
        elif command.startswith('cd'):
            if arg == '~':
                os.chdir(os.path.expanduser("~"))
            else:
                try:
                    os.chdir(arg)
                except FileNotFoundError:
                    print(f'cd: {arg}: No such file or directory')
        elif command.startswith('type'):
            if arg in builtin_cmds:
                print(f'{arg} is a shell builtin')
            else:
                fullname = file_exists(arg)
                if fullname is not None:
                    print(f'{arg} is {fullname}')
                else:
                    print(f'{arg}: not found')
        else:
            # cmds = shlex.split(command)
            cmds = split_args(command)
            if os.name == 'nt':  # in windows, add the '.exe' to the command
                cmds[0] = cmds[0] + '.exe'
            if file_exists(cmds[0]):
                if len(cmds) >= 3 and cmds[-2] in ['>', '1>']:  # redirect output to file
                    result = subprocess.run(cmds[:-2], capture_output=True, text=True)
                else:
                    result = subprocess.run(cmds, capture_output=True, text=True)
                if len(cmds) >= 3 and cmds[-2] in ['>', '1>']:
                    write_to_file(cmds[-1], result.stdout)
                else:
                    sys.stdout.write(result.stdout)  # display ouput to console
                if result.returncode != 0:  # error encountered
                    sys.stdout.write(result.stderr)
            else:
                print(f'{cmd}: command not found')


if __name__ == "__main__":
    main()
