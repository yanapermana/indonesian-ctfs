import os
file = open('flag.png', 'r')
file_one = open('jpg_one.jpg', 'w')
file_two = open('jpg_two.jpg', 'w')

data = file.read()

for i in range(0x47B9, len(data)):
    if i % 2 == 0:
        file_one.write(data[i])
    else:
        file_two.write(data[i])

file.close()
file_one.close()
file_two.close()

os.system('eog jpg_one.jpg')
os.system('eog jpg_two.jpg')
os.system('rm jpg_one.jpg')
os.system('rm jpg_two.jpg')