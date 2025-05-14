class ConstructorResolver:

    def resolve(self, type, dc):
        argValues = []
        constructorArguments = type.__init__.__annotations__.values() if hasattr(type.__init__, "__annotations__") else []
        for argType in constructorArguments:
            argValues.append(dc.resolve(argType))

        return type(*argValues)


class FieldResolver:

    def resolve(self, type, dc):
        obj = type()
        fields = type.__annotations__ if hasattr(type, "__annotations__") else {}
        for fieldName, fieldType in fields.items():
            setattr(obj, fieldName, dc.resolve(fieldType))

        return obj


class SingletonInstanceHolder:

    def __init__(self, resolver):
        self.resolver = resolver
        self.instance = None

    def getInstance(self, type, dc):
        if self.instance is None:
            self.instance = self.resolver.resolve(type, dc)

        return self.instance


class DependencyContainer:

    def __init__(self):
        self.instanceHolders = {}

    def initFromModule(self, module):
        module.init(self)

    def bindSingleton(self, type, resolveByFields=False):
        resolver = FieldResolver() if resolveByFields else ConstructorResolver()
        self.instanceHolders[type] = SingletonInstanceHolder(resolver)

    def resolve(self, type):
        if type not in self.instanceHolders:
            raise Exception(f"No dependency for {type} in container.")

        return self.instanceHolders[type].getInstance(type, self)

    def errorIfUnusedInstances(self):
        for type, holder in self.instanceHolders.items():
            if holder.instance is None:
                raise Exception(f"Unused instance for {type}.")
