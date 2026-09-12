# Autor: Gabriel Oliveira de Freitas
# Componente Curricular: MI Algoritmos
# Concluído em: 09/09/2024
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação. 

#Loop para definir o valor do problema difícil e garantir que seja um número válido e maior ou igual a 3.
continuar = True #Variável "continuar" como verdadeira, enquanto for verdadeira o código segue.
while continuar:
    D = input('Digite o valor do problema difícil: ').strip() #Variável pedindo o valor do problema difícil para o usuário, com strip() no final para tirar os espaços.
    if D.replace('.', '', 1).isdigit():  #Verifica se a entrada é um número.
        D = float(D) #Converte a dificuldade para float, para permitir que o valor do problema seja decimal.
        if D >= 3: #Verifica se o valor é maior ou igual a 3 (O valor do problema difícil não pode ser menor que 3, senão o valor do problema fácil será menor ou igual a 0).
            break #Se o valor digitado para o problema difícil for um número válido, sai do loop.
        else:
            print('O problema difícil não pode ter valor menor que 3.') #Mensagem de erro para valor inválido.
    else:
        print('Dificuldade inválida.') #Mensagem de erro se a entrada não for um número.

#Repete o processo para as dificuldades média e fácil.
#Loop para definir o valor do problema médio e garantir que ele seja menor que o problema difícil e maior ou igual a 2.
while continuar:
    M = input('Digite o valor do problema médio: ').strip() #Variável pedindo o valor do problema médio para o usuário.
    if M.replace('.', '', 1).isdigit():
        M = float(M)
        if M < D and M >= 2: #O valor do problema médio tem que ser maior que 2, senão o valor do problema fácil sera menor ou igual a 0.
            break
        else:
            print('O valor digitado para um problema médio deve ser maior que 1 e menor que o valor do problema difícil.')
    else:
        print('Dificuldade inválida.')
    
#Loop para definir o valor do problema fácil e garantir que ele seja menor que o problema médio e maior ou igual a 1.
while continuar:
    F = input('Digite o valor do problema fácil: ').strip() #Variável pedindo o valor do problema fácil para o usuário.
    if F.replace('.', '', 1).isdigit():
        F = float(F)
        if F < M and F >= 1:
            break
        else:
            print('O valor digitado para um problema fácil deve ser maior que 0 e menor que o valor do problema médio.')
    else:
        print('Dificuldade inválida.')
print('-'*100) #Linha decorativa para a interface.

e1 = str(input('Digite o nome da primeira equipe: ')).strip() #Variável para pedir o nome da primeira equipe.
while e1 == '': #Loop para garantir que o nome da equipe não seja vazio.
    print('Nome inválido, digite novamente.') #Mensagem de erro.
    e1 = str(input('Digite o nome da primeira equipe: ')).strip()
e2 = str(input('Digite o nome da segunda equipe: ')).strip() #Variável para pedir o nome da segunda equipe.
while e2 == '' or e2 == e1: #Loop para garantir que o nome da equipe não seja vazio nem seja igual o de outra equipe.
    print('Nome inválido, digite novamente.')
    e2 = str(input('Digite o nome da segunda equipe: ')).strip() 
#Repete o processo para as equipes 3, 4 e 5.
e3 = str(input('Digite o nome da terceira equipe: ')).strip() #Variável para pedir o nome da terceira equipe.
while e3 == '' or e3 == e1 or e3 == e2:
    print('Nome inválido, digite novamente.')
    e3 = str(input('Digite o nome da terceira equipe: ')).strip()
e4 = str(input('Digite o nome da quarta equipe: ')).strip() #Variável para pedir o nome da quarta equipe.
while e4 == '' or e4 == e1 or e4 == e2 or e4 == e3:
    print('Nome inválido, digite novamente.')
    e4 = str(input('Digite o nome da quarta equipe: ')).strip()
e5 = str(input('Digite o nome da quinta equipe: ')).strip() #Variável para pedir o nome da quinta equipe.
while e5 == '' or e5 == e1 or e5 == e2 or e5 == e3 or e5 == e4:
    print('Nome inválido, digite novamente.')
    e5 = str(input('Digite o nome da quinta equipe: ')).strip()

