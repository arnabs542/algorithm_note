with open ('poem1.txt','r',encoding='utf-8') as f:
    lines = f.readlines()  # 这时，lines 的数据存放在内存里。
    print(lines)
    f.close()
blank_sentences = ['[唐] 李商隐\n','一弦一柱思华年。\n', '沧海月明珠有泪，\n']
with open('result.txt','w',encoding='utf-8') as f:
    for line in lines:
        if line in blank_sentences:
            if line == '[唐] 李商隐\n':
                f.write('[__] ______\n')
            else:
                f.write('______________。\n')
        else:
            f.write(line)
    f.close()

with open('result.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    f.close()