def wordcount(filename):
    """
    Counts the incidences of each word in a text file.
    """    

    the_file = open(filename)

    word_count = {}
    for line in the_file:
        words = line.rstrip().split(" ")
        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
    
    for tup in word_count.iteritems():
        print "%s %d" % (tup[0], tup[1])
wordcount("twain.txt")