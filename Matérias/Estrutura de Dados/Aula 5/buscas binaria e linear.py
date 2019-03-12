import math
import matplotlib.pyplot as plt
N = 10

print("Com uma lista de %d elementos" %N)
print("Busca linear = %d" %N)
print("Busca binária = %d" %(math.log2(N)+1))

n = list(range(1,N))
p = [math.log2(i)+1 for i in n]

plt.title("Performance busca linear x busca binária")
plt.xlabel("Quantidade de elementos")
plt.ylabel("Quantidade de verificações")
plt.plot(n,n,label="Busca linear")
plt.plot(n,p,label="Busca binária")
plt.legend()
plt.grid()
plt.show()