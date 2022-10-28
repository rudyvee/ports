from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
 
def test_port_number(host, port):
    # create and configure the socket
    with socket(AF_INET, SOCK_STREAM) as sock:
        #timeout
        sock.settimeout(3)
        try:
            sock.connect((host, port))
            return True
        except:
            return False
 
def port_scan(host, ports):
    print(f'Scanning {host}...')
    for port in ports:
        if test_port_number(host, port):
            print(f'> {host}:{port} open')
 
HOST = 'python.org'
PORTS = range(1024)
port_scan(HOST, PORTS)
