#หากมีตัวที่จะจัดเก็บข้อมูลเป็นจำนวนมาก การแ้างตัวแปรที่ละตัวจะยุ่งยาก วึ่งเปลี่ยนเป้นการใช้วิธีการสร้างตัวแปรเก็บข้อมูลแทนได้
#Python สามารถเก็บข้อมูลได้หลายแบบ เช่น List Tuple Set Dictionary เป็นต้น
# ข้อมูลจะเป็นลักษระเป็นลำดับรายการที่ต่อเนื่อง ดังนั้นสามารถที่จะใช้ลูป for, while, function ที่เกี่ยวข้องมาดำเนินการได้
#==========================================================
print(' ============== การสร้าง List ============== ')
#รายการข้อมูลที่เก็บในลิสต์ เรียกว่า สมาชิก หรือ Element ข้อมูลในลิสต์อาจะเป็นชนิดเดียวกันหรือต่างชนิดกันก็ได้
#สามารถสร้างลิสต์ได้ 2 ลักษณะ คือ ใช้ฟังก์ชัน list() และกำหนดด้วย []

# ลักษณะการสร้างลิสต์ด้วยฟังก์ชัน list()
#a = list()                          #ลิสต์แบบว่างเปล่าไม่มีสมาชิกใดๆ
#b = list([1,2,3,4,5])               #ลิสต์ที่มี่สมาชิก 5 ตัว คือ 1-5
#c = list(['one','two','three'])     #ลิสต์ที่มีสมาชิกเป็น str
#d = list(range(3,6))                #สร้างลิสต์โดยใช้ range() มีสมาชิก คือ 3 4 5
#e = list('abc')                     #สร้างลิสต์ที่มีสมาชิกเป็นอักขระ คือ a b c
#f = list(1,True,'Three',4.5)        #สมาชิกของลิสต์อาจเป็นข้อมูลต่างชนิดกัน

#ลักษณะการสร้างลิสต์ด้วยวงเล็บ [] >> ทำได้ง่ายและสั้นกว่า
#a = []
#b = [1,2,3,4,5]
#c = ['one','two','three']
#d = [range(3,6)]
#e = [1,True,'Three',4.5]
#f = ['abc'] #** กรณีนี้จะมีสมาชิกตัวเดียวคือ abc แต่ถ้า list('abc') จะมีสมาชิก a,b,c

#=========================================================
#การอ้างถึงสมาชิกและใช้ลูป for-in ร่วมกับลิสต์

num = [2,4,6,8,10]
print(num[0]) #2
print(num[1]) #4
print(num[2],num[3],num[4],) #6,8,10
#print(num[5] #จะ Error เนื่องจากไม่มีสมาชิกที่เป็นลำดับ 5)

print()

#>>หากมีการแก้ไขสมาชิกตัวใด ให้กำหนดค่าใหม่ให้กับสมาชิกได้เลย
color = ['red','blue','green']
color[0] = 'yellow' #จาก red จะเปลี่ยนเป็น yellow แทน
#color[3] = 'white' #จะ Error เนื่องจากไม่มีสมาชิกลำดับที่ 3
print(color)

print()

#เนื่องจากลิสต์ คือ ช่วงของข้อมูลที่สมาชิกการจัดเรียงลำดับต่อเนื่องกัน จึงสามารถใช้ลูป for เพื่อเข้าถึงสมาชิกทุกตัวของลิสต์
#ค่าที่ได้ในการวนลูปแต่ละรอบ คือ ค่าของสมาชิกแต่ละตัว
    #การวนลูกครั้งที่ 1 จะได้ค่าสมาชิกลำดับที่ 0
    #การวนลูกครั้งที่ 2 จะได้ค่าสมาชิกลำดับที่ 1
    #การวนลูกครั้งที่ 3 จะได้ค่าสมาชิกลำดับที่ 2
    #...
    #การวนลูกครั้งที่ n จะได้ค่าสมาชิกลำดับที่ n-1

num = [1,3,5,7,9]
for n in num:
    print(n) # n ไม่ใช่เลขลำดับเหมือน range() แต่เป็นค่าของสมาชิกแต่ละตัว ที่มีค่า 1 3 5 7 9 คนละบรรทัด

