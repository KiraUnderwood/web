def application(environment, start_response):
    """
    The main WSGI Application. Doesn't really do anything
    since we're benchmarking the servers, not this code :)
    """

    start_response(
        '200 OK',  # Status
        [('Content-type', 'text/plain'), ('Content-Length', '2')]  # Headers
    )
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    return body
