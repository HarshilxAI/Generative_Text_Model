import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class text_writer {

    // Simulate generated text (placeholder AI)
    public static String generateText(String prompt) {
        String[] responses = {
            "AI will continue to shape the future of industries and education.",
            "The topic requires a deeper understanding of human and machine collaboration.",
            "This is a widely discussed area in modern research.",
            "There are ethical and technological implications to consider.",
            "Such advancements will open new doors in the coming years."
        };

        int index = (int) (Math.random() * responses.length);
        return prompt + " — " + responses[index];
    }

    // Save the generated text to a file
    public static void saveToFile(String prompt, String generatedText) {
        try {
            FileWriter writer = new FileWriter("output_java.txt");
            writer.write("Prompt: " + prompt + "\n\n");
            writer.write("Generated Text:\n" + generatedText);
            writer.close();
            System.out.println("\n✅ Output saved to output_java.txt");
        } catch (IOException e) {
            System.out.println("❌ Error writing to file.");
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("📄 Java Text Writer (AI Output Simulator)");
        System.out.print("Enter a prompt: ");
        String prompt = scanner.nextLine();

        String output = generateText(prompt);
        System.out.println("\n🔽 Generated Output:\n" + output);

        saveToFile(prompt, output);
    }
}
