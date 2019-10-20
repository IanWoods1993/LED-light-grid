import java.lang.Math;

public class Interpolation {
  public static int height = 8;
  public static int width = 8;
  public static void main(String args[]) {
    drawPixelLine(1, 1, 4, 5);
  }

  public static void drawPixelLine(int x1, int y1, int x2, double y2) {
    if (x1 > x2) {  // point 2 is to the left of point 1
      int tmpX = x2;
      double tmpY = y2;
      x2 = x1;
      y2 = y1;
      x1 = tmpX;
      y2 = tmpY;
    }
    double rise = y2 - y1;
    double run = x2 - x1;
    double denom = Math.sqrt(Math.pow(rise, 2) + Math.pow(run, 2));
    System.out.println("rise = " + rise);
    System.out.println("run = " + run);
    System.out.println("denom = " + denom);

    double currX = x1, currY = y1; 
    int iterationCounter = 0;
    System.out.printf("(%d, %d), (%d, %f)\n", x1, y1, x2, y2);
    while(true) {
      iterationCounter++;
      System.out.println("On iteration " + iterationCounter + ": " + currX + "," + currY);
      currX = currX + run / denom;
      currY = currY + rise / denom;
      // long addr = currX + height * currY;
      
      if (currX >= x2) {
        System.out.printf("values currX = %f, x2 = %d\n", currX, x2);
        break;
      }
      
      System.out.printf("Setting pixel (%d,%d)\n", Math.round(currX), Math.round(currY));
      // pixels[addr] = color(100, 50, 50);
    }
  }
}
