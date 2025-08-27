/*Janus Avionics Task2
Name: Aishani Kapoor
Id no. 2025A3RM2259H */


const int ledred= 4;
const int ledgreen= 2;
const int ledyellow= 3;
const int forceSensor= A1;
const int buzzer = 5;
int begin= 0;
  
void setup()
{
  pinMode(ledred, OUTPUT);
  pinMode(ledgreen, OUTPUT);
  pinMode(ledyellow, OUTPUT);
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
  
}

void loop()
  
{
  
  int total=0;
  int sample= 10;
  int i=0;
  for (i = 0; i < sample; i++) {
    total = total + analogRead(forceSensor);
    delay(4);
  }{
   

int avg = total/10;
  
    
 if (avg > begin + 5)
{
    digitalWrite(ledgreen, HIGH);
    digitalWrite(ledred, LOW);
    digitalWrite(ledyellow, LOW);
  }

 else if (avg < begin - 5) {     
    digitalWrite(ledgreen, LOW);
    digitalWrite(ledred, HIGH);
    digitalWrite(ledyellow, LOW);
 }

else{
    digitalWrite(ledred, LOW);
    digitalWrite(ledgreen, LOW);
    digitalWrite(ledyellow, HIGH);
}

 if (avg > 890) 
   tone(buzzer, 1000);
  else noTone(buzzer);
    
    Serial.println(avg);
    begin = total;
    delay(200);
}
}

