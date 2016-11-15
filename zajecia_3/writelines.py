a = [1, 2, 3, 4, 6]
with open('writelines_out.txt', 'w') as f:
    f.writelines((str(x) for x in a))
