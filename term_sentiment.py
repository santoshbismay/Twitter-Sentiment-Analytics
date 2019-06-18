import sys
import json

def read_sent_file(sent_file_name):
    sentfile = open(sent_file_name, 'r')
    scores = {} # initialize an empty dictionary
    for line in sentfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores

def read_tweet_file(tweet_file_name):
    tweet_data = []
    tweet_file = open(tweet_file_name, 'r')
    for line in tweet_file:
        tweet_data.append(json.loads(line))
    return tweet_data


def tweet_sentiment_dict(sent_file_name, tweet_file):
    sent_dict = read_sent_file(sent_file_name)
    tweet_data = read_tweet_file(tweet_file)
    tweet_sent_dict ={}
    for i in range(len(tweet_data)):
        sent_score = 0
        if "text" in tweet_data[i]:
            words = tweet_data[i]["text"].split()
            for word in words:
                word = word.lower()
                if word in sent_dict:
                    sent_score +=sent_dict[word]
            if sent_score != 0:
                tweet_sent_dict[tweet_data[i]["text"]]=sent_score
    return tweet_sent_dict

def word_sentiment_dict(tweet_sent_dict, sent_file_name):
    sent_dict = read_sent_file(sent_file_name)
    word_sent_dict = {}
    for tweet in tweet_sent_dict:
        words = tweet.split()
        for word in words:
            word = word.lower()
            word = word.encode('utf-8')
            if not(word in sent_dict) and not('@' in word) and not('http' in word):
                if word in word_sent_dict:
                    word_sent_dict[word][0] += 1
                    word_sent_dict[word][1] += tweet_sent_dict[tweet]                
                else:
                    word_sent_dict[word] = [1,tweet_sent_dict[tweet]]
    return word_sent_dict
	

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    word_sent_dict = word_sentiment_dict(tweet_sentiment_dict(sent_file, tweet_file),sent_file)
    for word in word_sent_dict:
        print word, (word_sent_dict[word][1]/word_sent_dict[word][0])

if __name__ == '__main__':
    main()