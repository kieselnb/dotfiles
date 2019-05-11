#!/usr/bin/env python

import json
import sys
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
        return ''

    title = player.get_title()

    # fall back to album if artist isn't avaiable
    #   more for podcasts, since spotify deems those don't have artist?!?
    artist_or_album = player.get_artist()
    if artist_or_album == '':
        artist_or_album = player.get_album()

    curr_playing = '{0} - {1}'.format(title.strip(), artist_or_album.strip())

    if status == 'Paused':
        curr_playing += ' '
    else:
        curr_playing += ' '

    return curr_playing.strip()

if __name__ == '__main__':
    # Skip the first line which contains the version header.
    print_line(read_line())

    # The second line contains the start of the infinite array.
    print_line(read_line())

    while True:
        line, prefix = read_line(), ''
        # ignroe comma at start of lines
        if line.startswith(','):
            line, prefix = line[1:], ','

        j = json.loads(line)

        # insert information into the start of the json
        music_info = get_music_info()
        if len(music_info) > 0:
            j.insert(0, {'full_text' : '%s' % get_music_info(), 'name' : 'music'})

        # and echo back new encoded json
        print_line(prefix+json.dumps(j))
