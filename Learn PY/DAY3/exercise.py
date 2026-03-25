# 🎯 DAY 3 Exercise (आपको ये solve करना है)

# 1️⃣ 1 से 20 तक के numbers print करो
for i in range(1,21):
    print(i)


# 2️⃣ 1 से 50 तक even numbers print करो
start = 1
end = 50
while(start <= end):
    if start % 2 == 0:
        print(start)
    start += 1


# 3️⃣ List = [10,20,30,40,50] का sum निकालो
Numbers = [10,20,30,40,50]
total = 0
for num in Numbers:
    total += num
print(total)

# 4️⃣ A से Z तक सारे letters print करो
for i in range(65,91):
    print(chr(i))

# 5️⃣ While loop से 10 से 1 तक reverse counting करो
num = 10
while num >= 1:
    print(num);
    num -= 1;
