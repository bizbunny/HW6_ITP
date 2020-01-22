#In case you're curious, I used this to convert the cubsRoster.csv file to json
def convertToJson(filePrefix):
    f = open("{}.csv".format(filePrefix))
    lines = f.readlines()[1:]
    f.close()

    records=[]
    for line in lines:
        words = line.split(",")
        names = words[0].split()
        records.append({
            "firstName":names[0],
            "lastName":" ".join(names[1:]),
            "age":int(words[1]),
            "country":words[2]
        })

    import json
    f=open("{}.json".format(filePrefix), "w")
    #both of these lines would work, but json.dump() is more elegant
    #f.write(json.dumps(records))
    json.dump(records, f)
    f.close()

#an alternate way to perform the rock paper scissors function with a dictionary (a decision tree here)
def rps(p1, p2):
    resultDict={
        "R":{
            "R":0,
            "S":1,
            "P":2
        },
        "P":{
            "R":1,
            "S":2,
            "P":0
        },
        "S":{
            "R":2,
            "S":0,
            "P":1
        }
    }
    return resultDict[p1][p2]

#an alternate way to do the vowel count function with a dictionary
def vowelCount(text):
    vowelDict={
        "a":0,
        "e":0,
        "i":0,
        "o":0,
        "u":0
    }
    for letter in text.lower():
        if letter in vowelDict:
            vowelDict[letter] += 1
    print("The number of times a, e, i, o, and u appear, respectively, are {a}, {e}, {i}, {o}, {u}".format(**vowelDict))
