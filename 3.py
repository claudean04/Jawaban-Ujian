def handshake(n):  
    if (n == 0): 
        return 0
    else: 
        return (n - 1) + handshake(n - 1)  
  
# Driver Code 
n = int(input("Masukkan Jumlah orang : "))
print(handshake(n))