#Keylogger stores whatever was typed in a text file.

# using the 'with' kwyword releases the memory automatically

with open("Keylogger/log.txt",'a') as f:
    f.write("Appending with the 'with' keyword now")