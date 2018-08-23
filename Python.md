# Python

## Commonly Used Python Expansions

Made by [@dustinknopoff](https://dustinknopoff.me)

### Included Expanders

- Function
- Request
- Regex
- Beautiful Soup
- Class
- In Tuple
- Open
- Shell in Python
- Main
- List Strings -> List Ints
- Global
- import
- Lambda
- String Slice
- Join

### Function

Description:

> Creates default function statement.

` -f do arr,index`

will render:


```python
 def do(arr, index):
     
```

` -f do`

will render:


```python
 def do():
     
```

Languages: ['python']



### Request

Description:

> Creates the default requests statement.

` req https://www.apple.com j`

will render:


```python
 r = requests.get("https://www.apple.com").json()
 
```

` req https://www.apple.com`

will render:


```python
 r = requests.get("https://www.apple.com")
 
```

Languages: ['python']



### Regex

Description:

> Default regex implementation:

` re \d+ str`

will render:


```python
 re.findall(r'd+', str)
```

> **NOTE: Must import `re`**

Languages: ['python']



### Beautiful Soup

Description:

> Creates default Beautiful Soup statement

` bs4 r.content`

will render:


```python
 soup = BeautifulSoup(r.content, 'html.parser')
 
```

> **NOTE: Must import `bs4`**

Languages: ['python']



### Class

Description:

> Creates a default class.

` class n Story`

will render:


```python
 class Story:
 
```

` class n Story title,details`

will render:


```python
 class Story:
     def __init__(title,details):
         self.title = title
         self.details = details
 
```

` class d Story`

will render:


```python
 @dataclass
 class Story:
 
```

` class d Story title:str,details:List[str]`

will render:


```python
 @dataclass
 class Story:
    title: str
    details: List[str]
 
```

> **NOTE: 'd' requires Python 3.7 and importing `dataclass`**

Languages: ['python']



### In Tuple

Description:

> Creates an if any statement:

` ifany ("Apple", "Banana", "Croissant")`

will render:


```python
 if any(w for w in ("Apple", "Banana", "Croissant")):
     
```

Languages: ['python']



### Open

Description:

> Creates default open statement.

` open ~/Downloads/example.txt`

will render:


```python
 with open('~/Downloads/example.txt') as f:
     
```

Languages: ['python']



### Shell in Python

Description:

> Creates default statement for shell scripts running in python.

` sh brew list`

will render:


```python
 script = subprocess.run("brew list".split(), stdout=subprocess.PIPE)
 
```

Languages: ['python']



### Main

Description:

` main`

will render:


```python
 if __name__ == "__main__":
     
```

` main Story().read()`

will render:


```python
 if __name__ == "__main__":
     Story().read()
```

Languages: ['python']



### List Strings -> List Ints

Description:

> Convert a list of strings into a list of integers

` [i] results`

will render:


```python
 results = list(map(int, results))
```

Languages: ['python']



### Global

Description:

> Creates the Shebang for global python usage

` gl 3.6`

will render:


```python
 #!/usr/bin/env python3.6
 
```

Languages: ['python']



### import

Description:

` @re`

will render:


```python
 import re
```

` @BeautifulSoup bs4`

will render:


```python
 from bs4 import BeautifulSoup
```

` @Dict,List typings`

will render:


```python
 from typings import Dict,List
```

Languages: ['python']



### Lambda

Description:

` -l x x*x`

will render:


```python
 lambda x: x*x
```

Languages: ['python']



### String Slice

Description:

> Can't remember where the `-` goes?

> If the number goes before or after the `:`? 

> Have TeaCode do it for you!

` -s s b lines 3`

will render:


```python
 lines[:3]
```

` -s e a lines 3`

will render:


```python
 lines[-3:]
```

> Ask yourself these questions:

> * Am I intending to slice this string from the start of end? 

> Use *s* for at the *start*, and *e* for at the *end*.

> * Am I intending to get everything before or after that index? 

> Use *b* for from *before*, and *a* for from *after*.

Languages: ['python']



### Join

Description:

> Join a list into a string

` -j lines , `

will render:


```python
 ', '.join(lines)
```

Languages: ['python']



