class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, amount):
        self.width = amount

    def set_height(self, amount):
        self.height = amount

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter
    
    def get_area(self):
        area = self.width * self.height
        return area

    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.height ** 2)) ** .5
        return diagonal

    def get_picture(self):
        """Takes the width and height and returns a visual representation of the shape"""
        w = self.width
        h = self.height
        rows = ""
        if h > 50 or w > 50:
            return "Too big for picture."
        else:
            for num in range(0, h):
                rows += "*" * w + "\n"
            return rows  

    def __str__(self):
        """returns the shape represented as a string"""
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_amount_inside(self,other):
        """Takes another shape as an argument and returns the number of times it will fit inside the shape"""
        main_shape = self.get_area()
        inner_shape = other.get_area()
        num_times = main_shape // inner_shape
        return num_times


class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, amount):
        Rectangle.set_width(self, amount)
        Rectangle.set_height(self, amount)
 
    def __str__(self):
        return f"Square(side={self.width})"
