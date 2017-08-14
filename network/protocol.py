import websocket
import time,readline,thread,sys
import threading
import os
import json
def init_protocal(conversation):
    def on_message(ws, message):
        message = json.loads(message)
        id = int(os.environ['user_id'])
        sender_id = int(message['sender_id'])
        if id != sender_id:
            print("%+*s %s" %(50,message['text'], ": Your friend said"))
        else:
            print("You said:" + message['text'])

    def on_error(ws, error):
        print error

    def on_close(ws):
        print "### closed ###"

    if 'messages' not in conversation:
        print 'No data'
    else:
        id = int(os.environ['user_id'])
        for message in conversation['messages']:
            if message['user_id'] != id:
                print("%+*s %s" %(50,message['body'], ": Your friend said"))
            else:
                print("You said:" + message['body'])



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


