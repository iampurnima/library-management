# API DOCUMENTATION
- /getAllBooks
    GET, No parameter, returns all info about book as a JSON/ dictionary
- /createBook
    POST, parameter (id, title, authorName, genre, aisle, ISBN, numberOfBooks), returns message(success/ fail)
- /getBookByID/id
    GET, parameter (id), returns all info about the book as a JSON
- /updateBook/id
    POST, parameter(id, updatedTitle, updatedAuthorName, updatedGenre, updatedAisle, updatedISBN, updatedNumberOfBooks), returns message(success/ fail) as a JSON
- /deleteBook
    POST, parameter (id), returns message (success/ fail) as JSON 

- /getAllMembers (- id, firstName, lastName, dob, memberSince, fee, memberExpiry)
     get
   - return name of all members
- /createMembers (name ,age, id ,fee ,membersince,memberExpiry)
    post
- /getMemberById/id
   get
- /updateMember/id
   post
- /deleteMember
   post

- /getAllTransaction 
- /createTransaction 
- /getTransactionById/id 
- /updateTransaction/id 
- /deleteTransaction