import matplotlib.pyplot as plt

# Neste arquivo estão contidos as mais novas classes adicionadas ao nosso jogo de Xadrez. 

# A primeira classe se chama "Player", ela será a responsável por fazer a separação   de
# informações de jogador a jogador durante o jogo. Através desse método será possível   
# registrar estatísticas específicas de cada jogador, além de ser possível verificar de quem
# é a vez durante o jogo.

# O método construtor da classe Player recebe dois argumentos obrigatórios e um Default. Os 
# parãmetros obrigatórios são 'player', o qual será um rótulo para o jogador, e 'inicio', o
# qual será responsável por ditar se é o início do jogo ou não. A depender deste parâmetro, 
# os valores que serão inderessados a cada variável, pode mudar, pois se não for o início do
# jogo, serão captados valores de um arquivo txt salvo.


class Player:
    def __init__(self, player, inicio, nome_arquivo=''):
        if inicio:
            self.player = player
            self.casas_percorridas = []
            self.pecas_capturadas = []
            if player == 'player1':
                self.vez = True
            else:
                self.vez = False
        else:
            self.player = player
            arquivo = open(nome_arquivo + f'_estatisticas_{self.player}.txt', 'r',encoding="utf-8")
            dados = arquivo.readlines()
            lista_stats = []
            for linha in dados:
                nova_linha = linha.split(',')
                lista_stats.append(nova_linha)

            self.casas_percorridas = [int(i) for i in lista_stats[0][:-1]]
            self.pecas_capturadas = lista_stats[1][:-1]
            self.vez = bool(int(lista_stats[2][0]))

            arquivo.close()

    def registrar_estatisticas(self, n_casas, peca_capturada):
        '''Método que recebe dois valores inteiros representando o número de casas percorridas e o número 
        de peças capturas em uma dada jogada, e as registra em uma lista.
        int, int -> None'''
        self.casas_percorridas.append(n_casas)
        self.pecas_capturadas.append(peca_capturada)

    def mudar_vez(self):
        '''Método que altera a vez do jogador
        None -> None'''
        self.vez = not self.vez



# A segunda mais nova classe do trabalho é a classe jogo, que é a responsável por gerenciar as relações com
# os jogadores, além de registrar salvamento de estatísticas e mais. Ao longo de cada método será abordado sua 
# devida funcionalidade.


