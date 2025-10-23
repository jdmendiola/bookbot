def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):

    characters = {}
    for x in range(0, len(text)):

        single_char = text[x].lower()
        if single_char in characters:
            characters[single_char] += 1
        else: 
            characters[single_char] = 1

    return characters

def report(characters):
    stats = []
    for item in characters:
        stats.append({"char": item, "num": characters[item]})

    stats.sort(reverse=True, key=sort_on)    
    
    return stats

def sort_on(items):
    return items["num"]