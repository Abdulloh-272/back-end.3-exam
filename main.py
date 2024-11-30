# NAZARIY😍😍
# 1. Qiymat qayratuvchi va qiymat qaytarmaydigan funksiyalar orasidagi farq nimada?
# qiymat qaytaradigan fuksiyalar amalni bajarib return orqali qiymatni qaytarib yuboradi va biz bu qiymatni boshqa joylardaham ishlatishimiz mumkun
# qiymat qaytarmaydigan funksiyalar esa return qilmaydi lekin amalni bajaradi va biz u funksiyadan hechnarsa ololmaymiz faqat print orqali javobni koramiz
# 2. Lambda nima? U qanday e’lon qilinadi? U qaysi xolatlarda ishlatiladi?
# lambda bu qisqa funksiya lambda ozgaruvchi orqali elon qilinadi a = lambda b: b*2
#  lambda amalni bir qatorda bajarilsa bolganda funksiya orniga ishlatilinadi 
# 3. Fayllar bilan ishlashdagi w va a rejim(mode)lar orasidagi asosiy farqlar nimada?

# w modi fayldagi malumotlarni ustiga yozib ketadi yani eski malumotlarni yengisiga ozgartirib
# a modi esa eski malumotlarni ozgartirmasdan yengi malumotlarni qoshib ketaveradi

# 5. Try, except, else va finally qadamlari orasidagi farqlarni yozing
# Try dasturda yuz bergan  xatolikni terminalga chiqarmasdan exceptga berib yuboradi
# Except esa 
# 6. Funksiya bu nima? U qanday e’lon qilinadi?
###
# 7. *args va **kwargs nima? Ular nima uchun ishlatiladi?
###
# 8. Fayllar bilan ishlashda r, w va a rejim(mode)larga ta’rif bering?
# w va a modi faylning ichiga malumot yozish uchun ishlatiladi 
# r modi esa faylning ichidagi malumotlarni oqish uchun
# 9. Dastur davomi kelib chiquvchi xatoliklarni aniqlashdan nimadan foydalaniladi? Pythonda qanday xatolik turlari mavjud?
# dastur davomida kelib chiquvchi xatoliklarni aniqlashda try,except,else,finally yaordamida aniqlanadi
# pythonda bir nechta xatolik turlari: ZeroDivisionError, IndexError, KeyError, SyntaxError, ValueError, TypeError ...........

# AMALIY🤑🤑
# 4ta matematik amal bo’yicha 2ta son o’rtasida hisob kitoblarni amalga oshirib beruvchi kalkulyator dasturi yaratilsin.

# 1.  Dasturni ishga tushirib beruvchi asosiy kalkulyator funksiyasi bo’ladi. U funksiya chaqirilganda foydalanuvchidan 2ta son va 1ta matematik amal kiritish so’raladi. 
# 2. Har bir matematik amalni bajarish uchun 2ta sonni qabul qilib hisoblab qayratib beruvchi alohida funksiyalar yaratilsin. 
# 3. Dasturni yaratish davomida xatoliklarni oldini olishni ham esdan chiqarmaslik kerak. Misol uchun bo’lish amali bajarilayotganda bo’luvchi 0ga teng bo’lmasligini oldini olish kerak.
# 4. Har bir hisoblash amaliyotini kalkulyatorning tarixi sifatida hisoblash_tarixi.txt nomli faylga saqlab borilishi kerak


# def calculator():
#     def tarix(amal,natija):
#         with open(file='hisoblash_tarixi.txt',mode='a') as file:
#             file.write(f"{num1} {amal} {num2} = {natija}\n")

#     num1 = float(input('Birinchi raqamni kiriting: '))
#     num2 = float(input('Ikkinchi raqamni kiriting: '))
#     amal = int(input('Amalni tanlang\n1.+\n2.-\n3.*\n4./\n'))
#     if amal == 1:
#         def qoshish(num1,num2):
#             res = num1 + num2
#             tarix(amal='+',natija=res)
#             return res
#         return qoshish(num1,num2)
#     elif amal == 2:
#         def ayirish(num1,num2):
#             res = num1 - num2
#             tarix(amal='-',natija=res)
#             return res
#         return ayirish(num1,num2)
#     elif amal == 3:
#         def kopaytirish(num1,num2):
#             res = num1 * num2
#             tarix(amal='*',natija=res)
#             return res
#         return kopaytirish(num1,num2)
#     elif amal == 4:
#         def bolish(num1,num2):
#             try:
#                 res = num1 / num2
#                 tarix(amal='/',natija=res)
#                 return res
#             except ZeroDivisionError:
#                 print('Nolga bolib bolmaydi')
#         return bolish(num1,num2)
#     else:
#         print('Notogri amal❌')
    
# print(calculator())

# Talabalar ma’lumotlari faylga saqlash va ularni o’qish imkonini beruvchi asosiy funksiya yaratilsin. Ushbu funksiya chaqirilganda foydalanuvchiga uchta tanlov berilsin: 

# 1. Talaba qo’shish
# 2. Talaba ma’lumotlarini o’qish
# 3. Barcha ma’lumotlarni o’chirish

# talabalarni qoshib olish uchun birmartda ishlaydigan funksiya

# def add_students(st:dict,check=True):
#     if check != 'False':
#         while True:
#             with open(file='students.txt',mode='a') as a:
#                 counter = 0
#                 for key,value in st.items():
#                     for x,y in value.items():
#                         counter +=1
#                         if counter == 3:
#                             a.write(f'{x}: {y}\n')
#                             a.write('\n')
#                             counter = 0
#                         else:
#                             a.write(f'{x}: {y}\n')
#             with open(file='check.txt',mode='w') as ch:
#                 ch.write('False')
#                 break

# students = {
#     1:{'name':'Student 1', 'last_name':'Last name 1', 'age': 19},
#     2:{'name':'Student 2', 'last_name':'Last name 2', 'age': 22},
#     3:{'name':'Student 3', 'last_name':'Last name 3', 'age': 20}
# }

# try:
#     with open(file='check.txt',mode='r') as checked:
#         ch = checked.read()
#     add_students(students,ch)
# except FileNotFoundError:
#     add_students(students)



# from functions import students,read_students,delate_file

# def talabalar():
#     tanlov = int(input('1.Talaba qoshish\n2.Talaba malumotlarni oqish\n3.Barcha malumotlarni ochirish\n'))
#     if tanlov == 1:
#         ismi = input('Ismingizni kiriting: ')
#         familiya = input('Familiyangizni kiriting: ')
#         yoshi = input('Yoshingizni kiriting: ')
#         students(name=ismi,last_name=familiya,age=yoshi)
#     elif tanlov == 2:
#         read_students()
#     elif tanlov == 3:
#         delate_file()

# while True:
#     talabalar()



# 1-vazifa:

# Agar tanlov 1 ga teng bo’lsa Asosiy f foydalanuvchidan ismi, familiyasi va yoshi so’ralsin, keyin shu ma’lumotlar boshqa bir funksiyaga argument sifatida yuborilganda ushbu ma’lumotlar students.txt nomli funksiga qo’shilsin.

# 2-vazifa:

# Agar tanlov 2ga ten bo’lsa, students.txt faylidagi barcha talabalar yangi qatordan chop etilsin. Ushbu vazifani bajarish uchun ham alohida funksiya yaratilsin

# 3-vazifa:

# Agar tanlov 2ga ten bo’lsa, students.txt faylidagi barcha ma’lumotlar o’chib ketsin. Ushbu vazifani bajarish uchun ham alohida funksiya yaratilsin
