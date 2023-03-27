# $language = "python"
# $interface = "1.0"

'''

This script reads lines from a text file and sends them to the current terminal window.

The script sleeps for $DELAY seconds between each line.

If the "EOF" string is encountered, the script stops without processing further lines.


'''

from time import sleep


# Delay between lines in seconds
DELAY = 0.2


def main():
    # crt.Screen.Synchronous = True
    filename = crt.Dialog.FileOpenDialog("Open file containing commands" + "\r")

    if filename:
        with open(filename) as f:
            crt.Screen.Send("! SENDING COMMANDS FROM FILE " + filename + " !")
            for line in f.readlines():
                if "EOF" in line or line.strip() == "end":
                    break
                crt.Screen.Send(line)
                if "crypto key" in line:
                    sleep(2)
                else:
                    sleep(DELAY)
            crt.Screen.Send("! EOF !" + "\r")
    # crt.Screen.Synchronous = False

main()