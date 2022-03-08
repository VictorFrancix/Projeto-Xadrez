# Nessa primeira parte estão as classes referentes as peças do jogo de xadrez. 
# Todas elas são herdeiras de uma classe maior chamada Peca a qual faz com que 
# todas as peças tenham por padrão as características de identificação, cor e 
# posição inicial. Agora, nas classes específicas de cada peça é possível ver 
# que todas têm um método chamado movimentacao, o qual é resposável por validar
# se o formato do movimento inserido pelo usuário é válido. Nesse método apenas
# são avaliados o formato do movimento, e não as casas ao redor, ou seja,    é 
# verificado se o bispo vai andar apenas em diagonal, se a torre apenas anda na 
# horizontal, se o cavalo anda apenas em formato de L e assim por diante.  Essa 
# verificação foi feita com base nas variações de linha e coluna do movimento.
# Além do método movimentacao, também temos o método casas_percorridas, o qual será
# responsável por armazenar 

# Uma ressalva com relação as movimentações é o peão. Ele possui uma movimentação 
# razoável, entretanto sua forma de ataque distoa do restante das peças, pois ela
# não possui o mesmo formato do movimento comum, assim sendo a definição    desse 
# método pra a classe peão se tornou mais extensa

# Além disso, outra ressalva é com relação a peça do rei. Como o jogo de xadrez  
# gira em torno desta peça, e principalmente, da verificação dele estar em xeque 
# ou em xequemate, essa peça possui um método a mais, que se chama


class Peca():
    def __init__(self, identificacao, cor, pos_inicial, simbolo):
        '''Método construtor
        None -> None'''
        self.identificacao = identificacao
        self.pos_inicial = pos_inicial
        self.cor = cor
        self.simbolo = simbolo


class Torre(Peca):  # movimentacao OK
    def __init__(self, identificacao, cor, pos_inicial, simbolo):
        Peca.__init__(self, identificacao, cor, pos_inicial, simbolo)

    def movimentacao(self, coord_1, coord_2):
        '''Método que dado duas coordenadas, verifica se o movimento da peça é valido partindo da coordenada
        1 para a coordenada 2.
        (tuple), (tuple) -> bool'''
        y_1 = coord_1[0]
        x_1 = coord_1[1]
        y_2 = coord_2[0]
        x_2 = coord_2[1]
        delta_y = abs(y_2 - y_1)
        delta_x = abs(x_2 - x_1)
        if delta_x != 0 and delta_y != 0:  # Como o movimento da torre é sempre uma reta, horizontal ou vertical, apenas podemos ter variação em uma coordenada. Portanto, se houver variação nos dois o movimento é inválido
            return False
        else:
            return True

    def casas_percorridas(self, coord_1, coord_2):
        '''Método que dado duas coordenadas de movimento da peça, retorna o número de casa que ela
        andou.
        (tuple), (tuple) -> int'''
        y_1 = coord_1[0]
        x_1 = coord_1[1]
        y_2 = coord_2[0]
        x_2 = coord_2[1]
        delta_y = abs(y_2 - y_1)
        delta_x = abs(x_2 - x_1)
        if delta_x == 0:
            return delta_y
        return delta_x


class Bispo(Peca):  # movimentacao OK
    def __init__(self, identificacao, cor, pos_inicial, simbolo):
        Peca.__init__(self, identificacao, cor, pos_inicial, simbolo)

    def movimentacao(self, coord_1, coord_2):
        '''Método que dado duas coordenadas, verifica se o movimento da peça é valido partindo da coordenada
        1 para a coordenada 2.
        (tuple), (tuple) -> bool'''
        y_1 = coord_1[0]
        x_1 = coord_1[1]
        y_2 = coord_2[0]
        x_2 = coord_2[1]
        delta_y = abs(y_2 - y_1)
        delta_x = abs(x_2 - x_1)
        if delta_x == delta_y:  # Movimentação em Diagonal, variação de x e y são iguais
            return True
        else:
            return False

    def casas_percorridas(self, coord_1, coord_2):
        '''Método que dado duas coordenadas de movimento da peça, retorna o número de casa que ela
        andou.
        (tuple), (tuple) -> int'''
        y_1 = coord_1[0]
        y_2 = coord_2[0]
        delta_y = abs(y_2 - y_1)
        return delta_y


