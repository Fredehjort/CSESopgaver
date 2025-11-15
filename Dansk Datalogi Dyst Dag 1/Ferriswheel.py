_, tykke = map(int, input().split())
vægt = sorted(map(int, input().split()))
a = 0
b = len(vægt) - 1
gondola = 0
while a <= b:
	if vægt[a] + vægt[b] <= tykke:
		a += 1
		b -= 1
	else:
		b -= 1
	gondola += 1
print(gondola)
