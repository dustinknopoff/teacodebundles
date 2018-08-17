# Vanilla JavaScript

## Common Vanilla JavaScript Expansions

Made by [twitter] @dustinknopoff

### Element Id

Description:

> Creates Element id selector statement.

` byid btns menu-button`

will render:


```js
 var btns = document.getElementById("menu-button");
 ```

Languages: ['js']



### Element Class

Description:

> Creates default statement for element selection by class name.

` byclass btns links`

will render:


```js
 var btns = document.getElementsByClassName("links");
 ```

Languages: ['js']



### Element Tag

Description:

> Creates default statement for element selection by tag name.

` bytag btns button`

will render:


```js
 var btns = document.getElementsByTagName("button");
 ```

Languages: ['js']



### Add Class

Description:

> Creates statement to add to a variable's class name.

` addc l active`

will render:


```js
 l.className += active;
 ```

Languages: ['js']



### forEach Key

Description:

> Creates forEach arrow function on dictionary/html node.

` forek query`

will render:


```js
 Object.keys(query)
     .forEach((key) => {
         
     });```

Languages: ['js']



### fetch

Description:

> Creates default fetch statement.

` fetch https://www.api.github.com`

will render:


```js
 fetch("https://www.api.github.com")
     .then(res => res.json())
     .then(result => {
         
     }, (error) => {
         console.log(error);
     });```

Languages: ['js']



### Express

Description:

> Express.js syntax for calls.

` ex app get /api/users`

will render:


```js
 app.get('/api/users', (req, res) => {
     
 }```

Languages: ['js']



### Log

Description:

> Creates console.log expression.

` cl chicken.little()`

will render:


```js
 console.log(chicken.little());
 ```

Languages: ['js']



