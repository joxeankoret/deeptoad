# Basic Arguments #

`-`e=extensions
  * The specified extensions (the character '.' is needed) are excluded from the analysis.
`-`i=extensions
  * Only the specified extensions will be analyzed.
`-`m=value
  * Specifies the maximum number of files to be hashed.
`-`d=distance
  * When comparing, it specifies the minimum Levenhstein distance to consider that 2 files are similar.
`-`ida
  * Ignore files created by IDA (IDB, ID0, ID1, TIL and NAM).
`-`p
  * Simply prints out the hashes and the filenames without doing any kind of comparison or sorting.
`-`c
  * Compare the files and print the similarity percent between the files.
`-`echo=msg
  * Simply, prints a message via STDOUT. Usefull to generate "reports" when using multiple algorithms and modifications in the same command line.

# Advanced Arguments #

`-`b=block size
  * The algorithms will operate in blocks of the specified size.
`-`r=ignore range
  * Specify the range of bytes to be ignored by the default hashing algorithm.
`-`s=output size
  * Specify the signature's size. By default is 32 bytes.
`-`f
  * Use the fastest algorithm. The default hashing algorithm and this one are the unique algorithms not subject to change.
`-`x
  * Use eXperimental algorithm. It's, right now, the weakest one. Subject to change.
`-`simple
  * Use the simplified algorithm. Subject to change.
`-`na
  * Use non aggressive method (do not discard too many blocks). It's only applicable to the default hashing algorithm.
`-`ag
  * Use aggressive method (discard many blocks). It's the default but maybe usefull to reset the aggressivenes flag when mixing many arguments in the same command line.
`-`nb
  * Ignore null blocks. When this flag is active, any block that match the rule SUM(block\_bytes) % 255 == 0 is discarded.
`-`cb
  * Consider null blocks. The opposite to `-`nb.