#Inicializa as variáveis para pontuações, tempos, contadores de dificuldades para cada equipe e contador de questões (problemas) resolvidos.
pe1 = pe2 = pe3 = pe4 = pe5 = 0 #Pontuação de cada equipe.
te1 = te2 = te3 = te4 = te5 = 0 #Tempo de cada equipe.
contadorD1 = contadorD2 = contadorD3 = contadorD4 = contadorD5 = 0 #Contador de difíceis de cada equipe.
contadorM1 = contadorM2 = contadorM3 = contadorM4 = contadorM5 = 0 #Contador de médias de cada equipe.
contadorF1 = contadorF2 = contadorF3 = contadorF4 = contadorF5 = 0 #Contador de fáceis de cada equipe.
contadorq1 = contadorq2 = contadorq3 = contadorq4 = contadorq5 = 0 #Contador de questões de cada equipe.
#Inicializa a variável "escolha" com o valor '1'.
escolha = '1'

#Loop que continua executando enquanto a escolha for '1'.
while escolha == '1':
    print('-'*100)
    #Variável para pedir ao usuário que escolha uma opção.
    escolha = input('Digite o que deseja fazer:\n(1) Registrar pontuação para uma equipe.\n(2) Mostrar Ranking.\n(3) Finalizar maratona.\n').strip()
    #Verifica se a escolha é válida (1, 2 ou 3).
    while escolha != '1' and escolha != '2' and escolha != '3':
        print('Escolha inválida.')
        escolha = input('Digite o que deseja fazer:\n(1) Registrar pontuação para uma equipe.\n(2) Mostrar Ranking.\n(3) Finalizar maratona.\n').strip()
    #Se a escolha for '1', o código registra o problema resolvido pela equipe desejada.
    if escolha == '1':
        registro = input('Digite a equipe que você deseja registrar: ').strip() #Variável para pedir ao usuário a equipe que ele deseja registrar.
        #Verifica se a equipe digitada é válida.
        while registro != e1 and registro != e2 and registro != e3 and registro != e4 and registro != e5:
            print('Essa equipe não está na competição.')
            registro = input('Digite a equipe que você deseja registrar: ').strip()
        #Se a equipe for válida, pede a dificuldade da questão.
        if registro == e1: #Registra a dificuldade escolhida pela equipe 1.
            dificuldade = input('Digite a dificuldade escolhida pela equipe:\n(1) Difícil\n(2) Média\n(3) Fácil\n').strip()
            while dificuldade != '1' and dificuldade != '2' and dificuldade != '3': #Verifica se a dificuldade digitada é válida.
                print('Dificuldade inválida.')
                dificuldade = input('Digite a dificuldade escolhida pela equipe:\n(1) Difícil\n(2) Média\n(3) Fácil\n').strip()
            #Abaixo, as condições para cada dificuldade, o contador de problemas de cada dificuldade e o somatório de pontos para a equipe.
            if dificuldade == '1':
                pe1 += D
                contadorD1 += 1
            elif dificuldade == '2':
                pe1 += M
                contadorM1 += 1
            elif dificuldade == '3':
                pe1 += F
                contadorF1 += 1
            contadorq1 +=1 #Atualiza o contador de problemas feitos.
            #Loop para pedir o tempo necessário para a realização da questão e garantir que um número inteiro seja digitado.
            while continuar:
                tempo = input('Digite o tempo necessário para a realização da questão em segundos: ').strip()
                if tempo.isdigit(): #Verifica se o tempo digitado é um número.
                    tempo = int(tempo) #Converte o tempo em inteiro, já que é pedido em segundos.
                    break #Se o valor digitado para o tempo for um número inteiro, sai do loop.
                else:
                    print('Tempo inválido.') #Mensagem de erro para o tempo.
            #Soma o tempo gasto pela equipe.
            te1 += tempo
        #Repete o processo para as equipes e2, e3, e4 e e5.
        elif registro == e2:
            dificuldade = input('Digite a dificuldade escolhida pela equipe:\n(1) Difícil\n(2) Média\n(3) Fácil\n').strip()
            while dificuldade != '1' and dificuldade != '2' and dificuldade != '3':
                print('Dificuldade inválida.')
                dificuldade = input('Digite a dificuldade escolhida pela equipe:\n(1) Difícil\n(2) Média\n(3) Fácil\n').strip()
            if dificuldade == '1':
                pe2 += D
                contadorD2 += 1
            elif dificuldade == '2':
                pe2 += M
                contadorM2 += 1
            elif dificuldade == '3':
                pe2 += F
                contadorF2 += 1
            contadorq2 +=1
            while continuar:
                tempo = input('Digite o tempo necessário para a realização da questão em segundos: ').strip()
                if tempo.isdigit():
                    tempo = int(tempo)
                    break
                else:
                    print('Tempo inválido.')
            te2 += tempo
        elif registro == e3:
            dificuldade = input('Digite a dificuldade escolhida pela equipe:\n(1) Difícil\n(2) Média\n(3) Fácil\n').strip()
            while dificuldade != '1' and dificuldade != '2' and dificuldade != '3':
                print('Dificuldade inválida.')
                dificuldade = input('Digite a dificuldade escolhida pela equipe:\n(1) Difícil\n(2) Média\n(3) Fácil\n').strip()
            if dificuldade == '1':
                pe3 += D
                contadorD3 += 1
            elif dificuldade == '2':
                pe3 += M
                contadorM3 += 1
            elif dificuldade == '3':
                pe3 += F
                contadorF3 += 1
            contadorq3 +=1
            while continuar:
                tempo = input('Digite o tempo necessário para a realização da questão em segundos: ').strip()
                if tempo.isdigit():
                    tempo = int(tempo)
                    break
                else:
                    print('Tempo inválido.')
            te3 += tempo
        elif registro == e4:
            dificuldade = input('Digite a dificuldade escolhida pela equipe:\n(1) Difícil\n(2) Média\n(3) Fácil\n').strip()
            while dificuldade != '1' and dificuldade != '2' and dificuldade != '3':
                print('Dificuldade inválida.')
                dificuldade = input('Digite a dificuldade escolhida pela equipe:\n(1) Difícil\n(2) Média\n(3) Fácil\n').strip()
            if dificuldade == '1':
                pe4 += D
                contadorD4 += 1
            elif dificuldade == '2':
                pe4 += M
                contadorM4 += 1
            elif dificuldade == '3':
                pe4 += F
                contadorF4 += 1
            contadorq4 += 1
            while continuar:
                tempo = input('Digite o tempo necessário para a realização da questão em segundos: ').strip()
                if tempo.isdigit():
                    tempo = int(tempo)
                    break
                else:
                    print('Tempo inválido.')
            te4 += tempo
        elif registro == e5:
            dificuldade = input('Digite a dificuldade escolhida pela equipe:\n(1) Difícil\n(2) Média\n(3) Fácil\n').strip()
            while dificuldade != '1' and dificuldade != '2' and dificuldade != '3':
                print('Dificuldade inválida.')
                dificuldade = input('Digite a dificuldade escolhida pela equipe:\n(1) Difícil\n(2) Média\n(3) Fácil\n').strip()
            if dificuldade == '1':
                pe5 += D
                contadorD5 += 1
            elif dificuldade == '2':
                pe5 += M
                contadorM5 += 1
            elif dificuldade == '3':
                pe5 += F
                contadorF5 += 1
            contadorq5 += 1
            while continuar:
                tempo = input('Digite o tempo necessário para a realização da questão em segundos: ').strip()
                if tempo.isdigit():
                    tempo = int(tempo)
                    break
                else:
                    print('Tempo inválido.')
            te5 += tempo

    #Se a escolha for '2', mostra o ranking das equipes.
    elif escolha == '2':
        #Atribui outras variáveis para o nome da equipe, pontuação, dificuldade e tempo, respectivamente,
        #para serem utilizadas exclusivamente no ranking sem dar conflito no resto do código.
        eq1, pont1, dif1, tempo1 = e1, pe1, contadorD1, te1
        eq2, pont2, dif2, tempo2 = e2, pe2, contadorD2, te2
        eq3, pont3, dif3, tempo3 = e3, pe3, contadorD3, te3
        eq4, pont4, dif4, tempo4 = e4, pe4, contadorD4, te4
        eq5, pont5, dif5, tempo5 = e5, pe5, contadorD5, te5
        #Ordena as equipes com base na pontuação, questões difíceis resolvidas e tempo.
        #No print do ranking, a variável tomada como base pra ser a primeira é a do eq1, a segunda é a  do eq2 e assim sucessivamente,
        #o mesmo acontece com a pontuação, as questões difíceis resolvidas e o tempo gasto, portanto, as trocas desse loop são baseadas nisso.
        for ranking in range(5): #Loop para ordenar as equipes com base na pontuação, dificuldade e tempo.
            #Comparação entre equipe 2 e equipe 1.
            if pont2 > pont1 or pont2 == pont1 and dif2 > dif1 or pont2 == pont1 and dif2 == dif1 and tempo2 < tempo1:
                #Troca de posições se a equipe 2 for melhor que a equipe 1. (Troca de variáveis).
                eq1, eq2 = eq2, eq1
                pont1, pont2 = pont2, pont1
                dif1, dif2 = dif2, dif1
                tempo1, tempo2 = tempo2, tempo1
            #Comparação entre equipe 3 e equipe 2.
            if pont3 > pont2 or pont3 == pont2 and dif3 > dif2 or pont3 == pont2 and dif3 == dif2 and tempo3 < tempo2:
                #Troca de posições se a equipe 3 for melhor que a equipe 2.
                eq2, eq3 = eq3, eq2
                pont2, pont3 = pont3, pont2
                dif2, dif3 = dif3, dif2
                tempo2, tempo3 = tempo3, tempo2
             #Comparação entre equipe 4 e equipe 3.
            if pont4 > pont3 or pont4 == pont3 and dif4 > dif3 or pont4 == pont3 and dif4 == dif3 and tempo4 < tempo3:
                #Troca de posições se a equipe 4 for melhor que a equipe 3.
                eq3, eq4 = eq4, eq3
                pont3, pont4 = pont4, pont3
                dif3, dif4 = dif4, dif3
                tempo3, tempo4 = tempo4, tempo3
            #Comparação entre equipe 5 e equipe 4.
            if pont5 > pont4 or pont5 == pont4 and dif5 > dif4 or pont5 == pont4 and dif5 == dif4 and tempo5 < tempo4:
                #Troca de posições se a equipe 5 for melhor que a equipe 4.
                eq4, eq5 = eq5, eq4
                pont4, pont5 = pont5, pont4
                dif4, dif5 = dif5, dif4
                tempo4, tempo5 = tempo5, tempo4
        #Mostra o ranking das equipes.
        print('-'*100)
        print(f'1° lugar: equipe {eq1} | {pont1}pts | difíceis: {dif1} | {tempo1}seg')
        print(f'2° lugar: equipe {eq2} | {pont2}pts | difíceis: {dif2} | {tempo2}seg')
        print(f'3° lugar: equipe {eq3} | {pont3}pts | difíceis: {dif3} | {tempo3}seg')
        print(f'4° lugar: equipe {eq4} | {pont4}pts | difíceis: {dif4} | {tempo4}seg')
        print(f'5° lugar: equipe {eq5} | {pont5}pts | difíceis: {dif5} | {tempo5}seg')
        #Após mostrar o ranking, volta para o menu principal.
        escolha = '1'

    #Se a escolha for '3', encerra o programa com break.
    elif escolha == '3':
        break
