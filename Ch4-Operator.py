# == เท่ากับ
# != ไม่เท่ากับ
# > มากกว่า
# < น้อยกว่า
# >= มากกว่าเท่ากับ
# <= น้อยกว่าเท่ากับ

#Operator กลุ่มนี้จะให้ผลลัพธ์ออกมาเป็น True,False
#เรียกค่า True/False ว่า BOOLEAN โดยไพธอน True = 1 / False = 0
# ==
a = (1==2)
b = (5==5)
c = (a==b)
print('Operator == : ', a,'/',b,'/',c,)
#!=
a = (1!=2)
b = (5!=5)
c = (a!=b)
print('Operator != : ', a,'/',b,'/',c,)

#>
a = (1>2)
b = (5>5)
c = (a>b)
print('Operator > : ', a,'/',b,'/',c,)

#<
a = (1<2)
b = (5<5)
c = (a<b)
print('Operator < : ', a,'/',b,'/',c,)

#>=
a = (1>=2)
b = (5>=5)
c = (a>=b)
print('Operator >= : ', a,'/',b,'/',c,)

#<=
a = (1<=2)
b = (5<=5)
c = (a<=b)
print('Operator <= : ', a,'/',b,'/',c,)

#=========================================================
print()
#ลักษณะคำสั่ง if
if True:
    print('Hello world')

if False:
    print('สวัสดีชาวโลก') #จะไม่ถูกดำเนินการเนื่องจากเงื่อนไขเป็นเท็จ

a = (1==1) #แสดงว่า a = True
if a:
    print('a = True')
    print('ตัวแปร a มีค่าเป็น True')

b = 1 #ในไพธอน True = 1
if b:
    print('b = True')

c = 0 #ในไพธอน False = 0 จึงไม่ถูกดำเนินการเนื่องจากเงื่อนไขเป็นเท็จ
if c:
    print('c = False')
#=======================================================
print()
#การกำหนดเงื่อนไขดเวย Comparison Operator
a = True
if a == True:
    print('ตัวแปร a มีค่าเป็น True')
b = False
if b == False:
    print('ตัวแปร b มีค่าเป็น False')
#======================================================
print()
x = int(input('x = '))
y = int(input('y = '))
if y == 0:
    print('ตัวหารเป็น 0 ไม่ได้ค่ะ')
if y != 0:
    z = format(x/y)
    print(f'{x}/{y}={z}')
#======================================================
print()
n = int(input('number ='))
if n % 2 ==0:
    print(f'{n} เป็นเลขคู่')
if n % 2 != 0:
    print(f'{n} เป็นเลขคี่')
print()
#======================================================
#if-else
#if เงื่อนไข :
#    คำสั่งต่างๆ ถ้าเงื่อนไขตรงกับที่กำหนด
#else:
#   คำสั่งต่างๆ ถ้าเงื่อนไขไม่ตรงกับที่กำหน
x = 99
if x %2 ==0:
    print(x,'เป็นเลขคู่')
else:
    print(x,'เป็นเลขคี่')
print()
#=======================================================
x = int(input('x = '))
y = int(input('y = '))
if y == 0:
    print('ตัวหารเป็น 0 ไม่ได้ค่ะ')
else:
    print(f'{x}/{y} = ',x/y)
print()
#=======================================================
pw1 = input('Password : ')
pw2 = input('Confirm Password :')
if pw1 == pw2:
    print('>>> Password OK <<<')
else:
    print('>>> Password not match <<<')
print()
#======================================================
#if-elif ใช้เมื่อต้องการแยกหลายๆ กรณี แต่มีเพียงกรณีเดียวเท่านั้นที่ถูกเลือกให้ดำเนินการ
x = input('x = ')
y = input('y = ')
if x>y :
    print('x มากกว่า y')
elif x<y:
    print('x น้อยกว่า y')
elif x == y:
    print('x เท่ากับ y')
#=======================================================
print()
size = 'M'
text = ()
if size == 'S':
    text = 'Small'
elif size == 'M':
    text = 'Medium'
elif size == 'L':
    text = 'Large'
elif size == 'XL':
    text = 'Extra Large'
print(text)
#======================================================
print()
age = 18
str()
if age >=60:
    str = 'วัยชรา'
elif age >=20 :
    str = 'วัยผู้ใหญ่'
elif age >= 12: #หลังจากที่ถูกดำเนินการจะข้าม elif อื่นไปเลย
    str = 'วัยรุ่น'
elif age >= 2:
    str = 'วัยเด็ย'
elif age > 0:
    str = 'วัยทารก'
print(str)
print()
#======================================================
#ความแตกต่างของ if และ if elif
print('วิธี if')

login = 'admit'
psw = ''
if login != 'admin':
    print('Login Incorrect')
if psw != '1234':
    print('Password Incorrect')
if psw == '':
    print('Password Empty')
print()
print('วิธี if-elif')

login = 'admit'
psw = ''
if login != 'admin':
    print('Login Incorrect')
elif psw != '1234':
    print('Password Incorrect')
elif psw=='':
    print('Password Empty')
#=======================================================
#if-elif-else >>กรณีที่มีเงื่อนไขอื่นๆ ที่นอกเหนือจากประเด็กหลัก
print('ยอดเงินคงเหลือ : 30,000 บาท')
balance = 30_000.00

withdraw = float(input('จำนวนเงินที่ต้องการถอน >> '))

if balance < withdraw :
    print('ยอดเงินคงเหลือไม่เพียงพอ')
elif withdraw > 20_000 :
    print('ถอนเงินได้ไม่เกิน 20,000 บาท')
elif withdraw %100 != 0:
    print('ต้องเป็นจำนวนเต็มร้อยเท่านั้น')
else:
    balance -= withdraw
    print(f'ยอดเงินคงเหลือ : {format(balance)} บาท')
#======================================================
print()
#if ซ้อนกัน >> อาจมีเงื่อนไขที่ต้องพิจารณาร่วมกันมากกว่า 1 อย่าง หรือกรณีขึ้นกับกรณีอื่นด้วย
login = input('Login : ')
password = input('Password >> ')

if login == 'admin':
    if password == 'abc456':
        print('คุณเข้าสู่ระบบแล้ว')
else:
    print('Login หรือ Password ไม่ถูกต้อง')
#======================================================
print()
#การใช้ if-else แบบ Conditional Expression
#คำสั่ง-ถ้าเงื่อนไขเป็นจริง if เงื่อนไข else คำสั่ง-ถ้าเงื่อนไขเป็นเท็จ
print('     >>> แบบเดิม <<<')
x = 52
if x % 2 == 0:
    print('เลขคู่')
else:
    print('เลขคี่')
print()
print('     >>> แบบใหม่ <<<')
x = 55
print('เลขคู่') if x%2 ==0 else print('เลขคี่')
print('เลขคู่'if x%2==0 else 'เลขคี่')
#======================================================
