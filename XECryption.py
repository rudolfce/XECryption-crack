#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    print "Usage: {} [encrypted file].".format(sys.argv[0])
    sys.exit(1)

try:
    in_file = open(sys.argv[1], 'r')
except IOError:
    sys.stderr.write("Could not open file {}\n".format(sys.argv[1]))
    sys.exit(1)

in_stream = [int(n) for n in in_file.read().split('.') if n]
# This will separate the numbers after each dot and ignore empty
# numbers, but won't sanitize the string in any other way.

i = 0
encrypted_char = 0
raw_outstream = []
for n in in_stream: # Find the encoded number for each character of the message
    encrypted_char += n
    i += 1
    if not i%3:
        raw_outstream.append(encrypted_char)
        encrypted_char = 0

# First subtraction factor - min value for an ASCII char not lower than 0
key = min(raw_outstream)
in_char = ''
while not in_char == 'q':
    out_stream = [chr(c-key) for c in raw_outstream] # Decoding attempts
    print ''.join(out_stream)
    in_char = raw_input()
    key -= 1

sys.exit(0)
