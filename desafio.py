presenca = input ("o aluno veio? ")
frequencia = 20

if presenca == "sim":
    frequencia = frequencia + 1

    if frequencia >= 21:
        print ("agora vc pode convidar um amigo")
        print ("vc esta partipando da nossa promocao")
    
elif presenca=="nao":
        frequencia= 0
        print("que bom ver vc de volta")
        print ("vc esta partipando da nossa promocao")

else:
        print ("vc esta participando da nossa promo")
        print(frequencia)

