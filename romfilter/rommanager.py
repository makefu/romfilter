
from os.path import join,exists

def in_store(live_path,game):
    """
    live path is the path to the current game directory which is used by 
    sdlmame
    """
    return exists((join(live_path,'roms',"{}.zip".format(game))))


def copy_rom(live_path,archive_path,game):
    """
    #!/bin/sh
    # Provides a simple way to copy single roms and the corresponding art work from
    # a hosting server
    GAME=${1?please provide game name you want to dl (e.g. boogwing or 1942)}
    MAMEDIR=${NAMEDIR:-$HOME/.mame}
    HOSTN=${HOSTN:-omo:8002}
    for i in roms:zip preview:png artwork:zip cabinet:png flyer:png icon:ico marquee:png  title:png cpanel:png; do
        NAME=${i%:*}  # split at :
        EXT=${i#*:}
        printf "Getting %-20s: " "$NAME/$GAME.$EXT"
        mkdir -p $MAMEDIR/$NAME
        cd $MAMEDIR/$NAME
        if wget $HOSTN/$NAME/$GAME.$EXT >/dev/null 2>&1 ;then
            echo "  [Success]"
        else
            echo "  [Failure]"
        fi
    done
    """
    from shutil import copyfile
    fe = { "roms":"zip","preview":"png","artwork":"zip",
           "cabinet":"png","flyer":"png","icon":"ico",
           "marquee":"png","title":"png","cpanel":"png" }
    for name,ext in fe.items():
        local = join(archive_path,name,"{}.{}".format(game,ext))
        remote = join(live_path,name,"{}.{}".format(game,ext))
        print(local ," --> ",remote)
