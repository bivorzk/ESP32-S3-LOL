#include <windows.h>
#include <iostream>
#include <cstdio>
#include <memory>
#include <string>
#include <fstream>

using namespace std;

bool isPythonRunning(const std::string& processName = "python") {
    std::string cmd = "pgrep -f " + processName;
    FILE* pipe = popen(cmd.c_str(), "r");
    if (!pipe) return false;

    char buffer[128];
    bool found = false;
    if (fgets(buffer, sizeof(buffer), pipe) != NULL) {
        found = true; // got a PID
    }
    pclose(pipe);
    return found;
}

int main() {
    bool running = false;
    if (isPythonRunning("reading_movement.py")) {
        running = true;
        cout << "Running." << endl;
    } else {
        running = false;
        cout << "Not running" << endl;
    }  
 
    int x, y;

    std::ifstream file("src/resource/mouse_coords.txt" , std::ios::in);
    std::string s;
    if (file.is_open()) {
        while (getline(file, s)) { 
            //std::cout << s << std::endl;
            if (GetKeyState(VK_ESCAPE) & 0x8000) {
                break; // EXIT ON ESCAPE KEY
            }

            for (size_t i = 0; i < s.length(); ++i) {
                if (s[i] == ' ') {
                    x = stoi(s.substr(0, i));
                    y = stoi(s.substr(i + 1));
                    Sleep(993);
                    SetCursorPos(x, y);
                    cout << "X: " << x << " Y: " << y << endl;
                    break;
                }
            }

            

        }
        file.close();
        
}

    cout << "Hello, World!" << endl;
    return 0;
    
}