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

    @staticmethod
    def makeBinaryTreeFromSortedList(items):

        def rec(leftIndex, rightIndex):
            if leftIndex <= rightIndex:
                middleIndex = int(leftIndex + (rightIndex - leftIndex) / 2)
                middle = items[middleIndex]
                middle.leftChild = rec(leftIndex, middleIndex - 1)
                middle.rightChild = rec(middleIndex + 1, rightIndex)
                return middle
            else:
                return None

        rootNode = rec(0, len(items) - 1)

        return rootNode
