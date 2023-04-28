const int thumb_out=2;
const int thumb_in=3;
const int point_out=4;
const int point_in=5;
const int mid_out=6;
const int mid_in=7;
const int ring_out=8;
const int ring_in=9;
const int palm_out=10;
const int palm_in=11;

void setup(){
Serial.begin(9600);
pinMode(thumb_in, INPUT);
pinMode(thumb_out, OUTPUT);
pinMode(point_in, INPUT);
pinMode(point_out, OUTPUT);
pinMode(mid_in, INPUT);
pinMode(mid_out, OUTPUT);
pinMode(ring_in, INPUT);
pinMode(ring_out, OUTPUT);
pinMode(palm_in, INPUT);
pinMode(palm_out, OUTPUT);
}
void loop()
{
long thumb_dur;
long thumb_dis;
long thumb_cm;
long point_dur;
long point_dis;
long point_cm;
long mid_dur;
long mid_dis;
long mid_cm;
long ring_dur;
long ring_dis;
long ring_cm;
long palm_dur;
long palm_dis;
long palm_cm;

digitalWrite(thumb_out,LOW);
delayMicroseconds(2);
digitalWrite(thumb_out,HIGH);
delayMicroseconds(10);
digitalWrite(thumb_out,LOW);
thumb_dur=pulseIn(thumb_in,HIGH);
thumb_cm=microsecondsToCentimeters(thumb_dur);
Serial.print(String(thumb_cm));
Serial.print("\t");

digitalWrite(point_out,LOW);
delayMicroseconds(2);
digitalWrite(point_out,HIGH);
delayMicroseconds(10);
digitalWrite(point_out,LOW);
point_dur=pulseIn(point_in,HIGH);
point_cm=microsecondsToCentimeters(point_dur);
Serial.print(String(point_cm));
Serial.print("\t");

digitalWrite(mid_out,LOW);
delayMicroseconds(2);
digitalWrite(mid_out,HIGH);
delayMicroseconds(10);
digitalWrite(mid_out,LOW);
mid_dur=pulseIn(mid_in,HIGH);
mid_cm=microsecondsToCentimeters(mid_dur);
Serial.print(String(mid_cm));
Serial.print("\t");

digitalWrite(ring_out,LOW);
delayMicroseconds(2);
digitalWrite(ring_out,HIGH);
delayMicroseconds(10);
digitalWrite(ring_out,LOW);
ring_dur=pulseIn(ring_in,HIGH);
ring_cm=microsecondsToCentimeters(ring_dur);
Serial.print(String(ring_cm));
Serial.print("\t");

digitalWrite(palm_out,LOW);
delayMicroseconds(2);
digitalWrite(palm_out,HIGH);
delayMicroseconds(10);
digitalWrite(palm_out,LOW);
palm_dur=pulseIn(palm_in,HIGH);
palm_cm=microsecondsToCentimeters(palm_dur);
Serial.print(String(palm_cm));
Serial.print("\t");

Serial.print("\n");
delay(30);
}
long microsecondsToCentimeters(long microseconds)
{
return microseconds / 29 / 2;
}
