# transform between motor speed and Get Values

When we control the motor move, we need to send a value to the web. This Document introduces the value calculation

## Equation

Value = (dx + (dy * 32768))

dx can be from -350 to 350: positive means turn left, negative means turn right
dy can be from -350 to 350: positive means move forward, negative means move backward
