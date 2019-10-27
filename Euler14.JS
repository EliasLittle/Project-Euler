var CollatzLeng = []; //set of lengths
var lV = [0,0];


for(var i = 2; i <= 1000000; i++){
  var Collatz = 0; //length of specific term
  var num = i; //specific term
  while (num > 1) {
    if(num % 2 === 0){
      num = num/2;
      Collatz++;
    }else{
      num = 3*num+1;
      Collatz++
    }
  }
  CollatzLeng.push(Collatz);
}

for(var j = 0; j < CollatzLeng.length; j++){
  if(CollatzLeng[j] > lV[0]){
    lV = [CollatzLeng[j], j+2];
    //console.log(lV[0]);
  }
}

console.log("Number of terms, number: " + lV);
