# PassGuesser

Generates all possible passwords that match a given pattern

If you forget a password, you sometimes still remember some details about it, like the first few letters, at which positions numbers are or how long the password is. This little Python script lets you define such a pattern and computes a list of all possible words that match that pattern. This list can then be used by brute force tools.

## Usage

Since this tool was primarily created for my personal use, usage is not very comfortable and easiest via command line.

Start the Python cli and import the module

```
import passguesser as pg
```

You can specify a pattern as a tuple. Each element specifies a set of possible combinations. The function `wordlist` creates a generator from that tuple that outputs all possible combinations.

The simplest element is just a String and will not be expanded. It is useful if you still remember exactly a part of your password. It is not very useful on its own of course.

```
pattern = ("Password",)
```

The function `comb` can be used as an element of the pattern to represent all combinations of some characters.
The first argument specifies the set of characters that the possible strings are made of. You can either provide a string containing a combination of `n`, `l` and `u`, representing numbers, lowercase and uppercase letters, respectively. Alternatively you can provide a custom list of strings that will be combined.
The second argument specifies the length of the strings. You can either pass a single integer or a list of integers.

Examples:

Passwords that begin with "Pass", followed by 4 numbers.
```
pattern = ("Pass",pg.comb("n", 4))
```

Totally random 8-character passwords that consist of numbers and letters.
```
pattern = (pg.comb("nlu", 8))
```

Passwords that begin with "Ab" , followed by 3 uppercase letters and by up to 4 numbers lower then 6.
```
pattern = ("Ab", pg.comb("u", 3), pg.comb(range(6), range(5)))
```

When you are done specifying your pattern, use `wordlist` to get the generator for all possible passwords and write it to a file via `writeWordlist`.
```
wordlistGen = pg.wordlist(pattern)
pg.writeWordlist(wordlistGen,"wordlist.txt")
```
