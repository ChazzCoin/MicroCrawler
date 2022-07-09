#! /bin/sh
# /usr/bin/bash
# -> run main.py with venv
#
cd ../.
sudo rsync -r MicroCrawler/ archivertwo@192.168.1.253:/home/archivertwo/bin/TiffanySystem/MicroCrawler
sudo rsync -r MicroCrawler/ archiverone@192.168.1.185:/home/archiverone/bin/TiffanySystem/MicroCrawler