# on going

def cmdList():


    N = 5
    cmdList = []

	for el in range(N):
		s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != "print":
            cmd += "("+ ",".join(args) +")"
            eval("cmdList. "+cmd)
        else:
            print(cmdList)