from Domain.Common import AggregateRoot


class User(AggregateRoot):

    def __init__(self, id, email, password, name, additional_info, phone):
        super().__init__(id)
        self.email = email
        self.password = password
        self.name = name
        self.additional_info = additional_info
        self.phone = phone
