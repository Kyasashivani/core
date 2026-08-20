class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius*9/5)+32

    def show_conversion(self):
        frenh=self.to_fahrenheit(self.celsius)
        print(f"celsius: {self.celsius}")
        print(f"fahrenheit: {frenh}")

t1=Temperature(25)
t1.show_conversion()