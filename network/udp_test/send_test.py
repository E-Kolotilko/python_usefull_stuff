import socket
import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', dest='ip', default='127.0.0.1', help='ip address of receiver')
    parser.add_argument('-p','--port', type=int, dest='port', help='port of receiver')
    return parser


def main(ip, port, message):
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #INTERNET, UDP
  sock.sendto(message, (ip, port))


if __name__ == '__main__':
    parser =get_parser();
    parse_result = parser.parse_args()
    ip = parse_result.ip
    port = parse_result.port if parse_result.port else int(input('Enter port: '))
    message = b'Hello'
    print("UDP target IP: %s" % ip)
    print("UDP target port: %s" % port)
    print("message: %s" % message)
    main(ip, port, message)
  
