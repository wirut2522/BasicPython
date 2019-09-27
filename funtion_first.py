# การสรา้ง funtion
def hello(name):
    print('Hello %s' % name)

# สรา้งฟังชั่นการหาพื้นที่
def area(width=0,height=0):
    c = width * height
    return c

#เรียกใช้ funtion
hello("wirut kamsai")

# เรียกใช้ฟั่งชั้น area

print(area(5,8))
print(area())