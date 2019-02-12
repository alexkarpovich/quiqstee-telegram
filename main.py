import sys
import grpc
import time
import logging
from threading import Thread
from concurrent import futures

from bot import bot
from proto.snip_pb2 import SnipResponse, SnipRequest
from proto.snip_pb2_grpc import add_UrlSnipServiceServicer_to_server, UrlSnipServiceServicer, UrlSnipServiceStub


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format="%(asctime)s - %(threadName)s - %(message)s")

class UrlSnipService(UrlSnipServiceServicer):

    def snip_it(self, request, context):
        return SnipResponse(url='pretty much it ' + request.url)


def run_telegram_bot():
    logging.debug('Start telegram bot')
    bot.polling(none_stop=True)

def run_grpc_server():
    logging.debug('Start grpc server')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_UrlSnipServiceServicer_to_server(UrlSnipService(), server)
    server.add_insecure_port('0.0.0.0:50053')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__=='__main__':
    telegram_thread = Thread(target=run_telegram_bot)
    grpc_thread = Thread(target=run_grpc_server)
    telegram_thread.start()
    grpc_thread.start()
