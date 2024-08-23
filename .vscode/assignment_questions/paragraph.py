paragraph='''The rapid advancement of technology has revolutionized the
 way we live and work. With the rise of artificial intelligence, machine learning,
 and the Internet of Things (IoT), we are witnessing a seismic shift in the tech landscape.'''

with open('paragraph.txt','w') as file:
    file.write(paragraph)
    file.close()
    
def read_file():
    with open('paragraph.txt','r') as file:
     return file.read()
           




     
