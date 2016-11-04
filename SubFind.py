import os
import sys
import argparse
import socket
import dns.resolver

class TColors:
    G = '\033[92m' #green
    Y = '\033[93m' #yellow
    B = '\033[94m' #blue
    R = '\033[91m' #red
    W = '\033[0m'  #white


def CNAME_Check():
    check = dns.resolver.query(normal2, 'CNAME')
    print

def save_to_file(filename, ip): ##Gotta fix this, add sorting feature if possible.
    with open(str(filename), 'ab') as f:
            f.write(ip+'\n')

def parse_args():
    parser = argparse.ArgumentParser(epilog= TColors.B + '\tCheck Alias Addresses and pull IP for more recon. Info is logged in Ip_results.\n' + TColors.G )
    parser._optionals.title = TColors.Y + 'Run with python ./' + TColors.G
    return parser.parse_args()

def IPLookup():
    file_name = raw_input('Select the file to use:\n')
    with open(file_name) as f:
        print TColors.R + "Sending query.." + TColors.G
        print TColors.B + "Info:\n" + TColors.G
        for url in f:
            try:
                url = url.strip()
                data = socket.gethostbyname_ex(url)
                Info = ("\n\n IP: "+repr(data))
                ip = data
                normal = data[1]
                normal2 = "".join(normal)
                alias = data[0:1]
                alias2 = "".join(alias)
                filelog = 'ip_results.txt'
                for ip in data[2]:
                    save_to_file(filelog, ip)
                    try:
                        valid = ip
                        print TColors.Y + '%s is vaild for %s, Version: %s\n' % (ip, normal2, '4') + TColors.G
                    except ValueError:
                        print "Not vaild."
                print TColors.R + (normal2 + " is an alias for " + alias2 + "\n")

            except socket.gaierror:
                print "Connection error...\n"
        
def main():
    args = parse_args()
    IPLookup()
    save_to_file = args.output


if __name__ == "__main__":
    main()
