var jan = 31;
var mar = 31;
var apr = 30;
var may = 31;
var june = 30;
var july = 31;
var sept = 30;
var oct = 31;
var nov = 30;
var dec = 31;

function feb(yr) {
  if(LeapYears.includes(yr)){
    feb = 29;
  }else {
    feb = 28;
  }
}

function leapYearChk(yr) {
  if (yr % 400 === 0) {
    return true;
  }else if (yr % 100 === 0) {
    return false;
  }else if (yr % 4 === 0) {
    return true;
  }else {
    return false;
  }
}

var LeapYears = [];

for (var i = 1900; i < 2001; i++) {
  if (leapYearChk(i)) {
    LeapYears.push(i);
  }
}

function numDays() {
  for (var i = 1901; i < 2001; i++) {
  }
}

console.log(LeapYears);
