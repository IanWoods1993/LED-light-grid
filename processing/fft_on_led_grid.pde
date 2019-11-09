import processing.sound.*;
OPC opc;
FFT fft;
AudioIn in;

int spacing;
int bands = 8;
float[] spectrum = new float[bands];
void setup()
{
  // Start of LED Screen setup
  size(64, 64);
  // Connect to the local instance of fcserver. You can change this line to connect to another computer's fcserver
  opc = new OPC(this, "127.0.0.1", 7890);  

  spacing = height / 8;
  opc.ledGrid8x8(0, width/2, height/2, spacing, 0, true);
  
  // Make the status LED quiet
  opc.setStatusLed(false);
  colorMode(RGB, 100);
  // End of LED Screen setup
  
  // Start of FFT setup
  // Create an Input stream which is routed into the Amplitude analyzer
  fft = new FFT(this, bands);
  in = new AudioIn(this, 0);
  
  // start the Audio Input
  in.start();
  
  // patch the AudioIn
  fft.input(in);
  // End of FFT setup
}

void draw() {
  loadPixels();
  fft.analyze(spectrum);

  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      pixels[x + height * y] = color(0, 0, 0);
    }
  }
  
  for(int i = 0; i < bands; i++){
    println("(x1, y1) = (" + i + ", " + height + "), (x2, y2) = (" + i + ", " + (height - spectrum[i]*height*5) + ")");
    //line( i, height, i, height - spectrum[i]*height*5 );
    drawPixelLine(i, height, i, height - spectrum[i]*height*5, 1);
  }
  
  updatePixels();
}

void drawPixelLine(double x1, double y1, double x2, double y2, float thickness) {
  if (x1 == x2 && y1 == y2)
    return;
  if (x1 > x2 || y1 > y2) {  // point 2 is to the left of, or above, point 1
    double tmpX = x2;
    double tmpY = y2;
    x2 = x1;
    y2 = y1;
    x1 = tmpX;
    y1 = tmpY;
  }
  double rise = y2 - y1;
  double run = x2 - x1;
  double denom = Math.sqrt(Math.pow(rise, 2) + Math.pow(run, 2));

  double currX = x1, currY = y1; 
  boolean outOfXBound = false, outOfYBound = false;
  while(true) {
    currX = currX + run / denom;
    currY = currY + rise / denom;
    outOfXBound = currX >= x2 || currX > width - 1;
    outOfYBound = currY >= y2 || currY > height - 1;

    // long addr = currX + height * currY;
    if (outOfXBound && outOfYBound) {
      break;
    }
    
    for (int t = 0; t < thickness; t++) {
      // x and yThickness are the current locations + the thickness on a normal (perpendicular) line
      double xThickness = currX - ((run / denom) * t);
      double yThickness = currY + ((rise / denom) * t);
      
      setPixel((int) Math.round(xThickness), (int) Math.round(yThickness), color(25, 100, 100));
      
      xThickness = currX + ((run / denom) * t);
      yThickness = currY + ((rise / denom) * t);

      setPixel(quantize(xThickness), (int) Math.round(yThickness), color(25, 100, 100));
    }
    // TODO I had to do + spacing / 2 here because the LEDs don't start at 0,0, they start at spacing/2, spacing/2
    setPixel(quantize(currX) + (spacing / 2), (int) Math.round(currY), color(25, 100, 100));
  }
}

int quantize(double value) {
  return (int) Math.round(value / spacing) * spacing;
}

void setPixel(int xPos, int yPos, color c) {
  xPos = Math.min(width - 1, xPos);
  xPos = Math.max(1, xPos);
  yPos = Math.min(height - 1, yPos);
  yPos = Math.max(1, yPos);
  pixels[xPos + height * yPos] = c;
}
