import socket
import json
import threading

allplayerdata = {}

def client_handler(addr, conn):
    while True:
        try:
            data = conn.recv(1024).decode()
            allplayerdata[addr] = data
            print(allplayerdata[addr])
            conn.send(json.dumps(allplayerdata).encode())
        except Exception as e:
                del allplayerdata[addr]
                print(addr + ' has disconnected')
                conn.close()
                break


def main():
    HOST = ''
    PORT = 8188

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        print("Server Started")
        server.listen(3)
        while True:
            conn, addr = server.accept()
            print(f"Connection Received from {addr}")
            allplayerdata[addr[0]] = {}
            client_thread = threading.Thread(target=client_handler, args=(addr[0], conn,))
            client_thread.start()


if __name__ == "__main__":
    main()