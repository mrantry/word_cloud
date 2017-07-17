import sys
import re
import operator

#should return a string without punctuation
def strip_punc(s):
    return re.sub(r'[^\w\s]', '', s)

def word_cloud(infile, stopwordsfile):

    wordcount = {}

    #Reads the stopwords into a list
    stopwords = [x.strip() for x in open(stopwordsfile, 'r').readlines()]


    #reads data from the text file into a list
    lines = []
    with open(infile) as f:
        lines = f.readlines()
        lines = [line.split() for line in lines]

    #does the wordcount
    for line in lines:
        for word in line:
            word = strip_punc(word).lower()
            if word not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1

    #sorts the dictionary, grabs 10 most common words
    output = dict(sorted(wordcount.items(),
                  key=operator.itemgetter(1), reverse=True)[:10])

    print(output)


if __name__=='__main__':

    try:

        word_cloud(sys.argv[1], sys.argv[2])

    except Exception as e:

        print('An exception has occured:')
        print(e)
        print('Try running as python3 word_cloud.py <input-text> <stopwords>')
