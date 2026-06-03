from itertools import permutations, combinations, product
from datetime import date, datetime, timedelta
import calendar

# 1. მოცემულია სიტყვა "ABCD". დაბეჭდე ყველა შესაძლო ვარიანტი და **დაითვალე**
# რამდენია სულ რაოდენობრივად (უნდა დააბრუნო რიცხვი)

word = 'ABCD'
count = 0
for i in permutations(word):
    print(''.join(i))
    count += 1
total = f'Total: {count} combinations'

print(total)


# 2. იპოვე მომდევნო კვირის პირველი სამშაბათი, საწყისი თარიღი არის დღევანდელი
# დღე (ხელით არ გაწეროთ თარიღი)


today = datetime.now()

next_tuesday = today + timedelta(days=(1 - today.weekday()) % 7)
if next_tuesday.date() == today.date():
    next_tuesday += timedelta(days=7)
print(next_tuesday.date())


# 3. დაადგინე, არის თუ არა შეყვანილი წელი ნაკიანი, მომხმარებელს შემოჰყავს
#მხოლოდ წელი და ვეუბნებით არის თუ არა ნაკიანი


year = int(input('Enter a year: '))
leap_year = f'{year} is a leap year.'
not_leap_year = f'{year} is not a leap year.'

if calendar.isleap(year):
    print(leap_year)
else:
    print(not_leap_year)


# 4. დაითვალე რამდენი კვირაა დარჩენილი ახალ წლამდე, საწყისი თარიღი არის
#დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)

today = datetime.now()
new_year = datetime(today.year + 1, 1, 1)
weeks_left = f'{(new_year - today).days // 7} weeks left until the new year.'

print(weeks_left)


# 5. შექმენი ყველა 3-ელემენტიანი კომბინაცია სიიდან \[1,2,3,4,5] (itertools-ის გამოყენებით)

numbers = [1, 2, 3, 4, 5]
combos = list(combinations(numbers, 3))
for i in combos:
    print(i)

total = f'Total: {len(combos)} combinations'
print(total)


# 6. მიიღე ყველა კომბინაცია "XYZ"-ის სიმბოლოებით სიგრძე 1-დან 3-მდე
# მაგალითი: X, Y, Z, XY, XZ, YZ, XYZ უნდა მივიღოთ მსგავსი შედეგი.


letters = "XYZ"
result = []

for i in range(1, 4):
    result.extend(combinations(letters, i))
for c in result:
    print(''.join(c))