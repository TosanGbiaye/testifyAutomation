//Add a toggleReadingStatus to your books object.This method should update the value of the 
//reading property of your book object. log the reading property to the console to confirm
// the new status.
const books = {
    title:'The Wives Revolt',
    description:'A True life story of some wives pushed to the wall by their husband',
    numberOfPages:203,
    author:'Deborah Agbakogun',
    reading: true,
    //Task 13 my personal library 2
    toggleReadingStatus:function(){
        if(books.reading===true){
            books.reading = false
        }else{
            books.reading = true
        }
    }
}
books.toggleReadingStatus()
console.log(books.reading)
