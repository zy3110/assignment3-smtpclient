from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    # print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
       print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print('after helo :\t' +recv1) 
    if recv1[:3] != '250':
       print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailCommand = 'MAIL FROM: <test1@gmail.com>\r\n'
    clientSocket.send(mailCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print('after mail :\t' + recv1) 
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptCommand = 'RCPT TO: <test2@gmail.com>\r\n'
    clientSocket.send(rcptCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print('after rcpt :\t' + recv1) 
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print( 'after data :\t' + recv1) 
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    msgCommand = msg
    clientSocket.send(msgCommand.encode())
    # recv1 = clientSocket.recv(1024).decode()
    # print( 'after msg :\t' + recv1) 
    # print(recv1) 
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    endmsgCommand = endmsg
    clientSocket.send(endmsgCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print('after endmsg :\t' + recv1) 
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print('after quit :\t' + recv1) 
    if recv1[:3] != '221':
        print('250 reply not received from server.')
    
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')