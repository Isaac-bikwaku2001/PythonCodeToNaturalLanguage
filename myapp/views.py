from django.shortcuts import render
import openai

# Create your views here.
openai.api_key = "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"

def generate_code(request):
    if request.method == "POST":
        python_code = request.POST.get("python_code")
        prompt = (f"Translate this Python code to natural language: {python_code}")
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        natural_language = completions.choices[0].text
        return render(request, "language.html", {'language':natural_language})
    else:
        return render(request, "index.html")