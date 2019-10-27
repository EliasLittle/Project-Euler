var math = require('mathjs');

var set = [];
var sumSqSet = [];

for(i = 0; i < 101; i++){
  set.push(i);
}

function sum(total, num) {
    return total + num;
}

function squareSet(v,w) {
  for(q = 1; q < v.length; q++){
    w.push(math.pow(v[q], 2));
  }
}

squareSet(set, sumSqSet);

var sqSum = math.pow(set.reduce(sum), 2);
var sumSq = sumSqSet.reduce(sum);

console.log(sqSum - sumSq);
