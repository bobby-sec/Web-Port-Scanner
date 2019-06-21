print """
  y/////////oy                                d                dhhhd                                                                                  
 sssso+sso+++++y                           doo              yooo++++od                                                                                
d   s+s     s+++h                         h++s             os     o+s                                                                                 
   doos      hooh                         soos            sooy    y                                                                                   
   dooy       so    hsooooy    yooydsoooysoooooooh        soooooyh          dyooooy    dsooooos   hsos  hooooy   yooy  yooosh      yooooy   sosdhooosh
   dssy      ds   hsd dhsssshdyysssy dssyhysssdd           dssssssssyd    dsd dysss   sd   yssy  hdssssh dsssshddhssssd hssss    yh  yssshyhssssd ysd 
   dsssssyhhyy   hs      hsssd dsss       dsss                dhyssssss  yss    h   dsh    yssh    yssy    sssh   sssh    sss  dss   dsh    ysss      
   dsssyyyyh     ssh      dss   sss       dsss            yh      dhyssddssy        ssd    hssh    yssy    sssd   sssd    sss  ssshdhd      hsss      
    yyh          yyyd      yy   yyy       dyyy          dyyyd        yy  yyyy      hyyy    hyyh    yyyy    yyyd   yyyd    yyy  yyyyh        hyyy      
   dyh           dyyyd    hh    yyy        yyy           hyyyyh      h   dyyyyd   d hyyyd  hyyh    hyyh    yyyd   yyyd    yyy   yyyyh    d  hyyy      
  dhhhhh           hhhhhhhd     hhhhd      hhhhd          dhhhhhhhhhd      hhhhhh     hhhhh hhhhd  dhhhd   hhhhd  hhhhd   hhhh   hhhhhhd    dhhhh     
 dddddd              ddd         d           d                dddd           dd         d     d      d      d      d       d       dd         d       
"""
from socket import *
open_port=[]
setdefaulttimeout(0.1)
def scan(ip,port):
    try:
        s=socket(AF_INET,SOCK_STREAM)
        s.connect((ip,port))
        print "[+]Port %d is open"%port
        open_port.append(port)
    except:
        print "[-]Port %d is not open"%port


name=raw_input("Enter Domain Name: ")
tgtName = gethostbyaddr(name)
print "1 Search for specific port:"
print "2 Search specific port range:"
ans=raw_input("> ")
if ans=="1":
    port=int(raw_input("Port: "))
    scan(name,port)
elif ans=="2":
    st_p=int(raw_input("Starting Port: "))
    cl_p=int(raw_input("Closing Port: "))
    for i in range(st_p,cl_p+1):
        scan(name,i)
if len(open_port)==0:
    print "[-]No Open ports found on " +str(name) + "\n[+]Host name is: " + str(tgtName[0]) + "\n[+]Host Ip:"+str(tgtName[2])
else:
    print "[+]Open ports:" + str(open_port) + " on " +str(name) + "\n[+]Host name is: " + str(tgtName[0]) + "\n[+]Host Ip:"+str(tgtName[2])
