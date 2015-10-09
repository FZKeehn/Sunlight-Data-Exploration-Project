# Sunlight-Data-Exploration-Project
This is a basic data mining project to help display my progress learning Python for Launchcode.

This project is being written in Python (x,y) 2.7.10, with Spyder 2.3.5.2
Libraries used beyond the defaults are sunlight and Orange:
https://python-sunlight.readthedocs.org/en/latest/
http://orange.biolab.si/

The project currently contains five files:

Data_Gathering.py - contains code for pulling the desired data from Sunlight's Capitol Words project through their python-based API. This file includes my API-key for accessing the data, although anyone else should technically use their own key.

Association_Rules.py - this file contains the code for using the .basket file generated in Data_Gathering.py to do association rules mining. Can be used to generate a file of unformatted rules, with support and confidence values for each, or a text file with rules interpreted in sentence format.

Phrases_2015.basket - An example of the file type that Association_Rules.py uses for its analysis. However, instead of actually using this file, it should be generated using Data_Gathering.py instead.

rules_2015.txt - an example of the unformatted association rules output, using data from January 2015 to October 2015.

interpretation.txt - an example of the January 2015 to October 2015 output in sentence format.
