class Lightbulb:
    def __init__(self):
        self.state = "off"

    def change_state(self,):
        if self.state == "on":
            self.state = "off"
        else:
            self.state = "on"
        print(f"Turning the light {self.state}")