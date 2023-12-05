class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = None  
        self.inches = None
        self.on_off_status = False
        self.volume = 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        # The TV has only 50 channels
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = None
        self.backlight = None

    def display_details(self):
        return f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, " \
               f"Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}, Viewing Angle: {self.viewing_angle}, " \
               f"Backlight: {self.backlight}"


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
       # self.display_details = None

    def display_details(self):
        return f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, " \
               f"Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}, Display Details: {self.display_details}"


#instance created for the class LedTV 
led_tv = LedTV("Sony", "Slim", "Low", "Long", "120Hz")
led_tv.set_channel(8)
led_tv.increase_volume()

plasma_tv = PlasmaTV("Panasonic", "Thick", "High", "Medium", "60Hz")
plasma_tv.decrease_volume()

print(led_tv.status())
print(led_tv.display_details())

print(plasma_tv.status())
print(plasma_tv.display_details())
