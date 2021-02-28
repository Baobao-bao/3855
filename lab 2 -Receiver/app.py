import connexion 
from connexion import NoContent
import json
from swagger_ui_bundle import swagger_ui_path
# from flask import Flask, Blueprint, send_from_directory, render_template
# import fcntl
# import sys
import threading
lock = threading.Lock()

MAX_EVENT = 10
EVENT_FILE = "events.json"

def limit_data():
    with open('c:/Users/Bao/Desktop/3855/lab 2 -Receiver/'+ EVENT_FILE,"r") as file:
        content = file.read()
        if len(content) == 0:
            print("hi")
            return []
        data = json.loads(content)
        if len(data) <= (MAX_EVENT - 1):
                return data
        else:
            del data[MAX_EVENT-1]
            return data

def read_stock_open_price(body):
    data = limit_data()
    data.insert(0,body)
    with lock:
        with open('c:/Users/Bao/Desktop/3855/lab 2 -Receiver/'+EVENT_FILE,"w") as file:
            json.dump(data, file)
    return NoContent,201

# def read_stock_close_price(body):
#     print(body)
#     return NoContent,201

def read_stock_news(body):
    data = limit_data()
    data.insert(0,body)
    with lock:
        with open('c:/Users/Bao/Desktop/3855/lab 2 -Receiver/'+ EVENT_FILE,"w") as file:
            json.dump(data, file)
    return NoContent,201

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yaml",strict_validation=True,validate_responses=True)

if __name__ == "__main__":
    app.run(port=8080)
    with open('c:/Users/Bao/Desktop/3855/lab 2 -Receiver/'+ EVENT_FILE,"r") as file:
        data = json.loads(file.read())
        print(data)
        print(len(data))
        print(type(data))
        
# localhost:8080/ui