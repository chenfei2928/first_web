import wordcloud

w = wordcloud.WordCloud()

w.generate('and that government of the people,by the people,for the people,shall not perish from the erath.')


w.to_file('output.png')
