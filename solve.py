from data import graph

print('''A : 皓神學長
B : 唐浩學長跳舞好帥
C : 奇哥
D : 謝老闆
E : 裴裴學長
F : 王娜麗莎
G : 陳宇浩克
H : 力娜
I : 苗栗人
J : 守德
K : 宜蘭巨砲
L : 卑鄙昊新
M : 正義雲
N : Bert
O : 叡叡
P : 學一
Q : 阿鶴
R : 酒鬼敬能
S : 傑神
T : Mandy姐''')

path = input('Enter path:').strip()

points = path.split(',')
_sum = 0




for i in range(len(points) - 1):
    for a, b, l in graph:
        if a == points[i] and b == points[i+1]:
            _sum += l
            break
        elif a == points[i+1] and b == points[i]:
            _sum += l
            break
    else:
        print('bad path')
        exit(1)

print('length:', _sum)


