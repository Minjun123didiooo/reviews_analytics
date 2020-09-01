#寫程式碼來讀取留言檔案
#印出總共幾筆
#利用索引印出特定留言

data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print(len(data))

print(data[0])
print('-------------------------------')
print(data[1])
