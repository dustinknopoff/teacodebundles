# Swift + Cocoa and UIKit

## `Swift` expanders for `Cocoa` and `UIKIt` frameworks.

Made by [twitter] @Apptorium.

### Outlet

Description:

> Creates an `IBOutlet`.

` out nameTextField: NSTextField`

will render:



```swift
 @IBOutlet weak var nameTextField: NSTextField!
```

Languages: ['swift']



### Action

Description:

> Creates an `IBAction`.

` act done`

will render:



```swift
 @IBAction func done(_ sender: Any) {
     
 }
```

Languages: ['swift']



### Localized String

Description:

> Simpifies string localization.

` _Hello World_First message`

will render:



```swift
 NSLocalizedString("Hello World", comment: "First message")
```

Languages: ['swift']



### if let segue destination

Description:

> Generates code for `guard-let` the `destinationViewcontroller` in a segue.

` ils controller: UITableViewController`

will render:



```swift
 if let controller = segue.destinationViewController as? UITableViewController {
     
 }
```

Languages: ['swift']



### guard let segue destination

Description:

> Generates code for `guard-let` the `destinationViewcontroller` in a segue.

` gls controller: UITableViewController`

will render:



```swift
 guard let controller = segue.destinationViewController as? UITableViewController else {
     return
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

Languages: []



