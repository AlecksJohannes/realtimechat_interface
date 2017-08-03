import websocket
import thread
import time,readline,thread,sys
import threading
import inquirer
questions = [
    inquirer.List('interests',
	message="What are you interested in?",
	choices=['Computers', 'Books', 'Science', 'Nature', 'Fantasy', 'History'],
    ),
]
answers = inquirer.prompt(questions)
print (answers)

def on_message(ws, message):
    print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"


def background(ws):
    while True:
        time.sleep(3)
        ws.send("haha")
        print 'disarm me by typing disarm'


if __name__ == "__main__":
    print 'init'
    ws = websocket.WebSocketApp("ws://localhost:8000/conversation/1",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)

    websocket.enableTrace(True)
    threading1 = threading.Thread(target=ws.run_forever)
    threading1.start()
    conn_timeout = 5
    while not ws.sock.connected and conn_timeout:
        time.sleep(1)
        conn_timeout -= 1
        msg_counter = 0
    while ws.sock.connected:
        a = raw_input('haha: ')
        ws.send(a)
        time.sleep(1)
        msg_counter += 1
