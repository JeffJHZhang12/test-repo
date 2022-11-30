import pyautogui
import time
import random


def xx():
    try:
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        width, height = pyautogui.size()
        while True:
            # x, y = pyautogui.position()
            # s = "X: " + str(x).rjust(4) + " Y: " + str(y) .rjust(4)
            # print(s, end="")
            # print("\b" * len(s), end="", flush=True)
            x = random.randint(1, width-1)
            y = random.randint(1, height-1)
            print(x, "--->", y)
            pyautogui.click(x, y)
            # yy = 100
            # for i in range(100):
            #     yy = yy+50
            #     if yy > y:
            #         return
            #     pyautogui.click(200, yy)
            time.sleep(20)

    except pyautogui.FailSafeException:

        print("Done")
    except KeyboardInterrupt:
        print("k")


if __name__ == "__main__":
    xx()
# pyautogui.PAUSE = 1
# x, y = pyautogui.size()
# yy = 100
# for i in range(100):
#     yy = yy+50
#     if yy > y:
#         break
#     pyautogui.click(200, yy)
