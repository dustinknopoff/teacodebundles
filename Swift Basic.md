# Swift Basic

## Basic Swift language expanders

Made by [twitter] @Apptorium

### Variable

Description:

` -v name: String`

will render:


```swift
 private var name: String
```

Languages: ['swift']



### Let

Description:

` -l name = "Joe Doe"`

will render:


```swift
 private let name = "Joe Doe"
```

` -l name: String = "Joe Doe"`

will render:


```swift
 private let name: String = "Joe Doe"
```

Languages: ['swift']



### Function

Description:

` -f run`

will render:


```swift
 private func run() {
     
 }
```

` -f run(hello: String, world: String) -> Bool`

will render:


```swift
 private func run(hello: String, world: String) -> Bool {
     
 }
```

Languages: ['swift']



### Class

Description:

` +c MainViewController`

will render:


```swift
 public class MainViewController {
     
 }
```

` +c MainViewController: NSViewController`

will render:


```swift
 public class MainViewController: NSViewController {
     
 }
```

Languages: ['swift']



### guard

Description:

` g value == true`

will render:


```swift
 guard value == true else {
     return
 }
 
```

Languages: ['swift']



### guard let

Description:

> Simplifies typing the `guard let – else` expression for one variable. 

` gl variable`

will render:


```swift
 guard let variable = variable else {
     return
 }
 
```

Languages: ['swift']



### if let

Description:

` il name`

will render:


```swift
 if let name = name {
     
 }
```

Languages: ['swift']



### do-try-catch

Description:

` try run()`

will render:


```swift
 do {
     try run()
 } catch {
     
 }
```

Languages: ['swift']



### Variable with get and set

Description:

` +gs name: String`

will render:


```swift
 public var name: String {
     get {
         
     }
     set {
         
     }
 }
```

Languages: ['swift']



### Getter

Description:

> Generates a variable with getter.

` +getName: String`

will render:


```swift
 public var name: String {
     return 
 }
```

Languages: ['swift']



### Boolean Getter: is / did / has / should

Description:

` isValid`

will render:


```swift
 var isValid: Bool {
     return 
 }
```

` didLoad`

will render:


```swift
 var didLoad: Bool {
     return 
 }
```

Languages: ['swift']



### Protocol Var Getter / Setter

Description:

` pg name: String`

will render:


```swift
 var name: String { get }
```

` pgs name: String`

will render:


```swift
 var name: String { get set }
```

Languages: ['swift']



### Operator

Description:

` +o ==: String`

will render:


```swift
 public static func ==(lhs: String, rhs: String) -> Bool {
     return 
 }
```

Languages: ['swift']



### Lazy var with block

Description:

> Creates a lazy variable.

` lv variableName: String`

will render:


```swift
 lazy var variableName: String = {
     
 }()
```

Languages: ['swift']



### Lazy var with constructor

Description:

> Creates a lazy variable with a simple (non parameter) constructor.

` lvc hello: MyClass`

will render:


```swift
 lazy var hello: MyClass = {
     let hello = MyClass()
     hello.
     return hello
 }()
```

Languages: ['swift']



### Special Comment

Description:

> Creates special comments: `MARK`, `TODO`, `FIXME`, `!`, `?`

` td Implement`

will render:


```
 <td>Implement</td>
```

` m View Lifecycle`

will render:


```
 // MARK: - View Lifecycle
```



### Import

Description:

> Imports a module with the given name.

` @UIKit`

will render:


```swift
 import UIKit
```

Languages: ['swift']



### Scope

Description:

> Swift scope. Used by other expanders.

Languages: ['swift']



### Protocol

Description:

` +p MyProtocol`

will render:


```swift
 public protocol MyProtocol {
     
 }
```

Languages: ['swift']



### Struct

Description:

Languages: ['swift']



### if

Description:

> Generates simple `if` statement.

` if condition`

will render:


```swift
 if condition {
     
 }
```

Languages: ['swift']



### Extension

Description:

Languages: ['swift']



### Enum

Description:

Languages: ['swift']



### defer

Description:

Languages: ['swift']



### Switch

Description:

Languages: ['swift']



