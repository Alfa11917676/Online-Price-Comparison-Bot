from selenium import webdriver
browser=webdriver.Chrome('C:\\Users\\ARNAB RAY\\Desktop\\python\\chromedriver_win32\\chromedriver.exe')
print("Checking price at Amazon-----------------")
browser.get('https://www.amazon.in/Test-Exclusive-544/dp/B077PWK5BY/ref=sr_1_2?crid=3ONKAV9Z3CQMK&dchild=1&keywords=oneplus+8+pro&qid=1598124400&sprefix=onep+%2Caps%2C297&sr=8-2')
pe=browser.find_element_by_id('priceblock_ourprice')
pr=pe.get_attribute('textContent')
pr=pr[2:]
pl=pr.split(',')
price_a=''
for i in pl:
    price_a+=i
price_a=float(price_a)
print("The price of the product on Amazon is "+str(price_a))
print("Checking price at Flipkart-----------------")
browser.get('https://www.flipkart.com/oneplus-8-pro-glacial-green-256-gb/p/itm4dcbd336cdd4f?pid=MOBFU897HFBWA7Y5&lid=LSTMOBFU897HFBWA7Y5XVBKK8&marketplace=FLIPKART&srno=s_1_8&otracker=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&fm=SEARCH&iid=1a781a30-6e90-4e2f-a148-efe45a5344c4.MOBFU897HFBWA7Y5.SEARCH&ppt=sp&ppn=sp&ssid=5a0no8vfio0000001598124433715&qH=8de9fb854f805dea')
pe=browser.find_element_by_xpath('//div[@class="_1vC4OE _3qQ9m1"]')
pr=pe.get_attribute('textContent')
pr=pr[1:]
pl=pr.split(',')
price_f=''
for i in pl:
 price_f+=i
price_f=float(price_f)
print("The price of the product on Flipkart is "+str(price_f))
if(price_a<price_f):
        sum=price_f-price_a
        print("You are suggested to take the item from Amazon as the item is at a lower price of "+str(sum)+" than in Flipkart")
elif(price_f<price_a):
    sum=price_a-price_f
    print("You are suggested to take the item from Flipkart as the item is at a lower price of " + str(
        sum) + " than in Amazon")
else:
    print("The price at both the website is same you can take from either of them")