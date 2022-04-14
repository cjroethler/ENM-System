int num_Measure = 1000; //Number of measurements we will want to take to average out
int pinSignal = A0;  //Pin that our sound sensor is connected to
long soundValue; //Input value from our reading
long sum = 0; //Sum of the number of measurements
long level = 0; //Average decibel level value
long aRef = 15; //Going to be our reference value for noise reading, this will be used to calculate the decibel level
long dbValue = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode (pinSignal, INPUT); //Setting up our pin as an input pin
  Serial.begin(9600);
}

void loop() {

  //128 signal readings
  for ( int i = 0 ; i <num_Measure; i ++)
  {
    //read in our value of the signal and then sum it over the 128 readings
    soundValue = analogRead(pinSignal);
    sum = sum + soundValue;
  }

  level = sum/num_Measure; //Average out our value

  //We are now going to use this formula which will calculate the change in decibel value from our reference value, and then we will at a known decibel value at our reference value
  dbValue = (20 * log10(level/aRef)) + 51;

  //Print out our level to the serial monitor
  Serial.print("Decibel Level = ");
  //Serial.println(level);
  Serial.println(dbValue);
  
  //reset our sum 
  sum = 0;
  delay(2000);
  }
  
