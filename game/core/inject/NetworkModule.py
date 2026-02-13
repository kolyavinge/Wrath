from game.network.ClientConnectionLogic import *
from game.network.ClientMultiplayerSynchronizer import *
from game.network.GameService import *
from game.network.GameServiceClient import *
from game.network.GameStateSynchronizer import *
from game.network.MessageSerializer import *
from game.network.ServerConnectionLogic import *
from game.network.ServerMultiplayerSynchronizer import *
from game.network.SnapshotDiffLogic import *
from game.network.SnapshotFactory import *


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
