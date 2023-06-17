#include "braille.h"

int dataPin = 2; // DATA 핀번호
int latchPin= 3; // LATCH 핀번호
int clockPin = 4; // CLOCK 핀번호
int no_module = 3; // 점자 출력기 연결 개수

braille bra(dataPin, latchPin, clockPin, no_module);

void setup() 
{
  bra.begin(); 
}

void loop() 
{
  for ( int i = 0; i < no_module; i++)
  {
    for ( int j = 0; j < 6; j++)
    {
      bra.on(i, j);
      bra.refresh();
      delay(1000);
      bra.off(i, j);
      bra.refresh();
    }
  }
}
