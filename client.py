import socket
import threading


class Client:
    def __init__(self):
        host = "24.144.85.169"
        port = 8188
        self.socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_connection.connect((host, port))
        self.ip = str(socket.gethostbyname(socket.gethostname()))
        print(self.ip)
        self.game_state = None
        self.update_game_state_thread = threading.Thread(target=self.update_game_state)
        self.update_game_state_thread.start()

    def update_game_state(self):
        buffer = ""
        try:
            while True:
                data = self.socket_connection.recv(1024).decode()
                buffer += data
                while "\n" in buffer:
                    message, buffer = buffer.split("\n", 1)
                    self.game_state = message
                    if not data:
                        print("Server Disconnected")
                        self.socket_connection.close()
        except Exception as e:
            print(e)
            print("Server Error")
            self.socket_connection.close()

    def send_data(self, data):
        try:
            # print("data sent")
            self.socket_connection.sendall(data.encode())
        except Exception as e:
            print(e)

    def stop(self):
        self.socket_connection.close()
# c = Client()
