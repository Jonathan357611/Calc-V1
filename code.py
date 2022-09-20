import board
from digitalio import DigitalInOut, Direction, Pull
import busio as io
import adafruit_ssd1306

# CONFIG
HID = False

class layout:
        def __init__(self):
            ...
        def write(self, *args):
            return 0
if HID:
    # Importing here reduces boot time for non-HID users
    import usb_hid
    from adafruit_hid.keyboard import Keyboard
    from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS7
    from adafruit_hid.keycode import Keycode
    
    try:
        keyboard = Keyboard(usb_hid.devices)
        layout = KeyboardLayoutUS(keyboard)  # Not important for Numpad
    except Exception:
        layout = layout()
else:
    layout = layout()

# OLEDS
i2c1 = io.I2C(board.GP3, board.GP2)
oled1 = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c1)

i2c2 = io.I2C(board.GP1, board.GP0)
oled2 = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c2)

oled1.text("C A L C _ V 1", 25, 10, 1)
oled1.show()

oled2.text("by Jonathan F.", 40, 24, 1)
oled2.show()

# Buttons
## Operators

btn_divide = DigitalInOut(board.GP16)
btn_multiply = DigitalInOut(board.GP21)
btn_subtract = DigitalInOut(board.GP14)
btn_add = DigitalInOut(board.GP15)

## Other
btn_decimal = DigitalInOut(board.GP17)
btn_clear = DigitalInOut(board.GP10)
btn_enter = DigitalInOut(board.GP26)

## Numbers
btn_zero = DigitalInOut(board.GP20)
btn_seven = DigitalInOut(board.GP18)
btn_eight = DigitalInOut(board.GP13)
btn_nine = DigitalInOut(board.GP27)
btn_four = DigitalInOut(board.GP22)
btn_five = DigitalInOut(board.GP9)
btn_six = DigitalInOut(board.GP28)
btn_one = DigitalInOut(board.GP11)
btn_two = DigitalInOut(board.GP19)
btn_three = DigitalInOut(board.GP12)

# Some lists to keep track of all the buttons
BTN_LIST = [btn_clear, btn_divide, btn_multiply, btn_subtract, btn_add, btn_seven, btn_eight, btn_nine, btn_four, btn_five, btn_six, btn_one, btn_two, btn_three, btn_zero, btn_decimal, btn_enter]
BTN_ALIAS = ["btn_clear", "btn_divide", "btn_multiply", "btn_subtract", "btn_add", "btn_seven", "btn_eight", "btn_nine", "btn_four", "btn_five", "btn_six", "btn_one", "btn_two", "btn_three", "btn_zero", "btn_decimal", "btn_enter"]
BTN_MATH = {
    "btn_seven": 7,
    "btn_eight": 8,
    "btn_nine": 9,
    "btn_four": 4,
    "btn_five": 5,
    "btn_six": 6,
    "btn_one": 1,
    "btn_two": 2,
    "btn_three": 3,
    "btn_zero": 0,
    "btn_decimal": "."
    }

# Set every button-pin as a Pulldown + Input
for button in BTN_LIST:
    button.direction = Direction.INPUT
    button.pull = Pull.DOWN

class Calculation:
    def __init__(self):
        self.calculation = []
        
    def clear(self):
        self.calculation = []
    
    def show(self):
        print(self.calculation)
        if len(self.calculation) == 0:
            return "0"
        return "".join([str(x) for x in self.calculation])
    
    def add_calculation(self, button):
        # Write to HID
        layout.write(str(BTN_MATH[button]))
        
        self.calculation.append(BTN_MATH[button])
        return self.show()
    
    def divide(self):
        if len(self.calculation) == 0 or type(self.calculation[-1]) == int:
            self.calculation.append("/")
        elif self.calculation[-1] != "/":
            self.calculation[-1] = "/"
        return self.show()
    
    def multiply(self):
        if len(self.calculation) == 0 or type(self.calculation[-1]) == int:
            self.calculation.append("*")
        elif self.calculation[-1] != "*":
            self.calculation[-1] = "*"
        return self.show()
        
    def subtract(self):
        if len(self.calculation) == 0 or type(self.calculation[-1]) == int:
            self.calculation.append("-")
        elif self.calculation[-1] != "-":
            self.calculation[-1] = "-"
        return self.show()
        
    def add(self):
        if len(self.calculation) == 0 or type(self.calculation[-1]) == int:
            self.calculation.append("+")
        elif self.calculation[-1] != "+":
            self.calculation[-1] = "+"
        return self.show()
    
    def calculate(self):
        try:
            return str(eval(self.show()))
        except:
            return "No 0-division!"
    

def clear(show=False):
    oled1.fill(0)
    oled2.fill(0)
    if show:
        oled1.show()
        oled2.show()

def print_lines(solution, display):
    pos_y = 0
    pos_x = 0
    for letter in solution:
        if pos_x >= 110:
            pos_x = 0
            pos_y += 8
        display.text(letter, pos_x, pos_y, 1)
        pos_x += 7
    
    oled1.show()
    oled2.show()
    
calculation = Calculation()
while True:
    for button, name in zip(BTN_LIST, BTN_ALIAS):
        was_pressed = False
        #while button.value:
        #    was_pressed = True
        if button.value: 
            if name == "btn_clear":
                calculation.clear()
                clear(True)
                print_lines("0", oled1)
                print_lines("0", oled2)
            elif name == "btn_enter":
                layout.write("\n")
                print_lines(calculation.calculate(), oled2)
            elif name == "btn_divide":
                layout.write("/")
                clear()
                print_lines(calculation.divide(), oled1)
            elif name == "btn_multiply":
                layout.write("*")
                clear()
                print_lines(calculation.multiply(), oled1)
            elif name == "btn_add":
                layout.write("+")
                clear()
                print_lines(calculation.add(), oled1)
            elif name == "btn_subtract":
                layout.write("-")
                clear()
                print_lines(calculation.subtract(), oled1)
            else:
                clear()
                print_lines(calculation.add_calculation(name), oled1)
            oled1.show()
            oled2.show()
            print(name)
