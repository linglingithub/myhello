//http://davidshariff.com/blog/what-is-the-execution-context-in-javascript/
// ​
(function() {

    console.log("foo: ", typeof foo); // function pointer
    console.log("bar and bar2: ", typeof bar, typeof bar2, typeof bar3); // undefined, undefined, function

    var foo = 'hello';
    var bar2 = 1;
    var bar = function() {
            return 'world';
        };
    function bar3 () {};

    function foo() {
        return 'hello';
    }


}());