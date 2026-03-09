funcionarios = [
    {"nome": "Ana", "cargo": "Analista", "salario": 3000},
    {"nome": "Carlos", "cargo": "Gerente", "salario": 5000},
    {"nome": "Joao", "cargo": "Estagiario", "salario": 1500},
    {"nome": "Maria", "cargo": "Desenvolvedor", "salario": 4000}
]

valor_x = 2500
total_bonus = 0

for f in funcionarios:
    if f["salario"] > valor_x:
        bonus = f["salario"] * 0.10
        total_bonus = total_bonus + bonus

print("Total gasto com bonus:", total_bonus)