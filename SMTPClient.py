# Router 66 
from socket import *
import ssl
import base64
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
sender = "ashtona123212@gmail.com"
receiver = "ashtona123212@gmail.com"
# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start
mailserver = ('smtp.gmail.com', 587)
#Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.

eheloCommand = "EHLO Alice\r\n"
clientSocket.send(eheloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# StartTTLS
starttls = "STARTTLS\r\n"
clientSocket.send(starttls.encode())
recv_tls = clientSocket.recv(1024).decode()
print(recv_tls)

# Wrap the socket with SSL
context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname=mailserver[0])

#EHLO AGAIN
clientSocket.send(eheloCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Auth Login
clientSocket.send("AUTH LOGIN\r\n".encode())
print(clientSocket.recv(1024).decode())

clientSocket.send(base64.b64encode(sender.encode()) + b"\r\n")
print(clientSocket.recv(1024).decode())

clientSocket.send(base64.b64encode("APP_PASSWD_HERE_NO_SPACE".encode()) + b"\r\n")
print(clientSocket.recv(1024).decode())

# Send MAIL FROM command and print server response.
# Fill in start

mailFrom = f"MAIL FROM:<{sender}>\r\n"
clientSocket.send(mailFrom.encode())

recv3 = clientSocket.recv(1024).decode()
print(recv3)

# Fill in end

# Send RCPT TO command and print server response.
# Fill in start

rcptTo= f"RCPT TO:<{receiver}>\r\n"
clientSocket.send(rcptTo.encode())

recv4 = clientSocket.recv(1024).decode()
print(recv4)

# Fill in end

# Send DATA command and print server response.
# Fill in start

data = "DATA\r\n"
clientSocket.send(data.encode())

recv5 = clientSocket.recv(1024).decode()
print(recv5)

# Fill in end

# Send message data.
# Fll in start

clientSocket.send(msg.encode())

# Fill in end

# Message ends with a single period.
# Fill in start

clientSocket.send(endmsg.encode())
# Fill in end

# Send QUIT command and get server response.
# Fill in start

quitCom = "QUIT\r\n"
clientSocket.send(quitCom.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
#Fill in end
clientSocket.close()