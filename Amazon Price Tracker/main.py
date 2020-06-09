import selenium
from selenium import webdriver
import time
import smtplib

while True:

    path = "C:/Users/Swati/PycharmProjects/Amazon Price Tracker/chromedriver.exe"

    driver = selenium.webdriver.Chrome(path)

    driver.get("https://www.amazon.in/ZenBook-UX433FA-A6111T-i7-8565U-Integrated-Graphics/dp/B07MC2XZ3X/ref=sr_1_2_sspa?dchild=1&keywords=asus+zenbook+i7&qid=1591386856&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyWjE4MFY0SlpCVlAmZW5jcnlwdGVkSWQ9QTA1NzE1NTlTV01ES0k2V0VGVUomZW5jcnlwdGVkQWRJZD1BMDU4MDg4N09DTFNFRllTQjc5VCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
    # replace the url with the product url of your choice

    def get_price():
        price = driver.find_element_by_id("priceblock_ourprice")
        price_text = price.text
        price_text = price_text.replace(',', '')
        price_text = price_text.replace(' ', '')
        num_price = int(price_text[1:6])
        return num_price


    def send_mail():
        num_price = get_price()
        current = 85991
        if num_price < current:
            email()
            print("An email has been sent!")
            current = num_price
            

    def email():
        sender = ""  # sender email in double quotes
        rec_email = ""  # receiving email in double quotes
        password = ""  # password of sender email address
        message = """Prices have gone down! Check the link->
        https://www.amazon.in/ZenBook-UX433FA-A6111T-i7-8565U-Integrated-Graphics/dp/B07MC2XZ3X/ref=sr_1_2_sspa?dchild=1&keywords=asus+zenbook+i7&qid=1591386856&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyWjE4MFY0SlpCVlAmZW5jcnlwdGVkSWQ9QTA1NzE1NTlTV01ES0k2V0VGVUomZW5jcnlwdGVkQWRJZD1BMDU4MDg4N09DTFNFRllTQjc5VCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="""
        # replace the url with the product url of your choice

        server = smtplib.SMTP('64.233.184.108')
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, rec_email, message)


    send_mail()
    driver.close()
    time.sleep(60 * 60 * 24)  # program will run every 24 hours
