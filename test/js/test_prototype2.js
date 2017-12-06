/**
 * Created by  on 12/5/17.
 *
 * About __proto__, prototype, [[prototype]]
 *
 * https://hackernoon.com/understand-nodejs-javascript-object-inheritance-proto-prototype-class-9bd951700b29
 *
 *
 */


function Foo(name) {
  this.name = name;
}
var b = new Foo('b');
var a = new Foo('a');

console.log(a.__proto__ === Foo.prototype, a.__proto__); // true
console.log(a.__proto__ === b.__proto__); // true
console.log(a.prototype === a.__proto__, a.prototype); // false
console.log(Foo.prototype === Foo.__proto__, Foo.prototype, Foo.__proto__); // false