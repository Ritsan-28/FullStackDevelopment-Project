
// voter age checking (if-else condition)
var a = Number(prompt("Enter age : "));
if(a<=18)
    console.log("Eligible for Vote")

//mark check (if else-if else)
var age = Number(prompt("Enter Mark : "));
if(age>0 && age<18){
    console.log("Kid.");
}
else if(age>40 && age<=18){
    console.log("Adult.")
}
else{
    console.log("Aged.");
}
