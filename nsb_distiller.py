import codecs
import re
import os



folder_path = 'nss/'
extension = '.nsb'
keyword_str = 'voice/CRS_'


out_path = "distilled_nsb.txt"
with open(out_path, 'w') as out:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)

                with codecs.open(file_path, mode='r', encoding='SHIFT_JIS', errors='replace') as f:
                    data = f.read()
                    matches = [(match.start(), match.end()) for match in re.finditer(keyword_str, data)]

                for start, end in matches:
                    voice_idx = re.search('\d+', data[end:])
                    sp = data[end:].find("「")
                    ep = data[end:].find("」")
                    out.write("voice/CRS_{idx} {stence}\n".format(idx = voice_idx.group(), stence = data[end + sp + 1 : end + ep]))
