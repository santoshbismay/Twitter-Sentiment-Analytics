import sys
import json
import re

def hw():
    print(Hello, world)

def lines(fp):
    print(str(len(fp.readlines())))
	
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


def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    sent_file =sys.argv[1]
    tweet_file = sys.argv[2]
    sent_dict = read_sent_file(sent_file)
    tweet_data = read_tweet_file(tweet_file)
    for i in range(len(tweet_data)):
        sent_score = 0
        if "text" in tweet_data[i]:
            words = tweet_data[i]["text"].split()
            for word in words:
                word = word.lower()
                if word in sent_dict:
                    sent_score +=sent_dict[word]
            print(sent_score)
    

if __name__ == '__main__':
    main()