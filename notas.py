aluno = input("Qual o nome do Aluno: ")
nota1 = float(input("Qual a média do 1º Bimestre: "))
nota2 = float(input("Qual a média do 2º Bimestre: "))
nota3 = float(input("Qual a média do 3º Bimestre: "))
nota4 = float(input("Qual a média do 4º Bimestre: "))

soma = nota1 + nota2 + nota3 + nota4
media= float(soma / 4)
print (f"ola, {aluno} sua media foi {media}")

