with open('sample_file', 'r') as f: # plik "sam" się zamknie
    for line in f:
        print(len(line), line, end='')
    print(80*'-')
    for line in f:
        print(len(line), line, end='')
    print(80*'-')
    f.seek(0)
    for line in f:
        print(len(line), line, end='')

print(type(f))
print(f.read())
