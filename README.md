# ShiftrCompletion
A selenium script that allows for Duke students employed by the CoLab to input their hours to shiftr more easily. Note that this code is currently set up to put in repeating shifts across a two-week span (i.e. office hours, recurring appointments, etc.), so any one time shifts will be duplicated and need to be deleted. Still faster than the usual Shiftr UI tho.

## SETUP STEPS:
1. *THIS CODE REQUIRES AN ENVIRONMENT WITH SELENIUM, PANDAS, AND NUMPY. Install these!* I ran this on Python 3.11.2, but many versions will likely work.
  1a) This code also makes use of an .exe called chromedriver. Currently, the chromedriver.exe in this repo is the up to date one as of 1/28/24. If it throws an error citing the problems with chromedriver compatibility, download the newest stable one from [here](https://chromedriver.chromium.org/downloads). I believe that Mac users can also download a Mac compatible version, but I haven't tried it yet.
2. Make a file called secret.py in the same folder as where you download this file to. In it, include two functions called getnetid() and getpassword() that return your netid and password, respectively, as strings. These functions will be automatically called so that all you have to do is click on your Duo Push option, accept it, and click login.
3. In Hours.xlsx, put in the day of your recurring (see above) shift, the hours of clock in and out (in MILITARY TIME i.e. 13:00 ), what part of the CoLab you were working for, and the description.

## TO USE:
1. Make sure you have completed the setup steps above! This is where most of the errors will come from.
2. Edit and SAVE Hours.xlsx. Make sure everything is in the same folder on your computer.
3. Run ShiftrCompletion.py. After inputting your username and password automatically, you then have to click on the Duo method. In the terminal, hit Enter on the input line when you are on the MAIN SHIFTR page. Do not go to the Hours tab.
4. Do not touch the tab until it is done processing every row of the table. Then, go in and delete duplicates if needed.

For any issues, email me at jkm53@duke.edu. It is a work in progress for sure, so I will try to tackle any issues that I find, but let me know if you have any ideas or suggestions for how to improve! The next thing that I will implement is one-time shifts, but this was the start. Note also, this code relies on calculating the date from the current time (i.e. the time that the code is run), so you may run into issues if you don't run it on a Sunday night like I do.