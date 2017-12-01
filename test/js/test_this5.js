/**
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this
 *
 As a DOM event handler

When a function is used as an event handler, its this is set to the element the event fired from (some browsers do not
 follow this convention for listeners added dynamically with methods other than addEventListener).


 test_this5.html

 *
 */


// When called as a listener, turns the related element blue
function bluify(e) {
  // Always true
  console.log(this === e.currentTarget);
  // true when currentTarget and target are the same object
  console.log(this === e.target);
  this.style.backgroundColor = '#A5D9F3';
}

// Get a list of every element in the document
var elements = document.getElementsByTagName('*');

// Add bluify as a click listener so when the
// element is clicked on, it turns blue
for (var i = 0; i < elements.length; i++) {
  elements[i].addEventListener('click', bluify, false);
}

/**
 *
 * In an in–line event handler

When code is called from an in–line on-event handler, its this is set to the DOM element on which the listener is placed:

<button onclick="alert(this.tagName.toLowerCase());">
  Show this
</button>
The above alert shows button. Note however that only the outer code has its this set this way:

<button onclick="alert((function() { return this; })());">
  Show inner this
</button>
In this case, the inner function's this isn't set so it returns the global/window object (i.e. the default object in non–strict mode where this isn't set by the call).
 *
 */