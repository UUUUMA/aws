'use strict'
const http = require('http');
const port = process.env.PORT || 3000
const server = http.createServer((_, res) => {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
        value: 'Hello World',
    }));
});


console.log('server runnig...');
server.listen(port, '0.0.0.0');

