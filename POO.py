class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10


class SistemaFolha:
    def __init__(self, funcionarios):
        self.funcionarios = funcionarios

    def calcular_total_bonus(self, valor_x):
        total = 0
        for f in self.funcionarios:
            if f.salario > valor_x:
                total += f.calcular_bonus()
        return total


lista = [
    Funcionario("Ana", "Analista", 3000),
    Funcionario("Carlos", "Gerente", 5000),
    Funcionario("Joao", "Estagiario", 1500),
    Funcionario("Maria", "Desenvolvedor", 4000)
]

sistema = SistemaFolha(lista)

print("Total gasto com bonus:", sistema.calcular_total_bonus(2500))