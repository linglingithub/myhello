/**
 * Created by ll on 12/5/17.
 *
 * http://adripofjavascript.com/blog/drips/basic-inheritance-with-javascript-constructors.html
 *
 */

function SuperHuman (name, superPower) {
    this.name = name;
    this.superPower = superPower;
}

SuperHuman.prototype.usePower = function () {
    console.log(this.superPower + "!");
};

var banshee = new SuperHuman("Silver Banshee", "sonic wail");

// Outputs: "sonic wail!"
banshee.usePower();

// function SuperHero (name, superPower) {
//     this.name = name;
//     this.superPower = superPower;
//     this.allegiance = "Good";
// }

// this is the fix  --->

function SuperHero (name, superPower) {
    // Reuse SuperHuman initialization
    SuperHuman.call(this, name, superPower);

    this.allegiance = "Good";
}
SuperHero.prototype = SuperHuman.prototype;
// SuperHero.prototype = new SuperHuman();
// <--- end of fix

SuperHero.prototype.saveTheDay = function () {
    console.log(this.name + " saved the day!");
};

var marvel = new SuperHero("Captain Marvel", "magic");

// Outputs: "Captain Marvel saved the day!"
marvel.saveTheDay();

// TypeError: Object <#SuperHero> has no method 'usePower'
marvel.usePower();

/**
 * While this gets us started, there are a couple of problems. First of all, the SuperHero constructor is repeating
 * some of the logic of the SuperHuman constructor. And more importantly, at this point instances of SuperHero don't
 * have access to SuperHuman methods. Let's fix those couple of issues.  -- see above fix part
 *
 *
 *
 * We've managed to eliminate the repeated constructor logic by calling SuperHuman with SuperHero's this object and passing along the necessary arguments. That ensures that SuperHuman's initialization logic will act on the new SuperHero object. And then we tack on the additional logic that is specific to SuperHero.

But where the inheritance comes in is on SuperHero.prototype.
 In order to ensure that it inherits the methods from SuperHuman.prototype, we actually make it an instance of SuperHuman
 with new SuperHuman().

 This basic inheritance pattern won't always work, particularly if the parent constructor is complex, but it will handle
 simple situations quite well.

In future issues we'll take a look at more sophisticated ways of doing inheritance.
 *
 *
 */

