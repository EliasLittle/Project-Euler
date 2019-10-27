var bigInt = require("big-integer");

function factorial(x) {
  if (x === 0) {
    return bigInt(1);
  }
  if (x < 0) {
    console.log("Negative numbers not valid")
  }
  return bigInt(x).times(factorial(x-1));
}

function digitSum(n) {
  var str = n.toString();
  var intArr = str.split("");
  var sum = 0;
  for(i = 0; i < intArr.length; i++){
    sum += parseInt(intArr[i]);
  }
  console.log(sum);
}

digitSum(factorial(100));
