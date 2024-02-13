var http = require('http')

var server = http.createServer(function(request, response) {
    if (request.url == '/hello'){
        response.writeHead(200, {'Content-Type': 'text/html'})
        response.write('<html><body><h1>Welcome</h1></body></html>')
        response.end()
    }

    if (request.url == '/greet'){
        response.writeHead(200, {'Content-Type': 'text/html'})
        response.write('<html><body><h1>Good Afternoon</h1></body></html>')
        response.end()
    }

    if (request.url == '/message'){
        response.writeHead(200, {'Content-Type': 'text/html'})
        response.write('<html><body><h1>How are you?</h1></body></html>')
        response.end()
    }
})

server.listen(5500)
console.log('Server Started with Port Number 5500')