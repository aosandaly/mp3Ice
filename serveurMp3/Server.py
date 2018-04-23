#!/usr/bin/env python3.6
import sys, Ice
from ServerI import ServerI

Ice.loadSlice('../interface/server.ice')

with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("ServerAdapter", "default -p 10000")
    object = ServerI()
    adapter.add(object, communicator.stringToIdentity("Server"))
    adapter.activate()
    communicator.waitForShutdown()