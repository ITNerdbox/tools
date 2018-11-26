from socket import * 

if __name__ == '__main__':
    targetIP = "10.0.3.140"
    print 'Starting scan on host ', targetIP

    #scan reserved ports
    for i in range(20, 2000):
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((targetIP, i))

        if(result == 0) :
            print 'Port %d: OPEN' % (i,)
        s.close()
 
