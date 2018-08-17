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

### Test class

Description:

> Creates a test class

` tc UpdateController @MyApp`

will render:


```swift
 import XCTest
 @testable import MyApp
 
 class UpdateControllerTests: XCTestCase {
     
     
 }```

Languages: ['swift']



### Test function

Description:

` tf update`

will render:


```swift
 func testUpdate() {
     
 }```

Languages: ['swift']



### Assert Equal

Description:

` ase value`

will render:


```swift
 XCTAssertEqual(, value)```

Languages: ['swift']



### Assert True

Description:

` ast value`

will render:


```swift
 XCTAssertTrue(value)```

Languages: ['swift']



### Assert False

Description:

` asf value`

will render:


```swift
 XCTAssertFalse(value)```

Languages: ['swift']



### Assert Nil

Description:

` asn value`

will render:


```swift
 XCTAssertNil(value)```

Languages: ['swift']



### Assert

Description:

` as value == "something"`

will render:


```swift
 XCTAssert(value == "something")```

Languages: ['swift']



