'''
servers = ["web1", "web2", "web3"]
print(f"servers are {servers}")
'''

'''
cpu = 95

if cpu>90:
    print("High cpu alert")
   '''
"""
status = "DOWN"

if status == "DOWN":
    print("Restart Service")
"""

"""    
cpu = 92

if cpu>90:
    print(f"ALERT: HIGH CPU USAGE is {cpu}%")
"""
"""
server = "UP"

if server == "UP":
    print(f"check server status: {server}")
"""   
"""
memory = 88
if (memory>85):
    print(f"High Memory usage")
"""  
"""
service = "stopped"

if(service == "stopped"):
    print(f"service is down: {service}")
"""
"""
cpu = 90
if(cpu>90):
    print("High cpu alert")
else:
    print("Normal usage")
 """ 
 
"""
services = ["nginx", "mysql", "redis"] 
for servers in services:
    print(f"servers are {services}")
"""

"""
servers = ["web1", "web2", "web3"]
for server in servers:
    print(f"web servers are: {server}")  
"""   
"""
servers = ["web1", "db1", "web2"]

for server in servers:
    if "web1" in servers:
        print(f"server = {servers}")
""" 

"""
servers = ["web1", "db1", "web2"]
for server in servers:
    if(server == "db1"):
        print(f"{server} database server found")
        
servers = ["web1", "web2", "db1"]
for server in servers:
    if server == "web1":
        print(f"{server}: web server exist")
"""
"""
servers = ["web1", "web2", "db1", "cache1"]
for server in servers:
    if "db1" in server:
        print(f"found db server {server}")
        
services = ["nginx", "apache", "mysql"]
for server in services:
    if "mysql" in server:
        print(f"database service found: {server}")
"""     

cpu_usage = [45, 60, 95, 70]

for cpu in cpu_usage:
    if cpu>80:
        print(f"High cpu detected: {cpu}%")