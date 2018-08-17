# Objective C

## Basic Objective-C language expanders

Made by [twitter] @Apptorium

### Short, void method

Description:

` -run`

will render:



```objc
 privaterun() {
     
 }
```

Languages: ['objc']



### Dispatch

Description:

> Creates Dispatch-block using combinations of `g` (global thread) and `m` (main thread) as well as `a` (async) and `s` (sync).

` dga`

will render:



```objc
 dga() {
     
 }
```

` dms`

will render:



```objc
 dms() {
     
 }
```

Languages: ['objc']



### Import

Description:

> Imports a file

` @ViewController`

will render:



```objc
 import ViewController
```

Languages: ['objc']



### if

Description:

> Generates simple `if` statement.

` if condition`

will render:



```objc
 if (condition) {
     
 }
```

Languages: ['objc']



### Protocol

Description:

` p MyProtocol`

will render:



```objc
 <p>MyProtocol</p>
```

Languages: ['objc']



### Action

Description:

> Creates an action.

` act done`

will render:



```objc
 @IBAction func done(_ sender: Any) {
     
 }
```

Languages: ['objc']



### Outlet

Description:

> Creates an outlet.

` out button: NSButton`

will render:



```objc
 @IBOutlet weak var button: NSButton!
```

Languages: ['objc']



### Localized String

Description:

> Simpifies string localization.

` _Hello World_First message`

will render:



```objc
 NSLocalizedString("Hello World", comment: "First message")
```

Languages: ['objc']



