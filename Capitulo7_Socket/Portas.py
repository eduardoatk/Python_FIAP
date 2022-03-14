import socket

print("------------------------------")
print("     PORTAS DO COMPUTADOR     ")
print("------------------------------")
print("DOMAIN:", socket.getservbyname("domain"))
print("HTTP:", socket.getservbyname("http"))
print("FTP:", socket.getservbyname("ftp"))