print('-'*100)

#Aqui se repete o mesmo processo realizado anteriormente, mas somente para mostrar o ranking final.
eq1, pont1, dif1, tempo1 = e1, pe1, contadorD1, te1
eq2, pont2, dif2, tempo2 = e2, pe2, contadorD2, te2
eq3, pont3, dif3, tempo3 = e3, pe3, contadorD3, te3
eq4, pont4, dif4, tempo4 = e4, pe4, contadorD4, te4
eq5, pont5, dif5, tempo5 = e5, pe5, contadorD5, te5
for ranking in range(5):
    if pont2 > pont1 or pont2 == pont1 and dif2 > dif1 or pont2 == pont1 and dif2 == dif1 and tempo2 < tempo1:
        eq1, eq2 = eq2, eq1
        pont1, pont2 = pont2, pont1
        dif1, dif2 = dif2, dif1
        tempo1, tempo2 = tempo2, tempo1
    if pont3 > pont2 or pont3 == pont2 and dif3 > dif2 or pont3 == pont2 and dif3 == dif2 and tempo3 < tempo2:
        eq2, eq3 = eq3, eq2
        pont2, pont3 = pont3, pont2
        dif2, dif3 = dif3, dif2
        tempo2, tempo3 = tempo3, tempo2
    if pont4 > pont3 or pont4 == pont3 and dif4 > dif3 or pont4 == pont3 and dif4 == dif3 and tempo4 < tempo3:
        eq3, eq4 = eq4, eq3
        pont3, pont4 = pont4, pont3
        dif3, dif4 = dif4, dif3
        tempo3, tempo4 = tempo4, tempo3
    if pont5 > pont4 or pont5 == pont4 and dif5 > dif4 or pont5 == pont4 and dif5 == dif4 and tempo5 < tempo4:
        eq4, eq5 = eq5, eq4
        pont4, pont5 = pont5, pont4
        dif4, dif5 = dif5, dif4
        tempo4, tempo5 = tempo5, tempo4

