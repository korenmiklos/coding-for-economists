def score_letter(letter, position, true_word):
    # >>> score_letter('A', 0, 'ABBA')
    # '*'
    # >>> score_letter('B', 0, 'ABBA')
    # 'o'
    # >>> score_letter('C', 0, 'ABBA')
    # '-'
    if (true_word[position] == letter):
        return '*' # for correct position
    if (letter in true_word):
        return 'o' # for correct letter, incorrect position
    else:
        return '-'

def score_word(guess, true_word):
    # >>> score_word('APPL', 'ABBA')
    # '*---'
    N = len(true_word)
    for position in range(N):
        print(position, guess[position], true_word[position], score_letter(guess[position], position, true_word))

score_word('APPL', 'ABBA')