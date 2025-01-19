class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_words = {}
        chars_to_remove = r",.=!?;:-'" # символы от которых надо избавиться

        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                word_in_file = []
                for line in file: # проходимся по строчкам
                    line = line.strip()
                    line = line.translate(str.maketrans("", "", chars_to_remove)).lower().split(' ') #Убираем символы
                    for word in line: # проходимся по словам в строке
                        word_in_file.append(word) # добавляем слово
                all_words[name] = word_in_file # пополняем словарь именованного файла словом
        return all_words

    def find(self, word: str):
        dicts = {}
        word = word.lower()
        all_dictionaries = self.get_all_words() # получаем словари со словами

        for file_name, words in all_dictionaries.items():
            if word in words:
                # определяем позицию слова в списке
                position = words.index(word) + 1
                dicts[file_name] = position
        return dicts

    def count(self, word: str):
        dicts = {}
        word = word.lower()
        all_dictionaries = self.get_all_words() # получаем словари со словами

        for file_name, words in all_dictionaries.items():
            counter = 0
            for w in words:
                if w == word:
                    counter += 1
            dicts[file_name] = counter
        return dicts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))