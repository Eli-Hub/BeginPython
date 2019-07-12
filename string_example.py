def find_a (x):
    for item in x:
        if item=='a':
            return True
    return False
print ("Program that returns True if a word has an 'A'\n")
word=input("Enter a word: ")
print(find_a(word))


'''def find_a2(b):
    print (b)
    a=len(b)
    while a <= 10:
        a+=1
        print (b)'''

'''b='orange'
find_a2(b)'''
    
'''name='word'   
ok=name.find('o')
print (ok)'''