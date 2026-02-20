class IdList(list):

    def getById(self, id):
        item = self.getByIdOrNone(id)
        if item is not None:
            return item
        else:
            raise Exception(f"List has no item with id={id}")

    def getByIdOrNone(self, id):
        for item in self:
            if item.id == id:
                return item

        return None
