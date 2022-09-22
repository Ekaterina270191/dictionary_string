input_line = "one two one tho three"

def find_index(string=input_line):
    
    # Разделяем входное предложение на отдельные слова и итерируем каждое слово
    result = string.split() # ['one', 'two', 'one', 'tho', 'three']
    
    # Подготавливаем список для сбора слов по отдельности
    result_intermediate = []

    # Подготавливаем список для сбора индексов
    result_final = []
    
    # Итерируем результирующий список со словами
    for element in result:

        # Делаем проверку, если не встретилось до
        if result_intermediate.count(element) == 0:
            # Добавляем результат
            result_final.append(-1) # [-1, -1, 0, -1, -1]
            
        # Делаем проверку, если встретилось до
        else:
            # Находим индекс
            indices = [i for i, x in enumerate(result) if x == element] # [0, 2]
            index = indices[result_intermediate.count(element) - 1]
            
            # Добавляем результат
            result_final.append(index) # [-1, -1, 0, -1, -1]

        result_intermediate.append(element) # ['one', 'two', 'one', 'tho', 'three']

    # Выводим финальный результат
    return ' '.join(list(map(str, result_final))) 
