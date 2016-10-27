# -*- coding: utf-8 -*-
#import sae

'''def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['作为张威的朋友，你一定很幸福吧']

application = sae.create_wsgi_app(app)'''

def application(environ, start_response):
    start_response('800 OK', [('Content-Type', 'text/html')])
    return '<h1>\n\n          作为张威的朋友，你一定很幸福吧!</h1>'