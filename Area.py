class area:
    def triangle(base,height):
       return 0.5 * base * height

    def rectangle(length,width):
        return length * width        
    
triangle_area = area.triangle (10,5)
print(f'area of triangle is {triangle_area}')

rectangle_area = area.rectangle (15,10)
print(f'area of rectangle is {rectangle_area}')
