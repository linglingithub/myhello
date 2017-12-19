/**
 * Created by  on 12/18/17.
 *
 * https://medium.com/craft-academy/javascript-arrow-functions-27d4c3334b83
 *
 */
"use strict";

function Person_wont_grow() {
  // The Person() constructor defines `this` as an instance of itself.
  this.age = 0; // age in this case is for that person instance
  setInterval(function growUp() {
    // In non-strict mode, the growUp() function defines `this`
    // as the global object, which is different from the `this`
    // defined by the Person() constructor.
    this.age++;
  }, 1000);
}

var p1 = new Person_wont_grow();
setInterval(function showAge() {
  console.log(p1.age);
}, 2000);
// will always show 0

function Person(){
  this.age = 0;

  setInterval(() => {
    this.age++; // |this| properly refers to the person object
  }, 1000);
}

var p2 = new Person();
setInterval(function showAge() {
  console.log(p2.age);
}, 2000); // shows 1, 3, 5, 7...


