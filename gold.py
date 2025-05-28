class Gold:   

	#constructor
    def __init__(self, value):
        self.name = "Gold Coin"
        self.value = value #assume that is an integer
		
    #setter
    def set_value(self, value):
        self.value = value
        print(f"Gold set to: {self.value}")

    #getter
    def get_value(self):
        print(f"This is my value: {self.value}")
    