from functools import reduce

funcionarios = [
    {"nome": "Ana", "cargo": "Analista", "salario": 3000},
    {"nome": "Carlos", "cargo": "Gerente", "salario": 5000},
    {"nome": "Joao", "cargo": "Estagiario", "salario": 1500},
    {"nome": "Maria", "cargo": "Desenvolvedor", "salario": 4000}
]

valor_x = 2500

filtrados = list(filter(lambda f: f["salario"] > valor_x, funcionarios))

bonus = list(map(lambda f: f["salario"] * 0.10, filtrados))

total = reduce(lambda a, b: a + b, bonus)

print("Total gasto com bonus:", total)