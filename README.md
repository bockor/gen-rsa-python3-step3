Python3 Exercise Step 3
-----------------------
- Consider this repo as the starting point.

- Ensure that user input is verified :
	- p & q: must be integer and prime number
	- m : must be integer and less than the modulus

- Work with a "while" loop(s) until the user gets it right.  See the expectations.png screenshot.

- It is evident that the focus is the implementation of the python code but in the light to get a grip on Git collaboration framework one could:
	- Fork the repo to your account, using the Fork button on the right
    - Install git on your Ubuntu box
		- https://linuxconfig.org/how-to-install-git-on-ubuntu-18-04-bionic-beaver-linux
	- git clone https://path-to-the-forked-git.git
	- cd  path-to-the-forked-git
	- git branch -a (show local & remote branches)
	- git branch validate-user-input (create a new branch)
	- git checkout validate-user-input (change to the new branch)
	- vim myfile.py (implement your code here and save)
	- git add myfile.py (stage the file)
	- git commit -m 'script changed' (snapshot the file)
	- git push -u origin validate-user-input (sync your local with your remote repo)

- BTW what's the difference between forking and cloning ?
	- https://github.community/t5/Support-Protips/The-difference-between-forking-and-cloning-a-repository/ba-p/1372
