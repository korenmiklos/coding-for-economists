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
    if len(guess) != len(true_word):
        return 'TWO WORDS ARE NOT OF SAME LENGTH.'
    score = ''
    N = len(true_word)
    for position in range(N):
        score = score + score_letter(guess[position], position, true_word)
    return score

# FIXME: add function to read random word
# FIXME: add function to get user guess

message = score_word('APPB', 'ABBA')
print(message)
