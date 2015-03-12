# Frequently Asked Questions #

### What is deeptoad? ###

DeepToad is a tool to generate fuzzy hashes for clustering and comparing similar files.

### What are the differences between a Cryptographic Hash and a Fuzzy Hash? ###

A cryptographic function tries to identify unequivocally one given input (i.e., tries to identify only one file). Extracted from the wikipedia, an ideal cryptographic hash function have 4 properties:
  1. it is easy to compute the hash value for any given message,
  1. it is infeasible to find a message that has a given hash,
  1. it is infeasible to modify a message without changing its hash,
  1. it is infeasible to find two different messages with the same hash.
A good fuzzy hashing function, in my opinion, must have the following properties:
  1. Minimal or no diffusion at all. A minimal change in the input should affect minimally to the generated output and only to the corresponding block of output, if it affects at all. In a good cryptographic hash, a minimal change in the input must change the complete hash.
  1. No confusion at all. Relationship between the key and the generated fuzzy hash are easy to identify, corresponding one to one. For example, a tiny change in the 1st block should change only the 1st generated output byte (if at all).
  1. A good collision's rate. The collision's rate must be defined by the application itself. For example, an high collision's rate maybe acceptable for spam detection but it may not be suitable for malware detection (due to high number of false positives).

### DeepToad loads the complete file in memory! ###

Yes, is a known issue. Support for big files is planned.

### Why DeepToad doesn't generate a signature for small files? ###

The file is too small for the specified block size and signature's output size. In example, to generate a 32 bytes signature operating over 512 bytes blocks, the file must have at least 512\*32 bytes, 16384 bytes. Try changing the block size or the signature's size.

### DeepToad is very slow! ###

You can use the provided SWIG extension, which greatly speeds it up. Use the version from the repository and compile the extension using the provided makefiles. The extension was provided by Thorsten Sick (Avira Gmbh).