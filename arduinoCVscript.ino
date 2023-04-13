#include <Wire.h>
#include <Adafruit_MCP4728.h>

#define MCP4728_ADDRESS 0x64  // MCP4728 default address (A0-A2 grounded)

Adafruit_MCP4728 dac;

void setup() {
  Serial.begin(9600);
  while (!Serial) {}

  Wire.begin();
  dac.begin(MCP4728_ADDRESS);
  dac.setChannelValue(MCP4728_CHANNEL_A, 0);
  dac.setChannelValue(MCP4728_CHANNEL_B, 0);
  dac.setChannelValue(MCP4728_CHANNEL_C, 0);
  dac.setChannelValue(MCP4728_CHANNEL_D, 0);
}

void loop() {
  if (Serial.available()) { 
    int channel = Serial.parseInt();
    int voltage = Serial.parseInt();

    if (channel == 1) {dac.setChannelValue(MCP4728_CHANNEL_A, voltage); } 
    else if (channel == 2) {dac.setChannelValue(MCP4728_CHANNEL_B, voltage);}
    else if (channel == 3) {dac.setChannelValue(MCP4728_CHANNEL_C, voltage);} 
    else if (channel == 4) {dac.setChannelValue(MCP4728_CHANNEL_D, voltage);}

  Serial.println("Sent!");
  }
}
