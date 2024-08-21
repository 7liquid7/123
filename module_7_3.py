import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                # Читаем весь текст, приводим к нижнему регистру
                text = file.read().lower()
                # Удаляем пунктуацию
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punct, '')
                # Разбиваем текст на слова
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            try:
                position = words.index(word) + 1  # +1 чтобы позиции начинались с 1
            except ValueError:
                position = -1  # Если слово не найдено
            results[file_name] = position

        return results

    def count(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)
            results[file_name] = count

        return results


# Пример использования
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('TEXT'))  # 3 слово по счёту
print(finder.count('teXT'))  # 4 слова teXT в тексте всего
