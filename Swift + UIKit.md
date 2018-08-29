# Swift + UIKit

## `Swift` expanders for `UIKIt` framework.

Made by [twitter] @Apptorium.

### Included Expanders

- [UIView subclass](#uiview-subclass)
- [viewDidLoad](#viewdidload)
- [viewDidAppear](#viewdidappear)
- [viewWillAppear](#viewwillappear)

### UIView subclass

Description:

> Generates a subclass of a UIView class.

` sub MyView: UIView`

will render:


```swift
 @IBDesignable class MyView: UIView {
     
     override init(frame: CGRect) {
         super.init(frame: frame)
         self.configure()
     }
     
     required init?(coder aDecoder: NSCoder) {
         super.init(coder: aDecoder)
         self.configure()
     }
     
     private func configure() {
         
     }
     
     override func layoutSubviews() {
         super.layoutSubviews()
     }
 }
```

Languages: ['swift']



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



