def is_anagram(string1, string2):
    if string1 == string2:
        return True
    elif not string1 or not string2:
        return False
    else:
        return sorted(string1.replace(" ", "")) == sorted(string2.replace(" ", ""))
        
