from nltk.parse import stanford
import nltk
from nltk import CFG
from nltk.tokenize import word_tokenize
import json
import os
from lexical_diversity import lex_div as ld
import numpy as np
from downloads_folder import downloads_folder
import re

os.environ['STANFORD_PARSER'] = f'{downloads_folder}\\stanford-parser-full-2020-11-17'
os.environ['STANFORD_MODELS'] = f'{downloads_folder}\\stanford-parser-full-2020-11-17'


def print_tree(tree, depth=0, embedding_depth=0):
    if type(tree) == nltk.tree.Tree:
        for i in range(depth):
            print("  ", end="")
        #print(tree.label())

        new_embedding_depth = embedding_depth
        if tree.label() == "S":
            new_embedding_depth += 1
        
        max_embedding_depth = 0
        for subtree in tree:
            subtree_embedding_depth = print_tree(subtree, depth+1, new_embedding_depth)
            if subtree_embedding_depth > max_embedding_depth:
                max_embedding_depth = subtree_embedding_depth
        
        return max_embedding_depth
    else:
        # for i in range(depth):
        #    print("  ", end="")
        # print(f"[{depth}] ", end="")
        # print(f"{tree} - {embedding_depth}")

        return embedding_depth


tweets_info_file = open("tweets_info.txt", "a+")
tweets_full_text = ""
sentence_complexities = []

current_file_url = "cathmartingreen_user_tweets.tsv"

with open(current_file_url, encoding="utf-8") as file:
    rows = [x.split("\t") for x in file.read().split("\n")]

tweet_number = 0

for tweet in rows:
    print(f"Tweet {tweet_number}/3191")

    if tweet[8] == "en":
        text = tweet[1]

        tweets_full_text += text

        text = re.sub("[@#]","",text)
        text = re.sub("   ", ". ", text)
        sentences = re.split('; |\!|\?|\. ', text)

        for sentence in sentences:
            print(f"$ {sentence} $")
            words = word_tokenize(sentence)

            if len(words) > 0:
                sp = stanford.StanfordParser()
                trees = [tree for tree in sp.parse(words)]
                sentence_tree = trees[0]

                sentence_complexities.append(print_tree(sentence_tree[0]))
                print(sentence_complexities)

    tweet_number += 1
                
tweets_mean_sentence_embedding_level = np.mean(sentence_complexities)
tweets_mtld = ld.mtld(tweets_full_text)

tweets_info_file.write(f"{tweets_mean_sentence_embedding_level},{tweets_mtld}\n")