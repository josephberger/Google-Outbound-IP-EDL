import subprocess  
from subprocess import PIPE  
import re  
import argparse

from flask import Flask
 
#create the parser
parser = argparse.ArgumentParser()

#add args
parser.add_argument(
    "--ip_address",
    "-i",
    default="0.0.0.0",
    action="store",
    type=str,
    help="IP address to bind to (default: 0.0.0.0)",
)

parser.add_argument(
    "--port",
    "-p",
    type=int,
    default="5000",
    action="store",
    help="port for example (default: 5000)",
)

args = parser.parse_args()

app = Flask(__name__)

@app.route('/')
def edl():
    p1 = subprocess.Popen(['nslookup', '-q=TXT','_spf.google.com','8.8.8.8'], stdout=PIPE, stderr=PIPE)  
  
    output = p1.communicate()[0].decode()  

    domains = re.findall("include:(.*?) ",output) 

    subnets = []

    for d in domains:
        p1 = subprocess.Popen(['nslookup', '-q=TXT',d,'8.8.8.8'], stdout=PIPE, stderr=PIPE)
        output = p1.communicate()[0].decode()
        for s in re.findall(r"ip\d:(.*?) ",output):
            subnets.append(s)

    return("\n".join(subnets))
 
if __name__ == '__main__':

    app.run(host=args.ip_address, port=args.port)
