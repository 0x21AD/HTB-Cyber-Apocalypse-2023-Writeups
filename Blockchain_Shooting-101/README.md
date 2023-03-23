I recommend you to read the first blockchain wirteup first before diving into this one


Okay , lets check the contract source code, We have 3 boolean variables firstShot , SecondShot and Third shot..

Follwing the naming conventions and the modifiers you need to trigger change their value to True respectively , which means you need set firstShot to true then secondshot to true then ThirdShot to true other wise will fail the conditions in the modifiers.


okay let's set them to true one by one :

1. FirstShot , Inorder to set first shot to true you will need to call the function fallback , after some googling , Fallback is a standard function is solidity which gets called whenever the contract receives a wrong function call, but in order to call a function from the web3py script you have to put in the abi , so lets put a function name that doesn't exist in the contract source code in our abi and call it.



2.  secondShot , this gets triggered whenever the contract recv a a transaction , atleast that's how i get it.


3. finally thats a public function , you can see it in the contract source code , public means , you can just call it.

4. finally we combine those and execute the script and the get the flag , conditions are satisfied , flag is printed out. YAAAY