class Cavalo(Peca):  # movimentacao OK
    def __init__(self, identificacao, cor, pos_inicial, simbolo):
        Peca.__init__(self, identificacao, cor, pos_inicial, simbolo)

    def movimentacao(self, coord_1, coord_2):
        '''Método que dado duas coordenadas, verifica se o movimento da peça é valido partindo da coordenada
        1 para a coordenada 2.
        (tuple), (tuple) -> bool'''
        y_1 = coord_1[0]
        x_1 = coord_1[1]
        y_2 = coord_2[0]
        x_2 = coord_2[1]
        delta_y = abs(y_2 - y_1)
        delta_x = abs(x_2 - x_1)
        if delta_x == 2 and delta_y == 1:  # Movimentação em 'L'
            return True
        if delta_y == 2 and delta_x == 1:  # Movimentação em "L deitado"
            return True
        else:
            return False

    def casas_percorridas(self, coord_1, coord_2):
        '''Método que dado duas coordenadas de movimento da peça, retorna o número de casa que ela
        andou.
        (tuple), (tuple) -> int'''
        y_1 = coord_1[0]
        x_1 = coord_1[1]
        y_2 = coord_2[0]
        x_2 = coord_2[1]
        delta_y = abs(y_2 - y_1)
        delta_x = abs(x_2 - x_1)
        return delta_y + delta_x


class Dama(Peca):  # movimentacao OK
    def __init__(self, identificacao, cor, pos_inicial, simbolo):
        Peca.__init__(self, identificacao, cor, pos_inicial, simbolo)

    def movimentacao(self, coord_1, coord_2):
        '''Método que dado duas coordenadas, verifica se o movimento da peça é valido partindo da coordenada
        1 para a coordenada 2.
        (tuple), (tuple) -> bool'''
        y_1 = coord_1[0]
        x_1 = coord_1[1]
        y_2 = coord_2[0]
        x_2 = coord_2[1]
        delta_y = abs(y_2 - y_1)
        delta_x = abs(x_2 - x_1)
        # dama também faz o movimento vertical e horizontal da torre
        if (delta_x > 0 and delta_y == 0) or (delta_y > 0 and delta_x == 0):
            return True
        if delta_y == delta_x:  # dama também realiza o movimento do bispo
            return True
        else:
            return False

    def casas_percorridas(self, coord_1, coord_2):
        '''Método que dado duas coordenadas de movimento da peça, retorna o número de casa que ela
        andou.
        (tuple), (tuple) -> int'''
        y_1 = coord_1[0]
        x_1 = coord_1[1]
        y_2 = coord_2[0]
        x_2 = coord_2[1]
        delta_y = abs(y_2 - y_1)
        delta_x = abs(x_2 - x_1)
        if delta_x == 0:
            return delta_y
        if delta_y == 0:
            return delta_x
        return delta_x

class Peao(Peca):  # movimentação OK
    def __init__(self, identificacao, cor, pos_inicial, simbolo):
        Peca.__init__(self, identificacao, cor, pos_inicial, simbolo)

    def movimentacao(self, coord_1, coord_2, ataque=False):
        '''Método que dado duas coordenadas, verifica se o movimento da peça é valido partindo da coordenada
        1 para a coordenada 2.
        (tuple), (tuple) -> bool'''
        y_1 = coord_1[0]
        x_1 = coord_1[1]
        y_2 = coord_2[0]
        x_2 = coord_2[1]
        delta_y = y_2 - y_1
        delta_x = x_2 - x_1

        if ataque:  # Movimentação com ataque é em diagonal
            if self.cor == 'p':
                # No caso da cor preta a variação sempre deve ser positiva, pois o peão não "anda"
                # para trás
                if delta_x == 1 and delta_y == 1 or delta_y == 1 and delta_x == -1:
                    return True
                else:
                    return False
            else:
                # No caso da cor branca a variação sempre deve ser negativa, pois o peão está indo
                # de uma posição de maior indice, para uma de menor indice
                if delta_x == -1 and delta_y == -1 or delta_y == -1 and delta_x == 1:
                    return True
                else:
                    return False

        else:  # Movimentação sem ataque
            if delta_x != 0:  # Movimentação do Peão acontece somente com variação de linhas
                return False
            if self.cor == 'p':
                if delta_y > 2 or delta_y < 1:
                    return False
                else:
                    if delta_y == 1:
                        return True
                    # condição para o peão poder andar até duas casas quando está na posição inicial
                    elif delta_y == 2 and self.pos_inicial == coord_1:
                        return True
                    else:
                        return False
            else:
                if delta_y > -1 or delta_y < -2:
                    return False
                else:
                    if delta_y == -1:
                        return True
                    # condição para o peão poder andar até duas casas quando está na posição inicial
                    elif delta_y == -2 and self.pos_inicial == coord_1:
                        return True
                    else:
                        return False

    def casas_percorridas(self, coord_1, coord_2):
        '''Método que dado duas coordenadas de movimento da peça, retorna o número de casa que ela
        andou.
        (tuple), (tuple) -> int'''
        y_1 = coord_1[0]
        y_2 = coord_2[0]
        delta_y = abs(y_2 - y_1)
        return delta_y



