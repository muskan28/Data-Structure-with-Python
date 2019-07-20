def Tower(n,beg,aux,end):
	if n==1:
		print("Move disk",1,"from",beg," to ",end)
		return
	#move n-1 disks from beg to end
	Tower(n-1,beg,end,aux)
	print("Move disk",n,"from",beg," to ",end)
	#move n-1 disks from peg aux to peg end
	Tower(n-1,aux,beg,end)
	return
Tower(3,'A','B','C')