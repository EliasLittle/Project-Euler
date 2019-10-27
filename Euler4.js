var pal = [];
var str = 0;

function reverse(num) {
  return parseInt(num.toString().split('').reverse().join(''));
}

function mult() {
  for(q = 999; q > 99; q--){
    for(i = 999; i > 99; i--){
      str = (q*i);
      if(reverse(str) === str){
        pal.push(str);
        i = 100;
      }
    }
  }
return pal;
}

mult();
var rav = mult();
var lV = 0;

for(j = 0; j < pal.length; j++){
  if(pal[j] > lV){
    lV = pal[j];
  }
}

console.log(lV);
