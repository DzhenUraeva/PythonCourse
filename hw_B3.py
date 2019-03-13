def ham_dist(a, b):
    diff_cnt = 0
    for i in range(0, len(b), 1):
        if(a[i] != b[i]):
            diff_cnt += 1
    return diff_cnt

with open('rosalind_hamm.txt', 'r') as file:
    a = file.readline()
    b = file.readline()

file.close()
print(ham_dist(a, b))
