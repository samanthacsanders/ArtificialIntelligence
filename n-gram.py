'''
Created on Nov 19, 2014
@author: Samantha Sanders
'''
from __future__ import print_function
import random
import sys

class Trainer:
    def __init__(self, infilename):
        self.num_words = 2
        self.infilename = infilename
        self.transition_model = {}
        self.transition_model_totals = {}
        self.emission_model = {}
        self.emission_model_totals = {}
        
    def train(self):
        self.n_gram()
        
    def n_gram(self):
        trainingdata = open(self.infilename).read()
        contextconst = [""]
        context = contextconst
        for token in trainingdata.split():
            word, pos = self.parse_word(token)
            
            self.transition_model[str(context)] = self.transition_model.setdefault(str(context),{})
            self.transition_model_totals[str(context)] = self.transition_model_totals.setdefault(str(context), 0)
            self.emission_model[pos] = self.emission_model.setdefault(pos,{})
            self.emission_model_totals[pos] = self.emission_model_totals.setdefault(pos, 0)
            
            #Increment the totals for this transition
            self.transition_model_totals[str(context)] = self.transition_model_totals[str(context)] + 1
            #Build transition frequency table
            if self.transition_model[str(context)].has_key(pos):
                self.transition_model[str(context)][pos] = self.transition_model[str(context)][pos] + 1 
            else:
               self.transition_model[str(context)][pos] = 1
            
            #Increment the totals for this part of speech
            self.emission_model_totals[pos] = self.emission_model_totals[pos] + 1
            #Build emission frequency table
            if self.emission_model[pos].has_key(word):
                self.emission_model[pos][word] = self.emission_model[pos][word] + 1
            else:
                self.emission_model[pos][word] = 1

            context = (context+[pos])[1:]
        print(self.transition_model)
        print(self.transition_model_totals)
        print(self.emission_model)
        print(self.emission_model_totals)
        '''
        context = contextconst
        for i in range(100):
            word = random.choice(self.transition_model[str(context)])
            #print (word,end=" ")
            context = (context+[word])[1:]
 
        print()
        '''
    
    def parse_word(self, token):
        word = token.split("_")[0]
        pos = token.split("_")[1]
        return word, pos
        
def main(argv):
    if len(argv) > 0:
        trainer = Trainer(argv[0])
        trainer.train()
    else:
        print("no input file given")

if __name__ == '__main__': 
    main(sys.argv[1:])