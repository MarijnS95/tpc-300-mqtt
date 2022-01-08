#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(
    description="Control KlikAanKlikUit lights over a USB-connected TPC-300"
)
parser.add_argument("channel", type=int)
parser.add_argument("state", type={"on": True, "off": False}.get)
args = parser.parse_args()

import tpc

tpc.control_channel(args.channel, args.state)