class Rei(Peca):  # movimentacao OK
    def __init__(self, identificacao, cor, pos_inicial, simbolo):
        Peca.__init__(self, identificacao, cor, pos_inicial, simbolo)

    def movimentacao(self, coord_1, coord_2) -> bool:
        '''Método que dado duas coordenadas, verifica se o movimento da peça é valido partindo da coordenada
        1 para a coordenada 2.
        (tuple), (tuple) -> bool'''
        y_1 = coord_1[0]
        x_1 = coord_1[1]
        y_2 = coord_2[0]
        x_2 = coord_2[1]
        delta_y = abs(y_2 - y_1)
        delta_x = abs(x_2 - x_1)
        if delta_x != 1 and delta_y != 1:  # os movimentos do rei são limitados a variações de 1 em alguma direção, se exceder isso o movimento já é inválido
            return False
        else:
            if delta_x == 1 and delta_y == 0:
                return True
            elif delta_x == 1 and delta_y == 1:
                return True
            elif delta_x == 0 and delta_y == 1:
                return True
            else:
                return False

    def casas_percorridas(self, coord_1, coord_2):
        '''Método que dado duas coordenadas de movimento da peça, retorna o número de casa que ela
        andou.
        (tuple), (tuple) -> int'''
        y_1 = coord_1[0]
        x_1 = coord_1[1]
        y_2 = coord_2[0]
        x_2 = coord_2[1]
        delta_y = abs(y_2 - y_1)
        delta_x = abs(x_2 - x_1)
        if delta_x == 0:
            return delta_y
        return delta_x

    def atacavel(self, coord, tab):
        '''O método admite como entrada uma tupla ou uma lista e um objeto da classe Tabuleiro, e retorna
        um valor booleano, True para caso esteja na mira de um ataque, e False para caso não esteja.'''

        # Como dito, esse método será o responsável por verificar se o rei está na mira de algum ataque ou não.
        # Nele é feito uma varredura em cada uma das oito direções ('cima', 'baixo', 'direita', 'esquerda', 'cima-
        # esquerda', 'cima-direita', 'baixo-esquerda', 'baixo-direita'), além das possíveis posições do cavalo.
        # A verificação desses caminho se dá até a 'borda' do tabuleiro, ou até o encontro de uma peça, sendo ela 
        # amiga ou inimiga.
        
        x = coord[0]
        y = coord[1]
        delta_x_positivo = 7 - x
        delta_y_positivo = 7 - y
        delta_x_negativo = abs(x)
        delta_y_negativo = abs(y)
        
        iteravel_direita = range(delta_y_positivo)
        iteravel_esquerda = range(delta_y_negativo)
        iteravel_acima = range(delta_x_negativo)
        iteravel_abaixo = range(delta_x_positivo)

        dicionario_iteravel = {delta_x_negativo: iteravel_acima, delta_x_positivo: iteravel_abaixo, delta_y_negativo: iteravel_esquerda, delta_y_positivo: iteravel_direita}

        # verificar à direita
        if delta_y_positivo > 0:
            iteravel_direita = range(delta_y_positivo)
            for i in iteravel_direita:
                y_final = y + i + 1
                if tab.verificar_posicao([x, y_final]):
                    if tab.tabuleiro[x][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x][y_final].movimentacao([x, y_final], [x, y]):
                            return True
                        break
                    break
        # verificar à esquerda
        if delta_y_negativo > 0:
            iteravel_esquerda = range(delta_y_negativo)
            for i in iteravel_esquerda:
                y_final = y - (i + 1)
                if tab.verificar_posicao([x, y_final]):
                    if tab.tabuleiro[x][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x][y_final].movimentacao([x, y_final], [x, y]):
                            return True
                        break
                    break
        # verificar abaixo
        if delta_x_positivo > 0:
            iteravel_abaixo = range(delta_x_positivo)
            for i in iteravel_abaixo:
                x_final = x + i + 1
                if tab.verificar_posicao([x_final, y]):
                    if tab.tabuleiro[x_final][y].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y].identificacao == 'p':
                            break
                        if tab.tabuleiro[x_final][y].movimentacao([x_final, y], [x, y]):
                            return True
                        break
                    break
        # verificar acima
        if delta_x_negativo > 0:
            iteravel_acima = range(delta_x_negativo)
            for i in iteravel_acima:
                x_final = x - (i + 1)
                if tab.verificar_posicao([x_final, y]):
                    if tab.tabuleiro[x_final][y].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y].identificacao == 'p':
                            break
                        if tab.tabuleiro[x_final][y].movimentacao([x_final, y], [x, y]):
                            return True
                        break
                    break
        # verificar diagonal acima à direita
        if delta_x_negativo > 0 and delta_y_positivo > 0:
            for i in dicionario_iteravel[min([delta_x_negativo, delta_y_positivo])]:
                x_final = x - (i + 1)
                y_final = y + i + 1
                if tab.verificar_posicao([x_final, y_final]):
                    if tab.tabuleiro[x_final][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y_final].identificacao == 'p':
                            if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y], True):
                                return True
                            break
                        if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y]):
                            return True
                        break
                    break
        # verificar diagonal acima à esquerda
        if delta_x_negativo > 0 and delta_y_negativo > 0:
            for i in dicionario_iteravel[min([delta_x_negativo, delta_y_negativo])]:
                x_final = x - (i + 1)
                y_final = y - (i + 1)
                if tab.verificar_posicao([x_final, y_final]):
                    if tab.tabuleiro[x_final][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y_final].identificacao == 'p':
                            if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y], True):
                                return True
                            break
                        if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y]):
                            return True
                        break
                    break
        # verificar diagonal abaixo à direita
        if delta_x_positivo > 0 and delta_y_positivo > 0:
            for i in dicionario_iteravel[min([delta_x_positivo, delta_y_positivo])]:
                x_final = x + i + 1
                y_final = y + i + 1
                if tab.verificar_posicao([x_final, y_final]):
                    if tab.tabuleiro[x_final][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y_final].identificacao == 'p':
                            if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y], True):
                                return True
                            break
                        if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y]):
                            return True
                        break
                    break
        # verificar diagonal abaixo à esquerda
        if delta_x_positivo > 0 and delta_y_negativo > 0:
            for i in dicionario_iteravel[min([delta_x_positivo, delta_y_negativo])]:
                x_final = x + i + 1
                y_final = y - (i + 1)
                if tab.verificar_posicao([x_final, y_final]):
                    if tab.tabuleiro[x_final][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y_final].identificacao == 'p':
                            if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y], True):
                                return True
                            break
                        if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y]):
                            return True
                        break
                    break
        # movimentos em L
        if x + 2 <= delta_x_positivo:
            x_final = x + 2
            if y + 1 <= delta_y_positivo:
                y_final = y + 1
                if tab.verificar_posicao([x_final, y_final]):
                    if tab.tabuleiro[x_final][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y]):
                            return True
            if abs(y - 1) <= delta_y_negativo:
                y_final = y - 1
                if tab.verificar_posicao([x_final, y_final]):
                    if tab.tabuleiro[x_final][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y]):
                            return True
        
        if x + 1 <= delta_x_positivo:
            x_final = x + 1
            if y + 2 <= delta_y_positivo:
                y_final = y + 2
                if tab.verificar_posicao([x_final, y_final]):
                    if tab.tabuleiro[x_final][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y]):
                            return True
            if abs(y - 2) <= delta_y_negativo:
                y_final = y - 2
                if tab.verificar_posicao([x_final, y_final]):
                    if tab.tabuleiro[x_final][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y]):
                            return True

        if abs(x - 1) <= delta_x_negativo:
            x_final = x - 1
            if y + 2 <= delta_y_positivo:
                y_final = y + 2
                if tab.verificar_posicao([x_final, y_final]):
                    if tab.tabuleiro[x_final][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y]):
                            print('aqui')
                            return True
            if abs(y - 2) <= delta_y_negativo:
                y_final = y - 2
                if tab.verificar_posicao([x_final, y_final]):
                    if tab.tabuleiro[x_final][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y]):
                            return True

        if abs(x - 2) <= delta_x_negativo:
            x_final = x - 2
            if y + 1 <= delta_y_positivo:
                y_final = y + 1
                if tab.verificar_posicao([x_final, y_final]):
                    if tab.tabuleiro[x_final][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y]):
                            return True
            if abs(y - 1) <= delta_y_negativo:
                y_final = y - 1
                if tab.verificar_posicao([x_final, y_final]):
                    if tab.tabuleiro[x_final][y_final].cor != tab.tabuleiro[x][y].cor:
                        if tab.tabuleiro[x_final][y_final].movimentacao([x_final, y_final], [x, y]):
                            return True
        return False
