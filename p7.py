from matplotlib import pyplot as p
pro_na=["intel","amd","snapdragon","tensor"]
use=[200,180,250,256]
p.bar(pro_na,use,color="yellow",width=0.2)
p.xlabel("processors"),p.ylabel("no.of users")
p.title("processor users in a community")
p.show()
