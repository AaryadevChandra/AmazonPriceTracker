# AmazonPriceTracker

The program is a simple Amazon Price Tracker to keep a track of the price of a particular product.
The program uses Selenium instead of conventional modules like Beautiful Soup or Scrapy.
Once the price is retrieved, the price is sent to a function to check whether the price of the product has come down.
If the price has indeed come down, the program makes use of the in-built smtplib module to send an email to the user regarding the price drop, along with a link of the amazon page containing the procuct so that the user can reach the product faster than anyone else and gain the epic victory royale by grabbing it first when the price goes down!
