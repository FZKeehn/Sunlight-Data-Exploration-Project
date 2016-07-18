# -*- coding: utf-8 -*-
"""
Frank Zebulon Keehn 
Sunlight Data Exploration Project
Written in Python (x,y) with Python 2.7.10
"""
import sunlight
sunlight.config.API_KEY = """enter your own sunlight API Key here, which can be obtained from 
                          https://sunlightfoundation.com/api/accounts/register/ """

"""The list of strings below, irrelevant_words, is something that I am
compiling manually as I explore the Capitol Words data, as a means of
filtering words out of the most frequently spoken words lists that 
are not relevant (in my opinion) to the analyses I want to conduct."""

irrelevant_words = ['that','is','for','we','this','it','have','are',
                    'with','our','they','or','has','an','he','his',
                    'my','who','their','but','would','so', 'no',
                    'what','there','more','other','about','which',
                    'you','been','do','new','1','these','one','ms.',
                    'when','can','if','us','were','those','such',
                    'than','any','because','department','many','had',
                    'up','going','just','them','year','them','also',
                    '?','out','shall','now','am','over','2015',
                    'make','pursuant','through','may','want','her',
                    'here','very','some','all','time','years',
                    'report','support','bill','committee','act',
                    'program','office','legislation','speaker','h.r.',
                    'need','should','first','get','b','amendment',
                    'ordered','percent','chairman','vote','think',
                    'u.s.','know','into','important','after',
                    'secretary','title','general','good','people',
                    'states','united','congress','american','federal'
                    'national','country','resolution','law',
                    'government','proposed', '8']

"""words_by_month is my function to simplify the process of gathering the
phrase data, pulling what I want from it, and filtering/formatting it. The 
month parameter must be a string in the same format as the main sunlight
function, e.g., "201501" for January 2015.The 
only_relevant words parameter filters out all words contained within the list
passed to the orw_list parameter if set to True. The default value, False, will
return the full list of words that sunlight.capitolwords.phrases would 
ordinarily give you. phrase_size is the same as the n parameter in the 
sunlight function, i.e. an integer from 1-5 for the length of the phrases you
would like to search for.

words_by day does the same thing, but returns the most frequently used words
for a specified day as opposed to a whole month. The format for the day 
parameter is "2015-01-01" for January 1, 2015
"""

def words_by_month(month, only_relevant_words = False,
                   orw_list = irrelevant_words, 
                   phrase_size = 1):
    wordlist = sunlight.capitolwords.phrases(entity_type = 'month',
                                         entity_value = month,
                                         n = phrase_size,
                                         sort = 'count desc')
    words = []
    if only_relevant_words == False:
        for item in wordlist:
            words.append(item['ngram'].encode("utf-8")) 
    else:
        for item in wordlist:
            if item['ngram'] not in orw_list:
                words.append(item['ngram'].encode("utf-8")) 
    return words                
    
def words_by_day(day, only_relevant_words = False,
                   orw_list = irrelevant_words, 
                   phrase_size = 1):
    wordlist = sunlight.capitolwords.phrases(entity_type = 'day',
                                         entity_value = day,
                                         n = phrase_size,
                                         sort = 'count desc')
    words = []
    if only_relevant_words == False:
        for item in wordlist:
            words.append(item['ngram'].encode("utf-8")) 
    else:
        for item in wordlist:
            if item['ngram'] not in orw_list:
                words.append(item['ngram'].encode("utf-8")) 
    return words  

"""Below are the function calls to get the 
frequent words lists for the respective months."""
   

january = words_by_month('201501', True, irrelevant_words)
february = words_by_month('201502', True, irrelevant_words)
march = words_by_month('201503', True, irrelevant_words)
april = words_by_month('201504', True, irrelevant_words)
may = words_by_month('201505', True, irrelevant_words)
june = words_by_month('201506', True, irrelevant_words)
july = words_by_month('201507', True, irrelevant_words)
august = words_by_month('201508', True, irrelevant_words)
september = words_by_month('201509', True, irrelevant_words)
october = words_by_month('201510', True, irrelevant_words)

#create a list of the top word lists for each month
top_words_2015 = [january, february, march, april,
                       may, june, july, august, 
                       september, october]

"""The following section is code to take the list of data from the words_by_
function and write it to a basket file so that it can be read by 
Orange.data.Table"""

"""turn each list within the bigger into a single string, to facilitate 
writing each month's list to its own line in the proper format, and create a
new list of these strings"""
top_words = []
for item in top_words_2015:
    top_words.append(", ".join(item))
    
    
"""this turns frequent words lists into a .basket file, a format used by 
Orange for association rules development. Creates Phrases_2015.basket if the 
file does not exist in the working directory, otherwise overwrites the file"""
basket_file = open('Phrases_2015.basket','w+')
basket_file.write("\n".join(top_words))
basket_file.close()

"""A function included in case the counts for each individual word are required"""
def counts_by_month(month, only_relevant_words = False,
                    orw_list = irrelevant_words,
                    phrase_size = 1):
    countlist = sunlight.capitolwords.phrases(entity_type = 'month',
                                         entity_value = month,
                                         n = phrase_size,
                                         sort = 'count desc')
    counts = []
    if only_relevant_words == False:
        for item in countlist:
            counts.append(item['count'])
    else:
        for item in countlist:
            if item['ngram'] not in orw_list:
                  counts.append(item['count'])
    return counts
    
  """unused function to be used when analyzing most frequently used words by 
  legislator, instead of by month, across all legislators"""
  def words_by_legislator(legislator_id,
                          start,
                          end,
                          only_relevant_words = False,
                          orw_list = irrelevant_words,
                          phrase_size = 1):
      wordlist = sunlight.capitolwords.phrases(entity_type = 'legislator',
                                               entity_value = legislator_id,
                                               start_date = start,
                                               end_date = end,
                                               n = phrase_size,
                                               sort = 'count desc')
      words[]
      if only_relevant_words == False:
          for item in wordlist:
              words.append(item['ngram'].encode("utf-8"))
      else:
          for item in wordlist:
            if item['ngram'] not in orw_list:
                words.append(item['ngram'].encode("utf-8"))
      return words
      
  """this is an example of how to create a dictionary of word counts, 
  using the words themselves as the keys"""
  january_counts = counts_by_month('201501',True, irrelevant_words)
  january_zipped = dict(zip(january, january_counts))
  
  """This prints out a formatted list of words with associated frequency counts"""
  
  """the length of the longest word is the minimum number of spaces the count
  will be right-aligned by when printed"""
  longest_word = max(len(word) for word in january)
  counts_ex = open('counts.txt','w+')
  for i in range(0,len*january)):
    """formatting is the number of additional spaces necessary to keep the
    counts aligned, based on the length of the current word"""
    formatting = longest_word - len(january[i])
    counts_ex.write(january[i])
    """In Python 2, a * after a % in a string allows a formatting variable to
    be passed along with the variable it is formatting, as opposed to
    specifying the value within the string, e.g., "%10s \n"""
    counts_ex.write("%*s /n" % ((longest_word+formatting),january_counts[i]))
  counts_ex.close()
  
              
