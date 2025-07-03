from flask import Flask, render_template, request
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Set up Flask app
app = Flask(__name__)

# Text generation function
def generate_text(prompt, max_length=150):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    generated_text = ""
    if request.method == 'POST':
        prompt = request.form['prompt']
        generated_text = generate_text(prompt)
    return render_template('index.html', output=generated_text)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
