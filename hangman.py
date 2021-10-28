print('1- kids','\n2-country','\n3-movies','\n4-Famous peoples','\n5-python words')
kids=['queen',"apple","mango","kite","lion"]
countries=['india','america','dubai','france','bangladesh']
movies=['sholay','krish','avengers','veer','gupt','dhoom','tubelight','baby','holiday','sooryavansham']
famous_peoples=['bhagatsingh','rajguru','sukhdev','ravindranathtegor','gandhi','jawaharlalnehru','aarif','mangalpanday','bahadurshahzafar','ranilaxmibai']
python=['append','replace','operators','list','dictionary','intezer','python','whileloop','error','syntext']
import random
topic=int(input('enter your number   -'))
if topic==1:
	a=random.randint(0,len(kids)-1)
	b=list(kids[a])
	c=list('_'*len(b))
	d=0
	e=0
	c=list('_'*len(b))
	h=[]
	print(c)
	while e<len(b):	
		f=input('               ')
		if f not in h:
			if f in b:
				for g in range(0,len(c)):
					if f==b[g]:
						e+=1
						h.append(f)
						c.pop(g)
						c.insert(g,f)
						print(c)				
			else:
				d+=1
				if d==1:
					print('\n-___-','\n|    ','\n|    ','\n|    ','\n|    ','\n====')
				elif d==2:
					print('\n-___-','\n|   ¦','\n|    ','\n|    ','\n|    ','\n====')
				elif d==3:
					print('\n-___-','\n|   ¦','\n|   o','\n|    ','\n|    ','\n====')
				elif d==4:
					print('\n-___-','\n|   ¦','\n|   o','\n|   |','\n|    ','\n====')
				elif d==5:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|','\n|    ','\n====')
				elif d==6:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|    ','\n====')
				elif d==7:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|  /','\n|    ','\n====')
				elif d==8:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|  / \.','\n|    ','\n====')
					print('Sorry you loose the game')
					print(b)
					break
elif topic==2:
	a=random.randint(0,len(countries)-1)
	b=list(countries[a])
	c=list('_'*len(b))
	d=0
	e=0
	c=list('_'*len(b))
	h=[]
	print(c)
	while e<len(b):	
		f=input('               ')
		if f not in h:
			if f in b:
				for g in range(0,len(c)):
					if f==b[g]:
						e+=1
						h.append(f)
						c.pop(g)
						c.insert(g,f)
						print(c.pop())				
			else:
				d+=1
				if d==1:
					print('\n-___-','\n|    ','\n|    ','\n|    ','\n|    ','\n====')
				elif d==2:
					print('\n-___-','\n|   ¦','\n|    ','\n|    ','\n|    ','\n====')
				elif d==3:
					print('\n-___-','\n|   ¦','\n|   o','\n|    ','\n|    ','\n====')
				elif d==4:
					print('\n-___-','\n|   ¦','\n|   o','\n|   |','\n|    ','\n====')
				elif d==5:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|','\n|    ','\n====')
				elif d==6:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|    ','\n====')
				elif d==7:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|  /','\n|    ','\n====')
				elif d==8:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|  / \.','\n|    ','\n====')
					print('Sorry you loose the game')
					print(b)
					break
elif topic==3:
	a=random.randint(0,len(movies)-1)
	b=list(movies[a])
	c=list('_'*len(b))
	d=0
	e=0
	c=list('_'*len(b))
	h=[]
	print(c)
	while e<len(b):	
		f=input('               ')
		if f not in h:
			if f in b:
				for g in range(0,len(c)):
					if f==b[g]:
						e+=1
						h.append(f)
						c.pop(g)
						c.insert(g,f)
						print(c)				
			else:
				d+=1
				if d==1:
					print('\n-___-','\n|    ','\n|    ','\n|    ','\n|    ','\n====')
				elif d==2:
					print('\n-___-','\n|   ¦','\n|    ','\n|    ','\n|    ','\n====')
				elif d==3:
					print('\n-___-','\n|   ¦','\n|   o','\n|    ','\n|    ','\n====')
				elif d==4:
					print('\n-___-','\n|   ¦','\n|   o','\n|   |','\n|    ','\n====')
				elif d==5:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|','\n|    ','\n====')
				elif d==6:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|    ','\n====')
				elif d==7:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|  /','\n|    ','\n====')
				elif d==8:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|  / \.','\n|    ','\n====')
					print('Sorry you loose the game')
					print(b)
					break
elif topic==4:
	a=random.randint(0,len(famous_peoples)-1)
	b=list(famous_peoples[a])
	c=list('_'*len(b))
	d=0
	e=0
	c=list('_'*len(b))
	h=[]
	print(c)
	while e<len(b):	
		f=input('               ')
		if f not in h:
			if f in b:
				for g in range(0,len(c)):
					if f==b[g]:
						e+=1
						h.append(f)
						c.pop(g)
						c.insert(g,f)
						print(c)				
			else:
				d+=1
				if d==1:
					print('\n-___-','\n|    ','\n|    ','\n|    ','\n|    ','\n====')
				elif d==2:
					print('\n-___-','\n|   ¦','\n|    ','\n|    ','\n|    ','\n====')
				elif d==3:
					print('\n-___-','\n|   ¦','\n|   o','\n|    ','\n|    ','\n====')
				elif d==4:
					print('\n-___-','\n|   ¦','\n|   o','\n|   |','\n|    ','\n====')
				elif d==5:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|','\n|    ','\n====')
				elif d==6:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|    ','\n====')
				elif d==7:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|  /','\n|    ','\n====')
				elif d==8:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|  / \.','\n|    ','\n====')
					print('Sorry you loose the game')
					print(b)
					break
elif topic==5:
	a=random.randint(0,len(python)-1)
	b=list(python[a])
	c=list('_'*len(b))
	d=0
	e=0
	c=list('_'*len(b))
	h=[]
	print(c)
	while e<len(b):	
		f=input('               ')
		if f not in h:
			if f in b:
				for g in range(0,len(c)):
					if f==b[g]:
						e+=1
						h.append(f)
						c.pop(g)
						c.insert(g,f)
						print(c)				
			else:
				d+=1
				if d==1:
					print('\n-___-','\n|    ','\n|    ','\n|    ','\n|    ','\n====')
				elif d==2:
					print('\n-___-','\n|   ¦','\n|    ','\n|    ','\n|    ','\n====')
				elif d==3:
					print('\n-___-','\n|   ¦','\n|   o','\n|    ','\n|    ','\n====')
				elif d==4:
					print('\n-___-','\n|   ¦','\n|   o','\n|   |','\n|    ','\n====')
				elif d==5:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|','\n|    ','\n====')
				elif d==6:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|    ','\n====')
				elif d==7:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|  /','\n|    ','\n====')
				elif d==8:
					print('\n-___-','\n|   ¦','\n|   o','\n|  /|\.','\n|  / \.','\n|    ','\n====')
					print('Sorry you loose the game')
					print(b)
					break