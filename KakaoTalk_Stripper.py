import random
import re

#making list of gender neutral names in Korean
def name_to_list():
    a = []
    file = open('names.txt','rt', encoding='UTF8')
    my_list = [line.strip() for line in file]
    str_list = list(filter(None, my_list))
    print(str_list)
    name_list = []
    for item in str_list:
        print(item)
        hangul_name = item[:2]
        print(hangul_name)
        name_list.append(hangul_name)
    print(name_list)

#anonymous name generator
def anonymous_name(name):
    anonymous_name_list = ['A', 'B', 'C', 'D', 'E']
    index = random.randint(0, len(anonymous_name_list) - 1)
    random_name = anonymous_name_list[index]
    #print(random_name)
    name = random_name
    return name

#this separates lines and create list out of it
def line_to_list():
    a = []
    file = open('input.txt','rt', encoding='UTF8')
    my_list = [line.strip() for line in file]
    str_list = list(filter(None, my_list))
    print(str_list)

#this simply writes input text on the file on local computer
def file_writer(text):
    with open("input.txt", "wt", encoding='UTF8') as text_file:
        text_file.write(text)


#This creates conversation of "anonymous person : conversation"
def anonymous_stripper():
    a = []
    name_list = []
    anonymous_list = []
    file = open('input.txt','rt', encoding='UTF8')
    my_list = [line.strip() for line in file] #print(my_list)
    str_list = list(filter(None, my_list)) #print(str_list)
    #print(str_list)
    #separating KakaoTalk list according to ']'
    for sentence in str_list:
        separated_list = sentence.split(']', 3)
        #print(separated_list)
        name_list.append(separated_list[0])
    #creating anonymous list
    participant_list = list(set(name_list))
    print(participant_list) #This is real name so far
    for participant in participant_list:
        #print(participant)
        anonymous_list.append(anonymous_name(participant)) #print(anonymous_list) #changing into anonymous list
    #print(anonymous_list)
    #print(str_list)
    for sentence in str_list:
        if sentence[0] == "[":
            separated_list = sentence.split(']', 3)
            anonymous_index_no = participant_list.index(separated_list[0]) #setting anonymous index number based on separated list
            #print(separated_list)
            name = anonymous_list[anonymous_index_no]
            stripped_text = separated_list[2][1:]
            a.append(name + ":" + stripped_text + '\n')
        else:
            text = sentence
            a.append(text + '\n')
    file = open('output.txt', 'wt', encoding='UTF8')
    print(a) #a is list of "anonymous_name : conversation\n"
    file.writelines(a) #writing each lines in a file
    file.close()

def real_name_stripper():
    a = []
    name_list = []
    real_name_list = []
    file = open('input.txt','rt', encoding='UTF8')
    my_list = [line.strip() for line in file] #print(my_list)
    str_list = list(filter(None, my_list)) #print(str_list)
    #print(str_list)
    #separating KakaoTalk list according to ']'
    for sentence in str_list:
        separated_list = sentence.split(']', 3)
        #print(separated_list)
        name_list.append(separated_list[0])
    #creating real name list
    participant_list = list(set(name_list))
    print(participant_list) #This is real name so far
    for participant in participant_list:
        #print(participant)
        text = re.compile('[^ a-zA-Zㄱ-ㅣ가-힣0-9]+')
        result = text.sub('', participant)
        print(result)
        real_name_list.append(result)
    print(real_name_list)
    #print(str_list)
    for sentence in str_list:
        if sentence[0] == "[":
            separated_list = sentence.split(']', 3)
            real_index_no = participant_list.index(separated_list[0]) #setting real index number based on separated list
            #print(separated_list)
            name = real_name_list[real_index_no]
            stripped_text = separated_list[2][1:]
            a.append(name + ": " + stripped_text + '\n')
        else:
            text = sentence
            a.append(text + '\n')
    file = open('output.txt', 'wt', encoding='UTF8')
    print(a) #a is list of "real_name : conversation\n"
    file.writelines(a) #writing each lines in a file
    file.close()


#This only gets the text of input
def text_stripper():
    a = []
    name_list = []
    file = open('input.txt','rt', encoding='UTF8')
    my_list = [line.strip() for line in file] #print(my_list)
    str_list = list(filter(None, my_list)) #print(str_list)
    #print(str_list)
    #separating KakaoTalk list according to ']'
    for sentence in str_list:
        separated_list = sentence.split(']', 3)
        #print(separated_list)
        name_list.append(separated_list[0])
    #print(anonymous_list)
    #print(str_list)
    for sentence in str_list:
        if sentence[0] == "[":
            separated_list = sentence.split(']', 3)
            #print(separated_list)
            stripped_text = separated_list[2][1:]
            a.append(stripped_text + '\n')
        else:
            text = sentence
            a.append(text + '\n')
    file = open('output.txt', 'wt', encoding='UTF8')
    print(a) #a is list of "anonymous_name : conversation\n"
    file.writelines(a) #writing each lines in a file
    file.close()

#write file -> strip
def kakao_stripper(text):
    file_writer(text)
    anonymous_stripper()

