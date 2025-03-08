import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")


    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client_connection, client_address =server_socket.accept() # wait for client
# get client request
    request = client_connection.recv(1024).decode
    response= b"HTTP/1.1 200 OK\r\n\r\n"
    server_socket.send(response)
    server_socket.close()
    print(response)


if __name__ == "__main__":
    main()
