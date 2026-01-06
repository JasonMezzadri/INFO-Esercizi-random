from typing import final


class Spaceship:
    def __init__(self, name: str):
        self.name = name
        self.fuel = 100

    def fly(self, distance: int) -> bool:
        """
        Ritorna True se il viaggio è avvenuto, False altrimenti
        """
        required_fuel = distance // 10

        if self.fuel < required_fuel:
            print(f"Errore: carburante insufficiente per {self.name}.")
            return False

        print(f"{self.name} percorre {distance} anni luce.")
        self.fuel -= required_fuel
        return True

    @final
    def dock(self):
        print(f"{self.name} esegue la procedura di attracco standard.")


class CargoShip(Spaceship):
    def __init__(self, name: str, max_load: int):
        super().__init__(name)
        self.max_load = max_load
        self.current_load = 0

    def load(self, amount: int):
        if self.current_load + amount > self.max_load:
            print("Errore: carico massimo superato.")
            return

        self.current_load += amount
        print(f"{self.name} carica {amount} tonnellate. "
              f"Carico attuale: {self.current_load}/{self.max_load}")

    def fly(self, distance: int):
        # Primo consumo standard
        success = super().fly(distance)

        if not success:
            return

        # Consumo extra per il peso
        extra_fuel = distance // 10
        if self.fuel < extra_fuel:
            print(f"Errore: carburante insufficiente per il peso del carico.")
            return

        self.fuel -= extra_fuel


@final
class ExplorationProbe(Spaceship):
    def __init__(self, name: str):
        super().__init__(name)

    def fly(self, distance: int):
        if distance < 100:
            print(f"{self.name} percorre {distance} anni luce.")
            return

        super().fly(distance)

    def scan(self):
        print(f"{self.name} scansiona l'area.")
