def alerts(request):
    alert = {'status': False,
             'type': '',
             'content': ''}
    
    error_content = ['<strong>Error:</strong> Please complete the form.',
                     '<strong>Error:</strong> Please submit a valid start date and end date range.', '<strong>Error:</strong> Invalid data.']

    success_content = ['<strong>Success!</strong> Transaction recorded successfully']
    
    params = request.GET

    # Test if request has params
    if params:
        print('PARAM')
        alert['status'] = True
        
        # if param == success
        if params.get('s'):
            alert['type'] = 'primary'
            alert['content'] = success_content[int(params.get('s'))]
        # if param == error
        elif params.get('e'):
            alert['type'] = 'danger'
            alert['content'] = error_content[int(params.get('e'))]

        return alert

    # elif request !has params
    elif not params:
        print('NO PARAM')
        return alert