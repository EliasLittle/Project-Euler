var math = require('mathjs');
var bigInt = require('big-integer');

var str = bigInt(2).pow(1000).toString();
var intArr = str.split("");
var sum = 0;

for(i = 0; i < intArr.length; i++){
  sum += parseInt(intArr[i]);
}

console.log(str);
console.log(sum);
