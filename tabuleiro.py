from pecas import Torre, Cavalo, Bispo, Rei, Dama, Peao

# Agora a classe abaixo é a referente a coisas do tabuleiro em si, as quais possuem
# uma maior necessidade de detalhamento uma a uma.


class Tabuleiro():
    def __init__(self):
        '''Método construtor
        None -> None'''
        self.tabuleiro = [['*' for i in range(8)] for i in range(8)]

    # O método arrumar_tabuleiro organiza nosso tabuleiro e possui um argumento de entrada opcional.
    # Esse argumento é o que define se o tabuleiro será organizado de acordo com algum arquivo    de
    # salvamento ou se ele será organizado do início. Por padrão esse argumento possui um default de True.

    def arrumar_tabuleiro(self, nome_arquivo='', inicio=True):
        '''Método que organiza as peças do tabuleiro. Se estiver iniciando um novo jogo, não é necessário
        parametro de entrada e ele dispôe as peças na configuração inicial. Se estiver reabrindo um  jogo
        salvo é necessário a entrada de um valor booleano e o nome do arquivo.
        bool -> None'''
        if inicio:
            # peças pretas:

            self.tabuleiro[0][0] = Torre('t', 'p', (0, 0), '♜')
            self.tabuleiro[0][1] = Cavalo('c', 'p', (0, 1), '♞')
            self.tabuleiro[0][2] = Bispo('b', 'p', (0, 2), '♝')
            self.tabuleiro[0][3] = Rei('r', 'p', (0, 3), '♚')
            self.tabuleiro[0][4] = Dama('d', 'p', (0, 4), '♛')
            self.tabuleiro[0][5] = Bispo('b', 'p', (0, 5), '♝')
            self.tabuleiro[0][6] = Cavalo('c', 'p', (0, 6), '♞')
            self.tabuleiro[0][7] = Torre('t', 'p', (0, 7), '♜')
            self.tabuleiro[1][0] = Peao('p', 'p', (1, 0), '♟')
            self.tabuleiro[1][1] = Peao('p', 'p', (1, 1), '♟')
            self.tabuleiro[1][2] = Peao('p', 'p', (1, 2), '♟')
            self.tabuleiro[1][3] = Peao('p', 'p', (1, 3), '♟')
            self.tabuleiro[1][4] = Peao('p', 'p', (1, 4), '♟')
            self.tabuleiro[1][5] = Peao('p', 'p', (1, 5), '♟')
            self.tabuleiro[1][6] = Peao('p', 'p', (1, 6), '♟')
            self.tabuleiro[1][7] = Peao('p', 'p', (1, 7), '♟')

            # peças brancas:

            self.tabuleiro[7][0] = Torre('t', 'b', (7, 0), '♖')
            self.tabuleiro[7][1] = Cavalo('c', 'b', (7, 1), '♘')
            self.tabuleiro[7][2] = Bispo('b', 'b', (7, 2), '♗')
            self.tabuleiro[7][3] = Rei('r', 'b', (7, 3), '♔')
            self.tabuleiro[7][4] = Dama('d', 'b', (7, 4), '♕')
            self.tabuleiro[7][5] = Bispo('b', 'b', (7, 5), '♗')
            self.tabuleiro[7][6] = Cavalo('c', 'b', (7, 6), '♘')
            self.tabuleiro[7][7] = Torre('t', 'b', (7, 7), '♖')
            self.tabuleiro[6][0] = Peao('p', 'b', (6, 0), '♙')
            self.tabuleiro[6][1] = Peao('p', 'b', (6, 1), '♙')
            self.tabuleiro[6][2] = Peao('p', 'b', (6, 2), '♙')
            self.tabuleiro[6][3] = Peao('p', 'b', (6, 3), '♙')
            self.tabuleiro[6][4] = Peao('p', 'b', (6, 4), '♙')
            self.tabuleiro[6][5] = Peao('p', 'b', (6, 5), '♙')
            self.tabuleiro[6][6] = Peao('p', 'b', (6, 6), '♙')
            self.tabuleiro[6][7] = Peao('p', 'b', (6, 7), '♙')

        # converter tabuleiro salvo em novo tabuleiro
        else:
            # Para retornar as peças do arquivo de salvamento para o tabuleiro foi feito o salvamento 
            # das peças junto de um código que representa sua posição inicial para, assim, podermos 
            # distinguir as peças. Isso é importante pricipalmente pensando nos peões, os quais saber 
            # a posição inicial é essencial para sua movimentação
            dicionario_pecas = {
                'tp00': Torre('t', 'p', (0, 0), '♜'),
                'cp01': Cavalo('c', 'p', (0, 1), '♞'),
                'bp02': Bispo('b', 'p', (0, 2), '♝'),
                'rp03': Rei('r', 'p', (0, 3), '♚'),
                'dp04': Dama('d', 'p', (0, 4), '♛'),
                'bp05': Bispo('b', 'p', (0, 5), '♝'),
                'cp06': Cavalo('c', 'p', (0, 6), '♞'),
                'tp07': Torre('t', 'p', (0, 7), '♜'),
                'pp10': Peao('p', 'p', (1, 0), '♟'),
                'pp11': Peao('p', 'p', (1, 1), '♟'),
                'pp12': Peao('p', 'p', (1, 2), '♟'),
                'pp13': Peao('p', 'p', (1, 3), '♟'),
                'pp14': Peao('p', 'p', (1, 4), '♟'),
                'pp15': Peao('p', 'p', (1, 5), '♟'),
                'pp16': Peao('p', 'p', (1, 6), '♟'),
                'pp17': Peao('p', 'p', (1, 7), '♟'),

                'tb70': Torre('t', 'b', (7, 0), '♖'),
                'cb71': Cavalo('c', 'b', (7, 1), '♘'),
                'bb72': Bispo('b', 'b', (7, 2), '♗'),
                'rb73': Rei('r', 'b', (7, 3), '♔'),
                'db74': Dama('d', 'b', (7, 4), '♕'),
                'bb75': Bispo('b', 'b', (7, 5), '♗'),
                'cb76': Cavalo('c', 'b', (7, 6), '♘'),
                'tb77': Torre('t', 'b', (7, 7), '♖'),
                'pb60': Peao('p', 'b', (6, 0), '♙'),
                'pb61': Peao('p', 'b', (6, 1), '♙'),
                'pb62': Peao('p', 'b', (6, 2), '♙'),
                'pb63': Peao('p', 'b', (6, 3), '♙'),
                'pb64': Peao('p', 'b', (6, 4), '♙'),
                'pb65': Peao('p', 'b', (6, 5), '♙'),
                'pb66': Peao('p', 'b', (6, 6), '♙'),
                'pb67': Peao('p', 'b', (6, 7), '♙'),

                '*': '*'}

            save = open(nome_arquivo + '_tabuleiro.txt', 'r', encoding="utf-8")
            dados = save.readlines()
            tabuleiro_vazio = []
            for linha in dados:
                nova_linha = linha.split(',')
                tabuleiro_vazio.append(nova_linha)

            for linha in range(8):  # Retirando o \n
                tabuleiro_vazio[linha][7] = tabuleiro_vazio[linha][7][0:-1]

            for i in range(8):
                for j in range(8):
                    tabuleiro_vazio[i][j] = dicionario_pecas[tabuleiro_vazio[i][j]]

            self.tabuleiro = tabuleiro_vazio

    # O método verificar_posicao recebe uma coordenada do tabuleiro e verifica se há alguma peça nessa coordenada

    def verificar_posicao(self, coord):
        '''Método que verifica se há ou não peças na coordenada dada.
        (Tuple) -> bool'''
        x = coord[0]
        y = coord[1]
        if self.tabuleiro[x][y] == '*':
            return False
        else:
            return True

    # Tanto o método verificar_xeque como o verificar_xeque_mate são os métodos que irão reger
    # o andamento do jogo e limitar as movimentações. O método verificar xeque utiliza o método
    # atacavel da classe Rei e verifica se o Rei estará na condição de xeque ou não. Já o método
    # verificar_xequemate faz um varredura em todo tabuleiro, e analisa se o rei de um determinado
    # jogador se encontra totalmente indefeso, a ponto de nenhuma peça ou nenhuma fuga se capaz 
    # de livrá-lo da condição de xeque-mate.

    # Além disso, o método informar_xeque é responsáel por informar que o rei de um jogador está em 
    # xeque.

    def verificar_xeque(self, coord, tab):
        '''Método que recebe a coordenada de um rei e um objeto da classe tabuleiro, e verifica se esse
        rei está em xeque.
        (tuple), Tabuleiro -> bool'''
        x = coord[0]
        y = coord[1]
        return self.tabuleiro[x][y].atacavel(coord, tab)
    
    def informar_xeque(self, cor, tab):
        '''Método que recebe uma string com o indicador de cor e um objeto da classe tabuleiro, e informa
        para o jogador que possui as peças da cor inserida que seu rei está em xeque.
        str, Tabuleiro -> None'''
        for i in range(8):
            for j in range(8):
                if not self.tabuleiro[i][j] == '*':
                    if (self.tabuleiro[i][j].identificacao == 'r') and (self.tabuleiro[i][j].cor == cor):
                        if self.verificar_xeque((i,j),tab):
                            print('Cuidado, seu rei está em xeque. Faça algo e proteja ele!!!')

    def verificar_xequemate(self, cor, tab):
        '''Método que recebe um string com o indicador de cor e um objeto da classe Tabuleiro, e varre o
        tabuleiro verificando se o rei da devida cor está em xeque-mate, ou seja, se ele está totalmente
        indefeso com relação a todas as direções possíveis de ataque. Caso o rei se encontre nessa condição 
        será retornado True, e caso não esteja retornará False. 
        str, Tabuleiro -> bool'''
        rei = []
        for i in range(8):
            for j in range(8):
                if not self.tabuleiro[i][j] == '*':
                    if self.tabuleiro[i][j].identificacao == 'r' and self.tabuleiro[i][j].cor == cor:
                        rei.append(i)
                        rei.append(j)
        
        x = rei[0]
        y = rei[1]
        delta_x_positivo = 7 - x
        delta_y_positivo = 7 - y
        delta_x_negativo = x 
        delta_y_negativo = y
        
        lista_coords = []

        if delta_y_negativo > 0:
            if not self.verificar_posicao((x, y - 1)):
                self.tabuleiro[x][y], self.tabuleiro[x][y - 1] = self.tabuleiro[x][y - 1], self.tabuleiro[x][y]
                if not self.verificar_xeque((x, y-1), tab):
                    self.tabuleiro[x][y - 1], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x][y - 1]
                    return False
                self.tabuleiro[x][y - 1], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x][y - 1]
                
            if delta_x_negativo > 0:
                if not self.verificar_posicao((x - 1, y - 1)):
                    self.tabuleiro[x][y], self.tabuleiro[x - 1][y - 1] = self.tabuleiro[x - 1][y - 1], self.tabuleiro[x][y]
                    if not self.verificar_xeque((x- 1, y-1), tab):
                        self.tabuleiro[x-1][y - 1], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x-1][y - 1]
                        return False
                    self.tabuleiro[x-1][y - 1], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x-1][y - 1]

                for i in range(min((delta_x_negativo, delta_y_negativo))):
                    if self.verificar_posicao((x - (i + 1), y - (i + 1))):
                        if self.tabuleiro[x - (i + 1)][y - (i + 1)].cor == self.tabuleiro[x][y].cor:
                            break
                        else:
                            lista_coords.append((x - (i + 1), y - (i + 1)))
                    lista_coords.append((x - (i + 1), y - (i + 1)))

                if delta_x_negativo >= 2 and delta_y_negativo >= 1:
                    lista_coords.append((x-2, y-1))
                if delta_x_negativo >= 1 and delta_y_negativo >=2:
                    lista_coords.append((x-1, y-2))

            if delta_x_positivo > 0:
                if not self.verificar_posicao((x + 1, y - 1)):
                    self.tabuleiro[x][y], self.tabuleiro[x + 1][y - 1] = self.tabuleiro[x + 1][y - 1], self.tabuleiro[x][y]
                    if not self.verificar_xeque((x+1, y-1), tab):
                        self.tabuleiro[x+1][y - 1], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x+1][y - 1]
                        return False
                    self.tabuleiro[x+1][y - 1], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x+1][y - 1]
                    
                for i in range(min((delta_x_positivo, delta_y_negativo))):
                    if self.verificar_posicao((x + (i + 1), y - (i + 1))):
                        if self.tabuleiro[x + (i + 1)][y - (i + 1)].cor == self.tabuleiro[x][y].cor:
                            break
                        else:
                            lista_coords.append((x + (i + 1), y - (i + 1)))
                    lista_coords.append((x + (i + 1), y - (i + 1)))

                if delta_x_positivo >= 2 and delta_y_negativo >= 1:
                    lista_coords.append((x+2, y-1))
                if delta_x_positivo >= 1 and delta_y_negativo >=2:
                    lista_coords.append((x+1, y-2))

            for i in range(delta_y_negativo):
                if self.verificar_posicao((x, y - (i + 1))):
                    if self.tabuleiro[x][y - (i + 1)].cor == self.tabuleiro[x][y].cor:
                        break
                    else:
                        lista_coords.append((x, y - (i + 1)))
                lista_coords.append((x, y - (i + 1)))

        if delta_y_positivo > 0:
            if not self.verificar_posicao((x, y + 1)):
                self.tabuleiro[x][y], self.tabuleiro[x][y + 1] = self.tabuleiro[x][y + 1], self.tabuleiro[x][y]
                if not self.verificar_xeque((x, y + 1), tab):
                    self.tabuleiro[x][y + 1], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x][y + 1]
                    return False
                self.tabuleiro[x][y + 1], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x][y + 1]
                
            if delta_x_negativo > 0:
                if not self.verificar_posicao((x - 1, y + 1)):
                    self.tabuleiro[x][y], self.tabuleiro[x - 1][y + 1] = self.tabuleiro[x - 1][y + 1], self.tabuleiro[x][y]
                    if not self.verificar_xeque((x- 1, y+1), tab):
                        self.tabuleiro[x-1][y + 1], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x-1][y + 1]
                        return False
                    self.tabuleiro[x-1][y + 1], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x-1][y + 1]
            
                for i in range(min(delta_y_positivo, delta_x_negativo)):
                    if self.verificar_posicao((x - (i + 1), y + i + 1)):
                        if self.tabuleiro[x - (i + 1)][y + i + 1].cor == self.tabuleiro[x][y].cor:
                            break
                        else:
                            lista_coords.append((x - (i + 1), y + i + 1))
                    lista_coords.append((x - (i + 1), y + i + 1))

                if delta_x_negativo >= 2 and delta_y_positivo >= 1:
                    lista_coords.append((x-2, y+1))
                if delta_x_negativo >= 1 and delta_y_positivo >=2:
                    lista_coords.append((x-1, y+2))

            if delta_x_positivo > 0:
                if not self.verificar_posicao((x + 1, y + 1)):
                    self.tabuleiro[x][y], self.tabuleiro[x + 1][y + 1] = self.tabuleiro[x + 1][y + 1], self.tabuleiro[x][y]
                    if not self.verificar_xeque((x+1, y+1), tab):
                        self.tabuleiro[x+1][y + 1], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x+1][y + 1]
                        return False
                    self.tabuleiro[x+1][y + 1], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x+1][y + 1]
                    
                for i in range(min(delta_y_positivo, delta_x_positivo)):
                    if self.verificar_posicao((x + (i + 1), y + i + 1)):
                        if self.tabuleiro[x + (i + 1)][y + (i + 1)].cor == self.tabuleiro[x][y].cor:
                            break
                        else:
                            lista_coords.append((x + (i + 1), y + i + 1))
                        lista_coords.append((x + (i + 1), y + i + 1))

                if delta_x_positivo >= 2 and delta_y_positivo >= 1:
                    lista_coords.append((x+2, y+1))
                if delta_x_positivo >= 1 and delta_y_positivo >=2:
                    lista_coords.append((x+1, y+2))

            for i in range(delta_y_positivo):
                if self.verificar_posicao((x, y + i + 1)):
                    if self.tabuleiro[x][y + i +1].cor == self.tabuleiro[x][y].cor:
                        break
                    else:
                        lista_coords.append((x, y + i + 1))
                lista_coords.append((x, y + i + 1))
                
        if delta_x_positivo > 0:
            if not self.verificar_posicao((x + 1, y)):
                self.tabuleiro[x][y], self.tabuleiro[x + 1][y] = self.tabuleiro[x + 1][y], self.tabuleiro[x][y]
                if not self.verificar_xeque((x + 1, y), tab):
                    self.tabuleiro[x + 1][y], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x + 1][y]
                    return False
                self.tabuleiro[x + 1][y], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x + 1][y]

            for i in range(delta_x_positivo):
                if self.verificar_posicao((x + i + 1, y)):
                    if self.tabuleiro[x + i + 1][y].cor == self.tabuleiro[x][y].cor:
                        break
                    else:
                        lista_coords.append((x + i + 1, y))
                    lista_coords.append((x + i + 1, y))

        if delta_x_negativo > 0:
            if not self.verificar_posicao((x - 1, y)):
                self.tabuleiro[x][y], self.tabuleiro[x - 1][y] = self.tabuleiro[x - 1][y], self.tabuleiro[x][y]
                if not self.verificar_xeque((x - 1, y), tab):
                    self.tabuleiro[x - 1][y], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x - 1][y]
                    return False
                self.tabuleiro[x - 1][y], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[x - 1][y]

            for i in range(delta_x_negativo):
                if self.verificar_posicao((x - (i + 1), y)):
                    if self.tabuleiro[x - (i + 1)][y].cor == self.tabuleiro[x][y].cor:
                        break
                    else:
                        lista_coords.append((x - (i + 1), y))
                lista_coords.append((x - (i + 1), y))       
        for i in range(8):
            for j in range(8):
                if self.tabuleiro[i][j] != '*':
                    if self.tabuleiro[i][j].cor == self.tabuleiro[x][y].cor and self.tabuleiro[i][j].identificacao != 'r':
                        peca_analise = self.tabuleiro[i][j]
                        for coord in lista_coords:
                            coord_x = coord[0]
                            coord_y = coord[1]
                            if self.caminho_livre((i,j), coord):
                                if self.verificar_posicao(coord):
                                    if self.tabuleiro[i][j].identificacao == 'p':
                                        if peca_analise.movimentacao((i,j), coord, True):
                                            self.tabuleiro[i][j], self.tabuleiro[coord_x][coord_y] = self.tabuleiro[coord_x][coord_y], self.tabuleiro[i][j]
                                            if not self.verificar_xeque(rei, tab):
                                                self.tabuleiro[coord_x][coord_y], self.tabuleiro[i][j] = self.tabuleiro[i][j], self.tabuleiro[coord_x][coord_y]
                                                return False
                                            self.tabuleiro[coord_x][coord_y], self.tabuleiro[i][j] = self.tabuleiro[i][j], self.tabuleiro[coord_x][coord_y]
                                
                                if peca_analise.movimentacao((i,j), coord) and peca_analise.identificacao != 'p':
                                    self.tabuleiro[i][j], self.tabuleiro[coord_x][coord_y] = self.tabuleiro[coord_x][coord_y], self.tabuleiro[i][j]
                                    if not self.verificar_xeque(rei, tab):
                                        self.tabuleiro[coord_x][coord_y], self.tabuleiro[i][j] = self.tabuleiro[i][j], self.tabuleiro[coord_x][coord_y]
                                        return False
                                    self.tabuleiro[coord_x][coord_y], self.tabuleiro[i][j] = self.tabuleiro[i][j], self.tabuleiro[coord_x][coord_y]
        return True

        
    def verificar_posicao_rei(self, coord_inicial):
        '''Método que dado uma coordenada inicial de uma peça, retorna da coordenada do rei de mesma cor 
        dessa peça.
        (tuple) -> (tuple)'''
        x_1 = coord_inicial[0]
        y_1 = coord_inicial[1]
        cor = self.tabuleiro[x_1][y_1].cor

        for i in range(8):
            for j in range(8):
                if self.tabuleiro[i][j] != '*':
                    if self.tabuleiro[i][j].cor == cor and self.tabuleiro[i][j].identificacao == 'r':
                        coord_rei = (i, j)
        return coord_rei


    # O método caminho_livre é o responsável por verificar as casas de um caminho proposto pelo jogador e
    # impedir que peças que não podem pular casas, pulem. Seu raciocínio foi baseado na ideia de que o xadrez
    # possui apenas três movimentos essenciais: os movimentos em diagonal, os movimentos retos, seja vertical
    # ou horizontal, e o movimento em L do cavalo. Para esse último não há restrição pois ele é permitido pular 
    # peças, já para os movimentos retos e diagonais há uma série de restrições pensando no sentido do movimento
    # que a peça está realizando. O uso do método verificar_posicao neste método é essencial.

    def caminho_livre(self, coord_inicial, coord_final):
        '''Método que varre o caminho da coordenada inicial até a final 
        verificando se há peças no caminho. Ele retornará True caso o caminho
        esteja sem peças e False caso haja alguma peça no meio do caminho. 
        (tuple), (tuple) -> bool'''
        x_1 = coord_inicial[0]
        y_1 = coord_inicial[1]
        x_2 = coord_final[0]
        y_2 = coord_final[1]
        delta_y = y_2 - y_1
        delta_x = x_2 - x_1
        if abs(delta_x) == abs(delta_y):  # movimentos diagonais
            if y_2 > y_1 and x_2 > x_1:
                i = x_1 + 1
                j = y_1 + 1
                while i < x_2 and j < y_2:
                    if self.verificar_posicao((i, j)):
                        return False
                    else:
                        i += 1
                        j += 1
                return True
            elif y_2 < y_1 and x_2 > x_1:
                i = x_1 + 1
                j = y_1 - 1
                while i < x_2 and j > y_2:
                    if self.verificar_posicao((i, j)):
                        return False
                    else:
                        i += 1
                        j -= 1
                return True
            elif y_2 < y_1 and x_2 < x_1:
                i = x_1 - 1
                j = y_1 - 1
                while i > x_2 and j > y_2:
                    if self.verificar_posicao((i, j)):
                        return False
                    else:
                        i -= 1
                        j -= 1
                return True
            else:
                i = x_1 - 1
                j = y_1 + 1
                while i > x_2 and j < y_2:
                    if self.verificar_posicao((i, j)):
                        return False
                    else:
                        i -= 1
                        j += 1
                return True

        # movimentos retos
        if delta_x == 0 and abs(delta_y) > 0 or abs(delta_x) > 0 and delta_y == 0:
            if delta_x == 0:
                if y_2 > y_1:
                    i = x_1
                    j = y_1 + 1
                    while j < y_2:
                        if self.verificar_posicao((i, j)):
                            return False
                        else:
                            j += 1
                    return True
                else:
                    i = x_1
                    j = y_1 - 1
                    while j > y_2:
                        if self.verificar_posicao((i, j)):
                            return False
                        else:
                            j -= 1
                    return True
            elif delta_y == 0:
                if x_2 > x_1:
                    i = x_1 + 1
                    j = y_1
                    while i < x_2:
                        if self.verificar_posicao((i, j)):
                            return False
                        else:
                            i += 1
                    return True
                else:
                    i = x_1 - 1
                    j = y_1
                    while i > x_2:
                        if self.verificar_posicao((i, j)):
                            return False
                        else:
                            i -= 1
                    return True

        if abs(delta_x) == 2 and abs(delta_y) == 1 or abs(delta_x) == 1 and abs(delta_y) == 2:  # movimento do cavalo
            return True

    def movimentacao_valida(self, coord_inicial, coord_final, tab):
        '''Método que verifica se uma jogada do usuário é válida a partir
        das coordenadas inseridas e do estado em que o rei se encontra.
        Esse método também retorna em sua tupla, uma mensagem para caso o movimento
        tenha sido inválido por algum motivo e contabiliza o número de casas
        percorridas em um movimento e o número de peças capturadas em um jogada.
        Todas essas informações são retornadas na tupla de saída.
        (tuple), (tuple) -> (tuple)'''
        x_1 = coord_inicial[0]
        y_1 = coord_inicial[1]
        x_2 = coord_final[0]
        y_2 = coord_final[1]
        cor = self.tabuleiro[x_1][y_1].cor

        if coord_inicial == coord_final:
            return (False, "Você soltou a peça, selecione uma nova peça!")
        # verifica se há uma peça na posição 1 inseridade
        if self.verificar_posicao(coord_inicial):
            # verifica se há uma peça na posição 2 inserida. se houver haverá um possível ataque
            if self.verificar_posicao(coord_final):
                # como o peão tem um parametro a mais, verificamos se a peça é um peão
                if self.tabuleiro[x_1][y_1].identificacao == 'p':
                    ataque = True
                    # se forem da mesma cor não há ataque
                    if self.tabuleiro[x_1][y_1].cor == self.tabuleiro[x_2][y_2].cor:
                        return (False, 'Você não pode atacar uma peça do seu time')
                    # verifica se o formato do movimento é válido
                    elif self.tabuleiro[x_1][y_1].movimentacao(coord_inicial, coord_final, ataque):
                        # verifica existem peças no meio do caminho do movimento
                        if self.caminho_livre(coord_inicial, coord_final):
                            peca_segunda_coord = self.tabuleiro[x_2][y_2]
                            self.tabuleiro[x_1][y_1], self.tabuleiro[x_2][y_2] = '*', self.tabuleiro[x_1][y_1]
                            coord_rei = self.verificar_posicao_rei(coord_final)
                            if self.verificar_xeque(coord_rei, tab):
                                self.tabuleiro[x_1][y_1], self.tabuleiro[x_2][y_2] = self.tabuleiro[x_2][y_2], peca_segunda_coord
                                return (False, 'Você não pode fazer essa movimentação. Está desprotegendo seu rei!!!', 0, 0)
                            return (True, 'Ataque bem sucedido', 1, 1)
                        else:  # se houver peças no caminho é retornado False
                            return (False, 'Existem peças no meio do seu caminho')
                    else:  # se o formato da movimentação não for válido é retornado False
                        return(False, 'Movimentação inválida')

                else:  # para caso a peça não seja um peão
                    if self.tabuleiro[x_1][y_1].cor == self.tabuleiro[x_2][y_2].cor:  # cor
                        return (False, 'Você não pode atacar uma peça do seu time')
                    # formato movimentacao
                    elif self.tabuleiro[x_1][y_1].movimentacao(coord_inicial, coord_final):
                        # peças no caminho
                        if self.caminho_livre(coord_inicial, coord_final):
                            peca_segunda_coord = self.tabuleiro[x_2][y_2]
                            self.tabuleiro[x_1][y_1], self.tabuleiro[x_2][y_2] = '*', self.tabuleiro[x_1][y_1]
                            coord_rei = self.verificar_posicao_rei(coord_final)
                            if self.verificar_xeque(coord_rei, tab):
                                self.tabuleiro[x_1][y_1], self.tabuleiro[x_2][y_2] = self.tabuleiro[x_2][y_2], peca_segunda_coord
                                return (False, 'Você não pode fazer essa movimentação. Está desprotegendo seu rei!!!', 0, 0)
                            return (True, 'Ataque bem sucedido', 1, self.tabuleiro[x_2][y_2].casas_percorridas(coord_inicial, coord_final))
                        else:
                            return (False, 'Existem peças no meio do seu caminho')
                    else:
                        return (False, 'Movimentação Inválida')

            # caso não tenha uma peça na segunda posição haverá apenas uma troca de posição
            elif self.tabuleiro[x_1][y_1].movimentacao(coord_inicial, coord_final):
                if self.caminho_livre(coord_inicial, coord_final):  # peças no caminho
                    self.tabuleiro[x_1][y_1], self.tabuleiro[x_2][y_2] = self.tabuleiro[x_2][y_2], self.tabuleiro[x_1][y_1]
                    coord_rei = self.verificar_posicao_rei(coord_final)
                    if self.verificar_xeque(coord_rei, tab):
                        self.tabuleiro[x_1][y_1], self.tabuleiro[x_2][y_2] = self.tabuleiro[x_2][y_2], self.tabuleiro[x_1][y_1]
                        return (False, 'Você não pode fazer essa movimentação. Está desprotegendo seu rei!!!', 0, 0)
                    return (True, 'Movimentação bem sucedida', 0, self.tabuleiro[x_2][y_2].casas_percorridas(coord_inicial, coord_final))
                else:
                    return (False, 'Existem peças no meio do seu caminho')

            else:  # retorna False caso a movimentação sem ataque não seja válida
                return (False, 'Movimentação Inválida')

        else:  # caso não haja nem mesmo um peça na primeira posiç3ão inserida é retornado False
            return (False, 'Você não selecionou uma peça')

    # O método imprimir_tabuleiro é responsável por imprimir no terminal o estado do tabuleiro naquele instante

    def imprimir_tabuleiro(self):
        '''Método que imprime a máscara do tabuleiro
        None -> None'''
        tabuleiro_cores = [
            ['\033[m', '\033[7;40m', '\033[m', '\033[7;40m', '\033[m', '\033[7;40m', '\033[m', '\033[7;40m'],
            [ '\033[7;40m', '\033[m', '\033[7;40m', '\033[m', '\033[7;40m','\033[m', '\033[7;40m', '\033[m'],
            ['\033[m', '\033[7;40m', '\033[m', '\033[7;40m', '\033[m', '\033[7;40m', '\033[m', '\033[7;40m'],
            [ '\033[7;40m', '\033[m', '\033[7;40m', '\033[m', '\033[7;40m','\033[m', '\033[7;40m', '\033[m'],
            ['\033[m', '\033[7;40m', '\033[m', '\033[7;40m', '\033[m', '\033[7;40m', '\033[m', '\033[7;40m'],
            [ '\033[7;40m', '\033[m', '\033[7;40m', '\033[m', '\033[7;40m','\033[m', '\033[7;40m', '\033[m'],
            ['\033[m', '\033[7;40m', '\033[m', '\033[7;40m', '\033[m', '\033[7;40m', '\033[m', '\033[7;40m'],
            [ '\033[7;40m', '\033[m', '\033[7;40m', '\033[m', '\033[7;40m','\033[m', '\033[7;40m', '\033[m']
        ]
        print()
        print('     A   B   C   D   E   F   G   H')
        print()
        for i in range(8):
            print(f'{i+1}', end='  ')
            for j in range(8):
                if self.tabuleiro[i][j] == '*':
                    print(tabuleiro_cores[i][j] + ' ' + tabuleiro_cores[i][j]+ '  ', end=' ')
                else:
                    print(tabuleiro_cores[i][j] + ' ' + tabuleiro_cores[i][j] + self.tabuleiro[i][j].simbolo + tabuleiro_cores[i][j] + ' ', end=' ')
            print(f'\033[m  {i+1}')
        print()
        print('     A   B   C   D   E   F   G   H')
        print()

    # O método salvar_tabuleiro é reponsavél por armazernar em um arquivo txt o estado atual do tabuleiro de xadrez.posta

    def salvar_tabuleiro(self, nome_arquivo):
        '''Método que dado uma string representando o nome de um arquivo a ser salvo contendo o estado da mascara e 
        do tabuleiro naquele devido instante.
        str -> None'''
        nome_formatado = nome_arquivo + '_tabuleiro'
        save = open(f'{nome_formatado}.txt', 'w', encoding="utf-8")
        for i in range(8):
            for j in range(8):
                if j == 7:
                    if self.tabuleiro[i][j] == '*':
                        save.write('*')
                    else:
                        save.write(
                            f'{self.tabuleiro[i][j].identificacao + self.tabuleiro[i][j].cor + str(self.tabuleiro[i][j].pos_inicial[0]) + str(self.tabuleiro[i][j].pos_inicial[1])}')
                else:
                    if self.tabuleiro[i][j] == '*':
                        save.write('*,')
                    else:
                        save.write(
                            f'{self.tabuleiro[i][j].identificacao + self.tabuleiro[i][j].cor + str(self.tabuleiro[i][j].pos_inicial[0]) + str(self.tabuleiro[i][j].pos_inicial[1])},')
            save.write('\n')
        save.close()
    
    def verificar_vencedor(self, tab):
        '''Método que dado um objeto da classe Tabuleiro, retorna o rótulo do jogador vencedor.'''
        if self.verificar_xequemate('b', tab):
            return 'Jogador 2'
        return 'Jogador 1'


