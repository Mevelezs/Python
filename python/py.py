faren = 10

print(f"{faren} grados fahrenheit son {(float (faren) - 32)*( 5/9):.1f} grados centigrados")
numero = 123.456

# Imprimir con dos cifras significativas
print(f"{numero:.2f}")

R = float (input())
W = (R * 0.19) + R
T = R * 0.1
U = R + W + T
print(f"Total consumido: COP$ {R}\nValor IVA: COP$ {W}\nValor propina: COP$ {T}\nA pagar: COP$ {U}")