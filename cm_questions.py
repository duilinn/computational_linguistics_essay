from nltk.parse import stanford
import nltk
from nltk import CFG
from nltk.tokenize import word_tokenize
import json
import os
from lexical_diversity import lex_div as ld
import numpy as np
from downloads_folder import downloads_folder
os.environ['STANFORD_PARSER'] = f'{downloads_folder}\\stanford-parser-full-2020-11-17'
os.environ['STANFORD_MODELS'] = f'{downloads_folder}\\stanford-parser-full-2020-11-17'


def print_tree(tree, depth=0, embedding_depth=0):
    if type(tree) == nltk.tree.Tree:
        for i in range(depth):
            print("  ", end="")
        print(tree.label())

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
        return embedding_depth
    
        for i in range(depth):
           print("  ", end="")
        print(f"[{depth}] ", end="")
        print(f"{tree} - {embedding_depth}")


questions_info_file = open("questions_info.txt", "a+")
questions_full_text = ""
sentence_complexities = []

for i in range(1, 5):
    current_file_url = f"cmq{i}.json"

    with open(current_file_url, "r", encoding='utf-8') as read_file:
        data = json.load(read_file)

    for question in data["results"]:
        text = question["question"]["showAs"]
        # print(text[:50])
        start_index = text.find("Deputy Catherine Martin asked the ") + 34
        end_index = text.find("[")
        #print(text[start_index:end_index] + "\n\n")

        questions_full_text += text[start_index:end_index]

        sentences = text[start_index:end_index].split(". ")

        for sentence in sentences:
            print(f"$ {sentence} $")
            words = word_tokenize(sentence)

            if len(words) > 0:
                sp = stanford.StanfordParser()
                trees = [tree for tree in sp.parse(words)]
                sentence_tree = trees[0]

                sentence_complexities.append(print_tree(sentence_tree[0]))
                print(sentence_complexities)
                
questions_mean_sentence_embedding_level = np.mean(sentence_complexities)
questions_mtld = ld.mtld(questions_full_text)

questions_info_file.write(f"{questions_mean_sentence_embedding_level},{questions_mtld}\n")