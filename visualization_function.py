 
 #Story generation and visualization from tweets
 
 # Import necessary packages
 
 from wordcloud import WordCloud
 
  def text_length_dist(input_column):
    """Checking distribution of length of the text or number of characters"""
    text_length=input_column.str.len()
    plt.hist(text_length, bins=20)
    plt.title("Text Length")
    plt.show()  
  
  
  def most_common_visual(input_column):
        """Most common words in text"""
        words = ' '.join([t for t in input_column])
        wordcloud = WordCloud(width=800, height=500, random_state=21,max_words=100, background_color="white").generate(words)
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.title("Most common words in text",fontdict={'fontsize':19,'fontweight':'bold'})
        plt.axis('off')
        plt.show()
    
  def pos_visual(input_text_column,input_label_column):
        """Visualization of most common words in positive text"""
        positive_words =' '.join([t for t in input_text_column [input_label_column == 0]])
        wordcloud = WordCloud(width=800, height=500, random_state=21,max_words=100,max_font_size=110).generate(positive_words)
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.title("Most common words in positive text",fontdict={'fontsize':19,'fontweight':'bold'})
        plt.axis('off')
        plt.show()
    
  def neg_visual(input_text_column,input_label_column):
        """Visualization of most common words in negative text"""
        negative_words =' '.join([t for t in input_text_column[input_label_column == 1]])
        wordcloud = WordCloud(width=800, height=500, random_state=21,max_words=100,max_font_size=110).generate(negative_words)
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.title("Most common words in negative text",fontdict={'fontsize':19,'fontweight':'bold'})
        plt.axis('off')
        plt.show()
