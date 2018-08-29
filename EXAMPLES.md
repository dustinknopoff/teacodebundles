# EXAMPLES

## Sample expanders to learn the TeaCode Language.

Made by [twitter] @Apptorium

### Included Expanders

- [1. Simplest Expander](#1.-simplest-expander)
- [2. Variable](#2.-variable)
- [3. Variable with filter](#3.-variable-with-filter)
- [4. Optional Variable](#4.-optional-variable)
- [5. Hash](#5.-hash)
- [6. Exp](#6.-exp)
- [7. Enum](#7.-enum)
- [8. Switch](#8.-switch)

### 1. Simplest Expander

Description:

> Simplest example. Expands a short text.

` hw`

will render:


```
 hw() {
     
 }
```



### 2. Variable

Description:

> Uses a variable (`name`) to say `Hello` to the given person.

` h John`

will render:


```
 h John() {
     
 }
```



### 3. Variable with filter

Description:

> Uses a variable (`password`) as well as `sha1` and `md5` filters.

` pass sha1 samplepassword123`

will render:


```
 pas<s>sha1 samplepassword123</s>
```



### 4. Optional Variable

Description:

> Optional variables is very simple concept of having variables that does not have to be set.

` opt test`

will render:


```
 opt test() {
     
 }
```

` opt test 123`

will render:


```
 opt test 123() {
     
 }
```



### 5. Hash

Description:

> By default cursor goes at the end of the expanded expression. However it is possible to point that place using hash (`#`).

` block`

will render:


```
 block() {
     
 }
```



### 6. Exp

Description:

> TeaCode allows to use existing expanders using `exp` variable type.

` exp h Joe`

will render:


```
 ex<p>h Joe</p>
```



### 7. Enum

Description:

> Enums are helpful when pattern requires one of certain texts.

` enum a hello world`

will render:


```
 enu// MARK: - a hello world
```

` enum b hello world`

will render:


```
 enu// MARK: - b hello world
```



### 8. Switch

Description:

> Switch changes value of variable to the given one.

` switch a`

will render:


```
 switch a() {
     
 }
```

` switch other`

will render:


```
 switch other() {
     
 }
```



