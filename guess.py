import random
start = input("請輸入最小值: ")
end = input("請輸入最大值")
start = int(start)
end = int(end)

a = random.randint(start, end)

count = 0

while True:
	count += 1
	n = input("請輸入數字: ")
	n = int(n)
	if a == n:
		print("恭喜你答對了，你總共猜了", count, "次")
		break
	elif a > n:
		print("答錯了， 請猜大一點!")
	else:
		print("答錯了， 請猜小一點!")
	print("這是你猜的", count, "次")