//Create a length converter function (Lesson 24-Return Values)
//cm is the symbol for centimeter and inch is the symbol for inches
function lengthConverter(inch){
    //convert to cm and return the eqvivalent cm value
    //conversion rate: 1inch = 2.54cm
    const cm =  inch * 2.54; 
    return cm;

}
const cmValue = lengthConverter(100)
console.log(cmValue)
