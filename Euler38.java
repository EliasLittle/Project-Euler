public class Euler38 {
  public static void main(String args[]){
    int largest = 0;
    final int LIMIT = 1000000000;
    for(int i = 1; i < LIMIT/2; i++){
      int num = 1;
      int n = 2;
      boolean run = true;
      while(run){
        long test = concatFunc(i,n);
        if(test>LIMIT){
          run = false;
        }
        else{
          num=(int)test;
          n++;
        }
      }

      if(num>largest && pandigital(num)){
        largest = num;
        System.out.println(largest);
      }
    }
    System.out.println(largest);
  }

  public static long concatFunc(int num, int nVal){
    String result = ""+num;
    for(int j = 2; j <= nVal; j++){
      int addTo = j*num;
      result=""+result+addTo;
    }
    return Long.parseLong(result);
  }

  public static boolean pandigital(int num){
    String val = ""+num;
    if(val.length() < 8 || val.length() > 8){
      return false;
    }
    for (int k = 1; k <= 9; k++) {
      if(!val.contains(""+k)){
        return false;
      }
    }
    return true;
  }

}
