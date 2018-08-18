# Rust

## Common Rust Expansions

Made by [@dustinknopoff](https://dustinknopoff.me)



### Fn

Description:

> Creates Rust default function template.

` fn main`

will render:


```
 fn if __name__ == "__main__":
     
```

` fn divide divisor: i32, dividend: i32`

will render:


```
 fn divide divisor: i32, dividend: i32() {
     
 }
```



### Impl

Description:

> Default statement for extending a struct.

` impl rectangle`

will render:


```
 impl rectangle() {
     
 }
```



### Struct

Description:

` struct Rectangle`

will render:


```
 struct Rectangle() {
     
 }
```

` struct Room String`

will render:


```
 struct Roo// MARK: - String
```



### Enum

Description:

` enum Coins`

will render:


```
 enu// MARK: - Coins
```



### Variables

Description:

` var integer 36`

will render:


```
 <var>integer 36</var>
```

` var integer 36 usize m`

will render:


```
 <var>integer 36 usize m</var>
```



### Type Conversion

Description:

` conv integer f32`

will render:


```
 integer as f32
```



### main

Description:

` main`

will render:


```
 if __name__ == "__main__":
     
```



### Match

Description:

` match number`

will render:


```
 match number {
     
 }
```

` match number 3,7,22`

will render:


```
 match number {
     3 => ,
     7 => ,
     22 => ,
 }
```



