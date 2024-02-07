from pulp import LpMaximize, LpProblem, LpVariable
import pulp
pulp.LpSolverDefault.msg = False

# Створення об'єкту проблеми
problem = LpProblem("MaximizeProduction", LpMaximize)

# Оголошення змінних рішення
Lemonade = LpVariable('Lemonade', lowBound=0, cat='Integer')
Fruit_Juice = LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Додавання обмежень
problem += 2 * Lemonade + Fruit_Juice <= 100, "WaterConstraint"
problem += Lemonade <= 50, "SugarConstraint"
problem += Lemonade <= 30, "LemonJuiceConstraint"
problem += 2 * Fruit_Juice <= 40, "FruitPulpConstraint"

# Додавання функції максимізації
problem += Lemonade + Fruit_Juice, "TotalProduction"

# Вирішення проблеми
problem.solve()

# Виведення результатів
print("Результати оптимізації:")
print("Кількість 'Лимонаду':", Lemonade.varValue)
print("Кількість 'Фруктового соку':", Fruit_Juice.varValue)
print("Загальна кількість продуктів:", Lemonade.varValue + Fruit_Juice.varValue)
