import subprocess
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def interpreter(request):
    examples = [
        ('hello',     '👋 Hello World',      'Your first Python program'),
        ('variables', '📦 Variables',         'Strings, integers, floats'),
        ('loops',     '🔄 Loops',             'for and while loops'),
        ('functions', '⚙️ Functions',          'Define and call functions'),
        ('lists',     '📋 Lists',             'List operations'),
        ('classes',   '🏗️ Classes & OOP',     'Object oriented Python'),
    ]
    return render(request, 'interpreter/interpreter.html', {'examples': examples})

@csrf_exempt
def run_code(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code = data.get('code', '').strip()

            if not code:
                return JsonResponse({'error': 'No code provided'}, status=400)

            # Security — block dangerous commands
            blocked = ['import os', 'import sys', 'import subprocess',
                      'open(', 'eval(', 'exec(', '__import__',
                      'shutil', 'socket', 'requests']

            for b in blocked:
                if b in code:
                    return JsonResponse({
                        'output': f'Error: "{b}" is not allowed for security reasons.',
                        'error': True
                    })

            # Run code with timeout
            result = subprocess.run(
                ['python3', '-c', code],
                capture_output=True,
                text=True,
                timeout=5
            )

            output = result.stdout or result.stderr or 'No output'
            is_error = bool(result.stderr) and not result.stdout

            return JsonResponse({
                'output': output,
                'error': is_error
            })

        except subprocess.TimeoutExpired:
            return JsonResponse({
                'output': 'Error: Code took too long to run (5 second limit)',
                'error': True
            })
        except Exception as e:
            return JsonResponse({'output': str(e), 'error': True})

    return JsonResponse({'error': 'Method not allowed'}, status=405)
