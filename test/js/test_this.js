/**
 * Created by linglin on 11/30/17.
 */
function f() {
  return this.a;
}

var g = f.bind({a: 'azerty'}); // now g is a new copy of function that return 'azerty', no more return this.a for g
console.log(g()); // azerty

var h = g.bind({a: 'yoo'}); // bind only works once! for 'chained' binding, because g has no return this.a inside, so binding does not work anymore actually
console.log(h()); // azerty
console.log("g == h ? : ", g==h); //false


var o = {a: 37, f: f, g: g, h: h};
console.log(o.f(), o.g(), o.h()); // 37, azerty, azerty


/**
* a different version
*/

console.log("====================================");

var g = f.bind({a: 'azerty'});
console.log(g()); // azerty

var h = f.bind({a: 'yoo'}); // now h is a second copy of function f but returns yoo,
console.log(h()); // yoo
console.log("g == h ? : ", g==h); //false


var o = {a: 37, f: f, g: g, h: h};
console.log(o.f(), o.g(), o.h()); // 37, azerty, yoo