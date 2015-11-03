class Words(object):

    def __init__(self,name = None,Words = ['Goat','Eagle','Apple','Football','Lady']):
        self.name = name
        self.Words = Words
        

    def add(self):
        self.name = raw_input('add your own words: ')
        self.Words.append(self.name)

    def words(self):    
        self.word = raw_input('A four legged animal? ')
        if self.word != self.Words[0]:
            print("Wrong Answer",'But you may be right but that\'s not what I want')
            self.word = raw_input('A kind of bird? ')
        elif self.word != self.Words[1]:
            print("Wrong Answer",'But you may be right but that\'s not what I want')
            self.word = raw_input('A type of fruit? ')               
        elif self.word != self.Words[2]:
            print("Wrong Answer",'But you may be right but that\'s not what I want')
            self.word = raw_input('A type of sport? ')                    
        elif self.word != self.Words[3]:
            print("Wrong Answer",'But you may be right but that\'s not what I want')
            self.word = raw_input('A gentle woman?' )

        else:
            print' You need to learn some words buddy', 'Try Again'
            run_time()
        
            
        

    def run_time():
        self.start = raw_input('do you want to play guess it? ')
        if self.start == 'yes':
            self.words()
        elif self.start == 'no':
            self.add()

def run():
    name_0 = raw_input('What\'s your name? hommie!  ')
    name = Words(name_0)
    choice = None

    while choice != 'crap':
        print \
              ''' valid Choices (yes,no)
                  This is a guess that word script.
                  A description would be given for
                  a word and your job is to guess the right word
                  '''
        choice = raw_input('choice: ')
        print
        
        if choice == 'yes':
            name.words()
        elif choice == 'no':
            name.add()
        else:
            print ' invalid choice'

run()
