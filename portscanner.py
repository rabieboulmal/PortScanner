import socket
import sys
from IPy import IP


def scan(**kwargs):

    target = kwargs['target']
    port = kwargs['port']

    # Check if IP is valid
    check_ip(target)

    if port:
        port = port_spliter(port)
        if type(port) == list:
            for p in port:
                scan_port(target, int(p))
        else:
            scan_port(target, int(port))
    else:
        for port in range(1, 65535):
            scan_port(target, port)

# This is a Port spliter if input port is a range
# The function will split it in a list


def port_spliter(port):
    if port.find('-') != -1:
        port = port.split('-')
        ports = []
        for p in range(int(port[0]), int(port[1])+1):
            ports.append(p)
        return ports
    else:
        return port

# This function take the first Ip and the last one
# and list all IPs from start till end in a list


def ip_lister(target1, target2):
    ip1_splited = target1.split('.')
    ip2_splited = target2.split('.')
    targets = []
    try:
        for i in range(int(ip1_splited[-1]), int(ip2_splited[-1])+1):
            targets.append('.'.join(ip1_splited[:-1])+'.'+str(i))
    except:
        print('Not the same range...')
    return targets


# This is a IP spliter if input IP is a range
# The function will split it in a list
def ip_spliter(ip):
    if ip.find('-') != -1:
        ip = ip.split('-')
        ip1 = ip[0]
        ip2 = ip[1]
        targets = ip_lister(ip1, ip2)
        return targets
    else:
        return ip

# This is an IP checker if the input not in the form "X.X.X.X"
# It will crash with ValueError message


def check_ip(target):
    try:
        IP(target)
        return(IP)
    except ValueError:
        print('[-_0] Invalid IP address')
        exit()

# This function convert name to IP
# example: google.com -> 142.250.200.142


def resolv_host(target):
    return socket.gethostbyname(target)

# This function take the IP and port as input and then open


def scan_port(target, port):

    try:
        # Create socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        # returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        else:
            print("Port {} is closed".format(port))
        s.close()

    except socket.error:
        print('[-_0] Could not create socket')
        exit()
    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
