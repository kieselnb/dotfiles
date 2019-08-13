#!/usr/bin/env python

import json
import sys

import gi
from gi.repository import Playerctl

def print_line(message):
    """ Non-buffered printing to stdout. """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()

def read_line():
    """ Interrupted respecting reader for stdin. """
    # try reading aline, removing any whitespace
    try:
        line = sys.stdin.readline().strip()
        # i3status sends EOF, or an empty line
        if not line:
            sys.exit(3)
        return line
    # exit on ctrl-c
    except KeyboardInterrupt:
        sys.exit()

def get_music_info():
    player = Playerctl.Player()

    status = player.get_property('status')

    # handle when there is no player
    if not status:
        return

    title_artist = '{} - {}'.format(player.get_title(), player.get_artist())

    if status == 'Paused':
        title_artist += ' '
    else:
        title_artist += ' '

    return title_artist.strip()

if __name__ == '__main__':
    # Skip the first line which contains the version header.
    print_line(read_line())

    # The second line contains the start of the infinite array.
    print_line(read_line())

    while True:
        line, prefix = read_line(), ''
        # ignore comma at start of lines
        if line.startswith(','):
            line, prefix = line[1:], ','

        j = json.loads(line)

        # insert information into the start of the json
        music_info = get_music_info()
        if music_info:
            j.insert(0, {'full_text' : '{}'.format(music_info), 'name' : 'music'})

        # and echo back new encoded json
        print_line(prefix + json.dumps(j))
