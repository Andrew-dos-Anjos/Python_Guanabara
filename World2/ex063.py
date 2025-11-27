#Sequência de Fibonacci
# ----------

n = int(input("Quantos termos deseja excecultar?"))
c = 3
t1 = 0
t2 = 1
print(f"{t1} -> {t2} ", end="")
while c <= n:
    t3 = t2 + t1
    print(f"-> {t3} ", end="")
    t1 = t2
    t2 = t3
    #Com o laço renovando os valores é possível realizar a substituição dos termos como demonstrado acima.
    c += 1
print("-> Fim")

#Phoenix 🏆