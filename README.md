# horriblesubs_rss

Python script that reads new entries from the [HorribleSubs RSS Feed](http://www.horriblesubs.info/rss.php?res=1080) and downloads them using the [Transmission Web Interface](https://transmissionbt.com/)

## Requirements
[feedparser](https://pypi.org/project/feedparser/).

## Setup
run the main.py as a crontab every 30 minutes or so and set the move.py script to execute every time a torrent is finished.
