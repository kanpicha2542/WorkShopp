string = " Hello, World! "

print(string.upper())  # output : "HeLLO, WORLD!"
print(string.lower())  # output : "hello, world!"
print(string.strip())  # output : "Hello, World!" กำจัดช่องว่างที่ไม่อยากให้มี
print(string.replace("H", "J"))  # output : Jello, World! แก้ไขตัวอัคระเปลี่ยน H เป็น J
print(string.split(","))  # output : [' Hello', 'World!'] # ตัดประโยคด้วย ,
print(len(string))  # 15 # นัย String มีกี่อัคระ รวมเว้นวรรค
