input_line = "apple orange banana banana orange"                                        

def most_often_word(string=input_line):
    dict_total = {}
    
    for simvol in string.split():
        
        if simvol not in dict_total:
            dict_total[simvol] = 1
        else:
            dict_total[simvol] += 1
                
    return sorted([k for k, v in  dict_total.items() if v == max(dict_total.values())])[0] # Вывод одного ключа с максималльным значением - banana
                                                                                           # если несколько ключей надо вывести, то убираем [0]
