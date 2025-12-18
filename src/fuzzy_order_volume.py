# Программа для определения объема заказа у поставщика
# на основе нечеткой логики
# Вариант 2

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Определяем входные переменные
# Текущий уровень запасов (0-1000 единиц)
current_stock = ctrl.Antecedent(np.arange(0, 1001, 1), 'current_stock')
current_stock['низкий'] = fuzz.trimf(current_stock.universe, [0, 0, 400])
current_stock['средний'] = fuzz.trimf(current_stock.universe, [200, 500, 800])
current_stock['высокий'] = fuzz.trimf(current_stock.universe, [600, 1000, 1000])

# Ожидаемый спрос (0-500 единиц в месяц)
expected_demand = ctrl.Antecedent(np.arange(0, 501, 1), 'expected_demand')
expected_demand['низкий'] = fuzz.trimf(expected_demand.universe, [0, 0, 200])
expected_demand['средний'] = fuzz.trimf(expected_demand.universe, [100, 250, 400])
expected_demand['высокий'] = fuzz.trimf(expected_demand.universe, [300, 500, 500])

# Срок доставки (1-30 дней)
delivery_time = ctrl.Antecedent(np.arange(1, 31, 1), 'delivery_time')
delivery_time['быстрый'] = fuzz.trimf(delivery_time.universe, [1, 1, 10])
delivery_time['средний'] = fuzz.trimf(delivery_time.universe, [5, 15, 25])
delivery_time['медленный'] = fuzz.trimf(delivery_time.universe, [20, 30, 30])

# Стоимость единицы товара (100-10000 рублей)
unit_price = ctrl.Antecedent(np.arange(100, 10001, 1), 'unit_price')
unit_price['низкая'] = fuzz.trimf(unit_price.universe, [100, 100, 4000])
unit_price['средняя'] = fuzz.trimf(unit_price.universe, [2000, 5000, 8000])
unit_price['высокая'] = fuzz.trimf(unit_price.universe, [6000, 10000, 10000])

# Выходная переменная - объем заказа (0-2000 единиц)
order_volume = ctrl.Consequent(np.arange(0, 2001, 1), 'order_volume')
order_volume['очень_маленький'] = fuzz.trimf(order_volume.universe, [0, 0, 400])
order_volume['маленький'] = fuzz.trimf(order_volume.universe, [200, 500, 800])
order_volume['средний'] = fuzz.trimf(order_volume.universe, [600, 1000, 1400])
order_volume['большой'] = fuzz.trimf(order_volume.universe, [1200, 1600, 2000])
order_volume['очень_большой'] = fuzz.trimf(order_volume.universe, [1800, 2000, 2000])

# База правил
# Правила составлены на основе экспертных знаний
rule1 = ctrl.Rule(current_stock['низкий'] & expected_demand['низкий'] & delivery_time['быстрый'], 
                  order_volume['маленький'])
rule2 = ctrl.Rule(current_stock['низкий'] & expected_demand['низкий'] & delivery_time['средний'], 
                  order_volume['маленький'])
rule3 = ctrl.Rule(current_stock['низкий'] & expected_demand['низкий'] & delivery_time['медленный'], 
                  order_volume['средний'])

rule4 = ctrl.Rule(current_stock['низкий'] & expected_demand['средний'] & delivery_time['быстрый'], 
                  order_volume['средний'])
rule5 = ctrl.Rule(current_stock['низкий'] & expected_demand['средний'] & delivery_time['средний'], 
                  order_volume['средний'])
rule6 = ctrl.Rule(current_stock['низкий'] & expected_demand['средний'] & delivery_time['медленный'], 
                  order_volume['большой'])

rule7 = ctrl.Rule(current_stock['низкий'] & expected_demand['высокий'] & delivery_time['быстрый'], 
                  order_volume['большой'])
rule8 = ctrl.Rule(current_stock['низкий'] & expected_demand['высокий'] & delivery_time['средний'], 
                  order_volume['большой'])
rule9 = ctrl.Rule(current_stock['низкий'] & expected_demand['высокий'] & delivery_time['медленный'], 
                  order_volume['очень_большой'])

rule10 = ctrl.Rule(current_stock['средний'] & expected_demand['низкий'] & delivery_time['быстрый'], 
                   order_volume['очень_маленький'])
rule11 = ctrl.Rule(current_stock['средний'] & expected_demand['низкий'] & delivery_time['средний'], 
                   order_volume['маленький'])
rule12 = ctrl.Rule(current_stock['средний'] & expected_demand['низкий'] & delivery_time['медленный'], 
                   order_volume['маленький'])

