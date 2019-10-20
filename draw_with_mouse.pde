
OPC opc;
void setup()
{
  size(80, 80);
  // Connect to the local instance of fcserver. You can change this line to connect to another computer's fcserver
  opc = new OPC(this, "127.0.0.1", 7890);  

  float spacing = height / 10;
  opc.ledGrid8x8(64, width/2 - spacing * 8, height/2, spacing, 0, true);
  
  // Make the status LED quiet
  opc.setStatusLed(false);
  colorMode(RGB, 100);
}

void draw() {
  loadPixels();
  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      pixels[x + height * y] = color(50, 50, 50);
    }
  }
  
  for (int x = max(0, mouseX - 10); x < min(mouseX, mouseX + 10); x++) {
    for (int y = max(0, mouseY - 10); y < min(mouseY, mouseY + 10); y++) {
      pixels[x + height * y] = color(75, 25, 25);
    }
  }
  
  
  updatePixels();
}
