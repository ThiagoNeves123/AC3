#AC3

#Exercício 1

salario = float(input("Salário do colaborador:"))
if (salario <= 280):
    percentual = 20
elif (salario <= 700):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5

print("Salário original: R$" , salario)
print( "Percentual: ", percentual, "%")

percentual = percentual/100
aumento = percentual * salario
novo_salario = salario + aumento

print("aumento: R$", aumento)
print("Novo salário: R$", novo_salario)

#Exercício 2 

def funcao():

    num = int(input("Digite um número:"))

    if num == 1:
        print("Domingo")
    elif num == 2:
        print("Segunda")
    elif num == 3:
        print("Terça")
    elif num == 4:
        print("Quarta")
    elif num == 5:
        print("Quinta")
    elif num == 6:
        print("Sexta")
    elif num == 7:
        print("Sábado")
    else:
        print("Número inválido")

funcao()

#Exercício 3

a = float(input("Digite o valor de A:"))
if a == 0:
    print("Digite outro valor que não seja zero")
else:
    b = float(input("Digite o valor de B:"))
    c = float(input("Digite o valor de C: "))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("A equação não possui raizes reais.")

else:
    x1 = ((- b + delta ** 0.5) / (2 * a))
    x2 = ((- b - delta ** 0.5) / (2 * a))
if delta == 0:
    print("Essa equação possui apenas uma raiz real =", x1 , ".")
else:
    print("Essa equação possui duas raízes reais -> x1 =" , x1 , "x2=", x2, ".")


    