class Book:
    def __init__(self,id,title,authorName,genre,aisle,ISBN,numberofBooks):
        self.id = id
        self.title = title
        self.authorName = authorName 
        self.genre = genre
        self.aisle = aisle
        self. ISBN = ISBN
        self.numberofBooks = numberofBooks
        
        
    def get_books(self):
        return     
        
        
class member:
    def __init__(self,id,firstname,lastname,dob,membersince,fee,memberExpiry):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.membersince = membersince
        self.fee = fee
        self.memberExpiry=memberExpiry
        
        
        
        
        
class transaction:
    def __init__(self,id,bookName,bookID,memberName,dueDate):
        self.id = id
        self.bookName = bookName
        self.bookID = bookID
        self.memberName = memberName
        self.dueDate = dueDate
      
        
