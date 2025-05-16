 #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# HIGA_Strings.py shows some basic lists in python and demonstrates some basic functions
#
# Created by Scott Higa, 2025-05-06
# Last edit: 2025-05-06
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

var1 = "Mr and Mrs Dursley of number four Privet Drive were proud to say that they were perfectly normal thank you very much. They were the last people you would expect to be involved in anything strange or mysterious because they just did not hold with such nonsense. Mr Dursley was the director of a firm called Grunnings which made drills. He was a big beefy man with hardly any neck although he did have a very large mustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck which came in very useful as she spent so much of her time craning over garden fences spying on the neighbors. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere. The Dursleys had everything they wanted but they also had a secret and their greatest fear was that somebody would discover it. They did not think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursleys sister but they had not met for several years. In fact Mrs Dursley pretended she did not have a sister because her sister and her good for nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbors would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son too but they had never even seen him. This boy was another good reason for keeping the Potters away. They did not want Dudley mixing with a child like that. When Mr and Mrs Dursley woke up on the dull gray Tuesday our story starts there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair. None of them noticed a large tawny owl flutter past the window. At half past eight Mr Dursley picked up his briefcase pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed because Dudley was now having a tantrum and throwing his cereal at the walls. Little tyke chortled Mr Dursley as he left the house. He got into his car and backed out of number fours drive. It was on the corner of the street that he noticed the first sign of something peculiar a cat reading a map. For a second Mr Dursley did not realize what he had seen then he jerked his head around to look again. There was a tabby cat standing on the corner."
# Setting the paragraph we are manipulating to a string and assigning it to var1

e_count = var1.count("e")
# setting the variable e_count to the number of times "e" appears in the string var1

print (e_count)
# print the number of times "e" appears in var1

b_count = var1.count("b")
# setting the variable b_count to the number of times "b" appears in the string var1

print (b_count)
# print the number of times "b" appears in var1

index = var1.find("e")
# using the find function to find the first "e" in var1 and setting it to the variable index

print(var1[index + 1 : index + 21])
# After setting an index in var 1, we can print the tuple of the twenty subsequent characters by slicing the index + 1 (first character after the first "e") with the index + 21.

word_count = int(var1.count(" ")) + 1
# Counting the number of spaces in var1, coverting it to an integer and adding 1

print(word_count)
# This will print the number of words in var1

sentence_count = var1.count(".")
# Counting the number of periods in var1. This will give us the same number of sentences

print(sentence_count)
# This will print the number of sentences in var1

sentences = var1.split(". ")
# Splitting var1 into sentences by using periods as an index

shortest_sentence = sorted(sentences, key=len)
# creating a list of all sentences and sorting them by length. The shortest will have the index of 0 while the longest will have the index of 22

print (shortest_sentence[0])
# Printing the 0 index ie. first index of the list we just made ie. the shortest sentence

x = var1.split( )
# spliting var1 into a list by spaces and setting the list to the variable x

y = set(x)
# changing the list into a set so that only unique words are stored

print (len(y))
# printing the number of parts in the set y

capitalize_h_only = var1.replace("h","H")
# Using the replace function to replace all "h" in var1 with "H"

print (capitalize_h_only)
# print the new string

print ("done")

    