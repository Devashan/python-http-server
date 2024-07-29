# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    connection, address = server_socket.accept()
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(data.decode())
            if (data.split(b"\r\n")[0].split(b" ")[1] == b"/"):
                response = b"HTTP/1.1 200 OK\r\n\r\n"
            elif (data.split(b"\r\n")[0].split(b" ")[1].startswith(b"/echo/")):
                echo_string = data.split(b"\r\n")[0].split(b"/echo/")[1].split(b" ")[0]
                string_length = len(echo_string)
                str_type = 'text/plain'
                response = b"HTTP/1.1 200 OK\r\nContent-Type: " + str_type.encode() + b"\r\nContent-Length: " + str(string_length).encode() + b"\r\n\r\n" + echo_string
            elif (data.split(b"\r\n")[0].split(b" ")[1] == b"/user-agent"):
                user_agent = data.split(b"\r\n")[1].split(b"User-Agent: ")[1].split(b"\r\n")[0]
                user_agent_length = len(user_agent)
                str_type = 'text/plain'
                response = b"HTTP/1.1 200 OK\r\nContent-Type: " + str_type.encode() + b"\r\nContent-Length: " + str(user_agent_length).encode() + b"\r\n\r\n" + user_agent
            else:
                response = b"HTTP/1.1 404 Not Found\r\n\r\n"
            print(response)
            connection.sendall(response)



if __name__ == "__main__":
    main()
