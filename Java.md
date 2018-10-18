# Java

## Commonly Used Java Expansions

Made by [@dustinknopoff](https://dustinknopoff.me)

### Included Expanders

- [Constant Variable](#constant-variable)
- [If](#if)
- [For](#for)
- [For(i)](#for(i))
- [Variable](#variable)
- [Method](#method)
- [Error](#error)
- [Cast](#cast)
- [Class](#class)
- [Interface](#interface)
- [Implements](#implements)
- [Function](#function)
- [Scope](#scope)
- [Print](#print)

### Constant Variable

Description:

> Creates constant variable.

` const int size 300`

will render:


```java
 private static final int SIZE = 300;
 
```

Languages: ['java']



### If

Description:

> Creates if statement.

` if x > 300`

will render:


```java
 if (x > 300) {
     
 }
```

Languages: ['java', 'js', 'c']



### For

Description:

> Creates for loop.

` for int ArrayList arr`

will render:


```java
 for (int i : ArrayList arr) {
     
 }
```

Languages: ['java']



### For(i)

Description:

> Creates iterative for loop.

` fori <= arr.length()`

will render:


```java
 for (int i = 0; i <= arr.length(); i++) {
     
 }
```

Languages: ['java', 'js', 'c']



### Variable

Description:

> Default variable declaration. (Private and final)

` -v List<Shape> shapes`

will render:


```java
 private final List<Shape> shapes;
 
```

` -v int maxHeight`

will render:


```java
 private final int maxHeight;
 
```

Languages: ['java']



### Method

Description:

> Creates default method syntax. (Private and final)

` fn void AnimatorModel`

will render:


```java
 fn void(AnimatorModel) {
     
 }
```

` fn boolean addShape Shape shape`

will render:


```java
 fn boolean(addShape Shape shape) {
     
 }
```

Languages: ['java']



### Error

Description:

> Creates exception statement.

` throw u Cannot do this in non-Hybrid View`

will render:


```java
 throw new UnsupportedOperationException("Cannot do this in non-Hybrid View");
 
```

Languages: ['java']



### Cast

Description:

> Creates default cast expression.

` cast Oval o s`

will render:


```java
 Oval o = (Oval) s;
 
```

Languages: ['java']



### Class

Description:

> Creates a class with a constructor. It’s possible to add inheriting classes after `:` character

` +c nombre: Familia`

will render:


```java
 public class Nombre extends Familia {
     
 }
```

Languages: ['java']



### Interface

Description:

> Creates an interface in Java.

` i Car im base`

will render:


```java
 interface Car implements Base {
     
 }
```

` i Car e base`

will render:


```java
 interface Car extends Base {
     
 }
```

> Created by @Gata

Languages: ['java']



### Implements

Description:

> Creates a Java Interface.

` c Car im base`

will render:


```java
 class Car implements Base {
     
 }
```

` c Car e base`

will render:


```java
 class Car extends Base {
     
 }
```

> Made by @Gata

Languages: ['java']



### Function

Description:

> Creates a function (method) with the given scope and name.

` +String run`

will render:


```java
 +String run() {
     
 }
```

` +int run(String param1, int param2)`

will render:


```java
 +int run(String param1, int param2) {
     
 }
```

Languages: ['java']



### Scope

Description:

` +`

will render:


```java
 public
```

` -`

will render:


```java
 private
```

` #`

will render:


```java
 protected
```

Languages: ['java']



### Print

Description:

` print array.length()`

will render:


```java
 System.out.println(array.length());
 
```

Languages: ['java']



