//14.Create a books array. (1) Each element of this array will be a 
//book object.(2)Each object will have the following properties:
//title(string),description(string),numberOfPages(number),
//author(string), reading(boolean).
//3. Use a for-loop to loop through the books array and log all
//books where the reading status is true to the console.
const books = [{
    title:'The Wives Revolt',
    description:'A True life story of some wives pushed to the wall by their husband',
    numberOfPages:203,
    author:'Deborah Agbakogun',
    reading: true
},
{
    title:'The good girl',
    description:'A book about good girls',
    numberOfPages:65,
    author:'Kelvin Meth',
    reading: false
},
{
    title:'The golden boot',
    description:'A book about Ronaldo',
    numberOfPages:109,
    author:'Mecando Green',
    reading: false

},
 {
    title:'Telepati',
    description:'Comic Children book',
    numberOfPages:45,
    author:'Lyn Yang',
    reading: true,
}
];
for(let i = 0; i < books.length; i++){
    if(books[i].reading === true){
        console.log(books[i])
    }
}
