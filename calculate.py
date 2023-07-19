class Units:
    def __init__(self, height_unit, weight_unit):
        self.height_unit = height_unit
        self.weight_unit = weight_unit
        self.units = {
            "height": ['cm', 'm', 'in'],
            "weight": ['kg', 'g', 'lb']
        }






class BMICalculate:

    def __init__(self, height, weight, units: Units):
        self.height = float(height)
        self.weight = float(weight)
        self.units = units

    def calculate(self):
        #     weight  to kg
        if self.units.weight_unit == "g":
            self.weight = self.weight / 1000
        elif self.units.weight_unit == "lb":
            self.weight = self.weight * 0.4535

        #     height to m
        if self.units.height_unit == "cm":
            self.height = self.height / 100
        elif self.units.height_unit == "in":
            self.height = self.height * 0.0254

        return self.weight / (self.height ** 2)