class Jogo:
    def __init__(self, inicio, nome_arquivo=''):
        if inicio:
            self.p_1 = Player('player1', inicio)
            self.p_2 = Player('player2', inicio)
        else:
            self.p_1 = Player('player1', inicio, nome_arquivo)
            self.p_2 = Player('player2', inicio, nome_arquivo)

    def transformar_letra(self):
        '''Método que solicita uma letra da coordenada de uma posição do tabuleiro e a converte
        para um número de 0 a 7, caso seja uma letra, ou retorna uma das palavras chaves para o
        jogo ("estatisticas" e "salvar").
        None -> int ou str'''
        letra = input('Digite a coluna (A-H): ').upper()
        dicionario_letras = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
                            "G": 6, "H": 7, "SALVAR": 'salvar', "ESTATISTICAS": 'estatisticas'}
        while True:
            try:
                numero = dicionario_letras[letra]
                return numero

            except KeyError:
                print('Você não inseriu uma coordenada válida')
                letra = input('Digite a coluna (A-H): ')
                letra = letra.upper()

    def verificar_numero(self):
        '''Método que solicita um número de uma coordenada de uma posição do tabuleiro e o converte
        para um número do tipo inteiro, ou retorna uma das palavras chaves para o jogo ("estatisticas"
        e "salvar"), caso sejam inseridas essas palavras.'''
        numero = input('Digite a linha (1-8): ').upper()
        dicionario_numeros = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5,
                            "7": 6, "8": 7, "SALVAR": 'salvar', 'ESTATISTICAS': 'estatisticas'}
        while True:
            try:
                numero = dicionario_numeros[numero]
                return numero

            except KeyError:
                print('Você não inseriu uma coordenada válida')
                numero = input('Digite a linha (1-8): ')

    def verificar_salvamento(self, resposta):
        '''Método que recebe uma palavra e verifica se ela é um pedido de salvamento.
        str -> bool'''
        return resposta == 'salvar'

    def verificar_estatisticas(self, resposta):
        '''Método que recebe uma palavra e verifica se ela é um pedido para ver as estatísticas
        str -> bool'''
        return resposta == 'estatisticas'

    def solicitar_nome_arquivo(self):
        '''Método que pergunta ao usuário o nome que ele deseja salvar seu jogo
        None -> str'''
        nome_arquivo = input('\nComo deseja salvar o jogo? ')
        return nome_arquivo

    def salvar_estatisticas(self, nome, player):
        '''Método que recebe duas strings, um que será o nome de um arquivo de salvamento e o outro que 
        indicará a qual player serão salvas as estatísticas.
        str, str -> None'''
        dicionario_players = {'player1': self.p_1, 'player2': self.p_2}
        dicionario_vez = {True: 1, False: 0}

        nome_formatado = nome + '_estatisticas' + f'_{player}'
        save = open(f'{nome_formatado}.txt', 'w', encoding="utf-8")
        for i in dicionario_players[player].casas_percorridas:
            save.write(f"{i},")
        save.write('\n')

        for i in dicionario_players[player].pecas_capturadas:
            save.write(f"{i},")
        save.write('\n')

        vez = dicionario_players[player]
        vez_codificada = dicionario_vez[vez.vez]
        save.write(f'{vez_codificada}')
        save.close()

    def mostrar_casas_percorridas(self):
        '''Método que plota o gráfico do número de casas percorridas por jogada.
        None -> None'''
        rodadas = list(range(1, len(self.p_1.casas_percorridas) + 1))

        plt.title("Número de Casas Percorridas por Rodada")
        plt.xlabel("Rodadas")
        plt.ylabel("Nº de Casas")

        plt.plot(rodadas, self.p_1.casas_percorridas, 'or-', label='Player 1')
        plt.plot(rodadas, self.p_2.casas_percorridas, 'ob--', label='Player 2')

        plt.xticks([i for i in range(1, len(self.p_1.casas_percorridas) + 1)])
        plt.yticks([i for i in range(1, max([max(self.p_1.casas_percorridas), max(self.p_2.casas_percorridas)]) + 1)])
        plt.legend()

        plt.show()

    def mostrar_historico_capturas(self):
        '''Método que plota o gráfico do número de peças capturadas por jogada.
        None -> None'''
        rodadas = list(range(1, len(self.p_1.pecas_capturadas) + 1))

        plt.title("Captura de Peças por Rodada")
        plt.xlabel("Rodadas")
        plt.ylabel("Nº de peças capturadas")

        plt.plot(rodadas, self.p_1.pecas_capturadas, 'or', label='Player 1')
        plt.plot(rodadas, self.p_2.pecas_capturadas, 'ob', label='Player 2')

        plt.xticks([i for i in range(1, len(self.p_1.casas_percorridas) + 1)])

        plt.legend()

        plt.show()

    def mostrar_estatisticas(self):
        '''Método mostrar simultaneamente os gráficos das peças capturadas e do número de casas
        percorridas.
        None -> None'''
        self.mostrar_casas_percorridas()
        self.mostrar_historico_capturas()

    # Apesar dos métodos solicitar_primeira_coordenada e solicitar_segunda coordenada aparentarem ser bem
    # semelhantes, eles são trabalhados de forma distinta, pois para o método solicitar_primeira_coordenada,
    # faz-se necessário que obrigatóriamente o usuário escolha uma casa com peça para dar seguimento ao jogo
    # enquanto que para a segunda coordenada, essa necessidade não é obrigatória.


    def solicitar_primeira_coordenada(self, tab):
        '''Método que recebe um objeto da classe Tabuleiro, solicita separadamente a letra e o número
        da primera coordenada do tabuleiro, e a depender da resposta dela pode salvar o jogo, pode mostrar 
        as estatísticas ou caso não seja solicitado nenhum dos dois, retorna a coordenada inserida já 
        formatada para o manuseio no tabuleiro
        Tabuleiro -> (tuple)'''
        y_inicial = self.transformar_letra()
        while self.verificar_salvamento(y_inicial):
            nome_salvamento = self.solicitar_nome_arquivo()
            tab.salvar_tabuleiro(nome_salvamento)
            self.salvar_estatisticas(nome_salvamento, self.p_1.player)
            self.salvar_estatisticas(nome_salvamento, self.p_2.player)
            y_inicial = self.transformar_letra()
        while self.verificar_estatisticas(y_inicial):
            self.mostrar_estatisticas()
            y_inicial = self.transformar_letra()
        x_inicial = self.verificar_numero()
        while self.verificar_salvamento(x_inicial):
            nome_salvamento = self.solicitar_nome_arquivo()
            tab.salvar_tabuleiro(nome_salvamento)
            self.salvar_estatisticas(nome_salvamento, self.p_1.player)
            self.salvar_estatisticas(nome_salvamento, self.p_2.player)
            x_inicial = self.transformar_letra()
        while self.verificar_estatisticas(x_inicial):
            self.mostrar_estatisticas()
            x_inicial = self.transformar_letra()
        coord_inicial = (x_inicial, y_inicial)
        print(' ')

        tem_peca = tab.verificar_posicao(coord_inicial)

        while not tem_peca:
            print('Você não escolheu uma peça')
            y_inicial = self.transformar_letra()
            while self.verificar_salvamento(y_inicial):
                nome_salvamento = self.solicitar_nome_arquivo()
                tab.salvar_tabuleiro(nome_salvamento)
                self.salvar_estatisticas(nome_salvamento, self.p_1.player)
                self.salvar_estatisticas(nome_salvamento, self.p_2.player)
                y_inicial = self.transformar_letra()
            while self.verificar_estatisticas(y_inicial):
                self.mostrar_estatisticas()
                y_inicial = self.transformar_letra()
            x_inicial = self.verificar_numero()
            while self.verificar_salvamento(x_inicial):
                nome_salvamento = self.solicitar_nome_arquivo()
                tab.salvar_tabuleiro(nome_salvamento)
                self.salvar_estatisticas(nome_salvamento, self.p_1.player)
                self.salvar_estatisticas(nome_salvamento, self.p_2.player)
                x_inicial = self.transformar_letra()
            while self.verificar_estatisticas(x_inicial):
                self.mostrar_estatisticas()
                x_inicial = self.transformar_letra()
            coord_inicial = (x_inicial, y_inicial)
            tem_peca = tab.verificar_posicao(coord_inicial)
            print(' ')
        return coord_inicial

    def solicitar_segunda_coordenada(self, tab):
        '''Método que recebe um objeto da classe Tabuleiro, solicita separadamente a letra e o número
        da segunda coordenada do tabuleiro, e a depender da resposta dela pode salvar o jogo, pode mostrar 
        as estatísticas ou caso não seja solicitado nenhum dos dois, retorna a coordenada inserida já 
        formatada para o manuseio no tabuleiro
        Tabuleiro -> (tuple)'''
        y_final = self.transformar_letra()
        while self.verificar_salvamento(y_final):
            nome_salvamento = self.solicitar_nome_arquivo()
            tab.salvar_tabuleiro(nome_salvamento)
            self.salvar_estatisticas(nome_salvamento, self.p_1.player)
            self.salvar_estatisticas(nome_salvamento, self.p_2.player)
            y_final = self.transformar_letra()
        while self.verificar_estatisticas(y_final):
            self.mostrar_estatisticas()
            y_final = self.transformar_letra()
        x_final = self.verificar_numero()
        while self.verificar_salvamento(x_final):
            nome_salvamento = self.solicitar_nome_arquivo()
            tab.salvar_tabuleiro(nome_salvamento)
            self.salvar_estatisticas(nome_salvamento, self.p_1.player)
            self.salvar_estatisticas(nome_salvamento, self.p_2.player)
            x_final = self.transformar_letra()
        while self.verificar_estatisticas(x_final):
            self.mostrar_estatisticas()
            x_final = self.transformar_letra()
        coord_final = (x_final, y_final)
        return coord_final

    def verifica_escolha_peca_inimigo(self, tab, coord, player):
        '''Método que avalia se um jogador escolheu uma peça que não o pertence. Como entrada, esse 
        método recebe um objeto da classe Tabuleiro, a coordenada de uma peça escolhida e o rótulo 
        do jogador que está tentando selecionar esta peça. O método retorna True, se a peça for do 
        jogador que está tentando selecioná-la e False, caso não seja.
        Tabuleiro, (tuple), str -> bool'''
        dicionario_cor = {'player1': 'b', 'player2': 'p'}
        x_inicial = coord[0]
        y_inicial = coord[1]

        if tab.tabuleiro[x_inicial][y_inicial].cor != dicionario_cor[player]:
            return True
        return False



# Abaixo está uma função que foi criada a parte da classe Jogo, pois na main ela teria que ser utilizada
# antes da iniciação da classe Jogo, a função dessa classe é verificar se dado o nome inserido pelo usuário
# para buscar um arquivo salvo, se ele existe ou não.


def verificar_existencia_arquivo(nome_arquivo):
    '''Função que tenta abrir um arquivo, dado um nome de entrada. Caso a função não encontre um arquivo com o
    nome inserido é retornado False, caso ele seja encontrado é retornado True.'''
    try:
        arquivo = open(nome_arquivo + '_tabuleiro.txt', 'r', encoding='utf-8')
        arquivo.close()
        return True
    except FileNotFoundError:
        return False
