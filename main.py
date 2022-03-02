import termcolor
import random

word_list = open("word list.txt", "r").readlines()
answer_word = ""
for i in range(len(word_list)):
    word_list[i] = (word_list[i].split("\n"))[0]
alt_word_list = open("alt word list.txt", "r").readlines()
for i in range(len(alt_word_list)):
    alt_word_list[i] = (alt_word_list[i].split("\n"))[0]
guess = ""
guess_num = 1
word_color = []
guess_letters = []
win = None


def start_game():
    print()
    print('which word list will you use? type "WORDLE" to use the original wordle word list, or type "ALT" for MY word list.')
    print('Note: anything else inputted will count as WORDLE.')
    print()
    if input() == "ALT":
        word_list = alt_word_list
    print()
    print("try to guess a 5-letter word within 6 attempts. write a 5-letter word here.")
    print()
    global answer_word, guess, guess_num, word_color, guess_letters, win
    answer_word = word_list[random.randrange(0, len(word_list), 1)]
    word_color = []
    guess_num = 1
    win = None
    for guess_num in range(6):
        if word_color == ['green', 'green', 'green', 'green', 'green']:
            win = True
            break
        guess_letters = []
        word_color = []
        guess = ""
        try_guess()
        for i in range(5):
            if guess[i] in answer_word and guess_letters.count(guess[i]) < answer_word.count(guess[i]):
                guess_letters.append(guess[i])
                if guess[i] == answer_word[i]:
                    word_color.append("green")
                else:
                    word_color.append("yellow")
            else:
                guess_letters.extend([guess[i], guess[i], guess[i], guess[i], guess[i]])
                word_color.append("white")
        print(termcolor.colored(guess[0], word_color[0]), " ", termcolor.colored(guess[1], word_color[1]),
              " ", termcolor.colored(guess[2], word_color[2]), " ", termcolor.colored(guess[3], word_color[3]),
              " ", termcolor.colored(guess[4], word_color[4]))
    if win == True:
        print("You Won! the word was", answer_word + "! You got the word in", guess_num, "attempt(s).")
    elif win == None:
        print("You Lost! The Word was", answer_word + ". better luck next time!")


def try_guess():
    global guess
    while not (len(guess) == 5):
        guess = str(input())
        if len(guess) < 5:
            print("guess too small! needs 5 letters.")
        elif len(guess) >= 6:
            print("guess too big! needs 5 letters.")


start_game()
