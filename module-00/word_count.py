def count_words(text):
    counts = {}
    
    for word in text.split():
        
        if word not in counts:
            counts[word] = 0
                    
        counts[word] = counts[word] + 1    
    
    return counts

print(count_words("the cat and the dog"))
print(count_words(""))
print(count_words("the  cat"))