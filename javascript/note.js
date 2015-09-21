/******  数据类型  ******/
Number
// JavaScript不区分整数和浮点数，统一用Number表示
123; // 整数123
0.456; // 浮点数0.456
1.2345e3; // 科学计数法表示1.2345x1000，等同于1234.5
-99; // 负数
NaN; // NaN表示Not a Number，当无法计算结果时用NaN表示
Infinity; // Infinity表示无限大，当数值超过了JavaScript的Number所能表示的最大值时，就表示为Infinity
0xff00;  // 16进制

// Number可以直接做四则运算
1 + 2; // 3
(1 + 2) * 5 / 2; // 7.5
2 / 0; // Infinity
0 / 0; // NaN
10 % 3; // 1
10.5 % 3; // 1.5



/******  字符串  ******/
'abc';
"xyz";
// 字符串是以单引号'或双引号"括起来的任意文本

'I\'m \"OK\"!';

// ASCII字符可以以\x##形式的十六进制表示，例如：
'\x41'; // 完全等同于 'A'

// 还可以用\u####表示一个Unicode字符：
'\u4e2d\u6587'; // 完全等同于 '中文'


var s = 'Hello, world!';
s.length; // 13

var s = 'Hello, world!';

s[0]; // 'H'
s[6]; // ' '
s[7]; // 'w'
s[12]; // '!'
s[13]; // undefined 超出范围的索引不会报错，但一律返回undefined


// 需要特别注意的是: 字符串是不可变的，如果对字符串的某个索引赋值，不会有任何错误，但是，也没有任何效果：
var s = 'Test';
s[0] = 'X';
alert(s); // s仍然为'Test'

// JavaScript为字符串提供了一些常用方法，
// 注意，调用这些方法本身不会改变原有字符串的内容，而是返回一个新字符串：
var s = 'Hello';
s.toUpperCase(); // 返回'HELLO'

var s = 'Hello';
var lower = s.toLowerCase(); // 返回'hello'并赋值给变量lower
lower; // 'hello'

var s = 'hello, world';
s.indexOf('world'); // 返回7
s.indexOf('World'); // 没有找到指定的子串，返回-1

var s = 'hello, world'
s.substring(0, 5); // 从索引0开始到5（不包括5），返回'hello'
s.substring(7); // 从索引7开始到结束，返回'world'



/******  布尔值  ******/
true;
false;

// 逻辑运算
true && true;
false || false;
!true;


// 比较运算符
2 > 5; // false
5 >= 2; // true
7 == 7; // true
NaN == NaN // ==, 它会自动转换数据类型再比较，很多时候，会得到非常诡异的结果
NaN === NaN; // ===，它不会自动转换数据类型，如果数据类型不一致，返回false，如果一致，再比较

// 唯一能判断NaN的方法是通过isNaN()函数
isNaN(NaN); // true



/******  null和undefined ******/
null;
// null表示一个“空”的值，它和0以及空字符串''不同，0是一个数值，''表示长度为0的字符串，而null表示“空”

undefined;
// null表示一个空的值，而undefined表示值未定义
// 事实证明，这并没有什么卵用，区分两者的意义不大。大多数情况下，我们都应该用null.
// undefined仅仅在判断函数参数是否传递的情况下有用。



/******  数组  ******/
// JavaScript的数组可以包括任意数据类型
[1, 2, 3.14, 'Hello', null, true];

new Array(1, 2, 3);

// 出于代码的可读性考虑，强烈建议直接使用[]
var arr = [1, 2, 3.14, 'Hello', null, true];
arr[0]; // 返回索引为0的元素，即1
arr[5]; // 返回索引为5的元素，即true
arr[6]; // 索引超出了范围，返回undefined

var arr = [1, 2, 3.14, 'Hello', null, true];
arr.length; // 6

// 请注意，直接给Array的length赋一个新的值会导致Array大小的变化：
var arr = [1, 2, 3];
arr.length; // 3
arr.length = 6;
arr; // arr变为[1, 2, 3, undefined, undefined, undefined]
arr.length = 2;
arr; // arr变为[1, 2]

// Array可以通过索引把对应的元素修改为新的值，因此，对Array的索引进行赋值会直接修改这个Array：
var arr = ['A', 'B', 'C'];
arr[1] = 99;
arr; // arr现在变为['A', 99, 'C']

// 请注意，如果通过索引赋值时，索引超过了范围，同样会引起Array大小的变化:
var arr = [1, 2, 3];
arr[5] = 'x';
arr; // arr变为[1, 2, 3, undefined, undefined, 'x']
// 在编写代码时，不建议直接修改Array的大小，访问索引时要确保索引不会越界.

