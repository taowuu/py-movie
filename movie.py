class Movie(object):
    def __init__(self):
        self.name = ''
        self.score = 0
        self.quote = ''
        self.cover_url = ''
        self.ranking = ''
        self.country = ''
        self.type = ''
        self.year = ''


def read_by_binary(path):
    with open(path, 'rb') as f:
        s = f.read()
        return s


def write_by_binary(path, r):
    with open(path, 'wb') as f:
        f.write(r)


def get_response(url):
    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    r = requests.get(url, headers=headers)
    return r


def cached_url(url):
    folder = 'cached'
    filename = url.split('=', 1)[-1] + '.html'
    import os
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        return read_by_binary(path)
    else:
        if not os.path.exists(folder):
            os.makedirs(folder)
        r = get_response(url)
        r = r.text.encode()
        write_by_binary(path, r)
        return r


def movie_from_div(div):
    from pyquery import PyQuery as pq
    e = pq(div)
    m = Movie()
    m.name = e('.title').text().split(' ')[0]
    # print(e('.title').text().split(' ')[0])
    m.score = e('.rating_num').text()
    m.quote = e('.inq').text()
    m.cover_url = e('img').attr('src')
    m.ranking = e('.pic').find('em').text()
    import unicodedata
    ct = e('.bd').find('p').text()
    ct = unicodedata.normalize('NFKC', ct)
    # print(ct)
    m.year = ct.split('\n')[1].split(' / ')[0]
    # print(ct.split('\n')[1].split(' / ')[0])
    m.country = ct.split('\n')[1].split(' / ')[1].split(' ')
    # print(ct.split('\n')[1].split(' / ')[1].split(' '))
    type_arr = ct.split('\n')[1].split(' / ')[2].split(' ')
    # print(type_arr[0:len(type_arr)-1])
    # print(len(type_arr))
    m.type = type_arr[0:len(type_arr)-1]
    return m


def movies_from_url(url):
    page = cached_url(url)
    from pyquery import PyQuery as pq
    e = pq(page)
    items = e('.item')
    movies = [movie_from_div(i) for i in items]
    return movies


def save_to_db(data, db_path):
    import json
    b = json.dumps(data, indent=4, ensure_ascii=False)
    with open(db_path, 'w+', encoding='utf-8') as f:
        f.write(b)


def download_cover(url):
    folder = "img"
    name = url.split("/")[-1]
    import os
    path = os.path.join(folder, name)
    if not os.path.exists(folder):
        os.makedirs(folder)
    if os.path.exists(path):
        return
    r = get_response(url)
    write_by_binary(path, r.content)


def save_movie():
    ls = []
    db_path = './data/movie.json'
    #
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}'.format(i)
        movies = movies_from_url(url)
        [download_cover(m.cover_url) for m in movies]
        for m in movies:
            ls.append(m.__dict__)
    save_to_db(ls, db_path)


def main():
    save_movie()


if __name__ == '__main__':
    main()
