**Requirements**

You should create a function, 'word\_count\_summary', which has the following features:

- Accept two arguments `file_path` and `search_terms`.
    - The first argument is the name (and path) of a file containing text.
    - The second argument is the word that is being searched for, which should be of type `str`.
- Search through the file for occurrences of the specified word.
    - The word should only be counted when it appears as a whole word. For example, when searching for `hope`, the
      word `orthopedic` should not count as a match.
    - To keep things simple, a word is defined as a continuous sequence of characters from the ranges A–Z, a–z, 0–9, and
      the underscore (`_`) character. All other characters should be ignored. Hence, `they're` counts as two separate
      words `they` and `re`.
- Return the results as a string.
    - The message printed should have the form "The word 'word' appears n time(s)."
    - For example:

``` The word 'animal' appears 17 times. ```

``` The word 'lugubrious' appears 1 time. ```

- Support searching for multiple words at once.
    - The second argument `search_terms` can be a list of strings instead of a single string – it should work with
      either type of input.
    - If a list is given as input, instead of printing the message specified above, the results should be shown as a
      table in the following form:

|---------|-------|
| WORD    | COUNT |
|---------|-------|
| round   |    17 |
| ability |     0 |
| enemy   |     1 |
|---------|-------|
| TOTAL   |    18 |
|---------|-------|

- The columns in this view should adapt to the lengths of the words and numbers it contains: they should be wide enough
  to display all words and numbers with at least one space on either side, as shown.
- Words and column-headers should be left-aligned, while numbers should be right-aligned.

**Resources allowed**

In this practical, you must solve the problem without importing any library except `re`. Many Python libraries exist for
solving problems like this, some of which would make this problem trivial – we want you to gain experience solving
problems and thinking algorithmically for yourself, rather than just learning to import and call the right function!

**Hints**

If you have watched the advised set of lectures preceding this practical, you have covered everything that you need for
this practical. If you get stuck, you may want to review some of the lecture notebooks or videos, especially those on
Files and Regular expressions.

You may also find it useful to look up other features online in Python. So long as your solution is your own, it's okay
to look up features in the documentation and educational resources.

We have provided you with two pieces of example text which you can use to test your program. The files are
included [here](https://pgt-digital.st-andrews.ac.uk/mod/folder/view.php?id=2386).

When running your program on files in different directories remember to use the absolute or relative path to the file.
For instance, if you are running your program from `CS5901-p1-wordcounter/src` but your text files are
in `CS5001-p1-wordcounter`, you could use the following function call, specifying the relative path
to `pride_and_prejudice.txt`, to search through the file for occurrences of the word "Elizabeth":

``` word_count_summary("../pride_and_prejudice.txt", "Elizabeth") ```

Note: you must include the quote marks around the file name if there are spaces in the file name/path.

The expected output of a few examples is shown in Appendix A: Sample runs. You can find further examples of output by
examining the tests provided (see Automated checking below).

**Notebook format**

Your solution should be submitted as a single Jupyter notebook in `.ipynb` format. This notebook should contain all your
code, along with a title and subheadings, text cells explaining your solution, and a Testing section. The Testing
section should show a set of calls to your `word_count_summary` function (perhaps 10 or so different calls), showing the
function's output in various situations, and demonstrating that it works correctly.

Your notebook should be \*reproducible\*, meaning that we should be able to re-run it and produce the same outputs you
did. You can make sure that this is the case by using the "fast-forward" button at the top of your Jupyter interface,
which restarts the kernal and re-runs the whole notebook from scratch.

Aside from a robust solution that performs correctly, we also want code that has good style. Some things you can do to
improve your grade are:

- decompose your code into small functions that call each other
- use meaningful identifiers
- avoid code repetition
- avoid "magic numbers"
- include comments where appropriate.

A solution that works correctly may not receive a high grade if it has poor style; conversely, an incomplete solution
can still receive a good grade if it shows sufficient understanding and good style.

If you have attempted any enhancements beyond those mentioned in this specification, you should explain them fully in
your notebook. You should describe what you have done, including any instructions for using additional features.

**Submission**

Upload the following item via
the [Assignment 1 submission point](https://pgt-digital.st-andrews.ac.uk/mod/assign/view.php?id=2179):

1. a single Jupyter notebook in `.ipynb` format
