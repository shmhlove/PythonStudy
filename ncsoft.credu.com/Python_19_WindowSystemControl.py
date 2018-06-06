#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

import time
import pyautogui

print('size : ',  pyautogui.size());
print('position : ',  pyautogui.position());

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

width, height = pyautogui.size();
pyautogui.moveTo(width/2, height/2)
print('position : ',  pyautogui.position());

pyautogui.moveRel(Nene, 20)

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

from lPython.display import clear_output
import time

x, y = -1, -1
while True:
	if (x,y) == pyautogui.position():
		continue
	x, y = pyautogui.position()
	clear_output()
	print('x={}, y={}'.format(x,y))

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

pyautogui.click()
pyautogui.click(width/2, height/2)
pyautogui.click(button='right')
pyautogui.rightClick()

time.sleep(5)
pyautogui.click(clicks=2)

time.sleep(5)
pyautogui.doubleClick()

time.sleep(5)
pyautogui.click(clicks=2, interval=1.5)

time.sleep(5)
pyautogui.mouseDown()
pyautogui.mouseUp()

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# Drag
time.sleep(5)
pyautogui.mouseDown(button='right')
pyautogui.mouseUp(button='right', x=1260, y=700)

time.sleep(5)
pyautogui.dragTo(x=1260, y=700)
pyautogui.dragTo(x=1260, y=700, duration=2)

time.sleep(5)
pyautogui.dragRel(-100m 100, duration=2)

time.sleep(5)
distance = 100
while distance > 0:
	pyautogui.dragRel(distance, 0, distance=0.5)
	distance -= 5
	pyautogui.dragRel(0, distance, distance=0.5)
	pyautogui.dragRel(-distance, 0, distance=0.5)
	distance -= 5
	pyautogui.dragRel(0, distance, distance=0.5)
	
#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# Scrolling
pyautogui.scroll(-100)
pyautogui.scroll(100)

pyautogui.scroll(200, x=100, y=100)
	
#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# keyboard input
time.sleep(5)
pyautogui.typewrite('Hello!')
pyautogui.typewrite('Hello!', interval=0.25)
pyautogui.typewrite('한글은 안 돼요..', interval=0.25)

time.sleep(5)
pyautogui.press('enter')
pyautogui.press(['backspace', 'enter'])

time.sleep(5)
pyautogui.typewrite('Hello')
pyautogui.keyDown('shift')
pyautogui.press('left')
pyautogui.keyUp('shift')

time.sleep(5)
pyautogui.keyDown('shift')
pyautogui.press('left')
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
pyautogui.press('right')
pyautogui.hotkey('ctrl', 'v')

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------