print()

#นอกจากนี้ยังสามารถใช้ for-in แบบ Expression เพื่อสร้างลิวต์ใหม่จากลิสต์เดิม
a = [1,2,3,4,5]
a = [x*10 for x in a]
print(a)

print()

#ถ้าต้องการระบุเงื่อนไขเพื่อคัดกรองเอาเฉพาะสมาชิกบางตัว กำหนดด้วย if ต่อจาก for-in
a = [-1,2,-3,4,-5]
b = [x for x in a if x%2 ==0]
print(b) #2 4

c = [abs(x) for x in a if x<0] #a=-1,2,-3,4,-5 print abs(x)ที่น้อยกว่า 0 = -1 -3 -5
print(c)

print()#=============================================================================
print(' ============== การใช้โอเปอร์เรเตอร์ร่วมกับลิสต์ ============== ')
#การใช้โอเปอร์เรเตอร์ร่วมกับลิสต์
#list1+list2 และ list1 += list2 >> การเชื่อมสมาชิกทั้ง 2 จากลิสต์เข้าด้วยกัน **ควรระวัง เนื่องจาก list1+list2 จะไม่เท่ากับ list2+list1
#list*n หรือ n*list >> คัดลอกสมาชิกทั้งหมดเป็นจำนวน n ครั้ง แล้วนำไปเชื่อมกับสตริงเดิม
#x in list >> ตรวจสอบว่ามีสมาชิกค่า x อยู่ในลิสต์หรือไม่ ถ้ามีจะคืนค่า True
#x not in list >> ตรวจสอบว่า'ไม่'มีสมาชิกค่า x อยู่ในลิสต์ใช่หรือไม่ ถ้าใช่จะคืนค่า True
#==, != >> เปรียบเทียบลิสต์ว่าเท่ากันหรือไม่
#list[start:stop] >> คัดลอกสมาชิกของลิสต์เริ่มตั้งแต่ลำดับ start ไปจนถึงก่อนลำดับ stop
#list[start:] >> คัดลอกสมาชิกของลิสต์เริ่มตั้งแต่ลำดับ start ไปจนถึงก่อนลำดับสุดท้าย
#list[stop] >> คัดลอกสมาชิกของลิสต์เริ่มตั้งแต่ลตัวแรกปจนถึงก่อนลำดับ stop

#การใช้ +,+=
a = [1,3,5]
b = [2,4,6,8]
c = a+b
print(c)        # [1,3,5,2,4,6,8]
print(b+a)      #[2,4,6,8,1,3,5]

d = [1,2,2,3,3,3,]
e = [1,2,3]
print(d+e)      #[1,2,2,3,3,3,1,2,3]

f = ['one','two','three'] + ['four','five']
print(f)        #['one','two','three','four','five']

g = []
g += [1.2 , 3.4 ,5.6]
print(g)        #[1.2,3.4,5.6]

print()

#การใช้ *
a = [1,3,5,0]
b = a*2
print(b)                # [1,3,5,0,1,3,5,0]
print(a*4)              # [1,3,5,0,1,3,5,0,1,3,5,0,1,3,5,0]
print(['x','y','z']*2)  # ['x','y','z','x','y','z']

print()

#การใช้ in(มี) และ not in(ไม่มี) สำหรับตรวจสอบสมาชิก
fruit = ['apple','banana','coconut','durian']
b = 'banana' in fruit #ตรวจสอบว่ามี banana เป็นสมาชิกใน fruit หรือไม่

if 'coconut' in fruit:
    print('yes')

if 'orange' not in fruit:
    print('on')

if 'Apple' not in fruit: #ผลลัพธ์จะตอบ on เนื่องจากตัวพิมพ์เล็กกับพิมพ์ใหญ่ไม่ตรงกัน
    print('yes')
else:
    print('no')

print()

#การใช้ == , !=
a = [1,2,3,4]
b = [1,2,3,4.0]
c = [1,2,4,3]
print(a == b)   #True
print(a == c)   #False
print(a != b)   #False

