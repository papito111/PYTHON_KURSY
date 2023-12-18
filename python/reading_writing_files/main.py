"""
f = open("C:\\Users\\adria\\Desktop\\programowanie\\python"
         "\\reading_writing_files\\funny.txt","r")
m=0
f_out = open("C:\\Users\\adria\\Desktop\\programowanie\\python"
         "\\reading_writing_files\\funny1.txt","w")
for line in f:
    tokens = line.split(' ')
    #print(str(tokens))
    f_out.write( "wordcount:"+str(len(tokens))+" "+ line)


f.close()
"""

"""
from collections import Counter
f = open("C:\\Users\\adria\\Desktop\\programowanie\\python\\reading_writing_files\\poem.txt","r")
content = f.read()
tokens = content.split(' ')
words_ocurrancy = Counter(tokens)

#print(words_ocurrancy)
most_popular_word = words_ocurrancy.most_common(1) # jak damy 0 to uporzadkowuje rosnąco, jesli damy 1 to wybierze max,2 to dwa najwieksze itd
print(most_popular_word)
f.close()

"""
f = open("C:\\Users\\adria\\Desktop\\programowanie\\python\\reading_writing_files\\stocks.csv","r")
f_out = open("C:\\Users\\adria\\Desktop\\programowanie\\python\\reading_writing_files\\stocks1.csv","r+")
f_out.write("Company name, PE ratio, Pb ratio\n")
next(f)
for line in f:
    tokens = line.split(',')
    stock = tokens[0]
    price = float(tokens[1])
    earnings = float(tokens[2])
    book_value = float(tokens[3])
    pe_ratio = round(price / earnings)
    price_to_book_ratio = round(price/book_value)
    #print(line, price_to_book_ratio, pe_ratio)

    f_out.write(f"{stock},{pe_ratio},{price_to_book_ratio}\n")

f.close()
for m in f_out:
    print(m)
f_out.close()