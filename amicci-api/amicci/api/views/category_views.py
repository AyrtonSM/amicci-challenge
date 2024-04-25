from django.http import JsonResponse


def get_all_categories(request) -> JsonResponse:
    if request.method != 'GET':
        raise Exception('Method not found exception')

    data = [{
                'id': 1,
                'name': 'Novo Produto',
            },
            {
                'id': 2,
                'name': 'Troca de Fornecedor',
            },
            {
                'id': 3,
                'name': 'Reformulação de Produto',
            }]

    return JsonResponse({'content-response': data})

