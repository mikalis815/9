def simple_automaton_search(text, word):
    n = len(text)
    m = len(word)
    
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == word[j]:
            j += 1
        if j == m:
            return i  # Начальная позиция слова
    return -1  # Не найдено

# Пример
text = "hello world, welcome to python"
word = "world"
result = simple_automaton_search(text, word)
print(f"Слово '{word}' найдено на позиции {result}")