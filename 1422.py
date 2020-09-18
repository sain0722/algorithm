import functools

def compare(x, y):
    if len(x) != len(y):
        return len(x)-len(y)
    return int(x)-int(y)

k, n = map(int, input().split())

num = sorted([input().rstrip() for _ in range(k)], key=functools.cmp_to_key(compare), reverse=True)
num.extend([num[0] for _ in range(n-k)])
num.sort(key=functools.cmp_to_key(
    lambda x, y: 1 if int(x+y) < int(y+x) else -1
))
print(''.join(num))
