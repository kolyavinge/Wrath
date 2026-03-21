from game.multiplayer.ClientConnectionLogic import *
from game.multiplayer.ClientMultiplayerSynchronizer import *
from game.multiplayer.GameService import *
from game.multiplayer.GameServiceClient import *
from game.multiplayer.GameStateSynchronizer import *
from game.multiplayer.MessageSerializer import *
from game.multiplayer.ServerConnectionLogic import *
from game.multiplayer.ServerMultiplayerSynchronizer import *
from game.multiplayer.SnapshotDiffLogic import *
from game.multiplayer.SnapshotFactory import *
from game.multiplayer.SnapshotPersonDiffLogic import *


class NetworkModule:

    def init(self, binder):
        binder.bindSingleton(ClientConnectionLogic)
        binder.bindSingleton(ClientMultiplayerSynchronizer)
        binder.bindSingleton(GameService)
        binder.bindSingleton(GameServiceClient)
        binder.bindSingleton(GameStateSynchronizer)
        binder.bindSingleton(MessageSerializer)
        binder.bindSingleton(ServerConnectionLogic)
        binder.bindSingleton(ServerMultiplayerSynchronizer)
        binder.bindSingleton(SnapshotDiffLogic)
        binder.bindSingleton(SnapshotFactory)
        binder.bindSingleton(SnapshotPersonDiffLogic)
