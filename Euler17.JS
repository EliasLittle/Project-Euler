var set1_9 = ['one','two','three','four','five','six','seven','eight','nine'];
var set10_19 = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'];

function charCount(word) {
  if (word.includes("-"||" ")) {
    return word.length - (word.split("-").length - 1) - (word.split(" ").length - 1);
  }else {
    return word.length;
  }
}

function setLength(set) {
  var totLength = 0;
  for (var i = 0; i < set.length; i++) {
    totLength += charCount(set[i]);
  }
  return totLength;
}

//console.log(charCount("one thousand"));

console.log((9*99*10)+(9*7)+(854*9)+(36*100)+854+11);

//1-9 : 36
//10-19 : 70
//20-99 : 10*(6+6+5+5+5+7+6+6)+36*8
//1-99 : 854
//100-199 7+(9*10)+854
//100-999 : (9*99*10)+(9*7)+(854*9)
