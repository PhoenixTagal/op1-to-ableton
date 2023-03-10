# op1-to-ableton
op1-to-ableton is a light weight wav file converter which makes wav files bounced from the op1 field ready for use in Ableton!

#
**Why use ob1-to-ableton?**

OP1 Field currently exports a 32-bit wav PCM file.

Ableton does not currently support 32-bit *integer* wav PCM files. Ableton does support 32-bit float Little Endian wav files.

A common workardound ableton reccomends is to bring the 32-bit wav PCM file into Audacity and convert it to a 32-bit *float* wav file. Which falls into the Ableton supported 32-bit float Little Endian wav format. 

op1-to-ableton makes this conversion in a lightweight software rather than opening up a seperate DAW.
#


**32-bit wav PCM file in Ableton:**

<p align="center">
  <img src="https://github.com/PhoenixTagal/op1-to-ableton/blob/main/test/unsupported_file_master.png"/>
</p>

You'll notice intense clipping that essentially breaks ableton. Faders will not work when trying to manipulate 32-bit wav PCM files in Ableton. 
This is most likely attributed to the larger noise floor of a 32-bit wav PCM file. 

**32-bit float wav file in Ableton:**
<p align="center">
  <img src="https://github.com/PhoenixTagal/op1-to-ableton/blob/main/test/supported_file_master.png"/>
</p>


The 32-bit float wav file has a smaller noise floor and you can see that when the file is brought in, the level ususally stays between -12db to -2db when initially imported into a session. 

Faders are workable with a 32-bit float wav file and the signal can be boosted or attenuated to the users desired level. 
#
