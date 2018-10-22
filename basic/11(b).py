def update(a,value):
			if a==[]:
					a.insert(0,value)
					return a
			elif value<a[0]:
					a.insert(0,value)
					return a
			else:
				a[1:]=update(a[1:],value)
				return a
