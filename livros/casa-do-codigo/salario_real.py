salario = int(input("Qual seu salário liquido? "))
imposto = input("Qual a taxa de imposto estabelecida? (ex: 27.5)? ")

if not imposto:
    imposto = 27.5
else:
    imposto = float(imposto)

if imposto < 10:
    print("Medio")
elif imposto < 27.5:
    print("Alto")
else:
    print("Muito alto") 

print("Seu salário real é de {0}".format(salario - (salario * (imposto * 0.01))))
