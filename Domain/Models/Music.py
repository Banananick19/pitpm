from Domain.Common import AggregateRoot


class Music(AggregateRoot):

    def __init__(self, id, file):
        super().__init__(id)
        self.file = file
