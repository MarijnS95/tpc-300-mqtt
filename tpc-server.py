#! /usr/bin/env python3

import paho.mqtt.subscribe as subscribe
import tpc
import logging
import sys

logging.basicConfig(format="%(asctime)s:" + logging.BASIC_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def set_light(client, userdata, msg):
    paths = msg.topic.split("/")
    index = int(paths.pop(2))
    assert paths == ["tpc-300", "light", "set"]
    state = {b"ON": True, b"OFF": False}[msg.payload]
    logger.debug(f"Setting {index} to {'on' if state else 'off'}")
    tpc.control_channel(index, state)


subscribe.callback(set_light, "tpc-300/light/+/set", hostname=sys.argv[1])
