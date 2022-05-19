#!/usr/bin/python

import argparse
import logging

logging.basicConfig(format="%(asctime)s:" + logging.BASIC_FORMAT)

parser = argparse.ArgumentParser(
    description="Control KlikAanKlikUit lights over a USB-connected TPC-300"
)
parser.add_argument("state", type={"on": True, "off": False}.get)
parser.add_argument("channel", type=int, nargs="?")
args = parser.parse_args()

import tpc

if args.channel is None:
    import time

    # for i in range(255, 0, -1):
    for i in range(0, 256):
        print(i)
        tpc.control_channel(i, args.state)
        time.sleep(1)
else:
    tpc.control_channel(args.channel, args.state)
