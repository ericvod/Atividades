from __future__ import annotations
from abc import ABC, abstractmethod

class Forma:
    def __init__(self, cor: Cor) -> None:
        self.cor = cor
    def mostrar(self) -> str:
        return ()

class FormaQuadrada(Forma):
    def mostrar(self) -> str:
        return (f"Forma: Quadrado "
                f"{self.cor.cor_colorir()}")

class FormaTriangulo(Forma):
    def mostrar(self) -> str:
        return (f"Forma: Triangulo "
                f"{self.cor.cor_colorir()}")

class Cor(ABC):
    def cor_colorir(self) -> str:
        pass

class CorAzul(Cor):
    def cor_colorir(self) -> str:
        return "Azul!"

class CorLaranja(Cor):
    def cor_colorir(self) -> str:
        return "Laranja!"

def usuario(forma: Forma) -> None:
    print(forma.mostrar(), end="")

if __name__ == "__main__":
    cor = CorAzul()
    forma = FormaQuadrada(cor)
    usuario(forma)

    print("\n")

    cor = CorLaranja()
    forma = FormaTriangulo(cor)
    usuario(forma)