#Mostra o ranking final das equipes após ordenação.
print(f'1° lugar: equipe {eq1} | {pont1}pts | difíceis: {dif1} | {tempo1}seg')
print(f'2° lugar: equipe {eq2} | {pont2}pts | difíceis: {dif2} | {tempo2}seg')
print(f'3° lugar: equipe {eq3} | {pont3}pts | difíceis: {dif3} | {tempo3}seg')
print(f'4° lugar: equipe {eq4} | {pont4}pts | difíceis: {dif4} | {tempo4}seg')
print(f'5° lugar: equipe {eq5} | {pont5}pts | difíceis: {dif5} | {tempo5}seg')
print('-'*100)

#Mostra a quantidade de questões resolvidas no total e por dificuldade para cada equipe.
print(f'{e1} - {contadorD1+contadorM1+contadorF1} total; {contadorD1} difíceis; {contadorM1} médias; {contadorF1} fáceis.')
print(f'{e2} - {contadorD2+contadorM2+contadorF2} total; {contadorD2} difíceis; {contadorM2} médias; {contadorF2} fáceis.')
print(f'{e3} - {contadorD3+contadorM3+contadorF3} total; {contadorD3} difíceis; {contadorM3} médias; {contadorF3} fáceis.')
print(f'{e4} - {contadorD4+contadorM4+contadorF4} total; {contadorD4} difíceis; {contadorM4} médias; {contadorF4} fáceis.')
print(f'{e5} - {contadorD5+contadorM5+contadorF5} total; {contadorD5} difíceis; {contadorM5} médias; {contadorF5} fáceis.')
print('-'*100)

