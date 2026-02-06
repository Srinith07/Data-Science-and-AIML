def cal_rectangle_area(length, width):
    return length * width


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = cal_rectangle_area(length, width)
print(f"The area of the rectangle is: {area}")
preimeter = 2 * (length + width)
print(f"The perimeter of the rectangle is: {preimeter}")
cal_rectangle_area(length, width)
