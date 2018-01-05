/**
 * Created by  on 12/21/17.
 *
 * http://2ality.com/2011/04/modules-and-namespaces-in-javascript.html
 *
 *
 *
 * Filling a module with content

Approach 1: Object literal.
    var namespace = {
        func: function() { ... },
        value: 123
    };
Approach 2: Assigning to properties.
    var namespace = {};
    namespace.func = function() { ... };
    namespace.value = 123;
Accessing the content in either approach:
    namespace.func();
    console.log(namespace.value + 44);
Assessment:
Object literal.
Pro: Elegant syntax.
Con: As a single, sometimes very long syntactic construct, it imposes constraints on its contents. One must maintain the opening brace before the content and the closing brace after the content. And one must remember to not add a comma after the last property value. This makes it harder to move content around.
Assigning to properties.
Con: Redundant repetitions of the namespace identifier.
The Module pattern: private data and initialization
 *
 */


/*
*
* The Module pattern: private data and initialization
*
* */

var namespace = function() {
        // set up private data
        var arr = []; // not visible outside
        for(var i=0; i<4; i++) {
            arr.push(i);
        }
        return {
            // read-only access via getter
            get values() {
                return arr;
            }
        };
    }();
console.log(namespace.values); // [0,1,2,3]

/**
 * Variation: Namespace is a function parameter.
 */

var namespace1 = {};
    (function(ns) {
        // (set up private data here)
      var arr = [];
      for(var i=0; i<4; i++) {
            arr.push(i);
        }
       Object.defineProperty(ns, 'values', {get: function() { return arr;} } );

        ns.func = function() { console.log('this is ns.func') };
        ns.value = 123;


    }(namespace1));

    console.log(namespace1.value); // 123
    console.log(namespace1.values);
    console.log(namespace1.func());
    console.log(namespace1.func);