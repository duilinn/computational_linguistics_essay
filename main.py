from nltk.parse import stanford
import nltk
from nltk import CFG
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup
import os
from lexical_diversity import lex_div as ld
import numpy as np

os.environ['STANFORD_PARSER'] = 'C:\\Users\\david\\Downloads\\stanford-parser-full-2020-11-17'
os.environ['STANFORD_MODELS'] = 'C:\\Users\\david\\Downloads\\stanford-parser-full-2020-11-17'

debates_file_path = "debates_Catherine-Martin.D.2016-10-03.list.txt"

with open(debates_file_path) as file:
    debate_urls = file.read().split("\n")

url_info_file = open("url_info.txt", "a+")

# print(nltk.pos_tag(word_tokenize(\
#     "In the present study"," we examine the outcomes of such a period of no \ exposure on the neurocognition of L2 grammar:")"," tagset='universal'))

# grammar = nltk.CFG.fromstring(""
# S -> S CONJ S | NP VP
# NP -> Det N | NP CONJ NP
# VP -> V NP
# Det -> "the" | "a"
# N -> "man" | "letter" | "girl" | "present" | "grandmother" | "cake" | "bread"
# V -> "wrote" | "bought" | "baked"
# CONJ -> "and"
# "")

# grammar = nltk.CFG.fromstring("""
# S -> NP VP | ADVP S | C S | ADJ S | NP
# ADVP -> ADV | PP | ADV NP PP
# ADV ->"almost" | "now" | "so" | "often"
# ADJP -> ADJ | ADJ PP
# ADJ ->"economic" | "high" | "our" | "challenging" | "hard" | "total" | "my" | "new" | "significant" | "state_of_the_art" | "local"
# ADJ -> "delighted" | "able"
# DET ->"one" | "these" | "27" | "other" | "an" | "the" | "a"
# NP -> DET N | ADJ N | N N | N | N PP | PRON | PRON S | DET N S | N1 C N2 | N VP | N3 N ADJP NP | N4 N4
# N1 -> NP
# N2 -> NP
# N3 -> N N | N
# N4 -> N3 N3
# N ->"year" | "pandemic" | "restrictions" | "sectors" | "conditions" | "inflation" | "energy" | "costs" | "pressure" | "businesses" | "urgency" | "climate" | "action" | "planet" | "future" | "generations" | "course" | "part" | "irelands" | "response" | "war" | "ukraine" | "hard" | "solidarity" | "understanding" | "societys" | "cohesion" | "well_being" | "funding" | "2023" | "department" | "funding" | "place" | "schools" | "irish" | "language" | "assistant" | "baitweets" | "research" | "desire" | "youth" | "radio" | "service" | "findings" | "support" | "centre" | "tglurgan" | "groups"
# PP -> P S | P NP | P VP | P NP PP | P P
# P ->"after" | "with" | "on" | "of" | "for" | "in" | "up" | "to" | "out"
# VP -> V | V NP | V NP PP | ADVP VP | AUX VP | V PP | V1 C V2 | V VP | V NP VP | V PP NP | V ADJP
# V1 -> VP
# V2 -> VP
# V ->"ended" | "face" | "putting" | "tackle" | "safeguard" | "play" | "done" | "reinforce" | "supported" | "is" | "follows" | "enable" | "employ" | "carried" | "show" | "planned" | "be" | "repair" | "use"
# C ->"and" | "so" | "to" | "by" | "as" | "that"
# PRON ->"they" | "we" | "it" | "everything"
# AUX ->"must" | "can" | "continue" | "have" | ADV ADV
# """)

# grammar = nltk.CFG.fromstring("""
# S -> NP VP | ADVP S | C S | ADJ S | NP
# ADVP -> ADV | PP | ADV NP PP
# ADV ->"almost" | "now" | "so" | "often"
# ADJP -> ADJ | ADJ PP
# ADJ ->"economic" | "high" | "our" | "challenging" | "hard" | "total" | "my" | "new" | "significant" | "state_of_the_art" | "local"
# ADJ -> "delighted" | "able"
# DET ->"one" | "these" | "27" | "other" | "an" | "the" | "a"
# NP -> DET N | ADJ N | N N | N | N PP | PRON | PRON S | DET N S | N1 C N2 | N VP | N3 N ADJP NP | N4 N4
# N1 -> NP
# N2 -> NP
# N3 -> N N | N
# N4 -> N3 N3
# N ->"year" | "pandemic" | "restrictions" | "sectors" | "conditions" | "inflation" | "energy" | "costs" | "pressure" | "businesses" | "urgency" | "climate" | "action" | "planet" | "future" | "generations" | "course" | "part" | "irelands" | "response" | "war" | "ukraine" | "hard" | "solidarity" | "understanding" | "societys" | "cohesion" | "well_being" | "funding" | "2023" | "department" | "funding" | "place" | "schools" | "irish" | "language" | "assistant" | "baitweets" | "research" | "desire" | "youth" | "radio" | "service" | "findings" | "support" | "centre" | "tglurgan" | "groups"
# PP -> P S | P NP | P VP | P NP PP | P P
# P ->"after" | "with" | "on" | "of" | "for" | "in" | "up" | "to" | "out"
# VP -> V | V NP | V NP PP | ADVP VP | AUX VP | V PP | V1 C V2 | V VP | V NP VP | V PP NP | V ADJP
# V1 -> VP
# V2 -> VP
# V ->"ended" | "face" | "putting" | "tackle" | "safeguard" | "play" | "done" | "reinforce" | "supported" | "is" | "follows" | "enable" | "employ" | "carried" | "show" | "planned" | "be" | "repair" | "use"
# C ->"and" | "so" | "to" | "by" | "as" | "that"
# PRON ->"they" | "we" | "it" | "everything"
# AUX ->"must" | "can" | "continue" | "have" | ADV ADV
# """)

