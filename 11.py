"task1"
def remove_longest_t_word(sentence):
    words = sentence.split()
    t_words = [w for w in words if w.lower().endswith('t')]
    if not t_words:
        return sentence
    longest = max(t_words, key=len)
    words.remove(longest)
    return ' '.join(words)
"task2"
def insert_after_min(tup):
    if not tup:
        return (-1,)
    min_idx = tup.index(min(tup))
    return tup[:min_idx + 1] + (-1,) + tup[min_idx + 1:]