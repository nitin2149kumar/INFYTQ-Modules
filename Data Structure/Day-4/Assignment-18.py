#DSA-Assgn-18

def find_unknown_words(text,vocabulary):
    #Remove pass and write your logic here
    l=[]
    status=0
    text_list=text.split(" ")
    for each_text in text_list:
        if each_text not in vocabulary:
            if "." in each_text:
                each_text=each_text.replace(".","")
            l.append(each_text)
            status=1
    if status:
        return set(l)
    else:
        return -1

#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)
