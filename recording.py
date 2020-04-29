import random
import sounddevice as sd
from scipy.io.wavfile import write
import time

mylist=['khoong','moojt','hai','ba','boosn','tuw','nawm','lawm','sasu','bary','tasm','chisn','muowfi','muowi','phaary','coojng','truwf','nhaan','chia','mux','cawn','aam','mowr','ddosng','ngoawjc']
thisdict={
'khoong':'không',
'moojt':'một',
'hai':'hai',
'ba':'ba',
'boosn':'bốn',
'tuw':'tư',
'nawm':'năm',
'lawm':'lăm',
'sasu':'sáu',
'bary':'bảy',
'tasm':'tám',
'chisn':'chín',
'muowfi':'mười',
'muowi':'mươi',
'phaary':'phẩy',
'coojng':'cộng',
'truwf':'trừ',
'nhaan':'nhân',
'chia':'chia',
'mux':'mũ',
'cawn':'căn',
'aam':'âm',
'mowr':'mở',
'ddosng':'đóng',
'ngoawjc':'ngoặc',
}
ii=0
while(1):
	print("\n Get ready")
	time.sleep(5)
	random.shuffle(mylist)
	for i in mylist:
		print(thisdict.get(i))
	fs = 16000  # Sample rate
	seconds = 17  # Duration of recording

	myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
	print("-----")
	sd.wait()  # Wait until recording is finished
	write('%d.wav' % ii, fs, myrecording)  # Save as WAV file
	print("saved record %d.wav" %ii)

	with open("trans.txt", "a") as f:
		f.write("\n%d" % ii)
		for item in mylist:
			f.write(" %s" % item)
	ii=ii+1

