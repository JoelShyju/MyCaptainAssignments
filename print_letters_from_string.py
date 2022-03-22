# Programme for printing letters in decreasing frequency from an input string

def most_frequent(string):
    dictionary = {}
    sorted_dictionary = {}
    for letter in string:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
            
    sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)
    for i in sorted_keys:
        sorted_dictionary[i] = dictionary[i]
    print("Letter in decreasing order of frequency : ", sorted_dictionary)
    
input_string = str(input("Enter a string : "))
most_frequent(input_string)
