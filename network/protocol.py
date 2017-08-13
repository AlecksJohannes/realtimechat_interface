import websocket
import time,readline,thread,sys
import threading
import os
import json
def init_protocal(conversation):
    print(conversation)
    def on_message(ws, message):
        print message

    def on_error(ws, error):
        print error

    def on_close(ws):
        print "### closed ###"


    if 'messages' not in conversation:
        print 'No data'
    else:
        for message in conversation['messages']:
            sys.stdout.write("\r{0}>".format("Test says: "*message))
            sys.stdout.flush()

    ws = websocket.WebSocketApp("ws://localhost:8000/conversation/" + str(conversation['conversation_id']),
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)

    threading1 = threading.Thread(target=ws.run_forever)
    threading1.start()
    conn_timeout = 5
    while not ws.sock.connected and conn_timeout:
        time.sleep(1)
        conn_timeout -= 1
        msg_counter = 0
        while ws.sock.connected:
            message = {}
            a = raw_input('Input your messages: ')
            message['text'] = a
            message['sender_id'] = int(os.environ['user_id'])
            if a == 'False':
                ws.close()
            else:
                ws.send(json.dumps(message))
                time.sleep(1)
                msg_counter += 1


