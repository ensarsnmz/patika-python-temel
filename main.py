
input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output = []

def flatten(liste):
    for item in liste:
        if type(item) == list:
            flatten(item)
        else:
            output.append(item)

flatten(input)

print(output)