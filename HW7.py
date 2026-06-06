# 1. შექმენი გენერატორი, რომელიც ტექსტის თითოეულ სიმბოლოს აბრუნებს.

Word = 'CODE'


def symbol_generator(word):
    yield from word


for symb in symbol_generator(Word):
    print(symb)

# 2. დაწერე პროგრამა რომელშიც მომხმარებელი შემოიყვანს მხოლოდ ციფრებს, ლოგიკა
# უნდა იყოს შემდეგი: გვაქვს კონკრეტული ლისტი და მომხმარებელი უნდა მიწვდეს
# შემოყვანილი ციფრით რომელიმე ელემენტს, თუ ვერ მიწვდება პროგრამა შეცდომაზე არ
# უნდა გავიდეს.

# arr = [1, 2, 3,4,5,6,7,8,9]

# try:
#     number = int(input('Enter a number: '))
#     if number in arr:
#         print(f'{number} is in the list.')
#     else:
#         print(f'{number} is not in the list.')
# except ValueError:
#     print('Please enter only numbers.')
# finally:
#     print('Program finished.')

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


try:
    index = int(input('Enter index: '))
    print(arr[index])

except (ValueError, IndexError):
    print('Invalid input or index out of range.')

finally:
    print('Thank you, Program finished.')



# 3. შექმენი დეკორატორი, რომელიც ითვლის რამდენჯერ გამოიძახეს ფუნქცია.

# მაგალითი:
# @counter
# def say():
# print("Hi")
# say()
# say()
# გამოძახება: 1
# Hi
# გამოძახება: 2
# Hi

# nonlocal გამოვიყენე, რადგან მაქვს nested function და შევძლო გარე ფუნქციის ცვლადის შეცვლა.

def counter(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print(f'Call number: {count}')
        return func()

    return wrapper


@counter
def greet():
    print('Welcome!')


greet()
greet()
greet()
greet()
greet()


# 4. მომხმარებელს უნდა დავუსვათ 5 მათემატიკური შეკითხვა, თითოეულზე სწორი
# პასუხი არის 10 ქულა ხოლო არასწორი 0 ქულა, მიღებული პასუხებიდან უნდა
# განვსაზღვროთ რამდენი ქულა აიღო მომხმარებელმა, შევქმნათ ლოფ ფაილი
# game.log და შევინახოთ ყველა ქულა. ბოლოს გამოვუტანოთ მიღებული შედეგი


questions = [
    '50 + 27 = ? ',
    '26 - 10 = ? ',
    '150 / 30 = ? ',
    '8 ** 3 = ? ',
    '100 // 45 = ? '
]

correct_answers = [77, 16, 5, 512, 2]

score = 0

for index in range(len(questions)):
    user_answer = int(input(questions[index]))

    if user_answer == correct_answers[index]:
        score += 10
        print('Correct!')
    else:
        print(
            f'Wrong! The correct answer is '
            f'{correct_answers[index]}'
        )

with open('game.log', 'a') as file:
    file.write(f'Score: {score}\n')

final_score = f'Your final score is {score}'

print(final_score)



# 5. შექმენით ფაილი quiz.log, შექმენით გენერატორი რომელშიც შენახული იქნება
# 5 შეკითხვა და სათითაოდ დააბრუნებს, მომხმარებელმა უნდა უპასუხოს ყველა
# შეკითხვას და პასუხები შეინახეთ ლოგ ფაილში.

def questions_generator():
    yield 'What is the capital of Georgia? '
    yield 'How many days are in a week? '
    yield 'How many days are in a leap year? '
    yield 'Which planet is closest to the Sun? '
    yield 'Which ocean is the largest in the world? '


with open('quiz.log', 'w') as file:
    for question in questions_generator():
        answer = input(question)

        file.write(f'Question: {question}\n')
        file.write(f'Answer: {answer}\n\n')

print('Answers saved, thank you!')




