public class Euler145 {
  public static void main(String[] args) {
    long rev, add;
    int out = 0;
    for (long i = 10; i < 1000000000; i += 2) {
      if (i % 10 == 0) {
        continue;
      }
      rev = reverse(i);
      if (rev % 2 == 0) {
        continue;
      }
      add = rev + i;
      if (allDigitsOdd(add)) {
        out += 2;
      }
    }
    System.out.println(out);
  }

  public static long reverse(long boi) {
    return new Long(new StringBuilder(Long.toString(boi)).reverse().toString());
  }

  public static boolean allDigitsOdd(long boi) {
    while (boi > 0) {
      if (boi % 2 == 0) {
        return false;
      }
      boi /= 10;
    }
    return true;
  }
}
