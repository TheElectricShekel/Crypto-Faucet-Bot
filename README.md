# Crypto-Faucet-Bot
This bot will cycle through 13 different crypto faucet sites and activate the faucet every 60mins that it is available.

In order to run the bot do the following:

Open 'creds.txt'
	- The formatting is very important in this document
	- You don't need to change any of the site names
	- Replace the word e-mail with the e-mail you want to use for the site
	- Replace the word password with the password you want to use for the site
	- Do this for all of the sites listed
	- Save and exit

Run 'FreeFaucet.io_Register_Bot.exe'
	- You only need to run this once
	- It will register the username and password provided in creds.txt for all 13 sites
	- You will need to click the verification links sent to your e-mail when it completes

Run 'FreeFaucet.io_Bot.exe'
	- Make sure you have clicked the verification links for each site in your e-mail
	- Run the bot
	- You can minimize the bot while it runs
	- After the bot cycles through all of the sites, it will close the browser
	- When the timer is up and the faucets can be activated again, the bot will open the browser and start the process over.
