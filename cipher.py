import enchant
import enchant.tokenize

en_dict = enchant.Dict("en_US")
tokenizer = enchant.tokenize.get_tokenizer("en_US")


class Cipher:

    def __init__(self, filename):
        print('abcdefghijklmnopqrstuvwxyz')

        self.en_dict = enchant.Dict("en_US")
        tokenizer = enchant.tokenize.get_tokenizer("en_US")
        filedata = open(filename, 'r')
        self.words = []
        self.scrambled = []
        for (word, _) in tokenizer(filedata.read()):
            word = word.lower()
            self.scrambled.append(word)
            self.words.append('')
        self.shift = 0
        self.score = 0.0

    def scoreLetters(self):
        count = 0
        correct = 0
        for word in self.words:
            count += 1
            if self.en_dict.check(word):
                correct += 1

        self.score = (correct * 1.0) / count
        return self.score

    def shiftConstant(self, const = 1):
        self.shift = self.shift - const
        for ii, word in enumerate(self.scrambled):
            shifted = ''
            for char in word:
                shifted += chr((ord(char) - ord('a') + 1)
                               % (ord('z') - ord('a') + 1) + ord('a'))
            self.words[ii] = shifted
            
    def shiftKey(self, key):
        self.shift = []
        for char in key:
            self.shift.append((ord(char) - ord('a')))
            
        index = 0
        
        for ii,word in enumerate(self.scrambled):
            shifted = ''
            for char in word:
                shifted += chr((ord(char) - ord('a') - self.shift[index])
                               % (ord('z') - ord('a') +1) + ord('a'))
                index = (index+1) % len(self.shift)
            self.words[ii] = shifted
        
            

    def solve(self, key = None):
        
        if not key:
            for _ in range(ord('z') - ord('a') + 1):
                self.shiftConstant()
                self.scoreLetters()
                if self.score > 0.8:
                    text = ""
                    for word in self.words:
                        text = text + word
                        text = text + ' '
                    print(text)
                    print(self.shift)
        else:
            self.shiftKey(key)
            self.scoreLetters()
            
            if self.score > 0.8:
                    text = ""
                    for word in self.words:
                        text = text + word
                        text = text + ' '
                    print(text)
                    print(self.shift)
            else:
                print("fail")
