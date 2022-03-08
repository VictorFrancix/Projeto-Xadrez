from tabuleiro import Tabuleiro
from jogo import Jogo, verificar_existencia_arquivo
from time import sleep


def main():
    print('='*29)
    print('Bem-vindo ao Xadrez dos crias')
    print('='*29)
    sleep(2)
    print('''\nA seguir serão ditadas algumas regras e comandos que os jogadores devem saber
para ter a experiência completa do jogo.

O jogo de xadrez consiste em um jogo de tabuleiro disputado entre dois jogadores,  os  quais
tem por objetivo protejer seu próprio rei e tentar ao máximo atacar o do seu adversário. 
Para isso cada jogador dispôe de um exército de peças contendo Cavalos, Torres, Bispos, Peões uma
Dama e o próprio Rei. Cada peça possui um movimento específico e você deve respeitar esses
movimentos. No jogo abaixo, as peças brancas são representadas apenas pelo contorno das peças
e as peças pretas são representadas pelas peças preenchidas completamente.

Para realizar um movimento, o jogador primeiramente deve aguardar a sua vez. Caso o jogo esteja
começando do início quem começa sempre é quem comanda as peças brancas. Após isso, o jogador deve
inserir a Letra da coluna a qual ele quer selecionar sua peça, essa letra deve estar contida no 
intervalo da letra "A" até a letra "H". Depois de inserir a letra, o jogador deve selecionar o 
número correspondente a linha da peça escolhida, esse número deve estar no intervalo de 1 até 8.
Após selecionar um peça, o jogador deve inserir as informações, seguindo o mesmo critério anterior,
para a segunda coordenada. Caso seja do interesse do jogador cancelar a sua jogada soltando um peça,
é necessário que seja inserido na coordenada final a mesma coordenada inserida na coordenada
inicial.

Com o seguimento do jogo, algumas estatísticas são geradas. Caso algum jogador deseje
ver as estatísticas ele deve digitar a palavra "estatisticas" (sem acento) a qualquer momento.

Além do mais, caso seja do interesse de um dos jogadores salvar o estado atual do jogo, apenas será
necessário digitar "salvar" e será solicitado que você escreva o nome que desejar salvar aquele jogo.

Além disso, caso não seja a primeira vez entrando no jogo, e deseje carregar um arquivo salvo,  será 
solicitado o nome de um salvamento existente.
''')
    sleep(2)

    pedir_resposta = True
    while pedir_resposta:
        print('\n(1) - Iniciar Novo Jogo\n(2) - Carregar Jogo')
        resposta = input('\nEscolha o que deseja fazer: ')

        while resposta != '1' and resposta != '2':
            print("\nResposta inválida!")
            resposta = input('Escolha o que deseja fazer: ')

        if resposta == '1':
            jogo = Jogo(True)
            tab = Tabuleiro()
            tab.arrumar_tabuleiro()
            while True:
                if jogo.p_1.vez: # solicitação das coordenadas - jogador 1
                    tab.imprimir_tabuleiro()
                    tab.informar_xeque("b",tab)
                    print('Jogador 1, digite a primeira coordenada.\n')
                    coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                    while jogo.verifica_escolha_peca_inimigo(tab, coord_inicial, jogo.p_1.player):
                        print('\nEeei, você escolheu uma peça do seu adversário. Preste atenção e escolha uma peça sua!!!')
                        coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                    print('Jogador 1, digite a segunda coordenada ou digite a mesma coordenada anterior para soltar a peça.')
                    coord_final = jogo.solicitar_segunda_coordenada(tab)
                    movimentacao = tab.movimentacao_valida(coord_inicial, coord_final, tab)
                    validacao = movimentacao[0]
                    mensagem = movimentacao[1]
                    
                    while not validacao: # validação para ver se o movimento é válido
                        print(f'{mensagem}')
                        tab.imprimir_tabuleiro()
                        print("\nJogador 1, digite a primeira coordenada.")
                        print(' ')
                        coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                        while jogo.verifica_escolha_peca_inimigo(tab, coord_inicial, jogo.p_1.player):
                            print('\nEeei, você escolheu uma peça do seu adversário. Preste atenção e escolha uma peça sua!!!')
                            coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                        print('\nJogador 1, digite a segunda coordenada ou digite a mesma coordenada anterior para soltar a peça.')
                        coord_final = jogo.solicitar_segunda_coordenada(tab)
                        movimentacao = tab.movimentacao_valida(coord_inicial, coord_final, tab)
                        mensagem = movimentacao[1]
                        validacao = movimentacao[0]
                    pecas_capturadas = movimentacao[2]
                    casas_percorridas = movimentacao[3]
                    jogo.p_1.mudar_vez()
                    jogo.p_2.mudar_vez()
                    jogo.p_1.registrar_estatisticas(casas_percorridas, pecas_capturadas)
                    jogo.p_2.registrar_estatisticas(0, 0)
                    if tab.verificar_xequemate('p', tab):
                        break
                else: # solicitação das coordenadas - jogador 2
                    tab.imprimir_tabuleiro()
                    tab.informar_xeque("p",tab)
                    print('Jogador 2, digite a primeira coordenada.\n')
                    coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                    while jogo.verifica_escolha_peca_inimigo(tab, coord_inicial, jogo.p_2.player):
                        print('\nEeei, você escolheu uma peça do seu adversário. Preste atenção e escolha uma peça sua!!!')
                        coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                    print('Jogador 2, digite a segunda coordenada ou digite a mesma coordenada anterior para soltar a peça.')
                    coord_final = jogo.solicitar_segunda_coordenada(tab)
                    movimentacao = tab.movimentacao_valida(coord_inicial, coord_final, tab)
                    validacao = movimentacao[0]
                    mensagem = movimentacao[1]

                    while not validacao: # validação para ver se o movimento é válido
                        print(f'{mensagem}')
                        tab.imprimir_tabuleiro()
                        print("\nJogador 2, digite a primeira coordenada.")
                        print(' ')
                        coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                        while jogo.verifica_escolha_peca_inimigo(tab, coord_inicial, jogo.p_2.player):
                            print('\nEeei, você escolheu uma peça do seu adversário. Preste atenção e escolha uma peça sua!!!')
                            coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                        print('\nJogador 2, digite a segunda coordenada ou digite a mesma coordenada anterior para soltar a peça.')
                        coord_final = jogo.solicitar_segunda_coordenada(tab)
                        movimentacao = tab.movimentacao_valida(coord_inicial, coord_final, tab)
                        mensagem = movimentacao[1]
                        validacao = movimentacao[0]
                        
                    pecas_capturadas = movimentacao[2]
                    casas_percorridas = movimentacao[3]
                    jogo.p_1.mudar_vez()
                    jogo.p_2.mudar_vez()
                    jogo.p_2.registrar_estatisticas(casas_percorridas, pecas_capturadas)
                    jogo.p_1.registrar_estatisticas(0, 0)
                    if tab.verificar_xequemate('b', tab):
                        break
        else:
            print('\nAbaixo digite o nome do arquivo que deseja carregar.')
            nome_arquivo = input('Nome do arquivo: ')
            while not verificar_existencia_arquivo(nome_arquivo):
                print('\nVocê não digitou o nome de um arquivo válido. Abaixo digite novamente o nome do arquivo. Caso deseje iniciar um novo jogo aperte Enter')
                decisao = input('Nome do arquivo: ')
                if decisao == '':
                    pedir_resposta = True
                    break
                nome_arquivo = decisao
            jogo = Jogo(False, nome_arquivo)
            tab = Tabuleiro()
            tab.arrumar_tabuleiro(nome_arquivo, False)
            while True:
                if jogo.p_1.vez: # solicitação das coordenadas - jogador 1
                    tab.imprimir_tabuleiro()
                    tab.informar_xeque("b",tab)
                    print('Jogador 1, digite a primeira coordenada.\n')
                    coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                    while jogo.verifica_escolha_peca_inimigo(tab, coord_inicial, jogo.p_1.player):
                        print('\nEeei, você escolheu uma peça do seu adversário. Preste atenção e escolha uma peça sua!!!')
                        coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                    print('Jogador 1, digite a segunda coordenada ou digite a mesma coordenada anterior para soltar a peça.')
                    coord_final = jogo.solicitar_segunda_coordenada(tab)
                    movimentacao = tab.movimentacao_valida(coord_inicial, coord_final, tab)
                    validacao = movimentacao[0]
                    mensagem = movimentacao[1]

                    while not validacao: # validação para ver se o movimento é válido
                        print(f'{mensagem}')
                        tab.imprimir_tabuleiro()
                        print("\nJogador 1, digite a primeira coordenada.")
                        print(' ')
                        coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                        while jogo.verifica_escolha_peca_inimigo(tab, coord_inicial, jogo.p_1.player):
                            print('\nEeei, você escolheu uma peça do seu adversário. Preste atenção e escolha uma peça sua!!!')
                            coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                        print('\nJogador 1, digite a segunda coordenada ou digite a mesma coordenada anterior para soltar a peça.')
                        coord_final = jogo.solicitar_segunda_coordenada(tab)
                        movimentacao = tab.movimentacao_valida(coord_inicial, coord_final, tab)
                        mensagem = movimentacao[1]
                        validacao = movimentacao[0]
                        
                    pecas_capturadas = movimentacao[2]
                    casas_percorridas = movimentacao[3]
                    jogo.p_1.mudar_vez()
                    jogo.p_2.mudar_vez()
                    jogo.p_1.registrar_estatisticas(casas_percorridas, pecas_capturadas)
                    jogo.p_2.registrar_estatisticas(0, 0)
                    if tab.verificar_xequemate('p', tab):
                        break
                else: # solicitação das coordenadas - jogador 2
                    tab.imprimir_tabuleiro()
                    tab.informar_xeque("p",tab)
                    print('Jogador 2, digite a primeira coordenada.\n')
                    coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                    while jogo.verifica_escolha_peca_inimigo(tab, coord_inicial, jogo.p_2.player):
                        print('\nEeei, você escolheu uma peça do seu adversário. Preste atenção e escolha uma peça sua!!!')
                        coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                    print('Jogador 2, digite a segunda coordenada ou digite a mesma coordenada anterior para soltar a peça.')
                    coord_final = jogo.solicitar_segunda_coordenada(tab)
                    movimentacao = tab.movimentacao_valida(coord_inicial, coord_final, tab)
                    validacao = movimentacao[0]
                    mensagem = movimentacao[1]

                    while not validacao: # validação para ver se o movimento é válido
                        print(f'{mensagem}')
                        tab.imprimir_tabuleiro()
                        print("\nJogador 2, digite a primeira coordenada.")
                        print(' ')
                        coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                        while jogo.verifica_escolha_peca_inimigo(tab, coord_inicial, jogo.p_2.player):
                            print('\nEeei, você escolheu uma peça do seu adversário. Preste atenção e escolha uma peça sua!!!')
                            coord_inicial = jogo.solicitar_primeira_coordenada(tab)
                        print('\nJogador 2, digite a segunda coordenada ou digite a mesma coordenada anterior para soltar a peça.')
                        coord_final = jogo.solicitar_segunda_coordenada(tab)
                        movimentacao = tab.movimentacao_valida(coord_inicial, coord_final, tab)
                        mensagem = movimentacao[1]
                        validacao = movimentacao[0]
                    pecas_capturadas = movimentacao[2]
                    casas_percorridas = movimentacao[3]
                    jogo.p_1.mudar_vez()
                    jogo.p_2.mudar_vez()
                    jogo.p_2.registrar_estatisticas(casas_percorridas, pecas_capturadas)
                    jogo.p_1.registrar_estatisticas(0, 0)
                    if tab.verificar_xequemate('b', tab):
                        break
        break 
    tab.imprimir_tabuleiro()
    vencedor = tab.verificar_vencedor(tab) # vencedor
    print(f'Parabéns, {vencedor}, você foi o campeão!!! A seguir serão mostradas as estatísticas do jogo.')
    jogo.mostrar_estatisticas()
    print("Até a próxima, brabão!")

if __name__ == '__main__':
    main()