#Mostra a equipe vencedora e sua pontuação.
print(f'A equipe vencedora foi a equipe {eq1}, com {pont1} pontos.')
print('-'*100)

equipe_maisdificeis = e1 #Variável para a equipe ou as equipes com o maior número de questões difíceis resolvidas.
contador_maisdificeis = contadorD1 #Variável para o contador de quem fez mais difíceis.
numero_equipes = 1 #Variável para ver se mais de uma equipe resolveu a maior quantidade de problemas difíceis.

#Compara a quantidade de questões difíceis resolvidas pelas equipes.
if contadorD2 > contador_maisdificeis:
    contador_maisdificeis = contadorD2
    equipe_maisdificeis = e2
    numero_equipes = 1
elif contadorD2 == contador_maisdificeis:
    equipe_maisdificeis = (f'{equipe_maisdificeis}, {e2}') #A equipe que empatou em questões difíceis é adicionada a variável "equipe_maisdificeis"
    numero_equipes += 1 #Soma 1 para a váriavel "numero_equipes" se mais de uma equipe resolveu a maior quantidade de problemas difíceis.
if contadorD3 > contador_maisdificeis:
    contador_maisdificeis = contadorD3
    equipe_maisdificeis = e3
    numero_equipes = 1
elif contadorD3 == contador_maisdificeis:
    equipe_maisdificeis = (f'{equipe_maisdificeis}, {e3}')
    numero_equipes += 1
