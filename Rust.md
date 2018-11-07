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
- [Attr](#attr)
- [Mod](#mod)
- [Print](#print)
- [Par Iter](#par-iter)
- [to JSON](#to-json)
- [to String](#to-string)
- [Open](#open)

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

` impl rectangle Iterator`

will render:


```rust
 impl Rectangle Iterator {
     
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

` var totalSize 36 usize m`

will render:


```rust
 <var>totalSize 36 usize m</var>
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



### Attr

Description:

` attr -d Debug`

will render:


```rust
 #[derive(Debug)]
 
```

` attr -c tests`

will render:


```rust
 #[cfg(Tests)]
 
```

Languages: ['rust']



### Mod

Description:

` mod Docs`

will render:


```rust
 mod Docs {
     
 }
```

Languages: ['rust']



### Print

Description:

` print "{}", x`

will render:


```rust
 System.out.println("{}", x);
 
```

Languages: ['rust']



### Par Iter

Description:

` parit array_of_strings`

will render:


```rust
 array_of_strings.par_iter().map(x {
     
 });
```

Languages: ['rust']



### to JSON

Description:

` 2json result`

will render:


```rust
 serde_json::to_string_pretty(&result)
```

Languages: ['rust']



### to String

Description:

` toS "Hi"`

will render:


```rust
 "Hi".to_string()
```

Languages: ['rust']



### Open

Description:

` open p`

will render:


```rust
 with open('p') as f:
     
```

` open ~/Documents/Gits/test.py`

will render:


```rust
 with open('~/Documents/Gits/test.py') as f:
     
```

Languages: ['rust']



