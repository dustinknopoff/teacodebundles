# Objective C

## Basic Objective-C language expanders

Made by [twitter] @Apptorium

### Included Expanders

- [Short, void method](#short,-void-method)
- [Dispatch](#dispatch)
- [Import](#import)
- [if](#if)
- [Protocol](#protocol)
- [Action](#action)
- [Outlet](#outlet)
- [Localized String](#localized-string)

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
 act done() {
     
 }
```

Languages: ['objc']



### Outlet

Description:

> Creates an outlet.

` out button: NSButton`

will render:


```objc
 out button: NSButton() {
     
 }
```

Languages: ['objc']



### Localized String

Description:

> Simpifies string localization.

` _Hello World_First message`

will render:


```objc
 _Hello World_First message() {
     
 }
```

Languages: ['objc']



