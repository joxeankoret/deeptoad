# Usage scenarios for DeepToad #

DeepToad is a good tool for:
  * Looking for similar or almost equal files.
  * Search for partial matching files.
  * Clusterize batteries of files (i.e., malware samples).

However, it isn't designed for:
  * File integrity, like MD5, SHA-1, etc...

# Why use this tool if there is another one (ssdeep)? #

Because, sometimes, it works better than ssdeep and is easier & faster to modify the algorithms or the complete tool. See ["Working with changed files"](WorkingWithChangedFiles.md) for a brief (and not in any way in detail) comparison with ssdeep.

Also, you may prefer to use "deeptoad" because it's written in pure python and, as so, is quite easy and fast to adapt it to your needs and/or to use it in another project.