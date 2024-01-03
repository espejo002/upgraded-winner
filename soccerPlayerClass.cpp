#include <iostream>
using namespace std;

class Player {
      public:
             string name;
             int age;
             string nationality;
             string club;
             int height;
             int clubShirtNumber;
             int nationShirtNumber;
             char dominantFoot;
             Player(string Name, int Age, string Nationality, string Club, int Height, int CSN, int NSN, char DominantFoot) {
                   name = Name;
                   setRules(Age);
                   nationality = Nationality;
                   club = Club;
                   height = Height;



             void ageRules(int aAge) {
                   if(Age >= 15 && Age <= 45) {
                         age = Age;
                   } else {
                         cout << "The age is not valid." << endl;
                         cout << "It must be between 15 and 45" << endl;
                   }
             }
             };

}