var arr = [10, 20, '30', 'xyz'];
arr.indexOf(10); // 元素10的索引为0
arr.indexOf(20); // 元素10的索引为1
arr.indexOf(30); // 元素30没有找到，返回-1
arr.indexOf('30'); // 元素'30'的索引为2

var arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
arr.slice(0, 3); // 从索引0开始，到索引3结束，但不包括索引3: ['A', 'B', 'C']
arr.slice(3); // 从索引3开始到结束: ['D', 'E', 'F', 'G']

// push()向Array的末尾添加若干元素，pop()则把Array的最后一个元素删除掉：
var arr = [1, 2];
arr.push('A', 'B'); // 返回Array新的长度: 4
arr; // [1, 2, 'A', 'B']
arr.pop(); // pop()返回'B'
arr; // [1, 2, 'A']
arr.pop(); arr.pop(); arr.pop(); // 连续pop 3次
arr; // []
arr.pop(); // 空数组继续pop不会报错，而是返回undefined
arr; // []

// 如果要往Array的头部添加若干元素，使用unshift()方法，shift()方法则把Array的第一个元素删掉：
var arr = [1, 2];
arr.unshift('A', 'B'); // 返回Array新的长度: 4
arr; // ['A', 'B', 1, 2]
arr.shift(); // 'A'
arr; // ['B', 1, 2]
arr.shift(); arr.shift(); arr.shift(); // 连续shift 3次
arr; // []
arr.shift(); // 空数组继续shift不会报错，而是返回undefined
arr; // []

// sort()可以对当前Array进行排序
var arr = ['B', 'C', 'A'];
arr.sort();
arr; // ['A', 'B', 'C']

// reverse() 反转
var arr = ['one', 'two', 'three'];
arr.reverse(); 
arr; // ['three', 'two', 'one']

// splice()方法是修改Array的“万能方法”，它可以从指定的索引开始删除若干元素，然后再从该位置添加若干元素：
var arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle'];
// 从索引2开始删除3个元素,然后再添加两个元素:
arr.splice(2, 3, 'Google', 'Facebook'); // 返回删除的元素 ['Yahoo', 'AOL', 'Excite']
arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
// 只删除,不添加:
arr.splice(2, 2); // ['Google', 'Facebook']
arr; // ['Microsoft', 'Apple', 'Oracle']
// 只添加,不删除:
arr.splice(2, 0, 'Google', 'Facebook'); // 返回[],因为没有删除任何元素
arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']

// concat() 连接数组
// 请注意，concat()方法并没有修改当前Array，而是返回了一个新的Array。
var arr = ['A', 'B', 'C'];
var added = arr.concat([1, 2, 3]);
added; // ['A', 'B', 'C', 1, 2, 3]
arr; // ['A', 'B', 'C']
var arr = ['A', 'B', 'C'];
arr.concat(1, 2, [3, 4]); // ['A', 'B', 'C', 1, 2, 3, 4]


// join()
var arr = ['A', 'B', 'C', 1, 2, 3];
arr.join('-'); // 'A-B-C-1-2-3'


// 多维数组
var arr = [[1, 2, 3], [400, 500, 600], '-'];



/******  对象  ******/
// JavaScript的对象是一组由键-值组成的无序集合
// JavaScript对象的键都是字符串类型，值可以是任意数据类型
var person = {
    name: 'Bob',
    age: 20,
    tags: ['js', 'web', 'mobile'],
    city: 'Beijing',
    zipcode: null,
    'middle-school': 'No.1 Middle School'
};

person.name; // 'Bob'
person['name'];
person.zipcode; // null
person['middle-school']; // 'No.1 Middle School'

// 如果访问一个不存在的属性, 返回undefined

// 由于JavaScript的对象是动态类型，你可以自由地给一个对象添加或删除属性
var xiaoming = {
    name: '小明'
};
xiaoming.age; // undefined
xiaoming.age = 18; // 新增一个age属性
xiaoming.age; // 18
delete xiaoming.age; // 删除age属性
xiaoming.age; // undefined
delete xiaoming['name']; // 删除name属性
xiaoming.name; // undefined
delete xiaoming.school; // 删除一个不存在的school属性也不会报错


// 如果我们要检测xiaoming是否拥有某一属性，可以用in操作符：
var xiaoming = {
    name: '小明',
    birth: 1990,
    school: 'No.1 Middle School',
    height: 1.70,
    weight: 65,
    score: null
};
'name' in xiaoming; // true
'grade' in xiaoming; // false

// 不过要小心，如果in判断一个属性存在，这个属性不一定是xiaoming的，它可能是xiaoming继承得到的：
'toString' in xiaoming; // true
// 因为toString定义在object对象中，而所有对象最终都会在原型链上指向object，所以xiaoming也拥有toString属性

