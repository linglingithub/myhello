/**
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this
 *
 * In arrow functions, this retains the value of the enclosing lexical context's this. In global code, it will be set to the global object:
 *
 * enclosing lexical context:
 */

var globalObject = this;
var foo = (() => this);
console.log(foo() === globalObject); // true

// Call as a method of an object
var obj = {foo: foo};
console.log(obj.foo() === globalObject); // true

// Attempt to set this using call
console.log(foo.call(obj) === globalObject); // true

// Attempt to set this using bind
foo = foo.bind(obj);
console.log(foo() === globalObject); // true


/**
 *
 */

// Create obj with a method bar that returns a function that
// returns its this. The returned function is created as
// an arrow function, so its this is permanently bound to the
// this of its enclosing function. The value of bar can be set
// in the call, which in turn sets the value of the
// returned function.
var obj = {bar: function() {
                    var x = (() => this);
                    return x;
                  }
          };
// Call bar as a method of obj, setting its this to obj
// Assign a reference to the returned function to fn
var fn = obj.bar();

// Call fn without setting this, would normally default
// to the global object or undefined in strict mode
console.log(fn() === obj); // true

// But caution if you reference the method of obj without calling it
var fn2 = obj.bar;
// Then calling the arrow function this is equals to window because it follows the this from bar.
console.log(fn2()() == global); // true