# Rust

## Common Rust Expansions

Made by [twitter] @dustinknopoff

### Fn

Description:

> Creates Rust default function template.

` fn main`

will render:



```any
 fn main() {
     
 }
```

` fn divide divisor: i32, dividend: i32`

will render:



```any
 fn divide(divisor: i32, dividend: i32) {
     
 }
```

Languages: ['any']



### Impl

Description:

> Default statement for extending a struct.

` impl rectangle`

will render:



```any
 impl Rectangle {
     
 }
```

Languages: ['any']



### Struct

Description:

` struct Rectangle`

will render:



```any
 struct Rectangle {
     
 }
```

` struct Room String`

will render:



```any
 struct Roo// MARK: - String
```

Languages: ['any']



### Enum

Description:

` enum Coins`

will render:



```any
 enum Coins {
     
 }
```

Languages: ['any']



### Variables

Description:

` var integer 36`

will render:



```any
 let mut integer = 36;
```

` var integer 36 usize m`

will render:



```any
 let mut integer: usize = 36;
```

Languages: ['any']



### Type Conversion

Description:

` conv integer f32`

will render:



```any
 integer as f32
```

Languages: ['any']



### main

Description:

` main`

will render:



```any
 fn main() {
     
 }
```

Languages: ['any']



### Match

Description:

` match number`

will render:



```any
 match number {
      => 
 }
```

Languages: ['any']



