var key = "property";
console.log(key);



var obj = {
    property: "my property"
};

console.log(obj[key]);

//定义一个变量s，并赋值为字符串
var s = "text";
console.log(s);

//赋值s为整型
s = 12+5;
console.log(s);

//赋值s为浮点型
s = 6.3;
console.log(s);

//赋值s为一个对象
s = new Object();
s.name = "object";

console.log(s.name);


var array = [1, 2, 3, 4, 5];
a = array.map(function(item){
    return item * 2;
});

console.log(array, a);


var staff = [
    {name: 'abruzzi', age: 24},
    {name: 'bajmine', age: 26},
    {name: 'chris', age: 25}
];

b = staff.map(function(item){
    return item.name.toUpperCase();
});

c = staff.filter(function(item){
    return item.age > 24;
});

console.log(staff, b, c);