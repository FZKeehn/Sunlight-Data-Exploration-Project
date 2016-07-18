# -*- coding: utf-8 -*-
"""
Frank Zebulon Keehn 
Sunlight Data Exploration Project
Written in Python (x,y) with Python 2.7.10
"""

"""Orange is a Python data mining and visualization library that I installed
for its association rules functions"""
 
import Orange
#save the basket file in a data table the association rules functions can use
data = Orange.data.Table("Phrases_2015.basket")




"""function that generates the set association rules for given constraints, in
this case support = 0.4."""
rules = Orange.associate.AssociationRulesSparseInducer(data,
                                                       support = 0.4)

""""
Next, these rules are written to another text file for exploration
 and interpretation.
"""
rules_file = open('rules_2015.txt','w+')
                                                       
for item in rules:
    rules_file.write("%5.3f   %5.3f   %s\n" % (item.support, item.confidence,
                                               item))
rules_file.close()

"""This code is for if you want to explore the frequent itemsets themselves, 
instead of just the association rules."""
inducer = Orange.associate.AssociationRulesSparseInducer(support = 0.4, 
                                                         store_examples = True)
itemsets = inducer.get_itemsets(data)     

"""The following section provides another text file with automatically 
generated examples of basic interpretations of some of the association rules.
"""                                                
interpretation = []
for item in rules:
    interpretation.append([item.support,item.confidence,
                           str(item).split(" -> ")])

interpretation_file = open('interpretation.txt','w+')

for item in interpretation:
    part1 = "The itemset '%s' occurs in %1.0f%% of cases in the dataset.\n" % \
    (item[2][0], item[0]*100)
    part2 = "The rule '%s -> %s' holds in %1.0f%% these cases.\n\n" % \
    (item[2][0], item[2][1], item[1]*100)                           
    interpretation_file.write(part1)
    interpretation_file.write(part2)
interpretation_file.close()
    
