from socket import * 

msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n" 
 
# Choose a mail server (e.g. Google mail server) and call it mailserver mailserver = #Fill in start   #Fill in end 
mailServer = 'smtp.gmail.edu'

# Create socket called clientSocket and establish a TCP connection with mailserver   
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, 587))

recv = clientSocket.recv(1024) 
print(recv)
if recv[:3] != '220':
 	print('220 reply not received from server.') 

# Send HELO command and print server response. heloCommand = 'HELO Alice\r\n' clientSocket.send(heloCommand.encode()) recv1 = clientSocket.recv(1024).decode() print(recv1) if recv1[:3] != '250': 
heloCommand = 'HELO ALICE\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode
print(recv1)
if recv1[:3] != '250':  
    print('250 reply not received from server.') 
     
# Send MAIL FROM command and print server response. 
mailFrom = "MAIL FROM: <**Enter mail from address**>>\r\n"
clientSocket.send(mailFrom)
recv2 = clientSocket.recv(1024)
print(recv2)
if recv2[:-2] != '250':
    print('250 reply not received from server.')
	 

# Send RCPT TO command and print server response.  
rcptto = "RCPT TO: <**Enter mail to address**>>\r\n"
clientSocket.send(rcptto)
recv3 = clientSocket.recv(1024)
if recv3[:9] != "250 2.1.5":
       print('250 2.1.5 reply not received from server.')


# Send DATA command and print server response.  
data = 'DATA\r\n'
clientSocket.send(data)
recv4 = clientSocket.recv(1024)
if recv4[:3] != 354:
       print('354 reply not received from server.')


# Send message data. 
print('msg to send: ')
print(msg)
clientSocket.send(msg.encode()) 

# Message ends with a single period. 
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024)
print(recv5[:2])
if recv5[:9] != '250 2.0.0':
    print('250 reply not received from server.')

# Send QUIT command and get server response. 
# Fill in start 
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024)
print(recv6[:-2])
if recv6[:-2] != '221 2.0.0':
    print('221 reply not received from server.')
clientSocket.close()
print('Mail sent, Great Success!')
# Fill in end 
  
#Fill in end recv = clientSocket.recv(1024).decode() print(recv) if recv[:3] != '220': 
 	# print('220 reply not received from server.') 
 
# Send HELO command and print server response. heloCommand = 'HELO Alice\r\n' clientSocket.send(heloCommand.encode()) recv1 = clientSocket.recv(1024).decode() print(recv1) if recv1[:3] != '250': 
    # print('250 reply not received from server.') 
     
# Send MAIL FROM command and print server response. 
# Fill in start 
 
# Fill in end 
 
# Send RCPT TO command and print server response.  
# Fill in start 
 
# Fill in end 
 
# Send DATA command and print server response.  
# Fill in start 
 
# Fill in end 
 
# Send message data. 
# Fill in start 
 
# Fill in end 
# Message ends with a single period. 
# Fill in start 
 
# Fill in end 
 
# Send QUIT command and get server response. 
# Fill in start 
 
# Fill in end 
