# Python Fundamentals and Best Practices   
## Best Practices   
### The PEP8 Style Guide   
The [PEP8 Style Guide](https://peps.python.org/pep-0008/) is a document outlining the Python coding conventions. Following the PEP8 style guide allows Python developers to write more "Pythonic" code.   

#### Indentations   
* PEP8 calls out the use of using **4 spaces per indentation level**. 
* Spaces are preferred over tabs, unless the code is already indented with tabs.
* Most code editors can be set to replace tabs with spaces.

#### Line Length
* Lines of code should be limited to a maxmimum of 79 characters. 
* [Black](https://github.com/psf/black) and [pylint](https://pylint.pycqa.org/en/latest/) are both useful tools for finding and correcting lines are that are too long.

#### Naming Conventions
* Functions should be lowercase with words sperated by underscores as necessary. (ex: get_device_info)
  * If using acronyms, preserve the capitalziation (ex: get_OSPF_neighbors)
* Variables should follow the same convention as functions. (ex: ip_address, device_list)
* Classes should use CapWords/CamelCase (ex: NetworkDevice)
* Constants should be all capitals with underscores separating words (ex: MAX_LENGTH).
* Package and Module names should be short and all lowercase with underscores separating words. (my_math_stuff.py)
* Single letters: Never use lowercase l (el), uppercase I (eye), uppercase O (oh). These can be ambiguous and are best avoided. 

#### Comments
* Comments should be complete sentences.
* Use two spaces between sentences for multi-line comments.
* Inline comments should be used sparingly
   ```python
   ip_address = get_ip_address()     # This is an inline comment
   ```
* Comments should always be up to date with the code. Inaccurate comments are worse than no comments.

#### Imports
* Imports should generally be on separate lines.
* Imports always go on top of the file, just after any module comments or docstrings.
* Import order matters:
  * Standard library imports come first.
  * Related third party imports come second.
  * Local application/library specific imports come last.
* Imports should be in alphabetical order.
* Blank lines are often used to separate standard library and third party imports.

Example Imports:
```python
"""
Module docstring...
"""

import getpass
import os

import rich
import scrapli

from network_devices import router1

...
```

## The Zen of Python
```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```


