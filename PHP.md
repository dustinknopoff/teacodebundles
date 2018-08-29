# PHP

## Basic PHP expanders.

Made by [twitter] @Apptorium

### Included Expanders

- [for](#for)
- [Function](#function)
- [Property](#property)
- [Getter](#getter)
- [Setter](#setter)
- [Exception](#exception)
- [Class](#class)
- [$this->variable](#$this-variable)
- [Map](#map)
- [for in](#for-in)
- [Getter and Setter](#getter-and-setter)
- [Function with doc](#function-with-doc)
- [PHP Tag](#php-tag)
- [Scope](#scope)
- [Empty constructor](#empty-constructor)

### for

Description:

> Creates a *for* loop with the given variable name and maximum number of iteration. 

> All the iteration are counted from 0.

` for i 100`

will render:


```php
 for interface 100 {
     
 }
```

Languages: ['php']



### Function

Description:

> Creates a function (method) with the given scope and name.

` +f run`

will render:


```php
 public func run() {
     
 }
```

` +f run($param1, $param2)`

will render:


```php
 public func run($param1, $param2) {
     
 }
```

Languages: ['php']



### Property

Description:

> Creates a property with the given name. If `type` is given, doc comment is generated as well.

` +v name: String`

will render:


```php
 public var name: String
```

Languages: ['php']



### Getter

Description:

> Creates a *getter* function for the given variable. If `type` is given, doc comment is generated as well.

` +g name: String`

will render:


```php
 +guard name: String else {
     return
 }
 
```

Languages: ['php']



### Setter

Description:

> Creates a *setter* function for the given variable. If `type` is given, doc comment is generated as well.

` +s firstName: String`

will render:


```php
 public struct FirstName: String {
     
 }
```

Languages: ['php']



### Exception

Description:

> Creates an exception class for the given exception name. 

> **Note**: exception name does not need *Exception* suffix. It’s added automatically.

` exc VeryBadThing`

will render:


```php
 exclass VeryBadThing {
     
 }
```

Languages: ['php']



### Class

Description:

> Creates a class with a constructor. It’s possible to add inheriting classes after `:` character

` +c ArticleController: BaseController`

will render:


```php
 public class ArticleController extends BaseController {
     
 }
```

Languages: ['php']



### $this->variable

Description:

> Helps to type expressions with `$this`.

` t propertyName`

will render:


```php
 t propertyName() {
     
 }
```

Languages: ['php']



### Map

Description:

> Simplifies defining array mapping to the class properties.

` map name`

will render:


```php
 <map>name</map>
```

Languages: ['php']



### for in

Description:

> Creates a *foreach* loop with the given variable names. It’s similar to other languages like *Swift* or *Java*, so it provides syntax like:

` for var in vars`

will render:


```php
 for (var i : in vars) {
     
 }
```

Languages: ['php']



### Getter and Setter

Description:

> Creates a *setter* function for the given variable. If `type` is given, doc comment is generated as well.

` +gs firstName: String`

will render:


```php
 public var firstName: String {
     get {
         
     }
     set {
         
     }
 }
```

Languages: ['php']



### Function with doc

Description:

> Creates a function with a doc template.

` +fd run`

will render:


```php
 +fd run() {
     
 }
```

Languages: ['php']



### PHP Tag

Description:

> Creates a `php` tag

` php`

will render:


```php
 php() {
     
 }
```

Languages: ['php']



### Scope

Description:

> Expands a scope. Mostly used by other expanders.

Languages: ['php']



### Empty constructor

Description:

> Empty class constructor.

` con`

will render:


```php
 con() {
     
 }
```

Languages: ['php']



