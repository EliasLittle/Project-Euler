//Binomial Coefficient Calculator
var bigInt = require('big-integer');

function calculate(n,k) {
  console.log((factorial(n)/factorial(k))/(factorial(k)));
}

var factorial = function(n) {
    if(n == 0) {
        return 1
    } else {
        return n * factorial(n - 1);
    }
}

calculate(40,20);
