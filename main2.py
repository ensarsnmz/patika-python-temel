
input = [[1, 2], [3, 4], [5, 6, 7]]
output = []

def reverse(liste):
    if type(liste) is list:
        return [reverse(item) for item in liste[::-1]]
    return liste
    
print(reverse(input))
