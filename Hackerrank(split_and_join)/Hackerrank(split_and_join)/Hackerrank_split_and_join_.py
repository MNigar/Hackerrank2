def split_and_join(line):
    newline=line.split(' ')
    joinline='-'.join(newline)
    return joinline
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
