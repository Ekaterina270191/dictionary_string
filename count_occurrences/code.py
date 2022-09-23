input_line = "one two one tho three"  
my_dict = {}
lst = []

def count_occurrences(string=input_line):

    for word in string.split():
        if word not in my_dict:
            my_dict[word] = 0 
        else: 
            my_dict[word] += 1

        lst.append(my_dict[word])
        
    return ' '.join(list(map(str, lst))) 
