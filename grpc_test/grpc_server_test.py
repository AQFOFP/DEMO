# -*- coding: utf-8 -*-
import grpc
import time
from concurrent import futures
import grpchello_pb2, grpchello_pb2_grpc

_HOST = 'localhost'
_PORT = '8188'

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class gRPCServicerImpl(grpchello_pb2_grpc.gRPCServicer):

    def SayHello(self, request, context):
        print("called with " + request.name)
        return grpchello_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  grpchello_pb2_grpc.add_gRPCServicer_to_server(gRPCServicerImpl(), server)
  server.add_insecure_port('[::]:'+_PORT)
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)


if __name__ == '__main__':
    serve()