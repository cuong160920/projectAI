import rule
import notes

def search(readuser2, readuser1):
    result = readuser1
    for i in readuser2:
        result = notes.criteria(i, result)
    
    return result

