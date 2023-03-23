It was my first time dealing with restricted bash.

1. look at the sshd_config to know that you will ssh under restricted user with empty password. (last 2 line Premit Empty password to user named restricted).

2. after ssh , it's rbash , nth is allowed that will help us cat the flag.

3. let's look at the files provided.

4. the bash_profile , sets the PATH env variable to $HOME/.bin , so we can't simply use any binaries in the /bin , because we can't type slashes in rbash

5. since it was my first time using rbash, I had to google it and found a great resource : https://www.exploit-db.com/docs/english/44592-linux-restricted-shell-bypass-guide.pdf

6. after some reading from the resource we found an interesting option in ssh, which is -t , -t forces a a psuedo-terminal , you can read the man page

7. Finally we can do the followng: 

ssh restricted@104.248.169.117 -p 32700 -t "bash"

8. now you are spawned in bash shell not rbash, but you will have to specify the full path to binaries as you are getting $PATH from the bash_profile provided by the challenge which doesn't see /bin 

9. simply you can ssh restricted@104.248.169.117 -p 32700 -t "bash --noprofile" to ignore the bash_profile provided by the challenge


it was an interesting one and first time to deal with rbash.