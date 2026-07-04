def connect(host,port=1080,protocol="udp"):
    print(f" I am using {host} with port {port} and protocol {protocol}")
connect("locolhost")
connect("internet",protocol="http")
connect("intranet",1999,"tcp")
connect("Lan",2000)