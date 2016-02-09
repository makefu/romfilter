# flask
DEBUG = True

HOST='0.0.0.0'
## custom
# path to the mamectl xml file:
# http://www.emulab.it/rommanager/datfiles.php (or )
# 
MAME_CTLDB = "./mame.dat"

# TODO: also use
# - http://www.arcade-history.com/index.php?page=download (history.dat)
# - http://www.mameworld.info/mameinfo/ (mameinfo.dat)
# - http://nplayers.arcadebelgium.be/ (nplayers.ini)
# - http://www.progettosnaps.net/icons/ (icons)
#   * http://icons.mameworld.info/icons.zip/icons.zip 
# - www.progettosnaps.net/series/ (series.ini)
# - http://samples.mameworld.info/Current%20Samples.htm (samples)

# overview: http://mrdo.mameworld.info/mame.php
#           http://www.mameworld.info/
MAMECACHE= "./mame.pickle"

SYNC_LIVEDIR = "/home/user/.mame"
SYNC_ARCHIVEDIR = "/media/truecrypt1/emu/mame/"
# or /opt/mame if it is just another folder
