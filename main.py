import random

condicao = 0

while condicao == 0:
    i = random.randrange(0, 3)

    print('Jogo do Pedra, Papel ou Tesoura')

    jogada = input('Selecione sua jogada abaixo:\n[1]Pedra\n[2]Papel\n[3]Tesoura\n')

    if jogada.isnumeric():
        jogada = int(jogada)
    else:
        print('Por favor, selecione uma das opções informadas.\n')
        continue

    if jogada >= 1 and jogada <= 3:
        print('JO...')
        print('KEN...')
        print('PÔ!')

        #Se a jogada for pedra, testa as condições abaixo
        if jogada == 1:
            print(f'Você jogou "Pedra".')
            if i == 0:
                condicao = int(input('A Maquina jogou "Pedra", foi um empate.\nDeseja jogar novamente?\n[0]Sim\n[1]Não\n'))
                if condicao == 1:
                    condicao += 1
                    break
                else:
                    continue
            if i == 1:
                condicao = int(input('A Maquina jogou "Papel", você perdeu!\nDeseja jogar novamente?\n[0]Sim\n[1]Não\n'))
                if condicao == 1:
                    condicao += 1
                    break
                else:
                    continue
            else:
                condicao = int(input('A Maquina jogou "Tesoura", você ganhou!\nDeseja jogar novamente?\n[0]Sim\n[1]Não\n'))
                if condicao == 1:
                    condicao += 1
                    break
                else:
                    continue

        #Se a jogada for Papel, testa as condições abaixo
        if jogada == 2:
            print(f'Você jogou "Papel".')
            if i == 0:
                condicao = int(input('A Maquina jogou "Pedra", Você ganhou!\nDeseja jogar novamente?\n[0]Sim\n[1]Não\n'))
                if condicao == 1:
                    condicao += 1
                    break
                else:
                    continue
            if i == 1:
                condicao = int(input('A Maquina jogou "Papel", foi um empate.\nDeseja jogar novamente?\n[0]Sim\n[1]Não\n'))
                if condicao == 1:
                    condicao += 1
                    break
                else:
                    continue
            else:
                condicao = int(input('A Maquina jogou "Tesoura", você perdeu :(\n Deseja jogar novamente?\n[0]Sim\n[1]Não\n'))
                if condicao == 1:
                    condicao += 1
                    break
                else:
                    continue

        #Se a jogada for Papel, testa as condições abaixo
        if jogada == 3:
            print(f'Você jogou "Tesoura".')
            if i == 0:
                condicao = int(input('A Maquina jogou "Pedra", Você perdeu :(\nDeseja jogar novamente?\n[0]Sim\n[1]Não\n'))
                if condicao == 1:
                    condicao += 1
                    break
                else:
                    continue
            if i == 1:
                condicao = int(input('A Maquina jogou "Papel", você Ganhou!\nDeseja jogar novamente?\n[0]Sim\n[1]Não\n'))
                if condicao == 1:
                    condicao += 1
                    break
                else:
                    continue
            else:
                condicao = int(input('A Maquina jogou "Tesoura", foi um empate.\n Deseja jogar novamente?\n[0]Sim\n[1]Não\n'))
                if condicao == 1:
                    condicao += 1
                    break
                else:
                    continue
    else:
        print('Selecione um dos valores informados.')
        continue
print("Fim de jogo.")




