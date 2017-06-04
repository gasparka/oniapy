#!/usr/bin/env python
#
# test_midiin_poll.py
#
"""Show how to receive MIDI input by polling an input port."""

from __future__ import print_function

import logging
import sys
import time

import rtmidi
from rtmidi.midiutil import open_midiinput


log = logging.getLogger('midiin_poll')
logging.basicConfig(level=logging.DEBUG)

# Prompts user for MIDI input port, unless a valid port number or name
# is given as the first argument on the command line.
# API backend defaults to ALSA on Linux.
port = sys.argv[1] if len(sys.argv) > 1 else None

midiout = rtmidi.MidiIn()
available_ports = midiout.get_ports()
print(available_ports)

try:
    midiin, port_name = open_midiinput(1)
except (EOFError, KeyboardInterrupt):
    sys.exit()

print("Entering main loop. Press Control-C to exit.")
try:
    timer = time.time()
    while True:
        msg = midiin.get_message()

        if msg:
            message, deltatime = msg
            timer += deltatime
            print(deltatime)
            print("[%s] @%0.6f %r" % (port_name, timer, message))

        time.sleep(0.01)
except KeyboardInterrupt:
    print('')
finally:
    print("Exit.")
    midiin.close_port()
    del midiin

# note offset = 21
# min = 21
# max = 108

# import mido
#
#
# print(mido.get_output_names())
#
# with mido.open_input('Digital Piano MIDI 1') as inport:
#     for msg in inport:
#         if msg.type != 'clock':
#             print(msg)