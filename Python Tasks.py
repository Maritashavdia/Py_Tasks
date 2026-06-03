from itertools import permutations, combinations, product
from datetime import date, datetime, timedelta
import calendar
import time
import random

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


# 7. თამაში უკუსვლაზე

# კომპიუტერი ირჩევს შემთხვევითობის პრინციპით რიცხვს 1-20 მდე, მოთამაშეს აქვს
# მხოლოდ 5 წამი რიცხვის გამოსაცნობად, თუ 5 წამში სწორ რიცხვს ვერ შეიყვანს, თამაში
# სრულდება და გამოდის ტექსტი "დრო ამოიწურა, თქვენ დამარცხდით".


number = random.randint(1, 20)
print('Guess the number between 1 and 20, You have only 5 seconds.')
start_time = time.time()
while time.time() - start_time < 5:
    player_guess = int(input('Enter your number: '))
    if player_guess == number:
        print('Congratulations! You won.')
        break
    else:
        print('Please, Try again.')
else:
    print("Time's up! You lost.")


# 8. ორი მოთამაშე იწყებს "გარბენს". უნდა შეამოწმო რომელი დაასრულებს ნაკლებ დროში.

start = datetime.now()
player1 = start + timedelta(seconds=random.randint(5,20))
player2 = start + timedelta(seconds=random.randint(5,20))

if player1 < player2:
    print('Player 1 wins!')
elif player2 < player1:
    print('Player 2 wins!')
else:
    print('Draw!')


#9 იღბლიანი დაბადების დღე

# მოთამაშემ უნდა შეიყვანოს დაბადების თარიღი და თამაში დაითვლის რამდენი დღეა
# დარჩენილი შემდეგ დაბადების დღემდე

while True:
    player_input = input('Enter your birthday in YYYY-MM-DD format: ')
    try:
        birthday = datetime.strptime(player_input, "%Y-%m-%d").date()
        break
    except ValueError:
        print('Invalid date format. Please enter the date in YYYY-MM-DD format.')

today = date.today()
next_birthday = date(today.year, birthday.month, birthday.day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)

days_until_next_birthday = (next_birthday - today).days
result = f'Your next birthday is in {days_until_next_birthday} days.'
print(result)


#10 საცავი - ჯუნიორ ჰაკერი :)

# თამაში არის შემდეგი - გვაქვს სეიფი რომელსაც აქვს ციფრები 1-6 მდე პაროლი
# არ ვიცით, ყოველ დღე კომპიუტერი აგენერირებს ახალ პაროლს (შემთხვევითობის პრინციპით)
# პაროლი არის 4 ციფრიანი. ჩვენი მიზანია დავწეროთ ისეთი კოდი რომელიც შეამოწმებს
# ვარიანტებს და როცა მოხდება კომპიუტერის მიერ დაგენერირებული პაროლის დამთხვევა
# უნდა გამოვიტანოთ შეტყობინება "პაროლი სწორია, საცავი გახსნილია", აუცილებელი პირობაა
# გამოვიტანოთ ყველა ჩვენს მიერ ნაცადი პაროლი სანამ მივალთ სწორ ვარიანტამდე.


today = date.today()
random.seed(today.toordinal())

password = ''.join(str(random.randint(1, 6)) for i in range(4))
print('The safe password has been generated. Let\'s start cracking it!')
total_attempts = 0

for attempts in product('123456', repeat=4):
    attempt = ''.join(attempts)
    print(f'Cracking... {attempt}')
    total_attempts += 1
    if attempt == password:
        print(f'\nPassword is correct, safe opened!')
        print(f'Password: {attempt}, Total attempts: {total_attempts}')
        break