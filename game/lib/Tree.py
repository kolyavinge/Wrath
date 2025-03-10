class Tree:

    @staticmethod
    def flattenToList(root, getChildrenFunc):
        result = []

        def rec(parent):
            result.append(parent)
            children = getChildrenFunc(parent)
            if children is not None:
                for child in children:
                    rec(child)

        rec(root)

        return result
