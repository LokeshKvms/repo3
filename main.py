def function_cicd(request):
    request_json = request.get_json(silent=True)

    if request.args.get('message'):
        return request.args.get('message')

    if request_json and 'message' in request_json:
        return request_json['message']

    # fallback: raw body
    data = request.data.decode('utf-8')
    if data:
        return data

    return 'Function - 1 with V1.0'