#CTI-110
#P4HW1 - Score List
#William "James" Ross
#11/10/2022
#Pseudocode (detail algorithm)

number_of_scores = int(input('How many scores do you want to enter?'))
print()

scores = []

i = 1
while i <= number_of_scores:
    i = i + 1
for i in range(1,number_of_scores+1):
    score =(float(input('Enter score #' + str(i) + ':')))
    while True:
        if 0 < score < 100:
               break
        print()
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        score = float(input('Enter score #' + str(i) + ' again:'))

    scores.append(score)

print()
print()
print()
print('--------------Results-----------')
print('Lowest Score  :', min(scores))
scores.remove(min(scores))
print('Modified List :', scores)
print(f'Scores Average: {sum(scores) / len(scores):.2f}')
average = sum(scores) / len(scores)
if average >= 90:
    print('Grade         : A')
elif average >= 80:
    print('Grade         : B')
elif average >= 70:
    print('Grade         : C')
elif average >= 60:
    print('Grade         : D')
elif average < 60:
    print('Grade         : F')
print('----------------------------------')
