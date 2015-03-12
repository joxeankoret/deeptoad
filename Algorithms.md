# Algorithms #

As of December 2009, there are 4 algorithms implemented:

  * The default hashing algorithm.
  * A modified version of it which is faster but weaker.
  * A simplified version of the algorithm.
  * An experimental algorithm.

From this 4 algorithms only the DHA (Default Hashing Algorithm) and the FHA (Fast Hashing Algorithm) will remain as they're implemented, the other ones are subject to change.

# Algorithms #

All algorithms operate over blocks and are deterministic.

# The Default Hashing Algorithm (DHA) #

The Default Hashing Algorithm (or DHA for sort) is the default algorithm used by deeptoad. Basically, the algorithm computes the sums of the byte's modulo 255 discarding some blocks and, the output, is a mix of the resulted bytes from various blocks's sums.

At the moment, see the source for more details (kfuzzy.py, method "_hash")._

# The Faster version of the Hashing Algorithm (FHA) #

The other recommended algorithm, which works more or less in the same way is the faster version. It works the same way but operates in blocks depending on the signature's output size, not reducing the generated output to fit the desired signature's output size as the DHA works and, also, discards the last block to be analyzed.

At the moment, see the source for more details (kfuzzy.py, method "_fast\_hash")._

# The eXperimental Hashing Algorithm (XHA) #

This algorithm works like the DHA but the sum operation is replaced by a xor operation and, also, the next block size (except for the 1st block) is calculated from the block's xor. This is the weaker algorithm.

At the moment, see the source for more details (kfuzzy.py, method "