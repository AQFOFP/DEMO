# -*- coding: utf-8 -*-
"""The Python implementation of the gRPC client."""
from __future__ import print_function
import grpc
from grpchello_pb2  import *    ## or import grpchello_pb2
from grpchello_pb2_grpc import *
## No grpcDemo!  from grpcDemo import grpchello_pb2, grpchello_pb2_grpc #error!

_PORT = '8188'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = gRPCStub(channel=conn)
    response = client.SayHello(HelloRequest(name='David'))
    print("received: " + response.message)


##
if __name__ == '__main__':

    if len(sys.argv) == 2:
        # print (sys.argv[1])
        _HOST = sys.argv[1]
    else:
        _HOST = 'localhost'

    #
    run()
