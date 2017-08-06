import websocket
import thread
import time,readline,thread,sys
import threading
import inquirer
from network import request

def init_menu():
    questions = [
        inquirer.List('interests',
            message ="Pick a person <3",
            choices = request.get_users_list()
        ),
    ]
    answers = inquirer.prompt(questions)

def on_message(ws, message):
    print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

if __name__ == "__main__":
    init_menu()
    ws = websocket.WebSocketApp("ws://localhost:8000/conversation/1",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)

    threading1 = threading.Thread(target=ws.run_forever)
    threading1.start()
    conn_timeout = 5
    try:
        while not ws.sock.connected and conn_timeout:
            time.sleep(1)
            conn_timeout -= 1
            msg_counter = 0
        while ws.sock.connected:
            print("Haha")
            a = raw_input('Input your messages: ')
            if a == 'False':
                ws.close()
            else:
                ws.send(a)
            time.sleep(1)
            msg_counter += 1
    except AttributeError:
        init_menu()
