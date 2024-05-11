import socket
import threading
import json

class Client:
    def __init__(self):
        host = "192.168.1.25"
        port = 8188
        self.socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_connection.connect((host, port))
        self.ip = "" #str(self.socket_connection.recv(1024).decode())
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
                    break  # Exit the loop if no data received
        except Exception as e:
            self.socket_connection.close()
            print(e)
            print("Server Error")
        finally:
            self.socket_connection.close()

    def send_data(self, data):
        try:
            self.socket_connection.send(data.encode())
        except Exception as e:
            print(e)

    def stop(self):
        self.socket_connection.close()


#c = Client()