rule13 = ctrl.Rule(current_stock['средний'] & expected_demand['средний'] & delivery_time['быстрый'], 
                   order_volume['маленький'])
rule14 = ctrl.Rule(current_stock['средний'] & expected_demand['средний'] & delivery_time['средний'], 
                   order_volume['средний'])
rule15 = ctrl.Rule(current_stock['средний'] & expected_demand['средний'] & delivery_time['медленный'], 
                   order_volume['средний'])

rule16 = ctrl.Rule(current_stock['средний'] & expected_demand['высокий'] & delivery_time['быстрый'], 
                   order_volume['средний'])
rule17 = ctrl.Rule(current_stock['средний'] & expected_demand['высокий'] & delivery_time['средний'], 
                   order_volume['большой'])
rule18 = ctrl.Rule(current_stock['средний'] & expected_demand['высокий'] & delivery_time['медленный'], 
                   order_volume['большой'])

rule19 = ctrl.Rule(current_stock['высокий'] & expected_demand['низкий'] & delivery_time['быстрый'], 
                   order_volume['очень_маленький'])
rule20 = ctrl.Rule(current_stock['высокий'] & expected_demand['низкий'] & delivery_time['средний'], 
                   order_volume['очень_маленький'])
rule21 = ctrl.Rule(current_stock['высокий'] & expected_demand['низкий'] & delivery_time['медленный'], 
                   order_volume['маленький'])

rule22 = ctrl.Rule(current_stock['высокий'] & expected_demand['средний'] & delivery_time['быстрый'], 
                   order_volume['маленький'])
rule23 = ctrl.Rule(current_stock['высокий'] & expected_demand['средний'] & delivery_time['средний'], 
                   order_volume['маленький'])
rule24 = ctrl.Rule(current_stock['высокий'] & expected_demand['средний'] & delivery_time['медленный'], 
                   order_volume['средний'])

rule25 = ctrl.Rule(current_stock['высокий'] & expected_demand['высокий'] & delivery_time['быстрый'], 
                   order_volume['средний'])
rule26 = ctrl.Rule(current_stock['высокий'] & expected_demand['высокий'] & delivery_time['средний'], 
                   order_volume['средний'])
rule27 = ctrl.Rule(current_stock['высокий'] & expected_demand['высокий'] & delivery_time['медленный'], 
                   order_volume['большой'])

# Создаем систему управления
order_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
                                  rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
                                  rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27])

# Создаем симулятор
order_sim = ctrl.ControlSystemSimulation(order_ctrl)

def calculate_order_volume(stock, demand, delivery, price):
    # Функция для расчета объема заказа
    # stock - уровень запасов
    # demand - спрос
    # delivery - срок доставки
    # price - цена
    
    order_sim.input['current_stock'] = stock
    order_sim.input['expected_demand'] = demand
    order_sim.input['delivery_time'] = delivery
    order_sim.input['unit_price'] = price
    
    order_sim.compute()
    
    result = order_sim.output['order_volume']
    return result

def main():
    # Основная функция
    print("=" * 60)
    print("Система определения объема заказа на основе нечеткой логики")
    print("=" * 60)
    print()
    
    # Пример 1
    print("Пример 1:")
    print("Текущий уровень запасов: 150 единиц")
    print("Ожидаемый спрос: 300 единиц/месяц")
    print("Срок доставки: 8 дней")
    print("Стоимость единицы: 5000 рублей")
    
    result1 = calculate_order_volume(150, 300, 8, 5000)
    print(f"Рекомендуемый объем заказа: {result1:.2f} единиц")
    print()
    
    # Пример 2
    print("Пример 2:")
    print("Текущий уровень запасов: 700 единиц")
    print("Ожидаемый спрос: 100 единиц/месяц")
    print("Срок доставки: 5 дней")
    print("Стоимость единицы: 2000 рублей")
    
    result2 = calculate_order_volume(700, 100, 5, 2000)
    print(f"Рекомендуемый объем заказа: {result2:.2f} единиц")
    print()
    
    # Пример 3
    print("Пример 3:")
    print("Текущий уровень запасов: 50 единиц")
    print("Ожидаемый спрос: 450 единиц/месяц")
    print("Срок доставки: 25 дней")
    print("Стоимость единицы: 8000 рублей")
    
    result3 = calculate_order_volume(50, 450, 25, 8000)
    print(f"Рекомендуемый объем заказа: {result3:.2f} единиц")
    print()
    
    print("=" * 60)

if __name__ == "__main__":
    main()
