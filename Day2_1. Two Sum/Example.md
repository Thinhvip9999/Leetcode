nums = [2, 7, 11, 15]
target = 9

# Lần lượt:
# i=0, num=2 -> complement=7, chưa có 7 trong hashmap -> lưu {2:0}
# i=1, num=7 -> complement=2, có 2 trong hashmap -> return [0,1]