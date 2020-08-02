ciphertxt = list(map(str, input().split()))
ciphertxt = [list(i) for i in ciphertxt]
ciphertxt = [[0 if (j=='a') else 1 for j in i] for i in ciphertxt]
ciphertxt = [''.join(map(str, i)) for i in ciphertxt]
ciphertxt = [chr(int(i,2)+97) for i in ciphertxt]
ciphertxt = ''.join(ciphertxt)
print(ciphertxt)