class IRepository:
    def get_by_id(self, id):
        """find element by id and return it"""

    def list(self):
        """return list of all elems"""

    def update(self, elem):
        """update element"""

    def add(self, elem):
        """add elem"""

    def delete(self, id):
        """delete elem by id"""


class InMemoryRepository(IRepository):

    def __init__(self, dblist):
        self.db = dblist

    def get_by_id(self, id):
        for value in self.db:
            if value.id == id:
                return value
        else:
            return None

    def list(self):
        return self.db

    def update(self, elem):
        for index, value in enumerate(self.db):
            if value.id == elem.id:
                self.db[index] = elem

    def add(self, elem):
        self.db.append(elem)

    def delete(self, id):
        for index, value in enumerate(self.db):
            if value.id == id:
                del self.db[index]



