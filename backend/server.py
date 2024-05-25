import socket
import json
import threading
from time import sleep
from random import randint

allplayerdata = {}
foodList = []


def check_food_collision(addr):
    global foodList, allplayerdata
    try:
        player = json.loads(allplayerdata[addr])
        #print(str(player["pos"][0]+12)+ "<+" +" x " + "<=" +str(player["pos"][0]+37))
        #print(str(player["pos"][1] + 12) + "<+" + " y " + "<=" + str(player["pos"][1] + 37))
        #print(foodList)
        for food in foodList:
            if player["pos"][0]+12 <= food[0] and food[0] <= player["pos"][0]+40 and player["pos"][1] <= food[0]+12 and food[1] <= player["pos"][1]+40:
                foodList.remove(food)
                player["food_consumed"] = player["food_consumed"]+1
                # print(player["food_consumed"])
                allplayerdata[addr] = json.dumps(player)
                allplayerdata["food"] = json.dumps(foodList)
        allplayerdata[addr] = json.dumps(player)
        allplayerdata["food"] = json.dumps(foodList)
    except Exception as e:
        print(e)
        print("error with food checkr")

def client_handler(addr, conn):
    while True:
        try:
            buffer = ""
            data = conn.recv(1024).decode()
            buffer += data
            if "\n" in buffer:
                message, buffer = buffer.split("\n", 1)
                allplayerdata[addr] = message
                #print(allplayerdata[addr])
                check_food_collision(addr)
                conn.send(json.dumps(allplayerdata).encode())
            else:
                allplayerdata[addr] = data
                #print(allplayerdata[addr])
                check_food_collision(addr)
                conn.send(json.dumps(allplayerdata).encode())
        except Exception as e:
            del allplayerdata[addr]
            print(addr + ' has disconnected')
            conn.close()
            break





def foodProduction():
    while True:
        global foodList
        maxFood = 1
        sleep(randint(2, 5))
        if len(foodList) < maxFood:
            foodList.append([randint(0, 790), randint(0, 590)])
            allplayerdata['food'] = json.dumps(foodList)
            print(foodList)

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
            fp_thread = threading.Thread(target=foodProduction)
            client_thread.start()
            fp_thread.start()


if __name__ == "__main__":
    main()