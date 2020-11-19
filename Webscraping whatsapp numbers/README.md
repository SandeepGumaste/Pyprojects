Whatsapp.py
This is for business owners who recieve orders on Whatsapp. As the customer already has your contact saved, you can save the customer's number and then later post shop updates on Whatsapp status. Let's say you recieve 20-30 new orders per day, then saving contacts one by one can be a pretty boring thing to do and also time consuming. I wrote this program to make the contact saving process easy. This program exports a CSV file which contains phone numbers and random 8 letter string as the name. The name of the CSV file is the date on which you run the program. You can use any free online file conversion service to convert it from .CSV to .vcf.
I could've exported it directly in .vcf format but I still have'nt figured out how to write a vcf file. I'll update it once I figure that out.
You'll have to install Selenium and pyAutoGUI for this to run.
Also download chrome driver and place it in the same folder as the program.
https://chromedriver.chromium.org/

 Stop using the mouse after you scan the qr code (Do not even touch it!).
 You can start using the mouse once it alerts you to log out of Whatsapp web.
 This program works for numbers starting with +91 but you can change it (line 28 in the code) to work for whichever country you live in. 