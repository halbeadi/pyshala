import os
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import anthropic

def ai_tutor(request):
    return render(request, 'ai_tutor/ai_tutor.html')

@csrf_exempt
@csrf_exempt
def ask_ai(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()

            if not user_message:
                return JsonResponse({'error': 'Empty message'}, status=400)

            api_key = settings.ANTHROPIC_API_KEY
            print(f"API KEY: {api_key[:20] if api_key else 'EMPTY'}")

            if not api_key:
                return JsonResponse({'error': 'API key not configured'}, status=500)

            client = anthropic.Anthropic(api_key=api_key)

            message = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                system="""You are Pyshala AI Tutor — a friendly Python tutor.
                Help students learn Python clearly and simply.
                Use short code examples when helpful.""",
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )

            response_text = message.content[0].text
            return JsonResponse({'response': response_text})

        except Exception as e:
            print(f"AI TUTOR ERROR: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Method not allowed'}, status=405)