# chart_parser = nltk.BottomUpChartParser(grammar, trace=2)


# sent1 = 'the man wrote a letter and the girl bought a present'.split()
d = [["almost", "one", "year", "after", "pandemic", "restrictions", "ended", "these", "sectors", "now", "face", "challenging", "economic", "conditions", "with", "high", "inflation", "and", "energy", "costs", "putting", "pressure", "on", "businesses"],
     ["they", "must", "tackle", "the", "urgency", "of", "climate", "action", "so",
     "we", "can", "safeguard", "our", "planet", "for", "future", "generations"],
     ["and", "of", "course", "they", "must", "play", "our", "part", "in",
     "irelands", "response", "to", "the", "war", "in", "the", "ukraine"],
     ["as", "we", "have", "so", "often", "done", "in", "hard", "times", "these", "sectors", "continue", "to", "reinforce",
     "our", "resilience", "solidarity", "and", "understanding", "and", "support", "societys", "cohesion", "and", "well_being"],
     ["total", "funding", "for", "2023", "for", "the", "sectors", "supported", "by", "my", "department", "is", "as", "follows"]]

s = [["funding", "is", "now", "in", "place", "to", "enable", "up", "to", "27", "schools", "employ", "an", "irish", "language", "assistant"],
     ["baitweets", "have", "carried", "out", "research", "on", "the", "desire",
      "for", "a", "new", "irish", "language", "youth", "radio", "service"],
     ["delighted", "these", "findings", "show",
         "significant", "support", "for", "it"],
     ["a", "new", "state_of_the_art", "centre", "planned",
     "for", "tglurgan", "and", "other", "local", "groups"],
     ["we", "must", "be", "able", "to", "repair", "everything", "that", "we", "use"]]

# grammar = r"""
#   NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
#   PP: {<IN><NP>}               # Chunk prepositions followed by NP
#   VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
#   CLAUSE: {<NP><VP>}           # Chunk NP, VP
#   """


grammar = nltk.PCFG.fromstring("""
    S    -> NP VP              [1.0]
    VP   -> TV NP              [0.4]
    VP   -> IV                 [0.3]
    VP   -> DatV NP NP         [0.3]
    TV   -> 'saw'              [1.0]
    IV   -> 'ate'              [1.0]
    DatV -> 'gave'             [1.0]
    NP   -> 'telescopes'       [0.8]
    NP   -> 'Jack'             [0.2]
    """)
# cp = nltk.RegexpParser(grammar)
viterbi_parser = nltk.ViterbiParser(grammar)

def print_tree(tree, depth=0, embedding_depth=0):
    if type(tree) == nltk.tree.Tree:
        # for i in range(depth):
        #     print("  ", end="")
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
        return embedding_depth
    
        #for i in range(depth):
        #    print("  ", end="")
        #print(f"[{depth}] ", end="")
        #print(f"{tree} - {embedding_depth}")
        

url_index = 0
for url in debate_urls:
    sentence_complexities = []
    document = requests.get(url)
    soup = BeautifulSoup(document.content, "lxml-xml")
    print(f"URL {url_index}")

    url_full_text = ""

    for speech in soup.find_all("speech", by="#CatherineMartin"):
        speech_time = speech.find("from").find("recordedTime")["time"]
        print(speech_time)

        for paragraph in speech.find_all("p"):
            paragraph_full_text = paragraph.decode_contents()
            url_full_text += paragraph_full_text

            sentences = paragraph_full_text.split(". ")

            for sentence in sentences:
                print(f"$ {sentence} $")
                words = word_tokenize(sentence)
                # print(nltk.pos_tag(paragraph_text))

                # for tree in viterbi_parser.parse(['Jack', 'saw', 'telescopes']):
                #   print(tree)

                if len(words) > 0:
                    sp = stanford.StanfordParser()
                    trees = [tree for tree in sp.parse(words)]
                    sentence_tree = trees[0]
                
                    sentence_complexities.append(print_tree(sentence_tree[0]))
                    print(sentence_complexities)
                    print("")
    print(url_full_text)
    url_mean_sentence_embedding_level = np.mean(sentence_complexities)
    url_mtld = ld.mtld(url_full_text)

    url_info_file.write(\
        f"{url_index},{url},{speech_time},{url_mean_sentence_embedding_level},{url_mtld}\n")
    
    url_info_file.flush()
    url_index += 1

    # print(speeches)


# for current_sentence in s:
#   for tree in chart_parser.parse(current_sentence):
#     print(tree)

# import stanza

# stanza.download("en")
# nlp = stanza.Pipeline("en")
# doc = nlp("Barack Obama was born in Hawaii.")
# print(doc)
# print(doc.entities)
