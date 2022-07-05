import requests

url = 'https://tianqi.2345.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
cookies = {
    'lastCountyPinyin': 'shenzhen',
}

r = requests.get(url, headers=headers, cookies=cookies)

print(r.text)

"""
<div class="item">
    <div class="pic">
        <em class="">1</em>
        <a href="https://movie.douban.com/subject/1292052/">
            <img width="100" alt="肖申克的救赎" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg" class="">
        </a>
    </div>
    <div class="info">
        <div class="hd">
            <a href="https://movie.douban.com/subject/1292052/" class="">
                <span class="title">肖申克的救赎</span>
                        <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
                    <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
            </a>
                <span class="playable">[可播放]</span>
        </div>
        <div class="bd">
            <p class="">
                导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
                1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
            </p>
            <div class="star">
                    <span class="rating5-t"></span>
                    <span class="rating_num" property="v:average">9.7</span>
                    <span property="v:best" content="10.0"></span>
                    <span>2634466人评价</span>
            </div>
                <p class="quote">
                    <span class="inq">希望让人自由。</span>
                </p>
        </div>
    </div>
</div>
"""