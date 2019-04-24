 
 #Story generation and visualization from tweets
 
 def most_common_visual(tweet_columns):
        """Most common words in all tweets"""
        words = ' '.join([t for t in tweet_columns])
        wordcloud = WordCloud(width=800, height=500, random_state=21,max_words=100, background_color="white").generate(words)
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.title("Most common words in all tweets",fontdict={'fontsize':19,'fontweight':'bold'})
        plt.axis('off')
        plt.show()
    
    def pos_visual(tweet_columns,label_columns):
        """Visualization of most common words in positive tweets"""
        positive_words =' '.join([t for t in tweet_columns [label_columns == 0]])
        wordcloud = WordCloud(width=800, height=500, random_state=21,max_words=100,max_font_size=110).generate(positive_words)
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.title("Most common words in positive tweets",fontdict={'fontsize':19,'fontweight':'bold'})
        plt.axis('off')
        plt.show()
    
    def neg_visual(tweet_columns,label_columns):
        """Visualization of most common words in negative tweets"""
        negative_words =' '.join([t for t in tweet_columns[label_columns == 1]])
        wordcloud = WordCloud(width=800, height=500, random_state=21,max_words=100,max_font_size=110).generate(negative_words)
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.title("Most common words in negative tweets",fontdict={'fontsize':19,'fontweight':'bold'})
        plt.axis('off')
        plt.show()
