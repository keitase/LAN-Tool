var http = require("http");
var url = require("url");
function start(route)
{
	var portNumber = 8888;
	function httpresponse(request,response)
	{
		var pathname = url.parse(request.url).pathname;
		var _get = url.parse(request.url).query;
		console.log("Request for" + pathname + "received.");
		route(pathname);
		response.writeHead(200,{"Content-Type": "text/plain"});
		response.write("Hello world");
		response.end();
	}
	http.createServer(httpresponse).listen(portNumber);
	console.log("server is up bitches");
}
exports.start = start;