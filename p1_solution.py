if __name__ == '__main__':
    n = int(input())

    seq = "" # sequence or seq is the name of the variable that will store the string sequence that the problem wants.
    for i in range(1, n+1):
        s = str(i)
        seq = seq + s
    print(seq)
