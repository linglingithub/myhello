/**
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this
 *
 * In arrow functions, this retains the value of the enclosing lexical context's this. In global code, it will be set to the global object:
 *
 * lexical environments:  (?? scope ? a part of  execution context)
 * A Lexical Environment is a specification type used to define the association of Identifiers to specific variables
 * and functions based upon the lexical nesting structure of ECMAScript code. A Lexical Environment consists of an
 * Environment Record and a possibly null reference to an outer Lexical Environment.
 *
 *
 * http://es5.github.io/#x10.3
 *
 * When control is transferred to ECMAScript executable code, control is entering an execution context.
 * Active execution contexts logically form a stack.
 *
 * An execution context contains whatever state is necessary to track the execution progress of its associated code.
 * In addition, each execution context has the state components listed in Table 19.

Table 19 —Execution Context State Components
Component  ----- Purpose

 LexicalEnvironment
Identifies the Lexical Environment used to resolve identifier references made by code within this execution context.

 VariableEnvironment
Identifies the Lexical Environment whose environment record holds bindings created by VariableStatements and FunctionDeclarations within this execution context.

 ThisBinding
The value associated with the this keyword within ECMAScript code associated with this execution context.



 *
 *
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