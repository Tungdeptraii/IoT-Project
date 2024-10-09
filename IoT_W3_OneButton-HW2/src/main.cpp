#include <Arduino.h>
#include "LED.h"
#include <OneButton.h>

LED led1(LED_PIN1, LED_ACT1);
LED led2(LED_PIN2, LED_ACT2);

void btnPush();
void doubleClick();
void btnHold();
OneButton button(BTN_PIN, !BTN_ACT);

bool flag = true;

void setup()
{
    led1.off();
    led2.off();
    button.attachClick(btnPush);
    button.attachDoubleClick(doubleClick);
    button.attachLongPressStart(btnHold);
}

void loop()
{
    led1.loop();
    led2.loop();
    button.tick();
}

void btnPush()
{
    if(flag) led1.flip(); 
    else led2.flip();
}

void doubleClick()
{
    flag = !flag;
}

void btnHold()
{
    if(flag) led1.blink(200);
    else led2.blink(200);
}