from models import db, User, Product, Order, Cart
from app import app

with app.app_context():

    print("Creating products...")
    watch = Product(name="oraimo watch 3 Pro, 1.83", description="BT call Smart Watch", price="5,999", image="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/04/1598351/1.jpg?5040", category="watch")
    watch2 = Product(name="oraimo Watch ES 2 1.95", description="AMOLED IP68 Smart Watch", price="4,500", image="https://cdn-img.oraimo.com/fit-in/600x600/KE/product/2024/05/25/OSW-810.png", category="watch")
    watch3 = Product(name="oraimo Watch Nova V 2.01", description="HD Video Watch Faces Smart Watch", price="5,200", image="https://cdn-img.oraimo.com/fit-in/600x600/KE/product/2024/06/20/OSW-802N.png", category="watch")
    headphones = Product(name="oraimo Necklace Lite Call", description="Vibration Wireless Headphones", price="1,900", image="https://cdn-img.oraimo.com/fit-in/600x600/MA/product/2024/03/19/OEB-311.png", category="headphones")
    earbuds = Product(name="oraimo Freepods pro + Hybrid ANC", description="True Wireless Earbuds", price="5,500", image="https://cdn-img.oraimo.com/fit-in/600x600/MA/product/2024/05/20/OEB-E108DC.png", category="earbuds")
    powerbank = Product(name="oraimo Traveler Link 27", description="27000mAh 12W Power Bank", price="4,100", image="https://cdn-img.oraimo.com/fit-in/600x600/KE/product/2024/06/28/opb-p5271-black.png", category="powerbank")
    headphones2 = Product(name="oraimo BoomPop 2 ENC", description="Over-Ear Wireless Headphones", price="2,600", image="https://cdn-img.oraimo.com/fit-in/600x600/NG/album/ohp-610/ohp-610-black.png", category="headphones")
    watch4 = Product(name="ZL02 Smart Watch", description="H Full S Reen Sport Fitness Black", price="2,690", image="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/37/523878/1.jpg?2248", category="smartwatch")
    phone = Product(name="Samsung Galaxy A35 5G, 6.6", description="256GB + 8GB RAM (Dual SIM), 5000mAh, Awesome Navy", price="45,999", image="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/34/2888232/1.jpg?2068", category="phones")
    phone2 = Product(name="Oppo Reno11 F 5G", description="8GB+256GB, 64MP,5000mAh,(Dual Sim) Palm Green (2YR WRTY)", price="46,999", image="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/59/0881742/1.jpg?1487", category="phones")
    phone3 = Product(name="Samsung Galaxy A55 5G, 6.6", description="256GB + 8GB RAM (Dual SIM), 5000mAh, Awesome Lilac", price="55,499", image="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/70/8221332/1.jpg?8433", category="phones")
    headphones3 = Product(name="Wireless L350", description="Foldable Sports Stereo Bluetooth Headset(Black)", price="5,000", image="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/45/2254212/1.jpg?9740", category="headphones")
    powerbank2 = Product(name="oraimo 27000 MAh", description="Travellers Portable Power Bank_Black", price="3,100", image="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/58/4494581/1.jpg?6507", category="powerbank")
    earbuds2 = Product(name="oraimo AirBuds 4 ENC", description="True Wireless Earbuds", price="2,100", image="https://cdn-img.oraimo.com/fit-in/600x600/AE/product/2024/02/06/OTW-340-680-1.png", category="earbuds")
    earbuds3 = Product(name="oraimo FreePods Neo", description="ENC True Wireless Earbuds", price="2,200", image="https://cdn-img.oraimo.com/fit-in/600x600/KE/product/2024/06/20/OTW-330S-black.png", category="earbuds")
    products = [watch,watch2,watch3,headphones,earbuds,powerbank, headphones2,watch4,phone,phone2,phone3,earbuds2,earbuds3]

    db.session.add_all(products)
    db.session.commit()

    print("Seeding done!")