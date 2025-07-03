#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

// Simulate simple text generation with placeholder phrases
string generateText(string prompt) {
    string responses[] = {
        "This topic highlights the importance of innovation and creativity in today's world.",
        "Many experts believe this will shape the future in surprising ways.",
        "It's a subject that demands more exploration and discussion.",
        "Technology and research are rapidly advancing in this field.",
        "Students and professionals alike are taking great interest in this topic."
    };

    srand(time(0));
    int index = rand() % 5;

    return prompt + " - " + responses[index];
}

int main() {
    string userPrompt;

    cout << "🧠 GPT Demo (C++ Version)" << endl;
    cout << "Enter a topic: ";
    getline(cin, userPrompt);

    string generated = generateText(userPrompt);

    cout << "\n🔽 Generated Response:\n" << generated << endl;

    return 0;
}
