int r[20]={1,0,1,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0};
int ra[20]={0,1,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,1,0};
int i=20,j;
void setup() {
DDRD=DDRD | B11111100; // to set 2,3,4,5,6,7 pins as output pins
}
void loop(){
for(j=0;j<i;j++){
//assigning values to output pins
PORTD = (r[j]<<PD7)|(ra[j]<<PD6)|(r[j]<<PD5)|(ra[j]<<PD4)|(r[j]<<PD3)|(ra[j]<<PD2);
asm("nop\n nop\n nop\n nop\n nop\n nop\n "); //nop statements used for delay
//asm("nop\n nop\n nop\n nop\n nop\n nop\n ");
}
}
