import pyautogui
pyautogui.sleep(5)

pyautogui.moveTo(673,596) #Moves mouse to Last Name,First Name
pyautogui.click()
pyautogui.write('John Doe')

pyautogui.moveTo(673,743) #Moves to Teacher- period
pyautogui.click()
pyautogui.write('teacher period 3')

pyautogui.moveTo(673,885)#Moves to learner option
pyautogui.click()
#Human like scrolling
pyautogui.scroll(-5)
pyautogui.sleep(0.5)
pyautogui.scroll(-5)
pyautogui.sleep(0.5)
pyautogui.scroll(-5)
pyautogui.sleep(0.5)
pyautogui.scroll(-5)
pyautogui.scroll(-5)
# submit button is clicked
pyautogui.moveTo(703,908)
pyautogui.click()
# reload page
pyautogui.moveTo(745,425)
pyautogui.sleep(1)
pyautogui.click()
