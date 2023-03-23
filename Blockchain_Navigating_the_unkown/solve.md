This is my first time ever dealing with a blockchain so here's what I learned to through solving the challenge

You will be given two different ports , which you normally nc to it it will give you the information you need , private key to sign your transactions , contract address , and your address , and the other port the one that you will be connecting to through the script to interact with the blockchain.

1. Alot of googling and chatgpt and you can craft out the general structure of web3 python code and modify it for each challenge

3. each challenge will have a setup.sol , take a look at it will tell you how you win. it will show the checks being made when you get the flag , if the conditions are satisfied you the flag will be printed out.

2. in order to call a function you need to define an abi , think of it as the structure of the contract source code , in order to get this abi , you can use: https://remix.ethereum.org/ , go to contracts create a new contract put the source code click compile and you can get the abi that describes the callable functions in the contract.

![alt text](https://github.com/SecYuri/HTB-Cyber-Apocalypse-2023-Writeups/blob/main/Blockchain_Navigating_the_unkown/1.png)


2. all you need to do for this challenge is to call function udpateSensors and give pass the value 10 to it then will set the update to true. 