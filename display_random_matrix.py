#2022/10/31

import random

# パスワードの設定
# 
# while True:
#     password = input("４桁のパスワード設定：")
#     if len(password) == 4:
#         break

while True:
    nums = ["1","2","3","4","5","6","7","8","9"]

    random.shuffle(nums)
    print("******")
    for i in range(len(nums)):
        if (i+1) % 3 != 0:
            print(f"{nums[i]} ",end="")
        else:
            print(f"{nums[i]} ")
    print("******")

    if input("終了(e), 繰り返し(e以外) : ") == "e":
        break
    else:
        print("\n")

# パスワードが一致するまでループ
#
#  while True:
#     # 入力
#     input_pass = input("パスワード：")

#     if input_pass == password:
#         print("パスワードが一致しました。")
#         break
