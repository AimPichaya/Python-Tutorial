x = y = z = 10
print(z)
print(y)
print(x)
#==========================================
print()
x,y = 10,3
print('x+y = ',x+y)     #บวก
print('x-y = ',x-y)     #ลบ
print('x*y = ',x*y)     #คูณ
print('x//y = ',x//y)   #หารเอาจำนวนเต็ม
print('x%y = ',x%y)     #เอาเศษ
print('x**y = ',x**y)   #ยกกำลัง
#==========================================
print()
a = 24/8
b = 24/-8
c = -24/8
d = -24/-8
print('24/8 =',a,'|  24/-8 =',b,'|  -24/8 =',c,' |  -24/-8 =' ,d,)
#==========================================
print()
quantity = int(input('จำนวนสินค้าที่ซื้อ : '))
price = float(input('ราคาสินค้า : '))
total = quantity*price
print('รวมเป็นเงิน : ', total)
pay = float(input('จำนวนเงินที่จ่าย : '))
change = pay-total
print('เงินทอน :',change)
print('====== ขอบคุณที่ใช้บริการค่ะ ======')
#==========================================
print()
withdraw = int(input('จำนวนเงินที่ต้องการถอน: '))
B1000 = withdraw//1000
remain = withdraw%1000
B500 = remain//500
remain= remain%500
B100=remain//100
print(f'B1000 = {B1000}\nB500 = {B500}\nB100 = {B100}')
#==========================================
print()
#Operatorสำหรับการคำนวณและกำหนดค่า
x = 5
x += 1
print(x) #x = x+1 = 5+1 = 6

y = 4.5
y += 0.5
print(y) #y = y+0.5 = 4.5+0.5 = 5.0

z = 10
z -= 2
print(z) #z = z-2 = 10-2 = 8
#===========================================
print()
#EX รับตัวเลข 5 จำนวนทางคีร์บอร์ด แล้วหาผลรวมและค่าเฉลี่ย
sum = 0
sum += int(input('จำนวนที่ 1 = '))
sum += int(input('จำนวนที่ 2 = '))
sum += int(input('จำนวนที่ 3 = '))
sum += int(input('จำนวนที่ 4 = '))
sum += int(input('จำนวนที่ 5 = '))
avg = sum/5
print('\nผลรวมเท่ากับ = ',sum)
print('ค่าเฉลี่ยเท่ากับ : ',avg)
#============================================
print()
#การสร้างเลขสุ่ม
import random
a = random.randint(1,10) #สุ่มเลขจำนวนเต็มระหว่าง 1-10
print('\na=',a)

b=random.random() #สุ่มเลขที่มีค่าระหว่าง 0.0-1.0
print('\nb=',b)

c=random.uniform(1.5,5.5) #สุ่มเลขชนิดทศนิยมที่มีค่าระหว่าง 1.5-5.5
print('\nc=',c)

d=random.choice('aim') #สุ่มตัวอักษร
print('\nd=',d)

e=random.choice(['ant','boy','cat','dog']) #สุ่มลิสต์
print('\ne=',e)

f = random.randrange(10,101,10) #จะได้ค่าที่เป็นจำนวนเต็ม 10
print('\nf=',f)
print()
#=============================================
#Ex สร้างเลขสุ่มแบบเลขจำนวนเต็ม เพื่อสมมติว่าเป็นการออกรางวัลเลขท้าย 2 ตัว 1 รางวัล,เลขหน้า 3 ตัวและเลขท้าย 3 ตัว อย่างละ 2 รางวัล โดยมีคำแนะนำดังนี้
# - รางวัลเลขท้าย 2 ตัว ไม่ควรใช้ randin(0,99) เพราะอาจได้เลขหลักเดียว แต่ถ้าใช้ randin(10,99) ก็จะไม่ครบคลุมกรณี 00-09
# - รางวัลเลขหน้าและท้าย 3 จัว ไม่ควรใช้ randin(0,999) เพราะอาจได้เลข 1-2หลัก แต่ถ้าใช้ randin(100,999) ก็จะไม่ครอบคลุมกรณี 000-0999
# - สำหรับวิธีที่ควรใช้ในแต่ละรางวัลนั้น ให้สุ่มเลขโดด (0-9) ด้วย randint(0,9) ทีละ 1 หลักแล้วนำมาต่อกันจนครบตามจำนวนหลักของรางวัลนั้นๆ
import random
print('รางวัลเลขท้าย 2 ตัว: ',end='')
l = f'{random.randint(0,9)}{random.randint(0,9)}'
print(l)

print('รางวัลเลขหน้า 3 ตัว: ',end='')
f_1 = f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
f_2 = f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
print(f_1,f_2,sep=' ')

print('รางวัลเลขท้าย 9 ตัว: ',end='')
b_1 = f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
b_2 = f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
print(b_1,b_2,sep=' ')
#==============================================

