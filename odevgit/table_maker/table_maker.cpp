#include <iostream>
#include <fstream>
#include <string>

#include <sstream>

using namespace std;









string* process_line(string line){
    string * data=new string[6];
    stringstream row(line);

    for(int i=0;i<6;i++){
        getline(row,data[i],';');
    }
    return data;
} 

int main(void){
    fstream fin,fout;
    string line;
    fin.open("EducationAndEnviron_Data.csv",ios::in);
    fout.open("my_table2.csv", ios::out);
    string table[5][8];
    string title="ID;CountryName;CountryCode;CleanFuels;ElectricityRural;ElectricityUrban;SchoolEnrollment;Date";
    fout << title << endl;


    table[0][1]="Brazil";
    table[1][1]="China";
    table[2][1]="India";
    table[3][1]="Russian Federation";
    table[4][1]="South Africa";
    
    table[0][2]="BRA";
    table[1][2]="CHN";
    table[2][2]="IND";
    table[3][2]="RUS";
    table[4][2]="ZAF";
    getline(fin,line);
    int id=1;
    while(!fin.eof()){
        string * data;
        getline(fin,line);
        data=process_line(line);
        if(data[0]=="Access to clean fuels and technologies for cooking (% of population)"){
            table[0][3]=data[5]; //value
            table[0][7]=data[4]; //date
            delete [] data;
            
            for(int i=1;i<=4;i++){
                getline(fin,line);
                data=process_line(line);
                table[i][3]=data[5]; //value
                table[i][7]=data[4]; //date
                delete [] data;
            }

        }
        else if(data[0]=="Access to electricity, rural (% of rural population)"){
            table[0][4]=data[5]; //value
            table[0][7]=data[4]; //date
            
            for(int i=1;i<=4;i++){
                getline(fin,line);
                data=process_line(line);
                table[i][4]=data[5]; //value
                table[i][7]=data[4]; //date
                delete [] data;
            }

        }

        else if(data[0]=="Access to electricity, urban (% of urban population)"){
            table[0][5]=data[5]; //value
            table[0][7]=data[4]; //date
            
            for(int i=1;i<=4;i++){
                getline(fin,line);
                data=process_line(line);
                table[i][5]=data[5]; //value
                table[i][7]=data[4]; //date
                delete [] data;
            }

        }
    
        else if(data[0]=="School enrollment, primary (% gross)"){
            table[0][6]=data[5]; //value
            table[0][7]=data[4]; //date
            
            for(int i=1;i<=4;i++){
                getline(fin,line);
                data=process_line(line);
                table[i][6]=data[5]; //value
                table[i][7]=data[4]; //date
                delete [] data;
            }
            

        }

        else if(data[0]=="" && line!=""){
            delete [] data;
            for(int i=0;i<5;i++){
                table[i][0]=to_string(id);
                fout << table[i][0] << ";" << table[i][1] << ";" << 
                table[i][2] << ";" << table[i][3] << ";" << 
                table[i][4] << ";" << table[i][5] << ";" <<
                table[i][6] << ";" << table[i][7] << ";" << endl;
                id++;
            }
            getline(fin,line);
            getline(fin,line);
            getline(fin,line);
            getline(fin,line);

        }





    }

    

}












/*
.: ⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
*/


