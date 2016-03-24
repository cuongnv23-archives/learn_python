

#!/usr/bin/python
#"99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows:

#    99 bottles of beer on the wall, 99 bottles of beer.
#    Take one down, pass it around, 98 bottles of beer on the wall.

#The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero.

#Your task here is write a Python program capable of generating all the verses of the song.

import time

BOTTLES = 99

while int(BOTTLES) > 0:
    print """
    %d bottles of beer on the wall, %d bottles of beer.
    Take one down, pass it around, %d bottles of beer on the wall.
    """ % (BOTTLES, BOTTLES, BOTTLES - 1)
    BOTTLES = BOTTLES - 1
    time.sleep(2)
