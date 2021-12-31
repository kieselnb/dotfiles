#!/bin/bash

IMAGE_FNAME=$(mktemp --suffix=.png /tmp/swaylock.XXXXX)
grim - | convert - -gaussian-blur 5x5 ${IMAGE_FNAME}
swaylock -f -i ${IMAGE_FNAME}
rm -f ${IMAGE_FNAME}
