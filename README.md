# cat-compromiser
A tool that modifies the "cat" command in Linux to send its output to a remote server. Used to demonstrate the MITRE ATT&amp;CK technique "Compromise Client Software Binary."

**Warning: DO NOT USE THIS COMMAND ON ANY COMPUTER THAT MATTERS TO YOU!** You will be modifying one of the most fundamental linux programs. Use at your own risk.

## How to use
1. Set up an Ubuntu server that you don't care about.
2. Clone the repository.
3. Mark the script as executable. `sudo chmod +x setup`
4. Run the script. `./setup`
5. Install python, pip, and flask as needed. `pip install flask`
6. Create the log file. `touch data.txt`
7. In another console window, start the "remote" server (which I assume is actually running on localhost, this is just a demo). `python remote_server.py`
8. Try using the cat command. `cat whatever_file.txt`
9. Either look at the data.txt or go to `localhost` in a web browser.
10. Enjoy seeing your file logged to the "remote" server.
