#! /usr/bin/env python3

import argparse
import logging
import sys

import paho.mqtt.client as mqtt

parser = argparse.ArgumentParser(
    description="Control KlikAanKlikUit lights over a USB-connected TPC-300, with commands received from MQTT"
)
parser.add_argument("mqtt_host", help="MQTT broker address")
parser.add_argument("mqtt_username", help="MQTT username")
parser.add_argument("mqtt_password", help="MQTT password")
args = parser.parse_args()

logging.basicConfig(format="%(asctime)s:" + logging.BASIC_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

import tpc


def set_light(client, userdata, msg):
    paths = msg.topic.split("/")
    index = int(paths.pop(2))
    assert paths == ["tpc-300", "light", "set"]
    state = {b"ON": True, b"OFF": False}[msg.payload]
    logger.debug(f"Setting {index} to {'on' if state else 'off'}")
    tpc.control_channel(index, state)


def on_connect(client, userdata, flags, rc):
    logger.debug(f"Connected to mqtt with result code {rc}")
    client.subscribe("tpc-300/light/+/set")
    client.publish("tpc-300/status", "online", qos=2, retain=True)


client = mqtt.Client()
client.will_set("tpc-300/status", "offline", qos=2, retain=True)
client.on_connect = on_connect
client.on_message = set_light
client.username_pw_set(args.mqtt_username, args.mqtt_password)
client.connect(args.mqtt_host)
client.loop_forever()
