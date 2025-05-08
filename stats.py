def word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

def char_count(text):
    charcs = {}
    for char in text:
        char = char.lower()
        if char in charcs:
            charcs[char] += 1
        else:
            charcs[char] = 1
    return charcs

def print_report(charcs):
    report = ""
    charcs = sorted(charcs.items(), key=lambda item: item[1], reverse=True)
    for char in charcs:
        if char[0].isalpha():
            report += f"{char[0]}: {char[1]}\n"
    return report
