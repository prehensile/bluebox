#!/usr/bin/env python3

import os, sys
import random
from asterisk.agi import AGI


agi = AGI()
agi.verbose( "jukebox.py started" )

media_dir = os.getenv( "BLUEBOX_PATH_MEDIA", "/usr/local/share/bluebox/jukebox/media" )
all_files = [ fn for fn in os.listdir( media_dir ) if fn.endswith( "mp3" ) ]

this_file = random.choice( all_files )
this_file = os.path.join( media_dir, this_file )

agi.appexec( "MP3Player", this_file )

