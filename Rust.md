# Rust

## Common Rust Expansions

Made by [twitter] @dustinknopoff



### Fn

Description:

> Creates Rust default function template.

` fn main`

will render:


```
 def main():
     ```

` fn divide divisor: i32, dividend: i32`

will render:


```
 def divide(divisor: i32, dividend: i32):
     ```



### Impl

Description:

> Default statement for extending a struct.

` impl rectangle`

will render:


```
 impl Rectangle {
     
 }```



### Struct

Description:

` struct Rectangle`

will render:


```
 struct Rectangle {
     
 }```

` struct Room String`

will render:


```
 struct Roo// MARK: - String```



### Enum

Description:

` enum Coins`

will render:


```
 enum Coins {
     
 }```



### Variables

Description:

` var integer 36`

will render:


```
 private final integer 36;
 ```

` var integer 36 usize m`

will render:


```
 private final integer 36 usize m;
 ```



### Type Conversion

Description:

` conv integer f32`

will render:


```
 integer as f32```



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
      => 
 }```



