# Rust

## Common Rust Expansions

Made by [@dustinknopoff](https://dustinknopoff.me)



### Included Expanders

- [Fn](#fn)
- [Impl](#impl)
- [Struct](#struct)
- [Enum](#enum)
- [Variables](#variables)
- [Type Conversion](#type-conversion)
- [main](#main)
- [Match](#match)

### Fn

Description:

> Creates Rust default function template.

` fn main`

will render:


```rust
 def main():
     
```

` fn divide divisor: i32, dividend: i32`

will render:


```rust
 def divide(divisor: i32,  dividend: i32):
     
```

Languages: ['rust']



### Impl

Description:

> Default statement for extending a struct.

` impl rectangle`

will render:


```rust
 impl Rectangle {
     
 }
```

Languages: ['rust']



### Struct

Description:

` struct Rectangle`

will render:


```rust
 struct Rectangle {
     
 }
```

` struct Room String`

will render:


```rust
 struct Room<String> {
     
 }
```

Languages: ['rust']



### Enum

Description:

` enum Coins`

will render:


```rust
 enum Coins {
     
     
 }
```

` enum Coins Penny,Nickel,Quarter,Dime`

will render:


```rust
 enum Coins {
     Penny,
 Nickel,
 Quarter,
 Dime
     
 }
```

Languages: ['rust']



### Variables

Description:

` var integer 36`

will render:


```rust
 <var>integer 36</var>
```

` var integer 36 usize m`

will render:


```rust
 <var>integer 36 usize m</var>
```

Languages: ['rust']



### Type Conversion

Description:

` conv integer f32`

will render:


```rust
 integer as f32
```

Languages: ['rust']



### main

Description:

` main`

will render:


```rust
 if __name__ == "__main__":
     
```

Languages: ['rust']



### Match

Description:

` match number`

will render:


```rust
 match number {
     
 }
```

` match number 3,7,22`

will render:


```rust
 match number {
     3=> ,
 	7=> ,
 	22=> ,
 }
```

Languages: ['rust']



