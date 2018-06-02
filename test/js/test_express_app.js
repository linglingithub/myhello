// http://www.zhufengpeixun.cn/docs/html/node%E8%BF%9B%E9%98%B6/Express.html

// 当请求到来的时候执行app,这是会对数组里的配置项一次匹配，匹配上的执行，匹配不上不执行
var app = function(req, res) {
    var i = 0;  //定义一个变量每次执行next后加一
    //每执行一次next,会取出一个中间件函数执行，并且把next传进去
    function next() {
        console.log("inside app.next >>>>")
        var fn = app.routes[i++];
        if (fn) {
            fn (req, res, next);
        }
        console.log("endding app.next <<<")
    }
    next();
}

// array for middleware functions
app.routes = [];

//配置函数， 作用是给（存放中间件函数的数组）添加函数
app.use = function(fn) {
    // add the parapmeter fn to array
    app.routes.push(fn);
}

// ------------------------------------------------
app.use(function(req, res, next) {
    console.log("1----->");
    console.log(req.url);
    next();  //if comment out this line, middleware 2 will not be executed.
    console.log("1<-----");
});

app.use(function(req, res, next) {
    console.log("2----->");
    res.end('ok');
    next();
    console.log("2<-----");

});

// -------------------------------------------------
var http = require('http');
var server = http.createServer(app);
server.listen(9090);