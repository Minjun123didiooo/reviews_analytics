#寫程式碼來讀取留言檔案
#每讀一萬筆 印出len(data)來得知讀取進度
#印出總共幾筆留言
#利用索引印出特定留言

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))


print(len(data))


print(data[0])
print('-------------------------------')
print(data[1])
