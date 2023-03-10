import soundfile as sf
import numpy as np

unsupported_file = 'track_2.wav'
supported_file = 'supported_track_2.wav'

# passing 'float32' as argument for dtype parameter converts from original file datatype
data, samplerate = sf.read(unsupported_file, dtype='float32')

# imported wav file properties
print('data is list of numpy.ndarrays \n')
print('each element of list holds 2 numpy.float-x objects, x is determined by dtype parameter')
print('data:', data, '\n')
print('length of data:', len(data))
print('object type of data variable:', type(data))
print('sample rate:', samplerate)

# looking at array dimensions of data
data_array_info = np.asarray(data)
print('tuple specifiying size of each dimension of the var data array:', data_array_info.shape)

# looking at class type of elements within ndarray of imported wav file
print(data[1])
for i in data[1]:
    print(type(i))
    print(type(float(i)))

# writing new file with new data type established in sf.read() args
# saves file to working directory
sf.write(data=data,
         samplerate=samplerate,
         endian='LITTLE',
         file=supported_file)
