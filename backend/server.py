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
        #print(player['pos'])
        for food in foodList:
            if player["pos"][0]+12 <= food[0] and food[0] <= player["pos"][0]+40+player["food_consumed"] and player["pos"][1]+12 <= food[1] and food[1] <= player["pos"][1]+40+player["food_consumed"]:
                foodList.remove(food)
                player["food_consumed"] = player["food_consumed"]+1
                print(player['food_consumed'])
                # print(player["food_consumed"])
                allplayerdata[addr] = json.dumps(player)
                allplayerdata["food"] = json.dumps(foodList)
                break
            else:
                pass
                #print(f"x: {player['pos'][0] + 12} < {food[0]} < {player['pos'][0] + 40}")
                #print(f"y: {player['pos'][1] + 12} < {food[1]} < {player['pos'][1] + 40}")
    except Exception as e:
        print(e)
        print("error with food checker")

def client_handler(addr, conn):
    while True:
        try:
            buffer = ""
            data = conn.recv(1024).decode()
            buffer += data
            if "\n" in buffer:
                message, buffer = buffer.split("\n", 1)
                allplayerdata[addr] = message
                check_food_collision(addr)
                conn.send((json.dumps(allplayerdata) + "\n").encode())
            else:
                allplayerdata[addr] = data
                check_food_collision(addr)
                conn.send((json.dumps(allplayerdata) + "\n").encode())
        except Exception as e:
            del allplayerdata[addr]
            print(addr + ' has disconnected')
            conn.close()
            break


def foodProduction():
    while True:
        global foodList
        maxFood = 10
        sleep(randint(2, 5))
        if len(foodList) < maxFood:
            foodList.append([randint(10, 790), randint(10, 590)])
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