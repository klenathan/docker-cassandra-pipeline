"""Produce openweathermap content to 'faker' kafka topic."""
import asyncio
import configparser
import os
import time
from collections import namedtuple
from kafka import KafkaProducer
import requests
import json



KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TOPIC_NAME = os.environ.get("TOPIC_NAME")
SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
TOKEN = '001c39cf7592e21c26d1c635516db7466ed020b2'

def fetchData():
    
    res_paris = requests.get(f'https://api.waqi.info/feed/paris/?token={TOKEN}')
    response_paris = json.loads(res_paris.text)


    res_hanoi = requests.get(f'https://api.waqi.info/feed/hanoi/?token={TOKEN}')
    response_hanoi = json.loads(res_hanoi.text)

    now = time.localtime()
    return [
        {"location": "hanoi", 
         "aqi": response_hanoi['data']['iaqi']['pm25']['v'],
         "time": time.strftime("%Y-%m-%d %H:%M:%S", now)
        },
        {"location": "paris",
         "aqi": response_paris['data']['iaqi']['pm25']['v'],
         "time": time.strftime("%Y-%m-%d %H:%M:%S", now)
        }
    ]

def run():
    iterator = 0
    print("Setting up faker producer at {}".format(KAFKA_BROKER_URL))
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BROKER_URL],
        # Encode all values as JSON
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
    )

    while True:        
        # adding prints for debugging in logs
        print("Sending new faker data iteration - {}".format(iterator))
        
        current_aqi =fetchData()

        producer.send(TOPIC_NAME, value=current_aqi[0])
        producer.send(TOPIC_NAME, value=current_aqi[1])
        print("New Air Quality Index sent")
        time.sleep(SLEEP_TIME)
        print("Waking up!")
        iterator += 1


if __name__ == "__main__":
    # fetchData()
    run()
