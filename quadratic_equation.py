import math

print('''Seja bem-vindo(a). Calcule equações do 2°grau!
Fórmula: ax² + bx + c = 0
Fórmula de Delta: Δ = b² – 4ac
fórmula de Bhaskara: x = –b ± √Δ / 2a\n''')

try:
    termA = int(input("Valor do coeficiente A: "))
    if termA == 0:
        print("Se A for 0, não existe uma equação de 2°grau. Reinicie e tente novamente.")
        quit()
    else:
        termB = int(input("Valor do coeficiente B: "))
        termC = int(input("Valor do coeficiente C: "))
except ValueError:
    print("Erro: digite apenas números. Reinicie e tente novamente.")
else:
    def quadratic_equation(a=0, b=0, c=0):
        delta = (b**2) - (4*a*c)
        if delta < 0:
            print("Delta negativo: não existe solução real.")
            print("\nPrograma encerrado. Reinicie e tente novamente")
            quit()
        elif delta == 0:
            print("Delta igual a 0: possuí duas raízes reais iguais.")
        else:
            print("Delta positivo: possuí duas raízes reais diferentes.")

        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        print(f"\nValor de Delta: {delta}")
        print(f"x1: {x1:.1f}  x2: {x2:.1f}")

    quadratic_equation(termA, termB, termC)
