from abc import ABC, abstractmethod
import json


# -----------------------------
# Sensor Classes (Modular System)
# -----------------------------
class Lidar:
    def scan(self):
        return "Scanning environment using LiDAR"


class GPS:
    def get_location(self):
        return "Getting GPS coordinates"


# -----------------------------
# Abstract Base Class
# -----------------------------
class Drone(ABC):

    def __init__(self, drone_id, battery_level, internal_temperature):
        self.drone_id = drone_id

        # encapsulated variables
        self.__battery_level = battery_level
        self._internal_temperature = internal_temperature

    # Abstract method
    @abstractmethod
    def Maps(self, destination):
        pass

    # Concrete method
    def update_battery(self, consumption):
        self.__battery_level -= consumption
        if self.__battery_level < 0:
            self.__battery_level = 0

    # Read-only property
    @property
    def battery_level(self):
        return self.__battery_level


# -----------------------------
# Subclass DeliveryDrone
# -----------------------------
class DeliveryDrone(Drone):

    def __init__(self, drone_id, battery_level, internal_temperature, sensors=None):
        super().__init__(drone_id, battery_level, internal_temperature)

        if sensors is None:
            sensors = []

        self.sensors = sensors

    # Override navigation logic
    def Maps(self, destination):
        print(f"Drone {self.drone_id} navigating to {destination}")

        for sensor in self.sensors:
            if isinstance(sensor, Lidar):
                print(sensor.scan())

            if isinstance(sensor, GPS):
                print(sensor.get_location())

    # Serialize drone state to JSON
    def save_state(self, filename):

        state = {
            "drone_id": self.drone_id,
            "battery_level": self.battery_level,
            "internal_temperature": self._internal_temperature
        }

        with open(filename, "w") as file:
            json.dump(state, file)

        print("Drone state saved to file.")

    # Class method to reboot drone
    @classmethod
    def reboot(cls, filename):

        with open(filename, "r") as file:
            state = json.load(file)

        drone = cls(
            state["drone_id"],
            state["battery_level"],
            state["internal_temperature"]
        )

        print("Drone rebooted from saved state.")
        return drone


# -----------------------------
# Simulation Example
# -----------------------------
if __name__ == "__main__":

    lidar = Lidar()
    gps = GPS()

    drone1 = DeliveryDrone(
        drone_id="DR-101",
        battery_level=100,
        internal_temperature=45,
        sensors=[lidar, gps]
    )

    drone1.Maps("Warehouse B")

    drone1.update_battery(20)

    print("Battery level:", drone1.battery_level)

    drone1.save_state("drone_state.json")

    rebooted_drone = DeliveryDrone.reboot("drone_state.json")

    print("Rebooted Drone Battery:", rebooted_drone.battery_level)