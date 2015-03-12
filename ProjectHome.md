"Deeptoad" is a (python) library and a tool to clusterize similar files using fuzzy hashing techniques. This project is inspired by the well known tool [ssdeep](http://ssdeep.sourceforge.net/).

Current Version is 1.2.0 (as of 2010-01-23).

```
ChangeLog:
  * DeepToad now considers big files those bigger than 32 MB.
  * When using the argument "-p" hashes are printed as soon as they are computed.
  * Added python interfaces compatibles with the hashing algorithms of hashlib, like md5 or sha1. They are: kdha, kfha and ksha.
  * Fixed a lot of bugs.
  * Added support for "somewhat more" big files.
  * Added the "spam" mode to the deeptoad tool.
  * Fixed a bug in the calculation of the edit distance.
  * Changes in the experimental algorithm.
```
