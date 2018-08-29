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

` -f main`

will render:


```rust
 def main():
     
```

` -f divide divisor: i32, dividend: i32`

will render:


```rust
 def divide(divisor: i32,  dividend: i32):
     
```

Languages: ['rust']



### Impl

Description:

> Default statement for extending a struct.

` -i rectangle`

will render:


```rust
 impl Rectangle {
     
 }
```

Languages: ['rust']



### Struct

Description:

` -s Rectangle`

will render:


```rust
 suct Rectangle {
     
 }
```

` -s Room String`

will render:


```rust
 suct Room<String> {
     
 }
```

Languages: ['rust']



### Enum

Description:

` -e Coins`

will render:


```rust
 enum Coins {
     
 }
```

Languages: ['rust']



### Variables

Description:

` -v integer 36`

will render:


```rust
 private final integer 36;
 
```

` -v integer 36 usize m`

will render:


```rust
 private final integer 36 usize m;
 
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
     3 => ,
     7 => ,
     22 => ,
 }
```

Languages: ['rust']



