# Swift + Cocoa

## `Swift` expanders for `Cocoa` framework.

Made by [twitter] @Apptorium

### viewDidLoad

Description:

> Creates `viewDidLoad` method.

` vdl`

will render:


```swift
 override func viewDidLoad() {
     super.viewDidLoad()
     
     
 }
```

Languages: ['swift']



### viewDidAppear

Description:

> Creates `viewDidAppear` method.

` vda`

will render:


```swift
 override func viewDidAppear() {
     super.viewDidAppear()
     
     
 }
```

Languages: ['swift']



### viewWillAppear

Description:

> Creates `viewWillAppear` method.

` vwa`

will render:


```swift
 override func viewWillAppear() {
     super.viewWillAppear()
     
     
 }
```

Languages: ['swift']



### View Controller

Description:

> Creates a class that inherits from `NSViewController`

` vc main`

will render:


```swift
 class MainViewController: NSViewController {
 
     override func viewDidLoad() {
         super.viewDidLoad()
         
         
     }
 }
```

Languages: ['swift']



### Window Controller

Description:

> Creates a class that inherits from `NSWindowController`

` wc main`

will render:


```swift
 class MainWindowController: NSWindowController {
 
     override func windowDidLoad() {
         super.windowDidLoad()
         
         
     }
 }
```

Languages: ['swift']



### Binding

Description:

> Creates a binding.

` bind sourceObject:variable to destinationObject:path`

will render:


```swift
 sourceObject.bind(NSBindingName("variable"), to: destinationObject, withKeyPath: "path", options: nil)
```

Languages: ['swift']



