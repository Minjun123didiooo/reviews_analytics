#寫程式碼來讀取留言檔案
#每讀一萬筆 印出len(data)來得知讀取進度
#印出總共幾筆留言
#算出留言的平均長度
#對清單進行篩選 篩選出小於100字的留言
#篩選出有'good'的留言

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


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

