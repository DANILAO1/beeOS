//this program is copyrighted by Danila(DANILAO)
//os isn't finished

#include <iostream>

//namespaces
using namespace std;


//the program itself
int main() {

//strings
    string username;
    string print;
    string choice;
    string settingschoice;
    char run = true;
    //the start
    cout << "welcome to Beeos v1.0beta \ncopyrighted by Danila\n\n\n\n";
    cout << "write your userpass>";
    cin >> username;
    cout << "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
    cout << "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
    cout << "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
    cout << "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
    cout << "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
    cout << "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
    cout << "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
    // the main functions
    while(run){
    cout << "/" << username << ">";
    getline(cin, choice);

    }
    if (choice == "beeOS=version") {
        cout << "BeeOS is currently at version 0.2aplha\n";
    }
    //settings
    if (choice == "open !settings"){
        cout << "/settings/" << username << ">";
        getline(cin, settingschoice);
        // ask system
        if (settingschoice == "system") {
        cout << "beeOS v0.1a. running on terminal...";
        }
    if (choice == "note") {
        
    } 
    }
    //exit function
    if (choice == "exit"){
        exit(0);
    }
    
    if (choice == "start !beeOSa")
    }
    return 0;
}