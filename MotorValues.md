# transform between motor speed and Get Values

When we control the motor move, we need to send a value to the web. This Document introduces the value calculation

## Equation

dx can be from -350 to 350: positive means turn left, negative means turn right   
postprocessing:  
  if (dx > 16383) dx = 16383;  
  if (dx < -16383) dx = -16383;  
  if (dx < 0) dx = -dx + 0x4000;  
		

dy can be from -350 to 350: positive means move forward, negative means move backward  
postprocessing:  
  if (dy > 16383) dy = 16383;  
  if (dy < -16383) dy = -16383;  
  if (dy < 0) dy = -dy + 0x4000;  

value = (dx + (dy * 32768))

 
