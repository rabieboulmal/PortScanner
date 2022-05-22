import sys
import getopt
import re
from portscanner import *
import pyfiglet


def main():
    # This is the main function
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:p:", ["ip=", "port="])

    except getopt.GetoptError:
        print('main.py -t <target> -p <port>')
        sys.exit(2)

    for opt, arg in opts:

        if opt == '-h':
            print('main.py -t <target> -p <port>')
            sys.exit()
        elif opt in ("-t", "--target"):
            target = arg

        elif opt in ("-p", "--port"):
            port = arg

    print(pyfiglet.figlet_format("PortScanner", font="digital"))

    # Verify if the target is Hostname, it will be converted to IP
    matched = re.match("[a-z]", target)
    if matched:
        target = resolv_host(target)
    # test if ip is a single one or a list of IPs
    target = ip_spliter(target)

    if type(target) == list:
        for t in target:
            print('\n' + '[-_0 Scanning Target] ' + str(t) + ':' + str(port))
            scan(target=t, port=port)
    else:
        print('\n' + '[-_0 Scanning Target] ' + str(target) + ':' + str(port))
        scan(target=target, port=port)


if __name__ == '__main__':

    main()
