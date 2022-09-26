input_line = "one two one tho three"

def count_occurrences(string=input_line):
    my_dict = {}
    lst = []
    
    for word in string.split():
        if word not in my_dict:
            my_dict[word] = 0 
        else: 
            my_dict[word] += 1
            
        lst.append(my_dict[word])
    return ' '.join(list(map(str, lst)))
