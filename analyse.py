import json
import neurolab as nl
import matplotlib.pyplot as pl

file=open('replay.txt','r')
d={}
route = 600
userid=1
play = [[0 for col in range(route+20)] for row in range(10)] 
for line in file.readlines():
	spl=line.split(' ')

	if spl[0]=='score':
		if int(spl[3])>route:
			break;

		play[d[spl[2].split(':')[0]]][int(spl[3])]=(int(spl[5])+int(spl[4]))
		
	if spl[0]=='reg:':
		id=spl[2].split('=')[1]
		
		d[id]=userid
		userid=userid+1


for i in d.keys():
	pl.plot(play[d[i]][1:route],'id='+i)


pl.legend('upper left', numpoints=1)
pl.xlabel('route number')
pl.ylabel('total money')

pl.show()
