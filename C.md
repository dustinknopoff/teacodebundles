# C

## Common C Expansions

Made by [@dustinknopoff](https://dustinknopoff.me)

### Included Expanders

- [Include](#include)
- [main](#main)
- [typedef](#typedef)
- [define](#define)
- [while](#while)
- [switch](#switch)
- [Struct](#struct)
- [String copy](#string-copy)
- [function](#function)
- [Scope](#scope)
- [assert](#assert)
- [print](#print)
- [String equality](#string-equality)
- [string contains](#string-contains)
- [array size](#array-size)

### Include

Description:

` # s`

will render:


```c
 #include <stdio.h>
 
```

` #math.h s`

will render:


```c
 #include <math.h>
 
```

` #foo.h u`

will render:


```c
 #include "foo.h"
 
```

Languages: ['c']



### main

Description:

` main`

will render:


```c
 int main(int argv, char *argv[]) {
     
     return 0;
 }
```

Languages: ['c']



### typedef

Description:

` td struct fraction Fraction`

will render:


```c
 typedef struct fraction Fraction;
 
```

Languages: ['c']



### define

Description:

` -d BOOL char`

will render:


```c
 #define BOOL char
 
```

Languages: ['c']



### while

Description:

` w i - 10`

will render:


```c
 while (i - 10) {
     
 }
```

Languages: ['c']



### switch

Description:

` switch stringtype`

will render:


```c
 switch (stringtype) {
     case :
         
         break;
     default:
         
         break;
 }
 
```

Languages: ['c', 'java', 'js']



### Struct

Description:

` struct Store`

will render:


```c
 struct Store {
     
 }
```

Languages: ['c']



### String copy

Description:

` len usrInput`

will render:


```c
 strlen(usrInput)
```

Languages: ['c']



### function

Description:

` fn + int power int base, int n`

will render:


```c
 int power(int base, int n);
 int power(int base, int n) {
  	
 	return ;
 }
```

Languages: ['c']



### Scope

Description:

Languages: ['c']



### assert

Description:

> **NOTE: must include #include <assert.h>**

` assert i > MAX_INTS`

will render:


```c
 assert(i > MAX_INTS);
 
```

Languages: ['c']



### print

Description:

Languages: ['c']



### String equality

Description:

` usrInput == "Charlie Day"`

will render:


```c
strcmp( usrInput,"Charlie Day")
```

Languages: ['c']



### string contains

Description:

` "Hello World".contains("orld")`

will render:


```c
strstr( "Hello World","orld")
```

Languages: ['c']



### array size

Description:

` size int_array int`

will render:


```c
 (sizeof(int_array) / sizeof(int))
```

Languages: ['c']



