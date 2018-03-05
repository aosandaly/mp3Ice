import sys, Ice
from ServerI import ServerI
import time

Ice.loadSlice('../interface/server.ice')
# ipServeur = "192.168.0.17" # momo parent
# ipServeur = "192.168.0.17" # momo appartement
ipServeur = "192.168.1.18" # moi

with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("ServerAdapter", "tcp -h "+ipServeur+" -p 10000")
    object = ServerI()
    adapter.add(object, communicator.stringToIdentity("Server"))
    adapter.activate()
    communicator.waitForShutdown()


    #
    # instance = vlc.Instance()
    #
    # # Create a MediaPlayer with the default instance
    # player = instance.media_player_new()
    #
    # # Load the media file
    # media = instance.media_new('music/MINIONS.mp3')
    #
    # # Add the media to the player
    # player.set_media(media)
    #
    # # Play for 10 seconds then exit
    # player.play()
    # time.sleep(10)
    #
    # # Build vlc option string
    # options = 'sout=#duplicate{dst=rtp{access=udp,mux=ts,dst=224.0.0.1,port=1233},dst=display}'
    # print(player.get_media().get_mrl())
    # # Load media with streaming options
    # media = instance.media_new('music/MINIONS.mp3', options)
    #
    # player.play()