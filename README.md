# XECryption crack #

Not the kind of encryption anyone would use these days (I hope), but works as an exercise.

XECryption encoding is a symmetric cryptography method that uses a password of ASCII chars
and produces a list of ~~mostly~~ random numbers separated by dots.

The password key is obtained by adding together all the ASCII codes of each character
of the password. The resulting number is used by both the encoding and the decoding
algorithms. The crack process is to find a shortcut to guess the key number, and not
the password (wich is irrelevant - any password that sums to the same key would work for
decryption).

## The encryption process ##

The encryption of a character by this method works as follows:

1- The key is added to the ASCII code of the character and the result id divided by 3
(integer division);
2- The first and second numbers are obtained by adding the result of the division to a
random number between -10 and 10;
3- The third number is calculated by the difference of the sum (ASCII + key) and the added
two first numbers.

An encrypted message is composed by all the numbers (in sequence) of each character
separated by dots.

## The decryption process ##

It is easy to see that this algorithm is designed to ensure that the sum of the three
numbers of the encoded character is equal to the sum of the ASCII code of the character
and the key.

The decryption process, then, starts by adding the numbers in groups of three, subtracting
the key (obtained from the same password, wich the receiver must ~~cough cough~~ know) and
then converting the resulting numbers to the corresponding ASCII characters.

## The crack process ##

If one happens to stumble on an encrypted message that uses this method and has absolutely
no idea of what is XECryption, it might just look like a mess of random numbers, and that
is probably good for the careless messenger who lost the piece of information. However,
since XECryption is well known and is that simple to decrypt, a trial and error method
might be enough to crack this message. Yes, simply trying every possible key number to
see if the resulting decrypted message makes sense.

The first step is to add toghether the numbers in groups of three, the same way the
legitimate decryption process would.

First of all, there is a maximum possible number for this key, wich is the smaller result
of the sums (if the key was bigger than that, it would mean that this character has a
negative ASCII code, wich is impossible). This number is tried as a key to see if the
resulting message makes any sense. If not, the key is subtracted by 1 and the decryption
attempt is repeated with the new key, and so on until a real message is obtained.

It looks like it could be made on a paper, with a pen and a lot of patience - and, as a
matter of fact, it could.