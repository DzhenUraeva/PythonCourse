with open('rosalind_revc.txt', 'r') as file:
    a = file.read()
    
a = a[::-1]
a = a.replace('A', 'X')
a = a.replace('T', 'A')
a = a.replace('X', 'T')
a = a.replace('C', 'X')
a = a.replace('G', 'C')
a = a.replace('X', 'G')

print(a)
file.close()
