import time

class Vehicle:
    def __init__(self, reg_num, vehicle_type):
        self.reg_num = reg_num
        self.vehicle_type = vehicle_type
        self.signal_entry_log = {}
        self.signal_exit_log = {}

    def enter_signal(self, signal):
        self.signal_entry_log[signal] = time.time()

    def exit_signal(self, signal, speed):
        if signal in self.signal_entry_log:
            entry_time = self.signal_entry_log[signal]
            time_difference = time.time() - entry_time
            if time_difference < 5:  # Just a simulation; it doesn't reflect real-world times
                print(f"Speeding Violation! Vehicle {self.reg_num} of type {self.vehicle_type} was too fast in Signal {signal}")
            self.signal_exit_log[signal] = time.time()
        else:
            print(f"Red Signal Violation! Vehicle {self.reg_num} of type {self.vehicle_type} exited from Signal {signal} without entering")

class TrafficSignalSystem:
    def __init__(self):
        self.vehicles = {}

    def vehicle_entry(self, reg_num, vehicle_type, signal):
        if reg_num not in self.vehicles:
            self.vehicles[reg_num] = Vehicle(reg_num, vehicle_type)

        self.vehicles[reg_num].enter_signal(signal)

    def vehicle_exit(self, reg_num, vehicle_type, signal, speed):
        if reg_num in self.vehicles:
            self.vehicles[reg_num].exit_signal(signal, speed)
        else:
            print(f"Red Signal Violation! Vehicle {reg_num} of type {vehicle_type} exited from Signal {signal} but was not detected entering any signal")

    def check_violations(self):
        for reg_num, vehicle in self.vehicles.items():
            for signal, entered in vehicle.signal_entry_log.items():
                if signal not in vehicle.signal_exit_log:
                    print(f"Red Signal Violation! Vehicle {reg_num} of type {vehicle.vehicle_type} entered Signal {signal} but did not exit")

# testing the system
system = TrafficSignalSystem()

# vehicle enters and exits signals
system.vehicle_entry("ABC-123", "Car", "A")
time.sleep(6)  # simulate time delay
system.vehicle_exit("ABC-123", "Car", "A", 60)

system.vehicle_entry("XYZ-789", "Truck", "A")
system.vehicle_exit("XYZ-789", "Truck", "B", 80)

# check violations
system.check_violations()

# vehicle not entered from any signal but tries to exit
system.vehicle_exit("JKL-456", "Bike", "C", 40)
