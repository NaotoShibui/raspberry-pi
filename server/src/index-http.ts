import { createServer } from 'http';

const server = createServer((request, response) => {
  response.writeHead(200,{'Content-Type':'text/html;charset=utf-8'});
  response.end('hello,world');
})

server.listen(3000);