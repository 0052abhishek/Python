s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
sd_a = s1 - s2
sd_b = s2 - s1
print(sd_a, sd_b)
