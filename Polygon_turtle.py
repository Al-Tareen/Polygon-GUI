import turtle 

class Polygon:

  def __init__(self, sides, name):
    self.sides = sides
    self.name = name
    self.sum_interior_angle = ((self.sides-2)*180) # <--- formula to calculate sum of interior angle of a polygon
    self.each_angle = (self.sum_interior_angle/self.sides) # <--- formula to calculate angle of each side of polygon

  def draw(self, size):
          print("Drawing your Polygon...")
          for i in range(self.sides):
              turtle.forward(size)
              turtle.right(180-self.each_angle)
          print("Drawing Complete")
          turtle.done()

shapes = {3: 'Equilateral-Triangle', 4: 'Square', 5: 'Pentagon', 6: 'Hexagon', 7: 'Heptagon', 8: 'Octagon', 9: 'Nonagon', 10: 'Decagon'}

shape = Polygon(int(input("Please enter your desired number of sides in your Polygon: ")), name='n-gon')

while shape.sides <3:
    shape = Polygon(int(input("A Polygon cannot be lower than 3. Please enter a number greater than 3: ")), name='n-gon')
    
if shape.sides > 12:
    print("Could not determine a name for your ", str(shape.sides) + "-gon")

elif shape.sides >= 3 and shape.sides <= 12:
    print(shapes[shape.sides] + " Detected.")

shape.draw(int(input("Please enter the size(px) of each side of your Polygon: ")))

