# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 04:22:45 2021

@author: Thien Tran
"""
import grpc
import MessageDelivery_pb2
import MessageDelivery_pb2_grpc
import logging
from concurrent import futures

class Branch(MessageDelivery_pb2_grpc.MsgDeliveryServicer):

    def __init__(self,id,balance,branches):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.stubList = list()
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # iterate the processID of the branches

        # TODO: students are expected to store the processID of the branches
        #pass

    # TODO: students are expected to process requests from both Client and Branch
    #def MsgDelivery(self,request, context):
        #cr = MessageDelivery_pb2.clientrequest()
        #cr = request
        #l=[]
        #for e in cr.events:
            #l.append(e)
        #return print(l)
    
    def Deposit(self,clientrequest):
        
        pass
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    br = Branch(1,1,[1,2])
    MessageDelivery_pb2_grpc.add_MsgDeliveryServicer_to_server(br,server)
    server_port = '[::]:' + str(50050 + 1)  
    server.add_insecure_port(server_port)
    server.start()
    server.wait_for_termination()
        
if __name__ == '__main__':
    logging.basicConfig()
    serve()