class Library:

    __book_list=[]

    def entry_book(self,book):
        Library.__book_list.append(book)
        print(f'{book.title} has been added')
    
    def view_book_info(self):
        print(f'Here are all the books and their info')
        for book in Library.__book_list:
            print(book)

    
    def borrow_book(self,curr_id):
        for book in Library.__book_list:
            
            if curr_id==book.book_id:
                if book.availability==True:
                    book.set_availability(False)
                    print(f'{book.title} has been borrowed')
                    return
                else:
                    print (f'{book.title} is already being borrowed')
                    return
        print(f'Invalid Book ID, Try again')        
        
    
    def return_book(self,curr_id):
        for book in Library.__book_list:
            if curr_id==book.book_id:
                if book.availability==False:
                    book.set_availability(True)
                    print(f'{book.title} has be returned')
                    return
                else:
                    print(f'This book already exists')
                    return
        


class Book:
    def __init__(self,id,title,author,availability):
        self.__book_id=id
        self.__title=title
        self.__author=author
        self.__availability=availability
    
    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def availability(self):
        return self.__availability


    def set_availability(self, status):
        self.__availability = status

    
    def __repr__(self):
        return f"Book(ID = {self.__book_id}, Title = '{self.__title}', Author = '{self.__author}', Available = {self.__availability})"

my_library=Library()
GOT=Book('1','Game of Thornes','Sir Maxwell',True)
Bangla=Book('2','Dipu No.2','Jafor',True)
English=Book('3','The Great Gatsby','Sir williams',True)
my_library.entry_book(GOT)
my_library.entry_book(Bangla)
my_library.entry_book(English)

while True:
    print('--------Library Menu----------')
    print('1)View all Books')
    print('2)Borrow Book')
    print('3)Return Book')
    print('4)Exit')
    menu=input('Enter number(1-4): ')
    if menu=='1':
       
        my_library.view_book_info()
    
    elif menu=='2':
       
        mybook=input('Enter the ID of your book: ')
        my_library.borrow_book(mybook)
    
    elif menu=='3':
        
        mybook=input('Enter the ID of your book: ')    
        my_library.return_book(mybook)
    
    else:
        
        break
