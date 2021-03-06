#!/bin/bash
test -z $1 && echo "need magnet link!
$0 <magnet link>" && exit -1

HOST=127.0.0.1
PORT=9091
USER=transmission
PASS=passwd

LINK="$1"
PAUSED="false"
SESSID=$(curl --silent --anyauth --user $USER:$PASS "http://$HOST:$PORT/transmission/rpc" | sed 's/.*<code>//g;s/<\/code>.*//g')
curl --silent --anyauth --user $USER:$PASS --header "$SESSID" "http://$HOST:$PORT/transmission/rpc" -d "{\"method\":\"torrent-add\",\"arguments\":{\"paused\":${PAUSED},\"filename\":\"${LINK}\"}}"
