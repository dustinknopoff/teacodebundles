# Swift Extra

## Additional expanders for Swift

Made by [twitter] @Apptorium

### Included Expanders

- [Set](#set)
- [New class instance](#new-class-instance)
- [Set self as delegate](#set-self-as-delegate)
- [Singleton](#singleton)
- [Delegate Protocol](#delegate-protocol)
- [Command Class](#command-class)

### Set

Description:

> Simplifies setting the prperty values as a parameter value.

` set name`

will render:


```swift
 this.setState({ name });
```

Languages: ['swift']



### New class instance

Description:

> Creates a class instance (with empty constructor).

` inst someViewController`

will render:


```swift
 inst someViewController() {
     
 }
```

Languages: ['swift']



### Set self as delegate

Description:

> Sets self as a delegate of the given object name

` sdel tableView`

will render:


```swift
 s<del>tableView</del>
```

Languages: ['swift']



### Singleton

Description:

> Creates a singleton class.

` +sing SingletonClass`

will render:


```swift
 +singuard SingletonClass else {
     return
 }
 
```

Languages: ['swift']



### Delegate Protocol

Description:

> Creates a Delegate protocol

` +del MyView`

will render:


```swift
 +<del>MyView</del>
```

Languages: ['swift']



### Command Class

Description:

> Creates a class according to `Command` Design Pattern

` +cmd MyClass`

will render:


```swift
 +cmd MyClass() {
     
 }
```

Languages: ['swift']