s1 = ['One','Two']
s2 = ['one','two']
print(s1 == s2) #False  เพราะตัวพิมพ์ใหญ่ พิมพ์เล็กไม่ตรงกัน
print(s1 != s2) #True

print()

#การใช้ [start:stop] หรือเรียกว่า Slicing
a = [0,1,2,3,4,5,6,7]
b = a[1:3]
print(b)    #[1,2] ไม่มีเลข 3 เพราะ 1:3 จะทำแค่ 1 2
print(a[3:6])   #[3,4,5]
print(a[4:10])  #[4,5,6,7] ถ้าไม่ครบจะคัดลอกเท่าที่มี
print(a[3:])    #[3,4,5,6,7] ลำดับที่ 3 จนถึงสุดท้าย
print(a[:5])    #[0,1,2,3,4] ลำดับที่ 4 จนถึงลำดับ 0

print()
#============================================================

print(' ============== ฟังก์ชันแบบ Built-in ที่สามารถใช้ร่วมกับลิสต์ ============== ')
# len(ลิสต์) = จำนวนสมาชิกภายในลิสต์
# max(ลิสต์) = สมาชิกที่มีค่าที่สุด
# min(ลิสต์) = สมาชิกที่มีค่าน้อยที่สุด
# sum(ลิสต์) = หาผลรวมของสมาชิกทั้งหมด ซึ่งสมาชิกทั้งหมดต้องเป็น'ตัวเลข'เท่านั้น
# enumerate(ลิสต์) = มักใช้ร่วมกับ for เพื่อเข้าถึงเลขลำดับและค่าของสมาชิก ตามรูปแบบ (index,value)
# del(ลิสต์) = คีเวิร์ดสำหรับลบตัวแปร สามารถนำมาลบสมาชิกตัวใดตัวหนึ่งของลิสต์ได้

#Ex
a = [1,3,5,7,9]
print(len(a)) #จำนวนภายในลิสต์ = 5
print(sum(a)) #1+3+5+7+9 = 25

b = ['aBCDeFG']
print(len(b)) #1
b = list('aBCDeFG')
print(b) #7

c = ['abc','def','g']
print(len(a))  #3

d = [2,-4,-6,8,10.5]
print(sum(d)) #2-4-6+8+10.5 = 10.5

e = [1,2,'three']
#print(sum(e)) #Error เพราะไม่ใช่ตัวเลขทั้งหมด

f = [108,1009,101,7,11]
print(max(f)) #ค่ามากสุด = 1009
print(min(f)) #ค่าน้อยสุด = 7

h = [10,15,35,45,60,75,90]
count_even = 0
for i in range(0,len(h)): #ใช้ range(0,len(h)) เพื่อให้เลขลำดับในการอ้างถึงสมาชิกอีกลักษณะหนึ่ง
    if h[i] % 2 == 0 :
        count_even += 1
print(count_even) #10 60 90 มี 3 จำนวน

g = [108,1009,7,11]
for (i,v) in enumerate(g): #เลขลำดับและเลขสมาชิก
    print(f'{i}-{v}')

nums = [1,2,4,5]
del nums[2] #ลบตัวแปรที่ 2 จะเหลือ 1 2 5
print(nums) #[1,2,5]

print()
#============================================================

print(' ============== ฟังก์ชันของลิสต์ ============== ')
#>> ตัวแปร.XXX()
#append(สมาชิก) = เพิ่มสมาชิกใหม่ 1 รายการต่อท้ายสมาชิกเดิม
#clear()       = ลบสมาชิกทั้งภายในลิสต์
#count(สมาชิก) = นับจำนวนสมาชิกที่ตรงกับค่าที่ระบุ
#extend(ลิสต์) = เพิ่มสมาชิกใหม่ในรูปแบบลิสต์ต่อท้ายสมาชิกเดิม คล้ายกับการ +
#index(สมาชิก) = ตรวจลำดับของสมาชิกที่ระบุที่พบเป็นครั้งแรก
#insert(ลำดับ,สมาชิก) = แทรกสมาชิกใหม่ลงไปในลำดับที่ระบุ แล้วลบสมาชิกนั้นออกจากลิสต์ แต่หากไม่ระบุจะดำเนินการกับสมาชิกตัวสุดท้าย
#pop(ลำดับ)หรือ pop() = อ่านค่าสมาชิกในลำดับที่ระบุ
#remove(สมาชิก) = ลบสมาชิกที่ระบุออกจากลิสต์
#reverse() = เรียงลำดับสมาชิกแบบย้อนกลับ
#sort() = เรียงลำดับสมาชิกจากน้อยไปมาก

