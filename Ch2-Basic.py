#Print()
#ถ้าเป็นตัวอักษรให้ใส่ ''
print('Hello')
print('สวัสดี')
#ถ้าเป็นตัวเลข ไม่ต้องใส่ ''
print(123)
print(456.7890)
print() #เว้นบรรทัด
#ถ้าทำการประกาศตัวแปรแล้ว ตรงprint() ไม่ต้องใส่ ''
language = 'Python'
version = 4.0
print(language,version)
#===========================================================
a = 'One'
b = 'Two'
c = 'Three'
d = 'Four'
print(a,b,c,d,sep=',') #sep=''มีไว้เพื่อแสดงเครื่องหมายคั่นระหว่าง

e = 'www'
f = 1234
g = 'com'
print(e,f,g,sep='.')

date = 8
month = 7
year = 2561
print('วันนี้ตรงกับวันที่ : ',end='') #end='' เพื่อไม่ให้ขึ้นบรรทัดใหม่
print(date,month,year,sep='/')
#==========================================================
#การเชื่อมสตริง
s1 = 30
s2 = 5
str3 = 'ขอเชิญหมายเลข ' + str(s1) + ' ที่ช่องบริการ ' + str(s2) + ' ค่ะ'
print(str3)
#==========================================================
#ใช้ \n
text = 'Model: iPhone XX \nDisplay: 5.67" ' #\n = ขึ้นบรรทัดใหม่
print(text)

print('LineA\nLineB\nLineC')
print('เกิดข้อผิดพลาด กรุณาแก้ไขดังนี้ \n' +\
      '- ต้องใส่ชื่อและนามสกุลให้ครบ \n' +\
      '- ต้องใส่อีเมล์ให้ถูกต้องตามรูปแบบ \n' +\
      '- ต้องใส่รหัสผ่านทั้งสองช่องให้ตรงกัน')
print()
#===========================================================
#ใช้ \t
print('1 < โอนเงินภายในธนาคาร\tถอนระบุจำนวน > 5')
print('2 < โอนเงินต่างธนาคาร\t สอบถามยอด > 6')
print('3 < ชำระเงินด้วยบาร์โค้ด\t เติมเงินมือถือ > 7')
print('4 < ชำระสินค้าและบริการ\t  รายการอื่นๆ > 8')
#===========================================================
#input = ต้องการข้อมูลจากแป้นพิมพ์
n = input('กรุณาใส่ชื่อของท่าน >> ')
w = input('กรุณาใส่น้ำหนักของท่าน >> ')
yb = int(input('ปี พ.ศ. ที่ท่านเกิด >> '))
yr = int(input('ปีนี้ตรงกับ พ.ศ.>> '))
print(f'\nชื่อ: {n}, น้ำหนัก: {w} , อายุ: {yr-yb}') #(f'') นำข้อมูล input เข้ามา
#===========================================================
