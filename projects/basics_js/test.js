var today=new Date();
var hourNow=today.getHours();
var greeting;
/*var number1, number2, number3;
number3=number2*number1;*/
if (hourNow>18){
    greeting="Good evening";
}
else if(hourNow>12){
    greeting="Good afternoon";
}
else if(hourNow>0){
    greeting="Good morning";
}
else{
    greeting="Welcome";
}

document.write('<h3>'+greeting+/*number3+*/'</h3>') //write