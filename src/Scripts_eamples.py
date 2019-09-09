# get hash
def calc_hash_crc(filename):
    """Calculate hash and crc32 of selected file"""
    data = open(filename, 'rb').read()
    fhash = hashlib.sha256(data).hexdigest()
    fcrc = zlib.crc32(data)
    return {'sha256': fhash, 'crc32' : fcrc}


# save csv
keys = ['name', 'grbs', 'budget2021']
def save(filename, data):
    wr = csv.DictWriter(open(filename, 'w', encoding='utf8'), fieldnames=keys)
    wr.writeheader()
    for r in data:
        wr.writerow(r)


# date
start_date = datetime.date(2019, 1, 1)
    end_date = datetime.datetime.now().date()
    delta = end_date - start_date
    daterange = []
    for i in range(delta.days + 1):
        ad = start_date + datetime.timedelta(days=i)
        daterange.append(ad)
