# Python

## Commonly Used Python Expansions

Made by [twitter] @dustinknopoff

### Function

Description:

> Creates default function statement.

` fn do arr`



```python
 fn do(arr) {
     
 }
```

` fn do`



```python
 fn do() {
     
 }
```

Languages: ['python']



### Request

Description:

> Creates the default requests statement.

` req https://www.apple.com j`



```python
 req https://www.apple.co// MARK: - j
```

` req https://www.apple.com `



```python
 r = requests.get("https://www.apple.com ")
 
```

Languages: ['python']



### Regex

Description:

> Default regex implementation:

` re \d+ str`



```python
 re.findall(r'd+', str)
```

> **NOTE: Must import `re`**

Languages: ['python']



### Beautiful Soup

Description:

> Creates default Beautiful Soup statement

` bs4 r.content`



```python
 soup = BeautifulSoup(r.content, 'html.parser')
 
```

> **NOTE: Must import `bs4`**

Languages: ['python']



### Class

Description:

> Creates a default class.

` class Story`



```python
 class Story:
     def __init__(self):
         
```

Languages: ['python']



### In Tuple

Description:

> Creates an if any statement:

` ifany ("Apple", "Banana", "Croissant")`



```python
 if any(w for w in ("Apple", "Banana", "Croissant")):
     
```

Languages: ['python']



### Open

Description:

> Creates default open statement.

` open ~/Downloads/example.txt`



```python
 with open('~/Downloads/example.txt') as f:
     
```

Languages: ['python']



### Shell in Python

Description:

> Creates default statement for shell scripts running in python.

` sh brew list`



```python
 script = subprocess.run("brew list".split(), stdout=subprocess.PIPE)
 
```

Languages: ['python']



### Main

Description:

` main`



```python
 fn main() {
     
 }
```

` main Story().read()`



```python
 if __name__ == "__main__":
     Story().read()
```

Languages: ['python']



### List Strings -> List Ints

Description:

> Convert a list of strings into a list of integers

` [i] results`



```python
 results = list(map(int, results))
```

Languages: ['python']



### Global

Description:

> Creates the Shebang for global python usage

` gl 3.6`



```python
 #!/usr/bin/env python3.6
 
```

Languages: ['python']



