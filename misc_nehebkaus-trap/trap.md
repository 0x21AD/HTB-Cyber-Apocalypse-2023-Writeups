1. Connecting to docker , we are spawned into a shell , writing any thing we get the following :
    Error: name 's' is not defined

2. That's a python error , okay let's try to print smth out, and ofcourse everyting is blacklisted , single qoutes , double qoutes , spaces , you name it...

![alt text](https://github.com/SecYuri/HTB-Cyber-Apocalypse-2023-Writeups/blob/main/misc_nehebkaus-trap/1.PNG)


3. Mmmm how can we get around , the answer is EXEC my friend , and for anyone how doesn't what exec do in python , it's exactly like eval in php , it takes input and executes it as a python code.

4. We can do exec(chr(112)+chr(114)+chr(105)+chr(110)+chr(116)+chr(40)+chr(34)+chr(121)+chr(117)+chr(114)+chr(105)+chr(34)+chr(41))
this maps to exec(print("yuri")) which will execute print("yuri")

5. last step just scripting it out , it will be pain if you did it manually xD.

6. just had to do some simple modifications manually , added chr(10) and chr(9) after with open which maps to new line and tap

-> with open ("flag.txt" , "r"):\n\t
    print(f.read())
python you have to put a correct indentation in order to work so the chr(10) maps to new line and chr(9) maps to \t 

![alt text](https://github.com/SecYuri/HTB-Cyber-Apocalypse-2023-Writeups/blob/main/misc_nehebkaus-trap/2.PNG)

worked locally ! NICE.

6. and we are done.

![alt text](https://github.com/SecYuri/HTB-Cyber-Apocalypse-2023-Writeups/blob/main/misc_nehebkaus-trap/3.PNG)