// 要判断一个属性是否是xiaoming自身拥有的，而不是继承得到的，可以用hasOwnProperty()方法：
var xiaoming = {
    name: '小明'
};
xiaoming.hasOwnProperty('name'); // true
xiaoming.hasOwnProperty('toString'); // false



/******  变量  ******/

var a; // 申明了变量a，此时a的值为undefined
var $b = 1; // 申明了变量$b，同时给$b赋值，此时$b的值为1
var s_007 = '007'; // s_007是一个字符串
var Answer = true; // Answer是一个布尔值true
var t = null; // t的值是null

var a = 123; // a的值是整数123
a = 'ABC'; // a变为字符串


/******  strict模式  ******/
// JavaScript在设计之初，为了方便初学者学习，并不强制要求用var申明变量。这个设计错误带来了严重的后果:
// 如果一个变量没有通过var申明就被使用，那么该变量就自动被申明为全局变量
// 在同一个页面的不同的JavaScript文件中，如果都不用var申明，恰好都使用了变量i，将造成变量i互相影响，产生难以调试的错误结果。
// 为了修补JavaScript这一严重设计缺陷，ECMA在后续规范中推出了strict模式，在strict模式下运行的JavaScript代码，强制通过var申明变量.
// 未使用var申明变量就使用的，将导致运行错误.
'use strict';
// 启用strict模式的方法是在JavaScript代码的第一行写上:

// 为了避免这一缺陷，所有的JavaScript代码都应该使用strict模式



/******  Map和Set  ******/
// JavaScript的默认对象表示方式{}可以视为其他语言中的Map或Dictionary的数据结构，即一组键值对
// 但是JavaScript的对象有个小问题，就是键必须是字符串
// 但实际上Number或者其他数据类型作为键也是非常合理的

// 最新的ES6规范引入了新的数据类型Map。要测试你的浏览器是否支持ES6规范，请执行以下代码:
'use strict';
var m = new Map();
var s = new Set();
alert('你的浏览器支持Map和Set！');


var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
m.get('Michael'); // 95

// 初始化Map需要一个二维数组，或者直接初始化一个空Map。Map具有以下方法:
var m = new Map(); // 空Map
m.set('Adam', 67); // 添加新的key-value
m.set('Bob', 59);
m.has('Adam'); // 是否存在key 'Adam': true
m.get('Adam'); // 67
m.delete('Adam'); // 删除key 'Adam'
m.get('Adam'); // undefined

var m = new Map();
m.set('Adam', 67);
m.set('Adam', 88);
m.get('Adam'); // 88


// Set和Map类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在Set中，没有重复的key

// 要创建一个Set，需要提供一个Array作为输入，或者直接创建一个空Set
var s1 = new Set(); // 空Set
var s2 = new Set([1, 2, 3]); // 含1, 2, 3

// 重复元素在Set中自动被过滤
var s = new Set([1, 2, 3, 3, '3']);
s; // Set {1, 2, 3, "3"}

// 通过add(key)方法可以添加元素到Set中，可以重复添加，但不会有效果:
s.add(4);
s;  // {1, 2, 3, 4}
s.add(4);
s;  // {1, 2, 3, 4}

var s = new Set([1, 2, 3]);
s; // Set {1, 2, 3}
s.delete(3);
s; // Set {1, 2}



/******  iterable  ******/
// Array、Map和Set都属于iterable类型
// 具有iterable类型的集合可以通过新的for ... of循环来遍历
// for ... of循环是ES6引入的新的语法
'use strict';
var a = [1, 2, 3];
for (var x of a) {
}
alert('你的浏览器支持for ... of');


var a = ['A', 'B', 'C'];
var s = new Set(['A', 'B', 'C']);
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
for (var x of a) { // 遍历Array
    alert(x);
}
for (var x of s) { // 遍历Set
    alert(x);
}
for (var x of m) { // 遍历Map
    alert(x[0] + '=' + x[1]);
}


var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x in a) {
    alert(x); // '0', '1', '2', 'name'
}

var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x of a) {
    alert(x); 'A', 'B', 'C'
}


// 更好的方式是直接使用iterable内置的forEach方法
var a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    alert(element);
});

// forEach()方法是ES5.1标准引入的，你需要测试浏览器是否支持

// Set与Array类似，但Set没有索引，因此回调函数最多两个参数
var s = new Set(['A', 'B', 'C']);
s.forEach(function (element, set) {
    alert(element);
});


// Map
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map) {
    alert(value);
});


// 如果对某些参数不感兴趣，由于JavaScript的函数调用不要求参数必须一致，因此可以忽略它们
var a = ['A', 'B', 'C'];
a.forEach(function (element) {
    alert(element);
});






