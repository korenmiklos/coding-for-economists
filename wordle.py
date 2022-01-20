from random import choice

USER_PROMPT = 'Guess the word: '
CORRECT_POSITION = '*'
CORRECT_LETTER = 'o'
INCORRECT_LETTER = '-'
ERROR_MESSAGE = 'TWO WORDS ARE NOT OF SAME LENGTH.'

def score_letter(letter, position, true_word):
    # >>> score_letter('A', 0, 'ABBA')
    # '*'
    # >>> score_letter('B', 0, 'ABBA')
    # 'o'
    # >>> score_letter('C', 0, 'ABBA')
    # '-'
    if (true_word[position] == letter):
        return CORRECT_POSITION
    # discuss 'in'
    if (letter in true_word):
        return CORRECT_LETTER
    else:
        return INCORRECT_LETTER

def score_word(guess, true_word):
    # >>> score_word('APPL', 'ABBA')
    # '*---'
    if len(guess) != len(true_word):
        return ERROR_MESSAGE
    score = ''
    N = len(true_word)
    for position in range(N):
        score = score + score_letter(guess[position], position, true_word)
    return score

def get_and_score_guess(true_word):
    guess = input(USER_PROMPT)
    score = score_word(guess, true_word)
    print(len(USER_PROMPT) * ' ' + score)
    return score

def loop_until_success(true_word):
    correct_guess = False
    while not correct_guess:
        score = get_and_score_guess(true_word)
        if score == len(score) * CORRECT_POSITION:
            correct_guess = True

def get_random_word(filename):
    # b/c we call the function on line 55, filename will have the value 'data/words.txt'
    word_file = open(filename, 'rt')
    words = word_file.readlines()
    return choice(words)

#only constant and function definitions until now, execution starts here
word = get_random_word('data/words.txt').strip()
loop_until_success(word)
