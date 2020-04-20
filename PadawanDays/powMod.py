
"""
Other way to solve:

a,b,m = [int(input()) for el in '123']
print(pow(a,b),pow(a,b,m),sep='\n')

-----------------------------------------------

inp = (int(input()),int(input()),int(input()))
print("{0}\n{1}".format(pow(inp[0], inp[1]), pow(*inp)))

"""

def powFunc():

	a,b,m = [int(input()) for el in '285']
	
	if 0 <= a <= 10:
	    if a <= b <= 10:
	        if 2 <= m <= 1000:
	            print(pow(a,b))
	            print(pow(a,b,m))
	        else:
	            print('m -> [2,1000]')
	    else:
	        print('b -> [0,10]')
	else:
	    print('a -> [0,10]')