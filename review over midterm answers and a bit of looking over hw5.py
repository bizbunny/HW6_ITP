Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> import csv
>>> os.chdir("C:\\Users\\anh17\\Desktop\\ComSci DePaul\\Fall 2019\\Intro to Programming\\Week4 and 5\\Week 5 Stuff")
>>> def playerHasLastInitial(filename, char):
	with open(filename,'r') as fiLe:
		header=next(fiLe)
		filRL=fiLe.readline()
		while fiLe.readline():
			filRL=fiLe.readline()
			if char in filRL:
				filRL=filRL.split()
				if char==filRL[1][0]:
					return True
				else:
					return False
		fiLe.close()

		
>>> playerHasLastInitial('cubsRoster.csv', 'A')
True
>>> playerHasLastInitial('cubsRoster.csv', 'V')
False
>>> playerHasLastInitial('cubsRoster.csv', 'J')
False
>>> playerHasLastInitial('cubsRoster.csv', 'Z')
True
>>> def playerHasLastInitial(filename, char):
	with open(filename,'r') as fiLe:
		header=next(fiLe)
		filRL=fiLe.readline()
		print(filRL, end=',')
		while fiLe.readline():
			filRL=fiLe.readline()
			print(filRL, end=',')
			if char in filRL:
				filRL=filRL.split()
				print(filRL, end=',')
				if char==filRL[1][0]:
					print(filRL[1][0]
					return True
				else:
					return False
		fiLe.close()
					      
SyntaxError: invalid syntax
>>> def playerHasLastInitial(filename, char):
	with open(filename,'r') as fiLe:
		header=next(fiLe)
		filRL=fiLe.readline()
		print(filRL, end=',')
		while fiLe.readline():
			filRL=fiLe.readline()
			print(filRL, end=',')
			if char in filRL:
				filRL=filRL.split()
				print(filRL, end=',')
				if char==filRL[1][0]:
					print(filRL[1][0])
					return True
				else:
					return False
		fiLe.close()

		
>>> playerHasLastInitial('cubsRoster.csv', 'Z')
Jim Adduci,34,CA,
,Adbert Alzolay,24,VE,
,Tony Barnette,35,US,
,Brad Brach,33,US,
,Victor Caratini,25,PR,
,Xavier Cedeno,32,PR,
,Steve Cishek,33,US,
,Willson Contreras,27,VE,
,Taylor Davis,29,US,
,Carl Edwards Jr.,27,US,
,Carlos Gonzalez,33,VE,
,Ian Happ,24,US,
,Jason Heyward,29,US,
,Derek Holland,32,US,
,Tony Kemp,27,US,
,Brandon Kintzler,34,US,
,Jonathan Lucroy,33,US,
,Dillon Maples,27,US,
,Mike Montgomery,29,US,
,David Phelps,32,US,
,Anthony Rizzo,29,US,
,Addison Russell,25,US,
,Kyle Schwarber,26,US,
,Duane Underwood Jr.,24,US,
,Rowan Wick,26,CA,
,Mark Zagunis,26,US,
,['Mark', 'Zagunis,26,US,'],Z
True
>>> def maxWordLength(text):
	words=text.split()
	maxLength=0
	for word in words:
		if len(word)>maxLength:
			maxLength=len(word)
	return maxLength

>>> maxWordLength("The Federal Buerau of INvestigation")
13
>>> #midterm answers review
>>> def isPositive(matrix):
	for row in matrix:
		for v in row:
			if v<=0:
				return False
	return True

>>> isPositive([1,0],[0,1])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    isPositive([1,0],[0,1])
TypeError: isPositive() takes 1 positional argument but 2 were given
>>> isPositive([[1,0],[0,1]])
False
>>> def isOrdred(lst):
	for i in range(0,len(lst)-1):
		if lst[i]>lst[i+1]:
			return False
	return True

>>> def rank(matrix):
	colLength=len(matrix)
	rowLength=len(matrix[0])
	if colLength<rowLength:
		return colLength
	else:
		return rowLength

	
>>> def rps(p1Choice,p2Choice):
	p1Choice=p1Choice.upper()
	p2Choice=p2Choice.upper()
	if(p1Choice==p2Choice):
		return 0
	elif(p1Choice=='R' and p2Choice=='P') or \
	(p1Choice=='S' and p2Choice=='R') or \
	(p1Choice=='P' and p2Choice=='S'):
		return 2
	elif(p1Choice=='R' and p2Choice=='S') or \
	(p1Choice=='P' and p2Choice=='R') or \
	(p1Choice=='S' and p2Choice=='P'):
		return 1

#alternative solution to Hw5 #1
# for HW5 isPrime Problem, else statement is outside the loop because we need to go through THE ENTIRE LOOP before going to else.

#Hw5 #3                             
def playerHasLastInitial(filename,char):
	f = open(filename,'r')
        f.readline()
	while True:
		line = f.readline()
		if not line:
			return False
		name = line.split(',')[0]
		lastName=name.split()[1]
		if latInitial==char:

#readline appears twice because the first one skips the header row.

#Hw5 Factorial Problem
def MaxFactorial(n):
	i=1
	fv=1
	while True:
		nextFv=fv*(i+1)
		if nextFv > n:
			return i
		else:
			i+=1
			fv=nextFv
			return True
	f.close()


# Lecture Notes

        #sets vs lists
                [1,2,3,4,5]
                [1, 2, 3, 4, 5]
                >>> a=[1,2,3,4,5]
                >>> type(a)
                <class 'list'>
                >>> b=a={1,2,3,4,5}
                >>> type(b)
                <class 'set'>
                >>> b.add(6)
                >>> b
                {1, 2, 3, 4, 5, 6}

                >>> b.add('m')
                >>> b
                {1, 2, 3, 4, 5, 6, 'm'}
                >>> type(b)
                <class 'set'>
                a | b
                {1, 2, 3, 4, 5, 6, 'm'}
                >>> a&b
                {1, 2, 3, 4, 5, 6, 'm'}
                >>> a.union(b)
                {1, 2, 3, 4, 5, 6, 'm'}
                >>> a.difference(b)
                set()
                #order does not matter in sets. Plus sets do not have repeats.
                # sets aren't used that often
                #Brian considers sets precursers for dictionaries.
                #dictionaries however, are used a lot
                #dictionaries are also called maps or value stores
                a = {'a':1,'b':2}
                >>> a['a']
                1
                #dict also called json. but json needs to be imported in
                >>> import json
                >>> json.dumps('a')
                '"a"'
                >>> #dump plus an s dumps the json into a string
                >>> a
                {'a': 1, 'b': 2}
                'file = json.loads(f.read()) is something you can do to upload and read a json file'
                #similar to matrix stuff (lists within lists}, you can have objects within objets (dict)
                
                f=open(fileName,'r')
                lines=f.readlines()[1:]
                records=[]
                for line in lines:
                        words = line.split(',')
                        names=words[0].split()
                        player={
                                "firstName": names[0],
                                "lastName": names[1],
                                "age": int(words[1]),
                                "country":words[2]
                                }
                        records.append(player)
                filePrefix=filename.split('.')[0]
                f=open('{}.json'.format(filePrefix),'w')
                f.write(json.dumps #TS 8:10
