import random

def simple_game_ai():
    # Статистика ходов игрока: камень, ножницы, бумага
    stats = {'камень': 0, 'ножницы': 0, 'бумага': 0}
    
    # Что побеждает что
    wins_against = {
        'камень': 'ножницы',
        'ножницы': 'бумага', 
        'бумага': 'камень'
    }
    
    for round_num in range(5):  # 5 раундов
        # Ход игрока (симуляция)
        player_move = random.choice(['камень', 'ножницы', 'бумага'])
        print(f"Раунд {round_num + 1}: Игрок 1 выбрал {player_move}")
        
        # Обновляем статистику
        stats[player_move] += 1
        
        # Предсказываем следующий ход игрока (самый частый)
        predicted_move = max(stats, key=stats.get)
        
        # Выбираем ход, который побеждает предсказанный
        # Если предсказанный ход 'камень', мы выбираем 'бумага'
        ai_move = [k for k, v in wins_against.items() if v == predicted_move][0]
        
        print(f"Игрок 2 выбрал: {ai_move}")
        
        # Определяем победителя
        if wins_against[ai_move] == player_move:
            print("Игрок 2 выиграл!")
        elif wins_against[player_move] == ai_move:
            print("Игрок 1 выиграл!")
        else:
            print("Ничья!")
        print()

# Запуск игры
simple_game_ai()