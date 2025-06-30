class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def send_sms(self,phone,sms):
        print(f'Sending SMS to {phone} na it is {sms}')

myphone=Phone('Goole','pixel 7',100000)
print(myphone.brand)
print(myphone.model)    
print(myphone.price)

herphone=Phone('Apple','iPhone 14',200000)
print(herphone.brand)   
print(herphone.model)
print(herphone.price)