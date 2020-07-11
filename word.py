from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for lines in story:
    line = lines.decode('utf8').split('\n')
    for word in line:
        story_words.append(word)
story.close()

for word in story_words:
    print(word)
