import os
from gtts import gTTS

#tts, function to convert text to speech
#parameters are text to convert, language, slow or not, filename
def tts(text='audio.txt', fLang='fr', Fslow=False, filename='', path=''):
    tts = gTTS(text=text, lang=fLang, slow=Fslow)
    #if no filename given, save as ttsX.mp3
    if filename == '' or filename == None:
        print('No filename given, saving as tts#.mp3')
        filename = 'tts'
    #if no path given, save in current directory
    if path == '' or path == None:
        print('No path given, saving in current directory')
        path = './'
    #else, if the path doesn't exist, create it
    else:
        if not os.path.exists(path):
            print('Path doesn\'t exist, creating it')
            os.makedirs(path)
    num_files = len([f for f in os.listdir(path) if f.startswith(filename)])
    tts.save(path + filename + str(num_files) + '.mp3')

#getText, function to read text from file
def getText(filename):
    with open(filename, 'r',encoding='utf-8') as f:
        return f.read()


#getComments, function to get comments from python code
def getComments(filename):
    #utf-8 encoding permite to read french accents
    with open (filename, 'r',encoding='utf-8') as f:
        lines = f.readlines()
        comments = ''
        for line in lines:
            if line.lstrip().startswith('#'):
                comments += line.lstrip()[1:] 
        return comments

#readText, implementation of tts function and getText function
def readText():
    text = getText('audio.txt')
    tts(text,fLang='fr', Fslow=False, path='audio/')
    print('Done')

#readCode, implementation of tts function and getComments function
def readCode():
    comments = getComments('synthese_vocale.py')
    tts(comments,fLang='en', Fslow=False, filename='code', path='code/')  
    print('Done')

readText()
readCode()