charName = {
    'D.VA':                 '英語：D.Va    韓国語：D.Va',
    'オリーサ':             '英語：Orisa    韓国語：오리사',
    'ラインハルト':         '英語：Reinhardt    韓国語：라인하르트',
    'ロードホッグ':         '英語：Roadhog    韓国語：로드호그',
    'シグマ':               '英語：Sigma    韓国語：시그마',
    'ウィンストン':         '英語：Winston    韓国語：윈스턴',
    'レッキング・ボール':   '英語：Wrecking Ball    韓国語：레킹볼',
    'ザリア':               '英語：Zarya    韓国語：자리야',
    'アッシュ':             '英語：Ashe    韓国語：애쉬',
    'バスティオン':         '英語：Bastion    韓国語：바스티온',
    'ドゥームフィスト':     '英語：Doomfist    韓国語：둠피스트',
    'ゲンジ':               '英語：Genji    韓国語：겐지',
    'ハンゾー':             '英語：Hanzo    韓国語：한조',
    'ジャンクラット':       '英語：Junkrat    韓国語：정크랫',
    'マクリー':             '英語：McCree    韓国語：맥크리',
    'メイ':                 '英語：Mei    韓国語：메이',
    'ファラ':               '英語：Pharah    韓国語：파라',
    'リーパー':             '英語：Reaper    韓国語：리퍼',
    'ソルジャー76':         '英語：Soldier:76    韓国語：솔저:76',
    'ソンブラ':             '英語：Sombra    韓国語：솜브라',
    'シンメトラ':           '英語：Symmetra    韓国語：시메트라',
    'トールビョーン':       '英語：Torbjörn    韓国語：토르비욘',
    'トレーサー':           '英語：Tracer    韓国語：트레이서',
    'ウィドウメイカー':     '英語：Widowmaker    韓国語：위도우메이커',
    'アナ':                 '英語：Ana    韓国語：아나',
    'バティスト':           '英語：Baptiste    韓国語：바티스트',
    'ブリギッテ':           '英語：Brigitte    韓国語：브리기테',
    'ルシオ':               '英語：Lúcio    韓国語：루시우',
    'マーシー':             '英語：Mercy    韓国語：메르시',
    'モイラ':               '英語：Moira    韓国語：모이라',
    'ゼニヤッタ':           '英語： Zenyatta    韓国語 ： 젠야타',
    'エコー':               '英語： Echo    韓国語 ： 에코'
    }

def transName(message):
    message = subMessage(message)

    try:
        return charName[message]
    except KeyError:
        return ('存在しないキャラ名だよ😱')

# メンション部分を削除
def subMessage(message):
    return message.replace('@ow-translate ', '')