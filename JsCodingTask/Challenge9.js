//Return the number of vowels in a string
const alphabets26 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
//let vowels =['a','e','i','o','u']
let vowel1 = alphabets26[0]
let vowel2 = alphabets26[4]
let vowel3 = alphabets26[8]
let vowel4 = alphabets26[14]
let vowel5 = alphabets26[20]
const numberOfVowels = [vowel1 +',' + vowel2 +','+ vowel3+','+ vowel4 +','+ vowel5]
console.log(numberOfVowels)


//Alternativel (A more Accurate solution)
function countVowel(str) {
    let count = 0;
    let vowels = ['a', 'e', 'i', 'o', 'u']
for (var i = 0; i < str.length; i++){
    if(vowels.indexOf(str[i].toLowerCase()) > -1){
        count++;
    }
}
return count;
}
console.log('Number of vowels in this string is ' + countVowel("JavaScript Coding Challenge is fun"));
