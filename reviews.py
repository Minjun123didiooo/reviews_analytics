#寫程式碼來讀取留言檔案
#每讀一萬筆 印出len(data)來得知讀取進度
#印出總共幾筆留言
#算出留言的平均長度

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))

print('檔案讀取完了, 總共', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度是', sum_len / len(data))




