# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    # server_socket.accept() # wait for client
    # server_socket.accept()[0].sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    connection, address = server_socket.accept()
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(data.decode())
            if (data.split(b"\r\n")[0].split(b" ")[1] != b"/"):
                response = b"HTTP/1.1 404 Not Found\r\n\r\n"
            else:
                response = b"HTTP/1.1 200 OK\r\n\r\n"
            print(response)
            connection.sendall(response)



if __name__ == "__main__":
    main()
