'''
pwd = 'a123456'
cnt = 3
print('start')

while True :
	inpu = input('請輸入密碼：')

	if pwd == inpu :
		print('登入成功！')
		break
	elif cnt != 1 :
		cnt -= 1
		print(f'密碼錯誤，還有{cnt}次機會')
	else :
		print('密碼輸入錯誤三次，請稍後再試')
		break

'''

'''
#溫度
c = input('輸入攝氏度：')
c = float(c)

f = c * 9 / 5 + 32
print(f'攝氏溫度{c}等於華氏溫度{f}')
'''



#猜數字遊戲
'''
import random 

while True:
	try:
		max_num = int(input('輸入範圍最大值： '))
		min_num = int(input('輸入範圍最小值： '))
		max_num > min_num
		break
	except :
		print('輸入的值有誤')
'''
'''
key_num = random.randint(min_num,max_num)
print(key_num)

while True:
	print(f'密碼{min_num}~{max_num}')
	gus_num = input('輸入數字：')
	gus_num = int(gus_num)

	if key_num > gus_num :
		min_num = gus_num
	elif key_num < gus_num :
		max_num = gus_num
	else :
		print(f'密碼{gus_num}正確！')
		break

'''

'''
#文字當清單
car = "Audi"
print("Au" in car)
print("au" in car)
'''
#讀取檔案

wd_list = []
count = 0
with open("reviews.txt", 'r') as f :
	for line in f :
		wd_list.append(line.strip())
		#print(len(wd_list))
		count += 1
		if count % 1000 == 0 :
			print(len(wd_list))




	

