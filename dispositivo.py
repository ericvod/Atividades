from __future__ import annotations


class ControleRemoto:
    def __init__(self, dispositivo: Dispositivo):
        self.disposivivo = dispositivo

    def ligar(self):
        if self.disposivivo.var != 1:
            print("Seu dispositivo estava desligado!")
            print("Ligando...\n")
            self.disposivivo.ligar()
        else:
            print("Seu dispositivo estava ligado!")
            print("Desligando...")
            self.disposivivo.desligar()

    def volumeCima(self):
        if self.disposivivo.var != 1:
            print("Dispositivo desligado!")
        else:
            self.disposivivo.volumeCima()

    def volumeBaixo(self):
        if self.disposivivo.var != 1:
            print("Dispositivo desligado!")
        else:
            self.disposivivo.volumeBaixo()

class ControleTV(ControleRemoto):
    pass

class Dispositivo():
    var = 0
    volume = 0

    def desligar(self):
        self.var = 0

    def ligar(self):
        self.var = 1

    def volumeCima(self):
        self.volume += 10

    def volumeBaixo(self):
        if self.volume == 0:
            print("Volume minimo atingido!")
        else:
            self.volume -= 10


class TV(Dispositivo):
    def nome(self) -> str:
        return "TV"

def usuario(controle: ControleRemoto):
    while (True):
        x = input('\nFunções controle:\nBotão Power (digite 1)\n'
                  'Botão VolumeCima (digite 2)\n'
                  'Botão volumeBaixo (digite 3)\n'
                  'Botão Status (digite 4)\n')
        if x == "1":
            controle.ligar()
        elif x == "2":
            controle.volumeCima()
        elif x == "3":
            controle.volumeBaixo()
        elif x == "4":
            if controle.disposivivo.var == 1:
                print('TV ligada')
                print(f'Volume: {controle.disposivivo.volume}')
            else:
                print('TV Desligada')
                print(f'Volume: {controle.disposivivo.volume}')
        else:
            print("Comando não existe")
            break

if __name__ == "__main__":
    tv = TV()
    controle = ControleTV(tv)
    usuario(controle)