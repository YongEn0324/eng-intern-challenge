import sys

brailleDic = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOO.O', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '.': 'OO..O.', ',': 'O.....', '?': '.O.O.O', '!': 'O.OO.O', '(': 'O.OO..', ')': 'O.OO..',
    ' ': '......', 'capital follows': '.....O', 'decimal follows': 'O.O...O','number follows': '.O.OOO',
    '.':'..OO.O', ',':'..O...', '?':'..O.OO','!': '..OOO.', ':':'..OO..', ';':'..O.O.','-':'....OO','/': '.O..O.',
    '<':'.O.O.O','>':'O.O.O.', '(':'O.O..O', ')':'.O.OO.'
}

def translatorInBraille(text):
    output= []
    numberMode = False

    for char in text: 
        if char.isupper():
            output.append(brailleDic['capital follows'])
            output.append(brailleDic[char.lower()])
        
        if char.isdigit():
            if not numberMode: 
                numberMode =True
                output.append(brailleDic['number follows'])
            output.append(brailleDic[char])
        
        elif char in brailleDic: 
            output.append(brailleDic[char])
            numberMode=False
    
    return ''.join(output)

if __name__ == "__main__":
    input_text = " ".join(sys.argv[1:])  
    result = translatorInBraille(input_text)
    print(result)