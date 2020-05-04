# Browser-and-Windows-App-Automation

**A project to automate browser and windows application steps**

## Idea:

While working from home I need to use various different programs and online logins to start a tender writing process for the company I work for. Doing this all by hand is rather tedious and takes roughly 5 mins to complete before I can actually start work. Because of this I wrote this program in order to start and speed up the process with just one click. The program takes under 30s to complete.

### What does it need to do:

**1)** Start up and login to a VPN in order to access company files (in this case Cisco AnyConnect)

**2)** Start up company webpage, log in and navigate to the tender page (using Chrome webdriver)

**3)** Open a specific spreadsheet located on the company server, accessible through VPN (Excel)

**4)** Create a new local folder at a specific location on my PC, ready to be filled with files regarding a new tender

## Tools used:

Python

PyCharm IDE

Selenium with chrome webdriver



 

## Auto-Run Cisco AnyConnect Secure Mobility Client

HOW TO:

Type the Cisco_Start script in Notepad and save as FILENAME.vbs, replace PASSWORD with your password and if neccesary replace the path to the VPN Client exe. The sleep times may need adjusting depending on your internet connection speed. 
