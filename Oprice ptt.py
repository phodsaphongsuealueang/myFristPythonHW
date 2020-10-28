from zeep import Client
from lxml import rtree

client = Client('http://www.pttor.com/oilPrice.asmx?WSDL')
resoult = client.service.CurrentOilPrice(Language="en")
root = etree.formstring(result)
n = len(root)
name = ['none']
price = [0]

y = 1
while y == 1:
    print('################################################################################')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                          Gasoline 95 ราคา 29.16 Bath                         #')
    print('#                          Gasoline 91 ราคา 25.30 Bath                         #')
    print('#                          Gasohol 91 ราคา 21.68 Bath                          #')
    print('#                          Gasohol E20 ราคา 20.2 Bath                          #')
    print('#                          Gasohol 95 ราคา 21.2 Bath                           #')
    print('#                          Diesel ราคา 21.1 Bath                               #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('################################################################################')
    t = input(
        "Gasoline 95,Gasoline 91,Gasohol 91,Gasohol E20,Gasohol 95,Diesel :\nต้องการ =")
    p = input("ผู้ใช้งานเลือกว่าจะคำนวณ : เงินเป็นลิตร : ลิตรเป็นเงิน ")
    if 'เงินเป็นลิตร' in p:
        g1 = input('กรุณาใส่จำนวนเงินที่ต้องการ:\n จำนวนเงิน = ')
        m1 = int(g1)
    if 'ลิตรเป็นเงิน' in p:
        g2 = input('กรุณาใส่จำนวนลิตรที่ต้องการ:\n จำนวนลิตร = ')
        m2 = int(g2)
    print('################################################################################')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                 คำนวณจากเงินเป็นลิตร                            #')
    print('#                                 คำนวณจากลิตรเป็นเงิน                            #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('################################################################################')
    if 'เงินเป็นลิตร' in p:
        if 'Gasoline 95' in t:
            k = (m1/29.15)
            print('จะได้', '%.2f' % k, 'ลิตร')
        elif 'Gasoline 91' in t:
            k = (m1/25.30)
            print('จะได้', '%.2f' % k, 'ลิตร')
        elif 'Gasohol 91' in t:
            k = (m1/21.68)
            print('จะได้', '%.2f' % k, 'ลิตร')
        elif 'Gasohol E20' in t:
            k = (m1/20.2)
            print('จะได้', '%.2f' % k, 'ลิตร')
        elif 'Gasohol 95' in t:
            k = (m1/21.2)
            print('จะได้', '%.2f' % k, 'ลิตร')
        elif 'Diesel' in t:
            k = (m1/21.1)
            print('จะได้', '%.2f' % k, 'ลิตร')

    if 'ลิตรเป็นเงิน' in p:
        if 'Gasoline 95' in t:
            k = (m2*29.15)
            print('ราคาน้ำมัน =', k, 'บาท')
        elif 'Gasoline 91' in t:
            k = (m2*25.30)
            print('ราคาน้ำมัน =', k, 'บาท')
        elif 'Gasohol 91' in t:
            k = (m2*21.68)
            print('ราคาน้ำมัน =', k, 'บาท')
        elif 'Gasohol E20' in t:
            k = (m2*20.2)
            print('ราคาน้ำมัน =', k, 'บาท')
        elif 'Gasohol 95' in t:
            k = (m2*21.2)
            print('ราคาน้ำมัน =', k, 'บาท')
        elif 'Diesel' in t:
            k = (m2*21.1)
            print('ราคาน้ำมัน =', k, 'บาท')
    else:
        print("ใส่ชนิดใหม่")
    x = int(input("ใส่ 1 หรือ 0"))
    if x == 1:
        y = 1
    elif x == 0:
        y = 0
