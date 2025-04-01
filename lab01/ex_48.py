# ex_48.py

# with open("file_w.txt", "w", encoding="utf-8") as f:
#     f.write("Hello python\n")
#     f.write("안녕 파이썬")


# with open("file_w.txt", "r", encoding='utf-8') as f:
#     lines = f.readlines()
#     # print(lines, type(lines))
#     for line in lines:
#         print(line, end='')

import ex_45 #ex_45py 파일 땡겨오기
import os #파이썬 os 실행시키기
    
input_files = os.listdir('./data') # 드라이브에 저장되어있는 파일 땡겨오기('./파일위치')

with open('ex_48.txt', 'w') as fw: # 땡겨온 파일 원하는 형태로 열기('저장하고싶은 이름', '원하는 파일 형태')
    for file in input_files:
        # print(file, type(file), file[-3:])
        if file[-3:] == 'txt':
            print(file)
            #      -5 -4 -3 -2 -1
            # jiso     .  t  x  t
            name = file[:-4]
            scores = []
            with open(f"./data/{file}", 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    scores.append(int(line))
                print(scores)
            m = ex_45.mean(scores)
            sigma = ex_45.std(scores)

            fw.write(f"{name:>10}: {m}, {sigma}\n")