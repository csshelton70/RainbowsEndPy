class Player:
    # private

    # public
    id: int
    name: str
    email: str
    money: int
    last_orders : int
    friend_list : list[int]
    units : list[int]
    removed_units : list[int]

    def Populate(self, id: int, name: str, email: str, starting_money: int) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.money = starting_money
        self.last_orders = 0
        self.friend_list = []
        self.units = []
        self.removed_units = []

    def Populate_From_Dict(self, item : dict) -> None:
        self.id = item["id"]
        self.name = item["name"]
        self.email = item["email"]
        self.money = item["money"]
        self.last_orders = item["lastorders"]
        self.friend_list = item["friends"]
        self.units = item["units"]
        self.removed_units = item["removedunits"]

    def To_Dict(self):
        return {
            "id":self.id,
            "name": self.name,
            "email": self.email,
            "money": self.money,
            "lastorders":self.last_orders,
            "friends":self.friend_list,
            "units":self.units,
            "removedunits":self.removed_units
        }
