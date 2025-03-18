import socket  # noqa: F401


#handle an incoming HTTP request by sending a 200 OK response
def handle_request(client_socket):
    #read data from the client
    client_socket.recv(1024)

    #send a 200 OK response
    response = "HTTP/1.1 200 OK\r\n\r\n"
    client_socket.send(response.encode())


def main():
    # You can use print statements as follows debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

 #create a TCP/IP socket
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    try:
        while True:
        # wait for a connectio
         print("waiting for a connection....")
         client_socket, addr = server_socket.accept()
         print(f"Connection from {addr} has been established")

         #handle the client's request
         handle_request(client_socket)

            #close the connection to the client
         client_socket.close()
    except KeyboardInterrupt:
        print("\nServer is shitting down.")


if __name__ == "__main__":
    main()
