with open('rosalind_rna.txt', 'r') as file:
    a = file.read()
    
print(a.replace('T', 'U'))

file.close()
