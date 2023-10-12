dictionary = {
    "apple": "A fruit with a red or green skin and a crisp white flesh.",
    "banana": "A long, curved fruit with a yellow skin.",
    "carrot": "A long, orange vegetable with a sweet taste."
}

def lookup_word(word):
    return dictionary.get(word, "Word not found in the dictionary.")

def suggest_words(prefix):
    suggestions = [word for word in dictionary.keys() if word.startswith(prefix)]
    return suggestions

def main():
    while True:
        user_input = input("Enter a word: ")
        
        if not user_input:
            break

        word = user_input.lower()

        if word in dictionary:
            print("Definition:", dictionary[word])
        else:
            suggestions = suggest_words(word)
            if suggestions:
                print("Word not found. Suggestions:")
                for suggestion in suggestions:
                    print("-", suggestion)
            else:
                print("No suggestions found.")

if __name__ == "__main__":
    main()
