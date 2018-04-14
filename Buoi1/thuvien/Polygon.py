class Polygon():
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
        self.slides = [0 for i in range(num_of_sides)]

    def input_sides(self):
        self.slides = [float(input('Enter side ' + str(i+1))) + ': ' for i in range(self.num_of_sides)]

    def display_sides(self):
        for i in range(self.num_of_sides):
            print('side ' + str(i + 1) + ' is ' + str(self.slides[i]))

if __name__ == '__main__':
    pol = Polygon(3)
    pol.input_sides()
    pol.display_sides()