1. After connecting you will have the option to either Create or load a config.
2. lets try to create a config and see how it looks like 
![alt text](https://github.com/SecYuri/HTB-Cyber-Apocalypse-2023-Writeups/blob/main/misc_hijack/1.PNG)

3. okay, it takes some info and returns a serliazed base64 , you can google for python deserialization attacks, here's a great quick resource to guide you https://www.slideshare.net/NSCONCLAVE/python-deserialization-attacks

4. okay all we need to do is just write a malicious object , implement __reduce__ function which gets called when the object is deserialized , put your system commands in their , run the exploit then take the serliazed object and base64 you can do it within the script if you want, then send the base64 to be loaded in the challenge.

![alt text](https://github.com/SecYuri/HTB-Cyber-Apocalypse-2023-Writeups/blob/main/misc_hijack/2.PNG)

![alt text](https://github.com/SecYuri/HTB-Cyber-Apocalypse-2023-Writeups/blob/main/misc_hijack/3.PNG)

