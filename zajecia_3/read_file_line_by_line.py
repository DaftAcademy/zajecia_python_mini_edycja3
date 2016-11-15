f = open('sample_file', 'r')
for i, line in enumerate(f):
    print(i, line) # dodać end='' do print, żeby nie dodawał swoich końców linii

# po raz drugi nie ma rady
for i, line in enumerate(f):
    print(i, line, end='')

# ale seek daje radę:
f.seek(0)
for i, line in enumerate(f):
    print(i, line, end='') # dodać end='' do print, żeby nie dodawał swoich końców linii
   
f.close()
