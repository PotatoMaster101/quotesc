# Quote Escape
Escapes inner and outer quotes in a string based on their location. 

# Usage
Syntax: 
```
$ python3 quotesc.py [-h] [-f] [-q QUOTE] [-l LVL] [-o OUTF] input
```

Escape double quotes from a simple file: 
```
$ cat test.txt
"x"xx"xxx"xx"x"
$ python3 quotesc.py -f test.txt
"x\"xx\\\"xxx\\\"xx\"x"
```

Escape double quotes from CLI input: 
```
$ python3 quotesc.py '"a"b"c"'
"a\"b\"c"
```

Change initial escape level: 
```
$ python3 quotesc.py '"a"b"c"' -l 2
\\\"a\\\\\\\"b\\\\\\\"c\\\"
```

Escape other characters instead of double quotes: 
```
$ python3 quotesc.py "'a'b'c'" -q \'
'a\'b\'c'
```

Reset the escape level on newline characters: 
```
$ cat test.txt
"x"xx"xxx"xx"x"
"x"xx"xxx"xx"x"
"x"xx"xxx"xx"x"
"x"xx"xxx"xx"x"
"x"xx"xxx"xx"x"
"x"xx"xxx"xx"x"
"x"xx"xxx"xx"x"
"x"xx"xxx"xx"x"
$ python3 quotesc.py -f test.txt -r
"x\"xx\\\"xxx\\\"xx\"x"
"x\"xx\\\"xxx\\\"xx\"x"
"x\"xx\\\"xxx\\\"xx\"x"
"x\"xx\\\"xxx\\\"xx\"x"
"x\"xx\\\"xxx\\\"xx\"x"
"x\"xx\\\"xxx\\\"xx\"x"
"x\"xx\\\"xxx\\\"xx\"x"
"x\"xx\\\"xxx\\\"xx\"x"
```

Write output to file: 
```
$ python3 quotesc.py '"e"s"c"a"p"e"m"e"!"' -o output.txt
$ cat output.txt
"e\"s\\\"c\\\\\\\"a\\\\\\\\\\\\\\\"p\\\\\\\\\\\\\\\"e\\\\\\\"m\\\"e\"!"
```

