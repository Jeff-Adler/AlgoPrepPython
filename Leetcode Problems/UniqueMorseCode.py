#Restatement:
    
#Examples:

#Approach: Create dictionary that maps alphabetic characters morse code values. Iterate through list to build words morse. Add each morse word to set. Get length of set.

#Code

english_chars = 'abcdefghijklmnopqrstuvwxyz'

morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        eng_morse_dic = {}
                
        def createDictionary():
            nonlocal eng_morse_dic
            eng_morse_dic = dict(zip(english_chars, morse))
            
        def mapWord(word):
            morse_word = ""
            for char in word:
                morse_word += eng_morse_dic[char]
            return morse_word
                
        createDictionary()

        morse_unique_list = {mapWord(word) for word in words}
        
        return len(morse_unique_list)
