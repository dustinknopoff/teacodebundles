# Swift Extra

## Additional expanders for Swift

Made by [twitter] @Apptorium

### Set

Description:

> Simplifies setting the prperty values as a parameter value.

` set name`

will render:



```swift
 self.name = name
```

Languages: ['swift']



### New class instance

Description:

> Creates a class instance (with empty constructor).

` inst someViewController`

will render:



```swift
 let someViewController = SomeViewController()
```

Languages: ['swift']



### Set self as delegate

Description:

> Sets self as a delegate of the given object name

` sdel tableView`

will render:



```swift
 tableView.delegate = self
```

Languages: ['swift']



### Singleton

Description:

> Creates a singleton class.

` +sing SingletonClass`

will render:



```swift
 public class SingletonClass {
 
     public static let instance = SingletonClass()
 
     
 }
```

Languages: ['swift']



### Delegate Protocol

Description:

> Creates a Delegate protocol

` +del MyView`

will render:



```swift
 public protocol MyViewDelegate {
     
 }
```

Languages: ['swift']



### Command Class

Description:

> Creates a class according to `Command` Design Pattern

` +cmd MyClass`

will render:



```swift
 public class MyClass {
 
     func run() {
         
     }
 }
```

Languages: ['swift']



