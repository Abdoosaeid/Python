def split_and_join(line):
    line=line.split("a")
    
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)