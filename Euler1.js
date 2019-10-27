var total = 0;

for(var count = 0; count < 1000; count++){
  if(count % 3 == 0){
    total += count;
  } else if(count % 5 == 0){
    total += count;
  }
}
console.log(total);
