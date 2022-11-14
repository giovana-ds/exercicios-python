nomecompleto = str(input("\nInforme o seu nome completo: "))
nome = lambda nome: nome.split()[0]
sobrenome = lambda nome: nome.split()[-1]

print(f"\nSeu primeiro nome é {nome(nomecompleto)} e o seu sobrenome é {sobrenome(nomecompleto)}.")