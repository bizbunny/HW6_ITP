# HW6
# Collaborator: Vi-Linh Nguyen

import json
# # Problem 1
# # Answer:
def intersect(set1, set2):
    set3=set()
    for i in set1:
        for j in set2:
            if j==i:
                k=j
                set3.add(k)
    return set3
# # _______________________________________________________________

# # Problem 2
# # Answer:
def union(set1, set2):
	set3=(set1 | set2)
	return set3
# # _______________________________________________________________

# # Problem 3
# # Answer:
def uniqueWords(text):
	text=text.split()
	text=set(text)
	return text
# # _______________________________________________________________

# Problem 4
# # Answer:
def printWithAge (file_name, age):
    with open(file_name, 'r') as fiLe:
        reader = json.load(fiLe)
        for i in reader:
            if (int(i ["age"]) == age):
                print(i ["firstName"] +" "+ i ["lastName"])
# # _______________________________________________________________

# # Problem 5
# # Answer:
def reverse(dict):
	newdict={v:k for k,v in dict.items()}
	return newdict
# # _______________________________________________________________
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('hw6_test.py', verbose=False))
