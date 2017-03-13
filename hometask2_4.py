#! python
#Hometask2_4 by ILYA_KHAMIAKOU
iplist=[0] #empty list to save IPs
for line in open('access.log'): #opening logfile. Its attached in my repo's root folder
        ip = line.split(' ')[0]
        #print ip
        iplist.append(ip)
#print iplist #uncomment if u want to see iplist
ip_counter = {} #creating a dict to store IP
#counting IPs
for ip in iplist:
    if ip in ip_counter:
        ip_counter[ip] += 1
    else:
        ip_counter[ip] = 1
topIP = sorted(ip_counter, key = ip_counter.get, reverse = True) #topIP saved and sorted
top= topIP[:10] #enter the number of unique IPs you want to see
print top #showing results

