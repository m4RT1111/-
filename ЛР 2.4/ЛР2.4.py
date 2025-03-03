# Итоговое задание по ООП на Python

class BaseVehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"

    def __repr__(self):
        return f"BaseVehicle(brand='{self.brand}', model='{self.model}')"


class PassengerCar(BaseVehicle):
    def __init__(self, brand, model, passenger_capacity):
        super().__init__(brand, model)
        self.passenger_capacity = passenger_capacity

    def __str__(self):
        return f"{super().__str__()}, Passenger Capacity: {self.passenger_capacity}"

    def __repr__(self):
        return f"PassengerCar(brand='{self.brand}', model='{self.model}', passenger_capacity={self.passenger_capacity})"


class Truck(BaseVehicle):
    def __init__(self, brand, model, cargo_capacity):
        super().__init__(brand, model)
        self.cargo_capacity = cargo_capacity

    def __str__(self):
        return f"{super().__str__()}, Cargo Capacity: {self.cargo_capacity}"

    def __repr__(self):
        return f"Truck(brand='{self.brand}', model='{self.model}', cargo_capacity={self.cargo_capacity})"


class SocialNetwork:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"SocialNetwork(name='{self.name}')"


class VK(SocialNetwork):
    def __init__(self, name, user_count):
        super().__init__(name)
        self.user_count = user_count

    def __str__(self):
        return f"{super().__str__()}, User Count: {self.user_count}"

    def __repr__(self):
        return f"VK(name='{self.name}', user_count={self.user_count})"


class Facebook(SocialNetwork):
    def __init__(self, name, active_users):
        super().__init__(name)
        self.active_users = active_users

    def __str__(self):
        return f"{super().__str__()}, Active Users: {self.active_users}"

    def __repr__(self):
        return f"Facebook(name='{self.name}', active_users={self.active_users})"


class BaseTree:
    def __init__(self, species):
        self.species = species

    def __str__(self):
        return self.species

    def __repr__(self):
        return f"BaseTree(species='{self.species}')"


class Pine(BaseTree):
    def __init__(self, species, height):
        super().__init__(species)
        self.height = height

    def __str__(self):
        return f"{super().__str__()}, Height: {self.height}m"

    def __repr__(self):
        return f"Pine(species='{self.species}', height={self.height})"


class Fir(BaseTree):
    def __init__(self, species, age):
        super().__init__(species)
        self.age = age

    def __str__(self):
        return f"{super().__str__()}, Age: {self.age} years"

    def __repr__(self):
        return f"Fir(species='{self.species}', age={self.age})"


# Пример использования классов
if __name__ == "__main__":
    car = PassengerCar("Toyota", "Camry", 5)
    truck = Truck("Volvo", "FH16", 20000)
    vk = VK("VKontakte", 100000000)
    facebook = Facebook("Facebook", 250000000)
    pine = Pine("Albus Grand", 15)
    fir = Fir("Abies alba", 50)

    print(car)
    print(truck)
    print(vk)
    print(facebook)
    print(pine)
    print(fir)