# Python

## Commonly Used Python Expansions

Made by [twitter] @dustinknopoff

### Function

Description:

> Creates default function statement.

` fn do arr`



```
 fn do(arr) {
     
 }
```

` fn do`



```
 fn do() {
     
 }
```

Languages: ['python']



### Request

Description:

> Creates the default requests statement.

` req https://www.apple.com j`



```
 req https://www.apple.co// MARK: - j
```

` req https://www.apple.com `



```
 r = requests.get("https://www.apple.com ")
 
```

Languages: ['python']



### Regex

Description:

> Default regex implementation:

` re \d+ str`



```
 re.findall(r'd+', str)
```

> **NOTE: Must import `re`**

Languages: ['python']



### Beautiful Soup

Description:

> Creates default Beautiful Soup statement

` bs4 r.content`



```
 soup = BeautifulSoup(r.content, 'html.parser')
 
```

> **NOTE: Must import `bs4`**

Languages: ['python']



### Class

Description:

> Creates a default class.

` class Story`



```
 class Story:
     def __init__(self):
         
```

Languages: ['python']



### In Tuple

Description:

> Creates an if any statement:

` ifany ("Apple", "Banana", "Croissant")`



```
 if any(w for w in ("Apple", "Banana", "Croissant")):
     
```

Languages: ['python']



### Open

Description:

> Creates default open statement.

` open ~/Downloads/example.txt`



```
 with open('~/Downloads/example.txt') as f:
     
```

Languages: ['python']



### Shell in Python

Description:

> Creates default statement for shell scripts running in python.

` sh brew list`



```
 script = subprocess.run("brew list".split(), stdout=subprocess.PIPE)
 
```

Languages: ['python']



### Main

Description:

` main`



```
 fn main() {
     
 }
```

` main Story().read()`



```
 if __name__ == "__main__":
     Story().read()
```

Languages: ['python']



### List Strings -> List Ints

Description:

> Convert a list of strings into a list of integers

` [i] results`



```
 results = list(map(int, results))
```

Languages: ['python']



### Global

Description:

> Creates the Shebang for global python usage

` gl 3.6`



```
 !/usr/bin/env python3.6
 #
```

Languages: ['python']



