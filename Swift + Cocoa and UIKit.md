# Swift + Cocoa and UIKit

## `Swift` expanders for `Cocoa` and `UIKIt` frameworks.

Made by [twitter] @Apptorium.

### Included Expanders

- [Outlet](#outlet)
- [Action](#action)
- [Localized String](#localized-string)
- [if let segue destination](#if-let-segue-destination)
- [guard let segue destination](#guard-let-segue-destination)
- [Dispatch](#dispatch)

### Outlet

Description:

> Creates an `IBOutlet`.

` out nameTextField: NSTextField`

will render:


```swift
 out nameTextField: NSTextField() {
     
 }
```

Languages: ['swift']



### Action

Description:

> Creates an `IBAction`.

` act done`

will render:


```swift
 act done() {
     
 }
```

Languages: ['swift']



### Localized String

Description:

> Simpifies string localization.

` _Hello World_First message`

will render:


```swift
 _Hello World_First message() {
     
 }
```

Languages: ['swift']



### if let segue destination

Description:

> Generates code for `guard-let` the `destinationViewcontroller` in a segue.

` ils controller: UITableViewController`

will render:


```swift
 ilstruct Controller: UITableViewController {
     
 }
```

Languages: ['swift']



### guard let segue destination

Description:

> Generates code for `guard-let` the `destinationViewcontroller` in a segue.

` gls controller: UITableViewController`

will render:


```swift
 glstruct Controller: UITableViewController {
     
 }
```

Languages: ['swift']



### Dispatch

Description:

> Creates Dispatch-block using combinations of `g` (global thread) and `m` (main thread) as well as `a` (async) and `s` (sync).

` dga`

will render:


```
 dga() {
     
 }
```

` dms`

will render:


```
 dms() {
     
 }
```



