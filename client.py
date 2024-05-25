import socket
import threading


class Client:
    def __init__(self):
        host = "192.168.1.43"
        port = 8188
        self.socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_connection.connect((host, port))
        self.ip = str(socket.gethostbyname(socket.gethostname()))  # str(self.socket_connection.rev(1024).decode())
        self.game_state = None
        self.update_game_state_thread = threading.Thread(target=self.update_game_state)
        self.update_game_state_thread.start()

    def update_game_state(self):
        try:
            while True:
                data = self.socket_connection.recv(1024)
                self.game_state = data.decode()
                if not data:
                    print("Server Disconnected")
                    self.socket_connection.close()
                print(data.decode())
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
