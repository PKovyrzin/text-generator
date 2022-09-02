import os
import pickle
import random
import re

class model:
    right_words = {}
    word_pattern = r'[\w]+[.,...?!;:]{0,3}'

    def fit(self, directory, model):
        if directory == None:
            text = input("Введите текст: ")
        else:
            text = ""
            files = os.listdir(directory)

            for file in files:
                file = directory + "/" + file
                with open(file, "r", encoding='utf-8') as f:
                    file_text = f.read()
                    text += file_text

        words = re.findall(self.word_pattern, text)
        for i in range(len(words) - 1):
            word = words[i].lower()
            next_word = words[i + 1].lower()
            self.right_words.setdefault(word, [])
            self.right_words[word].append(next_word)


        with open (model, "wb") as f:
            pickle.dump(self.right_words, f)

    def generate(self, file, length, prefix):
        with open (file, "rb") as f:
            best_words = pickle.load(f)

        if prefix == None:
            prefix = random.choice(list(best_words.keys()))

        word = prefix
        for _ in range (length):
            print(word, end = " ")
            word = random.choice(best_words[word])

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="обучение модели")
    parser.add_argument("--dir", type=str, help="путь к директории, в которой лежит коллекция документов")
    parser.add_argument("--model", type=str, required=True, help="путь к файлу, в который сохраняется модель")
    args = parser.parse_args()

    test_model = model()

    test_model.fit(args.dir, args.model)