if contadorD4 > contador_maisdificeis:
    contador_maisdificeis = contadorD4
    equipe_maisdificeis = e4
    numero_equipes = 1
elif contadorD4 == contador_maisdificeis:
    equipe_maisdificeis = (f'{equipe_maisdificeis}, {e4}')
    numero_equipes += 1
if contadorD5 > contador_maisdificeis:
    contador_maisdificeis = contadorD5
    equipe_maisdificeis = e5
    numero_equipes = 1
elif contadorD5 == contador_maisdificeis:
    equipe_maisdificeis = (f'{equipe_maisdificeis}, {e5}')
    numero_equipes += 1

#Mostra a equipe ou as equipes que resolveram mais questões difíceis.
if numero_equipes > 1: #Analisa se o número de equipes que resolveu a maior quantidade de questões difíceis é maior que 1.
    print(f'As equipes que fizeram mais questões difíceis foram as equipes {equipe_maisdificeis}, com {contador_maisdificeis} cada.')
else:
    print(f'A equipe que mais fez questões difíceis foi a equipe {equipe_maisdificeis}, com {contador_maisdificeis}.')
print('-'*100)

#Calcula e mostra a média de pontos por questão de cada equipe.
if contadorq1 != 0: #Condição para quando o contador de problemas é diferente de 0.
    print(f'Média de pontos, equipe {e1}: {pe1/contadorq1:.1f} pontos por questão.')
else: #Condição para que se o contador de problemas for 0, não ocorrer divisão e dar erro, apenas aparece o "0.0".
    print(f'Média de pontos, equipe {e1}: 0.0 pontos por questão.')
if contadorq2 != 0:
    print(f'Média de pontos, equipe {e2}: {pe2/contadorq2:.1f} pontos por questão.')
else:
    print(f'Média de pontos, equipe {e2}: 0.0 pontos por questão.')
if contadorq3 != 0:
    print(f'Média de pontos, equipe {e3}: {pe3/contadorq3:.1f} pontos por questão.')
else:
    print(f'Média de pontos, equipe {e3}: 0.0 pontos por questão.')
if contadorq4 != 0:
    print(f'Média de pontos, equipe {e4}: {pe4/contadorq4:.1f} pontos por questão.')
else:
    print(f'Média de pontos, equipe {e4}: 0.0 pontos por questão.')
if contadorq5 != 0:
    print(f'Média de pontos, equipe {e5}: {pe5/contadorq5:.1f} pontos por questão.')
else:
    print(f'Média de pontos, equipe {e5}: 0.0 pontos por questão.')
print('-'*100)

#Calcula e mostra a média geral de pontos por questão de todas as equipes juntas.
pontuacaogeral = pe1 + pe2 + pe3 + pe4 + pe5 #Variável para somar a pontuação de todas as equipes.
questoesgeral = contadorq1 + contadorq2 + contadorq3 + contadorq4 + contadorq5 #Variável para somar a quantidade de problemas resolvidos por todas as equipes.
if questoesgeral != 0:
    print(f'A média de pontos da competição foi de {pontuacaogeral/questoesgeral:.1f} pontos por questão.')
else:
    print(f'A média de pontos da competição foi de 0.0 pontos por questão.')
print('-'*100)

#Mostra o tempo total gasto pela equipe vencedora.
print(f'O tempo total gasto pela equipe vencedora, {eq1}, foi de {tempo1} segundos.')
