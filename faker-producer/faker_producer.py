"""Produce openweathermap content to 'faker' kafka topic."""
import asyncio
import configparser
import os
import time
from collections import namedtuple
from kafka import KafkaProducer
from faker import Faker
import json


fake = Faker()

def get_registered_user():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "year": fake.year(),
        "job": fake.job(),
        "date_of_birth": fake.date_of_birth(minimum_age=18).strftime("%m/%d/%Y"),

        "phone": fake.phone_number(),
        "origin": fake.country(),
        "credit_card_num":  fake.credit_card_number(),
        "credit_card_provider": fake.credit_card_provider(),
        "credit_card_expire": fake.credit_card_expire()
    }
    
KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TOPIC_NAME = os.environ.get("TOPIC_NAME")
SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))



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
        registered_user = get_registered_user()
        print(registered_user)
        producer.send(TOPIC_NAME, value=registered_user)
        print("New faker data sent")
        time.sleep(SLEEP_TIME)
        print("Waking up!")
        iterator += 1


if __name__ == "__main__":
    run()