#การใช้ append(),extend(),append()
a = [1,2,3]
a.append(4) #เพิ่มสมาชิกใหม่ 1 รายการต่อท้ายสมาชิกเดิม
print(a) #[1,2,3,4]

a.extend([5,6,7,2,2,3,2]) #เพิ่มสมาชิกใหม่ในรูปแบบลิสต์ต่อท้ายสมาชิกเดิม
print(a) #[1,2,3,4,5,6,7,2,2,3,2]
#                   ^^^^^
print(a.count(2)) #มี 2 อยู่ = 4 จำนวน

#การใช้ index(),insert(),pop(),remove()
a = [1,2,3,3,4,5]
i = a.index(3)
print(i) #2

if 4 in a:
    print(a.index(4)) #4

a.insert(4,3.5) #แทรก 3.5 ในลำดับที่ 4
print(a) #[1,2,3,3,3.5,4,5]

a.insert(100,10) #ระบุลำดับเกินจำนวนสมาชิกจะแทรกอยู่ลำดับสุดท้าย
print(a) #[1,2,3,3,4,5,10]

x = a.pop(4)
print(x)    #3.5 อ่านค่าสมาชิกในลำดับที่ระบุ แล้วลบสมาชิกออก
print(a)    #[1,2,3,3,4,5] 3.5 ถูกลบไปแล้ว

x = a.pop() #ถ้าไม่ระบุตำแหน่งจะลบตัวสุดท้ายออก
print(x)    #10
print(a)    #[1,2,3,3,4,5]

if 3 in a :
    a.remove(3)
    print(a) #[1,2,3,4,5]

#การใช้ reverse() , sort()
a = [108,1009,7,11,101]
a.reverse() #เรียงจากหลังไปหน้า
print(a) #[101,11,7,1009,108]

a.sort()   #เรียงค่าน้อยไปมาก
print(a) #[7,11,101,108,1009]

a.reverse()
print(a) #[1009,108,101,11,7]

print()#================================================================================================

print(' ============== EXCAMPLE ============== ')
#เป็นการรับค่าปี พ.ศ.เข้ามา แล้วตำนวณว่าปีนี้ตรงกับปีนักษัตรใด โดยใช้แนวทางดังนี้
# - เก็บชิื่อปีนักษัตริย์ไว้ในแบบลิสต์ เช่น constellayion = ['ชวด','ฉลู','กุน',...]
# - สำหรับหลักสูตรในการคำนวนหาปีนักษัติย์นั้น ถ้าจะคิดวิธีทางโหราศาสตร์นั้นค่อนข้างยุ่งยาก จึงได้ดัดแปลงมาเป็นวิธีทางคอมพิวเตอร์เพื่อใช้กับลิสต์
# >>> ค่าที่เหลือ = (ปีพ.ศ.+5)%10 <<<

constellations = ['ชวด','ฉลู','เถาะ','ขาล','มะโรง','มะเส็ง','มะเมีย','มะแม','วอก','ระกา','จอ','กุน']

print('ถ้าต้องการหยุด ให้ใส่ค่าน้อยกว่า 1')
while True:
    year = int(input('ปี พ.ศ. >> '))
    if year < 1:
     break

    x = (year+5) % 12
    c = constellations[x]
    print('ตรงกับปีนักษัตริย์: ',c)
print(' ============== Listหลายมิติ ============== ')
num = [[0,1,2,3],[4,5,6,7],[8,9]]
print(num[0]) #[0,1,2,3]
print(num[1]) #[4,5,6,7]
print(len(num)) #3
print(len(num[0])) #4
print(len(num[2])) #2

