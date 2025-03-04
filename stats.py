def word_counter(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words
    
def character_counter(text):
    total_count = {}
    lower_text = text.lower()
    for char in lower_text:
        total_count[char] = total_count.get(char, 0) + 1
    return total_count
    
def sort_char_counts(dict):
    sorted_chars = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    result = ""
    for char, count in sorted_chars:
        result += f"{char}: {count}\n"
    return result.strip()