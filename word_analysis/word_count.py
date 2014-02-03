import sys
import csv
import string
import pprint
import collections

import Levenshtein

with open('stuff.csv') as csvfile:
    
words = open('expectations.txt')
remove = open('exclude_words.txt')
remove = [l.strip() for l in remove]
counter = collections.Counter()
valid_letters = set(string.ascii_letters)
pp = pprint.PrettyPrinter(indent=2)

for l in words:
    words = l.split(' ')
    for word in words:
        original_word = "'%s'" % word
        word = word.lower()
        word = word.strip()
        word = word.strip(string.punctuation)

        # Split up words joined with / & ,.. might be a better way to do this
        comma_words = word.split(',')
        slash_words = word.split('/')

        '''if word == '':
            print 'skipping', original_word'''

        if len(comma_words) > 1:
            words.extend(comma_words)
        if len(slash_words) > 1:
            words.extend(slash_words)

        try:
            assert not word in remove
            assert set(word).issubset(valid_letters)
            assert not word == ''
        except AssertionError:
            #print 'Skipping word... ', word
            continue

        counter[word] += 1

'''
words = counter.keys()
updates = {}
for outer_word in words:
    for inner_word in words:
        if outer_word == inner_word:
            continue
        
        if Levenshtein.ratio(outer_word, inner_word) > 0.5:
            counter[outer_word] -= 1
            counter[inner_word] += 1

        if inner_word == 'nix':
           print "found nix"
           counter['unix'] += 1
           counter['nix'] -= 1
    
sys.exit(1)
'''

#counter.update({'nix':-1})
# Match all similar words... this was hacked quickly, a better way must exist
'''
for outter_word in counter:
    for inner_word in counter:
        if outter_word == inner_word:
            continue

        if Levenshtein.ratio(outter_word, inner_word) > 0.5:
            counter[outter_word] -= 1
            counter[inner_word] += 1
'''

#pp.pprint(counter)
pp.pprint(counter.most_common(500))
print len(counter.most_common(500))
elements = [e for e in counter.elements()]
elements.sort()
for e in elements:
    print e
