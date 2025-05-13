class SingletonInstanceHolder:

    def __init__(self, factoryFunc):
        self.factoryFunc = factoryFunc
        self.instance = None

    def getInstance(self, type, resolver):
        if self.instance is None:
            self.instance = self.factoryFunc(type, resolver)

        return self.instance


class DependencyContainer:

    def __init__(self):
        self.instanceHolders = {}

    def initFromModule(self, module):
        module.init(self)

    def bindSingleton(self, type):
        def factoryFunc(type, resolver):
            argValues = []
            constructorArguments = type.__init__.__annotations__.values() if hasattr(type.__init__, "__annotations__") else []
            for argType in constructorArguments:
                argValues.append(resolver.resolve(argType))

            return type(*argValues)

        self.instanceHolders[type] = SingletonInstanceHolder(factoryFunc)

    def resolve(self, type):
        if type not in self.instanceHolders:
            raise Exception(f"No dependency for {type} in container.")

        return self.instanceHolders[type].getInstance(type, self)

    def errorIfUnusedInstances(self):
        for type, holder in self.instanceHolders.items():
            if holder.instance is None:
                raise Exception(f"Unused instance for {type}.")
