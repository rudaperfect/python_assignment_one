# Base class
class SmartDevice:
    def reset(self):
        print("Resetting Smart Device to default settings")


# Subclass
class SmartLight(SmartDevice):
    # Method overriding
    def reset(self):
        print("Resetting Smart Light and turning brightness to default")


# Function demonstrating polymorphism
def reset_all_devices(devices_list):
    for device in devices_list:
        device.reset()


# Create objects
device1 = SmartDevice()
device2 = SmartLight()
device3 = SmartLight()

# List containing different device objects
devices = [device1, device2, device3]

# Call the function
reset_all_devices(devices)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
