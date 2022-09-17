int r[161];
int n=100;
int i,j;
void setup(){
DDRD=DDRD | B10000000;
Serial.begin(9600);
}
void loop(){
while(i!=n)
if(Serial.available()){ //From RPi to Arduino
r[i]=Serial.read()-48;
//Serial.println(r[i]);
i=i+1;
}
}
if(i==n){
for(j=0;j<i;j++){
PORTD = (r[j]<<PD7);
asm("nop\n nop\n nop\n ");
}
}
