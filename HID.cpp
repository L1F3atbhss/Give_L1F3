#include "USB.h"
#include "USBHIDKeyboard.h"

USBHIDKeyboard Keyboard;

void setup() {
    USB.begin();
    Keyboard.begin();
    delay(5000); // Wait for USB initialization

    // Example: Open Run, type "cmd", and execute commands
    Keyboard.press(KEY_LEFT_GUI);
    Keyboard.press('r');
    Keyboard.releaseAll();
    delay(500);
    
    Keyboard.println("cmd");  // Open Command Prompt
    delay(500);
    
    Keyboard.println("echo BadUSB Activated!");  // Example payload
    delay(500);

    Keyboard.println("exit"); // Close CMD
}

void loop() {
    // Empty loop, script runs only once
}
