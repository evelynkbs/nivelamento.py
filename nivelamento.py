class exercicio:
    def __init__(self):
        print('')

    def ex1(self):
        nomeFuncio = "Érika"
        idade = 17
        salario = 5000
        cargo = "gerente"
        turno = "matutino"
        setor = "rh"
        print("Funcionário:", nomeFuncio)
        print("Idade:" , idade)
        print("Salário:" , salario)
        print("Cargo:" , cargo)
        print("Turno" , turno)
        print("Setor:" , setor)

   
    def ex2(self):
        nomeEscola = "CCM"
        estado = "Paraná"
        numProf = 50
        cidade = "Cdo"
        numMil = 4
        logradouro = "Rua Santos Drumond"
        endNum = 364
        numAlun = 700
        colegioMili = True
        disciplinas = ["Port", "Mat", "Ingl", "Quim"]
        print("O nome da escola é:", nomeEscola)
        print("Se localiza no estado do" , estado)
        print("Tem" , numProf , "professores")
        print("Na cidade de" , cidade)
        print("Militares: " , numMil)
        print("logradouro:" , logradouro)
        print("Número do endereço:", endNum)
        print("Número de alunos:" , numAlun)
        print ("O colégio é militar?", colegioMili)
        print("Algumas disciplinas são:" , disciplinas)
       

    def ex3(self):
        valor1 = 10
        valor2 = 5
        valor3 = "2"
        valor4 = 8
        valor5 = -5
        soma1 = valor1 + valor2
        soma2 = valor1 + valor2 + valor4
        soma3 = valor1 + valor2 - valor5
        soma4 = valor1 + int(valor3)
        soma5 = valor1 + valor2
        soma6 = (valor4 + valor2) / 2
        soma7 = (valor1 + valor2 + valor4 + valor5) / 4
        print("A soma do valo1 + valor2 é:", soma1)
        print("A soma do valor1 + valor2 + valor4 é:" , soma2)
        print("A soma do valor1 + valor2 - valor5 é:", soma3)
        print("A soma do valor1 + valor3 é:" , soma4)
        print("O valor1 x valor2 é: " , soma5)
        print("O valor4 x valor2 dividiso por 2 é:" , soma6)
        print("A soma do valor1 + valor2 + valor4 + valor5 dividido por 4 é:", soma7)


    def ex4(self):
        v1 = 2
        v2 = 3
        v3 = 5
        v4 = 6
        soma = v1 + v2 + v3 +v4
        media = soma / 4
        print("A soma dos valores é:", soma)
        print("A média dos valores é:", media)


    def ex5(self, nota):
        if (nota <= 60):
            print("Reprovado")
        else:
            print("Aprovado")


    def ex6(self, nota):
        if (nota < 60):
            print("Aluno reprovado")
        else:
            print("Aluno aprovado")
        if (nota > 80):
            print("Aluno foi aprovado com certificado")

   
    def ex7(self):
        lista=[1,2,3,4,5]
        print(lista[0])
        print(lista[1])
        print(lista[2])
        print(lista[3])
        print(lista[4])


    def ex8(self):
        notas = [0]
        notas[0] = 80
        notas.append(60)
        notas.append(30)
        notas.append(40)
        notas.append(80)
        notas.append(90)
        print("Notas:", notas)
        notas.pop()
        notas.pop()
        print("Notas após remover os 2 últimos elementos:", notas)


    def ex9(self, notas):
        if (notas < 60):
            print("A nota é menor que 60")
        elif notas <= 60:
            print("A nota é igual a 60")
        else:
            print("A nota é maior que 60")
           

    def ex10(self):
        lista1 = [1, 3, 5, 7]
        lista2 = [2, 4, 6, 8, 10, 12]
        lista3 = [10, 20, 30]
        lista4 = [11, 22, 33, 44, 55, 66, 77]
        lista5 = [70, 60, 50, 40, 30 ,20, 10, 5, 0]
        print("lista 1")
        for item in lista1:
         print(item)
        print("lista 2")
        for elemento in lista2:
         print(elemento)
        print("lista 3")
        for elemento in lista3:
         print(elemento)
        print("lista 4")
        for elemento in lista4:
         print(elemento)
        print("lista 5")
        for elemento in lista5:
         print(elemento)

ex = exercicio()
ex.ex1()
ex.ex2()
ex.ex3()
ex.ex4()
ex.ex5(64)
ex.ex5(45)
ex.ex5(60)
ex.ex6(90)
ex.ex6(70)
ex.ex6(50)
ex.ex7()
ex.ex8()
notas = [60,55,80,90,59,30]
ex.ex9(notas[0])
ex.ex9(notas[1])
ex.ex9(notas[2])
ex.ex9(notas[3])
ex.ex9(notas[4])
ex.ex9(notas[5])
ex.ex10()