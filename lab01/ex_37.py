# ex_37.py

en2ko = {
    'book' : '책',
    'snake' : '뱀',
    'language' : '언어'
}

ko2en = {}

for eng,kor in en2ko.items():
    ko2en[kor] = eng

print(ko2en)
