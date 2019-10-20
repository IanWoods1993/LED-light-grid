import java.lang.Math;

public class Interpolation {
  public static int height = 8;
  public static int width = 8;
  public static void main(String args[]) {
    drawPixelLine(0, 3, 0, 0); // | ^ 
    // drawPixelLine(0, 0, 0, 3); // |v
    // drawPixelLine(4, 5, 1, 1); // <\
    // drawPixelLine(1, 1, 4, 5); // \>
    // drawPixelLine(4, 1, 1, 5); // </
    // drawPixelLine(1, 5, 4, 1);// />
  }

  public static void drawPixelLine(double x1, double y1, double x2, double y2) {
    if (x1 > x2 || y1 > y2) {  // point 2 is to the left of point 1
      System.out.println("Switching points 1 and 2");
      double tmpX = x2;
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
    boolean outOfXBound = false, outOfYBound = false;
    int iterationCounter = 0;
    System.out.printf("(%f, %f), (%f, %f)\n", x1, y1, x2, y2);
    while(true) {
      iterationCounter++;
      System.out.println("On iteration " + iterationCounter + ": " + currX + "," + currY);
      currX = currX + run / denom;
      currY = currY + rise / denom;
      outOfXBound = currX >= x2;
      outOfYBound = currY >= y2;

      // long addr = currX + height * currY;
      if (currX >= x2 && currY >= y2) {
	System.out.println("currX >= x2: " + outOfXBound);
	System.out.println("currY >= y2: " + outOfYBound);
        System.out.printf("values currX = %f, x2 = %f\n", currX, x2);
	System.out.printf("values currY = %f, y2 = %f\n", currY, y2);
        break;
      }
      
      System.out.printf("Setting pixel (%d,%d)\n", Math.round(currX), Math.round(currY));
      // pixels[addr] = color(100, 50, 50);
    }
  }
}
