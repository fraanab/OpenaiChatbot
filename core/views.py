from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

load_dotenv()
api_key = os.getenv('OPENAI_KEY', None)

@csrf_exempt
def main(request):
	return render(request, 'main.html')

@csrf_exempt
def chatbot(request):
	chatbot_res = None
	if api_key is not None and request.method == 'POST':
		
		openai.api_key = api_key
		user_input = request.POST.get('user_input') # input with name: user_input 
		# prompt = user_input
		prompt = f'Your name is now David, your job is to answer any following question: {user_input}.'

		response = openai.Completion.create(
			# model = 'text-babbage-001',
			model = 'text-davinci-003',
			prompt = prompt,
			max_tokens = 256,
			# stop = '.',
			temperature = 0.5,
		)
		
		chatbot_res = response['choices'][0]['text']
		print(chatbot_res)
	return JsonResponse({'response':chatbot_res})