colors = [['red','green','blue'],['black','white']]
print(colors[0])
print(len(colors)) #2
print(len(colors[1])) #2

print()

#เนื่องจากมีลิสต์ซ้อนกัน 2 ชั้น ดังนั้นในการอ้างถึงสมาชิกย่อยๆ ต้องใช้วงเล็บ [] 2 อัน
# ในรูปแบบ [ลำดับในลิสต์ชั้นนอก][ลำดับลิสต์ชั้นใน]
colors = [['red','green','blue'],['black','white']]
print(colors[0][0]) #red
print(colors[0][1]) #green
print(colors[1][0]) #black
print(colors[1][1]) #white

print()

# ถ้าจะเข้าถึงสมาชิกย่อยๆ ของลิสต์ 2 มิติ ด้วยลูป for-in ก็ต้องใช้ลูปซ้อนกัน
colors = [['red','green','blue'],['black','white']]
for cols in colors:
    for c in cols:
        print(c, end=' ')

print()

colors = [['red','green','blue'],['black','white']]

colors[1].append('yellow')
colors[1] += ['pink','purple']
print(colors[1])

if 'green' in colors[0]: #ให้ตรวจสอบเฉพาะสมาชิกกลุ่มแรก
    print('yes')
for cols in colors:
    if 'blue' in cols:
        print('yes')

print(' ============== รายการข้อมูลแบบ Set ============== ')
#add() = เพิ่มสมาชิกใหม่ 1 รายการ
#clear()= ลบสมาชิกทั้งหมดภายในลิสต์
#pop() = อ่านค่าสมาชิก 'ตัวแรก' แล้วลบสมาชิกตัวนั้นออก
#remove(สมาชิก) = ลบสมาชิกที่ระบุออกจากลิสต์
#set1.issubset(set2) = ตรวจสอบว่า set1 เป็นซับเซตของ set2 หรือไม่
#set1.issuperset(set2) = ตรวจสอบ set1 เป็นซูปเปอร์เซตของ set2 หรือไม่
#set1.union(set2) = เป็นกสนรวมสมาชิกทั้ง 2 เซตเข้าด้วยกัน
#set1.intersection(set2) = คัดเอาเฉพาะสมาชิกที่มีซ้ำกันของทั้งสองเซต
#set1.difference(set2) = คัดเอาเฉพาะสมาชิกที่มีใน set1 แต่ไม่มีใน set2 หรือใช้โอเปอเรเตอร์ -
#set1.symmetric_difference(set2) = คัดเอาเฉพาะสมาชิกที่มีเพียงในเซตใดเซตหนึ่ง แต่ต้องมีไม่ซ้ำกันในทั้งสองเซตหรือใช้โอเปอเรเตอร์ ^

print()

#การใช้ add(), clear(), pop(), remove()
a = {10,20,30,40}
a.add(50)
print(a)

if 100 in a:
    a.remove(100)

x = a.pop()
print(x)
print(a)

#การใช้ issubset(), issuperset()
s1 = {1,2,4}
s2 = {1,4,5,2,6}
print(s1.issubset(s2))
print(s2.issubset(s1))

print()

print(s1.issuperset(s2))
print(s2.issuperset(s1))

print()

#การใช้ union() หรือโอเปอเรเตอร์ |
set1 = {1,2,4,5}
set2 = {1,3,5}
set3 = set1.union(set2)
print(set3)

set4 = set1 | set2
print(set4)

print()

#การใช้ intersection() หรือโอเปอเรเตอร์ &
set1 = {1,2,4,5}
set2 = {1,3,5}
set3 = set1.intersection(set2)
print(set3)

set4 = set1 & set2
print(set4)

print()

#การใช้ difference() หรือโอเปอเรเตอร์ -
set1 = {1,2,4,5}
set2 = {1,3,5}
set3 = set1.difference(set2)
print(set3)

set4 = set1 - set2
print(set4)

print()

#การใช้ symmetric_difference() หรือโอเปอเรเตอร์ ^
set1 = {1,2,4,5}
set2 = {1,3,5}
set3 = set1.symmetric_difference(set2)
print(set3)

set4 = set1 ^ set2
print(set4)
