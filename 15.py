class House:
    def __init__(self, area: float, price: float):
        self.__area = area
        self.__price = price

    def final_price(self, discount: float) -> float:
        return self.__price - self.__price * discount / 100

    def get_area(self):
        return self.__area

    def get_price(self):
        return self.__price


class SmallHouse(House):
    def __init__(self, price: float):
        super().__init__(40, price)


class LuxuryHouse(House):
    def final_price(self, discount: float) -> float:
        return super().final_price(discount / 2)


class Human:
    @staticmethod
    def default_info():
        print("Клас Human представляє людину, яка може володіти будинком.")

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def __str__(self):
        house_info = f"Будинок: {self.__house.get_area()} м², ціна {self.__house.get_price()}" if self.__house else "Будинок: немає"
        return f"Ім'я: {self.name}, Вік: {self.age}, Гроші: {self.__money}, {house_info}"

    def get_money(self):
        return self.__money

    def __make_deal(self, house: House, price: float):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount: float):
        self.__money += amount

    def buy_house(self, house: House, discount: float):
        final_price = house.final_price(discount)
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
            print(f"{self.name} купил за {final_price} грн")
        else:
            print(f"У {self.name} не хватает денег -_-")
if __name__ == "__main__":
    Human.default_info()
    person = Human("Вани", 11)
    print(person)
    small_house = SmallHouse(50000)
    person.buy_house(small_house, 10)
    person.earn_money(60000)
    print(f"После заработку: {person.get_money()} грн")
    person.buy_house(small_house, 10)
    print(person)