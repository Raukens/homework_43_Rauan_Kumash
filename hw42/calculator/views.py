from django.shortcuts import render


def calculate(request):
    if request.method == 'POST':
        if request.POST['operation_type'] == 'add':
            result = float(request.POST['first_number']) + float(request.POST['second_number'])
            operand = '+'
        elif request.POST['operation_type'] == 'subtract':
            result = float(request.POST['first_number']) - float(request.POST['second_number'])
            operand = '-'
        elif request.POST['operation_type'] == 'multiple':
            result = float(request.POST['first_number']) * float(request.POST['second_number'])
            operand = '*'
        else:
            result = float(request.POST['first_number']) / float(request.POST['second_number'])
            operand = '/'
        if '.0' in str(result):
            result = str(result).replace('.0', '')
        context = {'result': result, 'operand': operand, 'result_text': 'Result: ', 'equal': ' = ',
                   'first_number': request.POST['first_number'],
                   'second_number': request.POST['second_number']}
        return render(request, 'calculate.html', context)
    else:
        return render(request, 'calculate.html')