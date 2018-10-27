# TeaCode Bundles

This repo includes my bundles and a markdown version of them.

**NOTE: Requires Python 3+**

To create your own:

1. clone this repo and delete all files except `.gitignore` and `autogeneratemd.py`. 
3. Run `python autogeneratemd.py`.

`autogeneratemd.py` generates it's previews from the description field on expanders. Therefore, to include an example showing the syntax and output requires including an example in the description field.

For example the description for an expander for making functions in python would look something like this:

> Creates default function statement.
> 
> \> -f do arr
> 
> \> -f do

which will be shown in the output markdown file as:

> Creates default function statement.

` -f do arr`

will render:


```python
 def do(arr):
     
```

` -f do`

will render:


```python
 def do():
     
```
