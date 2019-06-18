import sys
import json


	
def read_sent_file(sent_file):
    scores = {} 
    for line in sent_file:
        term, score  = line.split("\t")  
        scores[term] = int(score) 
    return scores

def read_tweet_file(tweet_file):
    tweet_data = []
    for line in tweet_file:
        tweet_data.append(json.loads(line))
    return tweet_data

def line_sent_score(tweet_line, sent_dict):
    sent_score = 0
    if "text" in tweet_line:
        words = tweet_line["text"].split()
        for word in words:
            word = word.lower()
            if word in sent_dict:
                sent_score += sent_dict[word]
    return sent_score
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = read_sent_file(sent_file)
    tweet_data = read_tweet_file(tweet_file)
    dict_state={}
    count = 0
    for i in range(len(tweet_data)):
        try:
            if tweet_data[i]['place']['country_code']=='US':
                place = tweet_data[i]['place']['full_name'].split(', ')
                if len(place[1])==2:
                    if place[1] in dict_state:
                        dict_state[place[1]] += line_sent_score(tweet_data[i],sent_dict)
                        if count < line_sent_score(tweet_data[i],sent_dict):
                            count = line_sent_score(tweet_data[i],sent_dict)
                            happy_state = place[1]
                    else:
                        dict_state[place[1]] = 1
        except:
            continue
    print(happy_state)
    

if __name__ == '__main__':
    main()

