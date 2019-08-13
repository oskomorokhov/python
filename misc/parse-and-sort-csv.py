'''
stats.csv

#host,port,inbytes,outbytes
sw01,g0/1,10001,20005
sw02,eth1/1,10003,20003
rtr01,gi1/2,10002,20001
rtr02,gi3/1,10004,20004
sw03,te1/1,10005,20002

'''

with open("stats.csv", "r") as f:
    l = [line.rstrip().split(",") for line in f if line[0] != "#"]
    max_in = max(list(zip(*l))[2])
    max_out = max(list(zip(*l))[3])
    print("MAX INPUT: ", [','.join(i) for i in l if max_in in i][0])
    print("MAX OUTPUT: ",  [','.join(i) for i in l if max_out in i][0])

'''
... 
MAX INPUT:  sw03,te1/1,10005,20002
MAX OUTPUT:  sw01,g0/1,10001,20005
'''
