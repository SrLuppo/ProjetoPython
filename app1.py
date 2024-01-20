import keyboard
import time

time.sleep(2)

# Envie as teclas "Windows + R" e aguarde um pouco antes de enviar "Enter"
keyboard.press_and_release("win+r")
time.sleep(1)
keyboard.press_and_release("enter")


# keyboard.send("windows+r+enter")
# keyboard.send("ctrl+shift+esc")
