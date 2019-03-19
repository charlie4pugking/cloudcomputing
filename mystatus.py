from flask import Flask
import socket
import multiprocessing
from psutil import virtual_memory
import json

app = Flask(__name__)


@app.route("/status")
def mystatus():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(socket.gethostname())
    amount = multiprocessing.cpu_count()
    mem = virtual_memory()
    ram = round((mem.total/1000000000), 2)

    mylist = {"Hostname": hostname, "IP Address": ip, "CPUS": amount, "Memory": ram}

    jsonlist = json.dumps(mylist)

    return jsonlist


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
