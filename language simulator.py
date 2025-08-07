import random

def mutate_word(word, mutation_rate=0.1):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    word = list(word)

    for i in range(len(word)):
        if random.random() < mutation_rate:
            # Choose mutation type: substitution, insertion, or deletion
            mutation_type = random.choice(['sub', 'ins', 'del'])

            if mutation_type == 'sub':
                # Substitute letter
                word[i] = random.choice(letters)
            elif mutation_type == 'ins':
                # Insert random letter before current position
                word.insert(i, random.choice(letters))
            elif mutation_type == 'del' and len(word) > 1:
                # Delete current letter
                word.pop(i)
                break  # Avoid index issues after deletion
    return ''.join(word)

def evolve_language(language, generations=10, mutation_rate=0.1):
    current_language = language[:]
    for gen in range(1, generations + 1):
        new_language = []
        for word in current_language:
            new_word = mutate_word(word, mutation_rate)
            new_language.append(new_word)
        current_language = new_language

        print(f"Generation {gen}: {current_language}")

if __name__ == "__main__":
    # Starting language words
    proto_language = ['mama', 'papa', 'water', 'fire', 'sun', 'moon', 'tree', 'fish', 'bird', 'stone']

    print("Starting language:", proto_language)
    evolve_language(proto_language, generations=15, mutation_rate=0.2)

