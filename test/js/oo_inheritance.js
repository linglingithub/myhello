/**
 * Created by linglin on 11/13/17.
 */


/*

https://www.ibm.com/developerworks/cn/java/j-cb12196/

 清单 7. 创建一个构造函数

 <script type='text/javascript'>
 Animal = function() {
 this.name = "nobody"
 this.speak = function () {
 return "Who am I?"
 }
 }

 myAnimal = new Animal();
 alert('The animal named ' + myAnimal.name +
 ' says ' + myAnimal.speak());

 </script>
 * 对于 Java 开发人员而言，清单 7 中的代码看起来多少有点生疏和奇怪。实际上对于没有亲自构建过对象的许多 JavaScript 开发人员来说，这些代码
 * 同样看起来有点生疏和奇怪。也许，下面的解释可以让大家能够更好地理解这段代码。
 实际上，您只需重点关注其中三段信息。首先，JavaScript 用嵌套函数表示对象。这意味着清单 7 中的 Animal 的定义是一种有效的语法。
 第二，JavaScript 基于原型或现有的对象的实例来构造对象，而非基于类模板。funct() 是一种调用，但 new Animal() 却基于 Animal 内的原型构
 造一个对象。最后，在 JavaScript 中，对象只是函数和变量的集合。每个对象并不与类型相关，所以可以自由地修改这种结构。
 回到 清单 7。如您所见，JavaScript 基于在 Animal 中指定的原型定义一个新对象：myAnimal。继而可以使用原型中的属性和函数，甚或重定义函数和
 属性。这种灵活性可能会让 Java 开发人员受不了，因为他们不习惯这种行为，但它的确是一种十分强大的模型。
 现在我还要更深入一步。您还可以使用名为 prototype 实例变量来指定对象的基础。方法是设置 prototype 实例变量使其指向继承链的父。如此设置
  prototype 之后，您所创建的对象会为未指定的那些对象继承属性和函数。这样一来，您就可以模仿面向对象的继承概念。以清单 8 为例
 *
 *
 * */

Animal = function () {
    this.name = "nobody";
    this.speak = function () {
        return "Who am I?"
    }
};
Dog = function () {
    this.speak = function () {
        return "Woof!"
    }
};
Dog.prototype = new Animal();

myAnimal = new Dog();
console.log('The animal named ' + myAnimal.name +
    ' says ' + myAnimal.speak());

/**
 *
 *

 在清单 8 中，创建了一个 Dog 原型。此原型基于 Animal。Dog 重定义 speak() 方法但却不会对 name() 方法做任何改动。随后，将原型 Dog 设置成 Animal。
 */