import sys
import json
    
def clean_word(word):
    #coerce to lower
    temp = word.lower()
    # remove special characters
    exclude = set([",","!","?",":",".", ";"])
    temp = "".join(ch for ch in temp if not (ch in exclude))
    return temp
       
def count_hashtags(json_file):
    
    hash_counts = {} #initialize empty dictionary
    with open(json_file) as twitter_file:
        tweets = twitter_file.readlines() #ignore the first line
        for line in tweets:
            try:
                # load tweet
                mydict = json.loads(line)
                
                #get hashtags
                #tweet = mydict[u'text'].encode('utf-8')
                hashtags = mydict[u'entities']['hashtags']
                for tag_data in hashtags:
                    tag_text = tag_data[u'text'].encode('utf-8')
                    word_cln = clean_word(tag_text)                    
                    if word_cln in hash_counts.keys():
                        hash_counts[word_cln] += 1
                    else:
                        hash_counts[word_cln] = 1
            except:
                continue #handle errors from misformatted JSON
    return hash_counts
               
def main():
   
    tweet_file = sys.argv[1]
    hashtag_summary = count_hashtags(tweet_file)
    #get a sorted list of key-val pairs
    # (sorted in descending order by count)
    counts = sorted(hashtag_summary.items(), key=lambda x: x[1], reverse=True)
    
    
    top = 10    
    for dummy_i in range(top):
        hashtag = counts[dummy_i][0]
        count = counts[dummy_i][1]
        sys.stdout.write(hashtag + " " + str(count)+"\n")

      
if __name__ == '__main__':
    main()
    