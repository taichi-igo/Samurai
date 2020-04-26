#２．コーヒーの注文を出力
#入力:
#キーワード引数
#suger,  指定しない or ("なし"、"少なめ"、"普通"、"多め")のどれか
#milk,指定しない or ("なし"、"少なめ"、"普通"、"多め")のどれか ice　(True or False) default False
#戻り値なし

def coffee(ice = 'アイス', **kwargs) :
    print(ice+'コーヒー')
    for a in kwargs :
        print(kwargs[a])

coffee(suger = '砂糖　少なめ', milk = 'ミルク　多め', ice = 'ホット')
