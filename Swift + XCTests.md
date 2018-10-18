# Swift + XCTests

## Write unit tests more efficently.

Start with a class:

> tc UpdateController @MyApp

Write test function:

> tf update

And make some tests:

> ast isStarted
> ase progress

Made by [twitter] @Apptorium

### Included Expanders

- [Test class](#test-class)
- [Test function](#test-function)
- [Assert Equal](#assert-equal)
- [Assert True](#assert-true)
- [Assert False](#assert-false)
- [Assert Nil](#assert-nil)
- [Assert](#assert)

### Test class

Description:

> Creates a test class

` tc UpdateController @MyApp`

will render:


```swift
 tc UpdateController import MyApp
```

Languages: ['swift']



### Test function

Description:

` tf update`

will render:


```swift
 tfunc update() {
     
 }
```

Languages: ['swift']



### Assert Equal

Description:

` ase value`

will render:


```swift
 ase value() {
     
 }
```

Languages: ['swift']



### Assert True

Description:

` ast value`

will render:


```swift
 ast value() {
     
 }
```

Languages: ['swift']



### Assert False

Description:

` asf value`

will render:


```swift
 asfunc value() {
     
 }
```

Languages: ['swift']



### Assert Nil

Description:

` asn value`

will render:


```swift
 asn value() {
     
 }
```

Languages: ['swift']



### Assert

Description:

` as value == "something"`

will render:


```swift
strcmp( as value,"something")
```

Languages: ['swift']



