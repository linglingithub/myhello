/**
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this
 *
 * When a function is called as a method of an object, its this is set to the object the method is called on.
 *
 * In the following example, when o.f() is invoked, inside the function this is bound to the o object.
 *
 */

var o = {
  prop: 37,
  f: function() {
    return this.prop;
  }
};

console.log(o.f()); // 37

/**
 * Note that this behavior is not at all affected by how or where the function was defined. In the previous example, we
 * defined the function inline as the f member during the definition of o. However, we could have just as easily defined
 * the function first and later attached it to o.f. Doing so results in the same behavior:
 *
 */

var o = {prop: 37};

function independent() {
  return this.prop;
}

o.f = independent;

console.log("invoked by o: ", o, o.f()); // 37

/**
 * This demonstrates that it matters only that the function was invoked from the f member of o.

Similarly, the this binding is only affected by the most immediate member reference. In the following example, when we
 invoke the function, we call it as a method g of the object o.b. This time during execution, this inside the function
 will refer to o.b. The fact that the object is itself a member of o has no consequence; the most immediate reference is
 all that matters.
 *
 */


o.b = {g: independent, prop: 42};
console.log("invoked by o.b: ", o.b, o.b.g()); // 42
console.log("compare o.f and o.b.g -- true for reference, true for toString: ", o.f === o.b.g, o.f.toString() == o.b.g.toString());

var funcvar = function independent() {
  return this.prop;
}

console.log("compare o.f and funcvar -- false for reference, true for toString: ", o.f == funcvar, o.f.toString() == funcvar.toString(), o.f.toString(), funcvar.toString());
console.log("compare o.f and independent: ", o.f == independent, o.f.toString() == independent.toString(), o.f.toString(), independent.toString());

/**
 *
 * this on the object's prototype chain

The same notion holds true for methods defined somewhere on the object's prototype chain. If the method is on an object's prototype chain, this refers to the object the method was called on, as if the method were on the object.

var o = {f: function() { return this.a + this.b; }};
var p = Object.create(o);
p.a = 1;
p.b = 4;

console.log(p.f()); // 5
In this example, the object assigned to the variable p doesn't have its own f property, it inherits it from its prototype. But it doesn't matter that the lookup for f eventually finds a member with that name on o; the lookup began as a reference to p.f, so this inside the function takes the value of the object referred to as p. That is, since f is called as a method of p, its this refers to p. This is an interesting feature of JavaScript's prototype inheritance.

 */

console.log("====================================");

/**
 *
 * this with a getter or setter

Again, the same notion holds true when a function is invoked from a getter or a setter. A function used as getter or setter has its this bound to the object from which the property is being set or gotten.

function sum() {
  return this.a + this.b + this.c;
}

var o = {
  a: 1,
  b: 2,
  c: 3,
  get average() {
    return (this.a + this.b + this.c) / 3;
  }
};

Object.defineProperty(o, 'sum', {
    get: sum, enumerable: true, configurable: true});

console.log(o.average, o.sum); // 2, 6
 *
 */


function sum() {
  return this.a + this.b + this.c;
}

var o = {
  a: 1,
  b: 2,
  c: 3,
  get average() {
    return (this.a + this.b + this.c) / 3;
  }
};


o.a = 10;

Object.defineProperty(o, 'sum', {
    get: sum, enumerable: true, configurable: true});

console.log(o.average, o.sum); // 2, 6