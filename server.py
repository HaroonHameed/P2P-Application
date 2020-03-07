from socket import *
import threading
import random
import json
import pickle


class server:
    counter = 0
    serverPort = random.randint(7000,9000)
    print(serverPort)
    
    def __init__(self):
        self.peer_list = []
        self.file_list = []
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind(('',self.serverPort))
        self.serverSocket.listen(10)
        
        self.listen()

    def listen(self):
        while True:
            
            self.client_conn, self.addr = self.serverSocket.accept()
            
            threading.Thread(target = self.listenToclient).start()
            print(self.addr)
            # self.listenToclient()
    # def add_peers(self,client_conn,addr):
    #     self.peer.append(addr)




    def listenToclient(self):
        # self.add_peers(client_conn,addr)
        while True:
            print("hello")
            data = pickle.loads(self.client_conn.recv(4096))
            print(data)
            if(data[0] == "peer_port_info"):
                self.peer_list.append(data)
                self.client_conn.sendall("done".encode())
            if(data[0] == "get_peers_info"):
                print("line 39")
                data = pickle.dumps(self.peer_list)
                self.counter+=1
                print(self.counter)
                s = self.client_conn.sendall(data)
                print("status",s)
            if(data[0] == "file_upload"):
                self.file_list.append(data)
                self.client_conn.sendall("done file saved ".encode())
            if (data[0]=="get_file_upload"):
                data = pickle.dumps(self.file_list)
                # self.counter+=1
                # print(self.counter)
                s = self.client_conn.sendall(data)
                print("status",s)

        # print("message recv from client_conn: ", fileName)
        # fileName = fileName.upper()
        # client_conn.send(fileName.encode())
        # print(self.peer)
        # self.client_conn.close()

    # def dict_to_binary(self,the_dict):
    #     data_string = pickle.dumps(the_dict) 
    #     return data_string


    def binary_to_dict(self,the_binary):
        data_loaded = pickle.loads(the_binary) #data loaded.
        return data_loaded

    
    
server = server()


