from game.network.ClientMultiplayerSynchronizer import *
from game.network.GameService import *
from game.network.GameServiceClient import *
from game.network.GameStateSynchronizer import *
from game.network.MessageSerializer import *
from game.network.MultiplayerSynchronizer import *
from game.network.NetworkConnectionInitializer import *
from game.network.ServerConnector import *
from game.network.SnapshotDiffLogic import *
from game.network.SnapshotFactory import *


class NetworkModule:

    def init(self, binder):
        binder.bindSingleton(ClientMultiplayerSynchronizer)
        binder.bindSingleton(GameService)
        binder.bindSingleton(GameServiceClient)
        binder.bindSingleton(GameStateSynchronizer)
        binder.bindSingleton(MessageSerializer)
        binder.bindSingleton(MultiplayerSynchronizer)
        binder.bindSingleton(NetworkConnectionInitializer)
        binder.bindSingleton(ServerConnector)
        binder.bindSingleton(SnapshotDiffLogic)
        binder.bindSingleton(SnapshotFactory)
