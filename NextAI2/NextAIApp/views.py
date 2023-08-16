from django.shortcuts import render
from django.template import Context, Template
from django.shortcuts import render
from django.http import HttpResponse
import openai
openai.api_key = "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"
def hi(request):
    return render(request,"NextApp/index.html")

def chat(request):
    user_input = None
    prompt=''
    def generate_text(prompt):
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        temperature=0.1)
        return response.choices[0].text
    
    if request.method == 'POST':
        user_input = request.POST.get('NextAI1', '')
        
        prompt = user_input
        
        generate_texteds = generate_text(prompt)
       
        context = {'generate_texted': generate_texteds}
        with open('D:/djangoprojects/NextAI2/templates/NextAIApp/back.html',encoding='UTF-8') as file:
            template_content = file.read()
        template = Template(template_content)
        rendered_html = template.render(Context(context))

        return HttpResponse(rendered_html)

    return render(request, 'NextAIApp/index.html')