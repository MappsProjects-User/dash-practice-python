import numpy as np
import pandas as pd

# ============================================
#　データを読み込む関数
# ============================================


def read_csv_df_add_hq1_HML():
    """
    アンケート調査結果データの読み込み
    """
    result = pd.read_csv("data/df_add_hq1_HML.csv")

    return result


def read_csv_src_honkirin():
    """
    スクリーニングデータの読み込み
    """
    src_honkirin = pd.read_csv(
        "data/scr_data_hit_honkirinn.csv", encoding='cp932')

    return src_honkirin


def read_csv_df_add_hq1_HML_fill_na_0():
    """
    アンケートデータを０埋めしたデータ
    """
    df = read_csv_df_add_hq1_HML()
    result = df.fillna(0)

    return result

# ============================================
#　各質問のリストを作成する関数
# ============================================

#　Q7 缶ビール（ビール・発泡酒・第３のビール）で、重視する点を選んでください。
# ============================================


def create_q7c_list_item():
    """
    Q7 缶ビール（ビール・発泡酒・第３のビール）で、重視する点を選んでください。
    q7c1 泡がきめ細かいこと
    q7c2 飲みごたえがあること
    q7c3 のど越しが良いこと
    q7c4 キレがあること
    q7c5 飲みやすいこと
    q7c6 後味が良いこと
    q7c7 苦味があること
    q7c8 コクがあること
    q7c9 香りが良いこと
    q7c10 味が濃いこと
    q7c11 食事に合うこと
    q7c12 気軽に飲めること
    q7c13 本格的なこと
    q7c14 話題性があること
    q7c15 高級感があること
    q7c16 品質が良いこと
    q7c17 素材にこだわっていること
    q7c18 健康にこだわっていること
    q7c19 あてはまるものはない
    """
    q7c_list = []
    # 19項目全て作成
    for i in range(1, 20):
        q7c_i = str("q7c") + str(i)
        q7c_list.append(q7c_i)

    result = q7c_list

    return result


#　認知率 Q8 以下の中から、知っている商品を選んでください。
# ============================================
def c_q8_list():
    """　
    Q8　以下の中から、知っている商品を選んでください。
    q8c1 キリン「本麒麟」 
    q8c2 サントリー「金麦」
    q8c3 アサヒ「クリアアサヒ」
    """
    df_fillna_0 = read_csv_df_add_hq1_HML_fill_na_0()
    q8_1_pt = pd.pivot_table(
        df_fillna_0, index=["q8c1"], values="ID", aggfunc="count")
    q8_2_pt = pd.pivot_table(
        df_fillna_0, index=["q8c2"], values="ID", aggfunc="count")
    q8_3_pt = pd.pivot_table(
        df_fillna_0, index=["q8c3"], values="ID", aggfunc="count")

    q8_table = pd.concat([q8_1_pt, q8_2_pt, q8_3_pt], axis=1)
    q8_table_rate = round(q8_table.apply(
        lambda x: x / sum(x), axis=0) * 100, 1)

    q8_table_rate.columns = ['1 キリン「本麒麟」', '2 サントリー「金麦」', '3 アサヒ「クリアアサヒ」']
    q8_table_rate_1 = q8_table_rate.loc[1]

    result = q8_table_rate_1

    return result


#　q10　買ったことのある商品を選んでください。
# ============================================
def c_q10_list():
    """　
    q10　買ったことのある商品を選んでください。
    q10c1 キリン「本麒麟」 
    q10c2 サントリー「金麦」
    q10c3 アサヒ「クリアアサヒ」
    """
    df_fillna_0 = read_csv_df_add_hq1_HML_fill_na_0()
    q10_1_pt = pd.pivot_table(
        df_fillna_0, index=["q10c1"], values="ID", aggfunc="count")
    q10_2_pt = pd.pivot_table(
        df_fillna_0, index=["q10c2"], values="ID", aggfunc="count")
    q10_3_pt = pd.pivot_table(
        df_fillna_0, index=["q10c3"], values="ID", aggfunc="count")

    q10_table = pd.concat([q10_1_pt, q10_2_pt, q10_3_pt], axis=1)
    q10_table_rate = round(q10_table.apply(
        lambda x: x / sum(x), axis=0) * 100, 1)

    q10_table_rate.columns = ['1 キリン「本麒麟」', '2 サントリー「金麦」', '3 アサヒ「クリアアサヒ」']
    q10_table_rate_1 = q10_table_rate.loc[1]

    result = q10_table_rate_1

    return result


#　q12　３ヶ月以内に買った商品を選んでください。
# ============================================
def c_q12_list():
    """　
    q12　３ヶ月以内に買った商品を選んでください。
    q12c1 キリン「本麒麟」 
    q12c2 サントリー「金麦」
    q12c3 アサヒ「クリアアサヒ」
    """
    df_fillna_0 = read_csv_df_add_hq1_HML_fill_na_0()
    q12_1_pt = pd.pivot_table(
        df_fillna_0, index=["q12c1"], values="ID", aggfunc="count")
    q12_2_pt = pd.pivot_table(
        df_fillna_0, index=["q12c2"], values="ID", aggfunc="count")
    q12_3_pt = pd.pivot_table(
        df_fillna_0, index=["q12c3"], values="ID", aggfunc="count")

    q12_table = pd.concat([q12_1_pt, q12_2_pt, q12_3_pt], axis=1)
    q12_table_rate = round(q12_table.apply(
        lambda x: x / sum(x), axis=0) * 100, 1)

    q12_table_rate.columns = ['1 キリン「本麒麟」', '2 サントリー「金麦」', '3 アサヒ「クリアアサヒ」']
    q12_table_rate_1 = q12_table_rate.loc[1]

    result = q12_table_rate_1

    return result


#　q13　３ヶ月以内に買った商品の中から、主に買っている商品を選んでください。
# ============================================
def c_q13_list():
    """　
    q13　３ヶ月以内に買った商品の中から、主に買っている商品を選んでください。
    1 キリン「本麒麟」 
    2 サントリー「金麦」
    3 アサヒ「クリアアサヒ」
    """
    df_fillna_0 = read_csv_df_add_hq1_HML_fill_na_0()

    df_fillna_0 = pd.get_dummies(df_fillna_0, columns=['q13'])

    q13_1_pt = pd.pivot_table(
        df_fillna_0, index=["q13_1.0"], values="ID", aggfunc="count")
    q13_2_pt = pd.pivot_table(
        df_fillna_0, index=["q13_2.0"], values="ID", aggfunc="count")
    q13_3_pt = pd.pivot_table(
        df_fillna_0, index=["q13_3.0"], values="ID", aggfunc="count")

    q13_table = pd.concat([q13_1_pt, q13_2_pt, q13_3_pt], axis=1)
    q13_table_rate = round(q13_table.apply(
        lambda x: x / sum(x), axis=0) * 100, 1)

    q13_table_rate.columns = ['1 キリン「本麒麟」', '2 サントリー「金麦」', '3 アサヒ「クリアアサヒ」']
    q13_table_rate_1 = q13_table_rate.loc[1]

    result = q13_table_rate_1

    return result

# ============================================
#　飲用頻度・飲用量の性年代別分布
# ============================================


#　X軸の作成
# ============================================
def x_axis_list():
    """
    ピポットテーブルを使用
    行ラベル：hq1（性年代）
    値：df_coefficient（飲用頻度の係数）
    hq1（性年代）ごとのdf_coefficient（飲用頻度の係数）の平均値を算出
    """
    df = read_csv_df_add_hq1_HML()
    hq1_df = pd.pivot_table(
        df, index="hq1", values="df_coefficient", aggfunc="mean")
    result = [round(i, 1) for i in hq1_df['df_coefficient']]

    return result


#　Y軸の作成
# ============================================
def y_axis_list():
    """
    ピポットテーブルを使用
    行ラベル：hq1（性年代）
    値：da_coefficient（飲用量の係数）
    hq1（性年代）ごとのda_coefficient（飲用量の係数）の平均値を算出
    """
    df = read_csv_df_add_hq1_HML()
    hq1_da = pd.pivot_table(
        df, index="hq1", values="da_coefficient", aggfunc="mean")
    result = [round(i, 1) for i in hq1_da['da_coefficient']]

    return result


#　バブルサイズの作成
# ============================================
def bubble_size_list():
    src_honkirin = read_csv_src_honkirin()
    """
    インプットデータは、read_csv_src_honkirin（スクリーニングデータ）
    ピポットテーブルを使用
    行ラベル：q4c1
    列ラベル：gensex
    値：ID
    行q4c1、列gensexごとの個数の合計値を算出
    """
    src_honkirin_count = pd.pivot_table(
        src_honkirin, index="q4c1", columns="gensex", values="ID", aggfunc="count")
    src_honkirin_rate = round(src_honkirin_count.apply(
        lambda x: x / sum(x), axis=0) * 100, 1)
    result = [i for i in src_honkirin_rate.loc[1]]

    return result


#　ラベル用のテキストを作成
# ============================================
def text_list():
    bubble_size = bubble_size_list()

    gender_age = ['20代男性', '30代男性', '40代男性', '50代男性', '60代男性',
                  '20代女性', '30代女性', '40代女性', '50代女性', '60代女性', ]

    result = []
    for (gender_age, rate) in zip(gender_age, bubble_size):
        i = '<b>' + str(gender_age) + '<br>' + str(rate) + '%' + '<b>'
        result.append(i)

    return result


#　飲用頻度・飲用量の性年代別分布作成用に関数をまとめる
# ============================================
def gender_age_bubble_chart():
    text = text_list()
    x_axis = x_axis_list()
    y_axis = y_axis_list()
    bubble_size = bubble_size_list()
    result = {'text_list': text,
              'x_axis_list': x_axis,
              'y_axis_list': y_axis,
              'bubble_size_list': bubble_size,
              }

    return result


# ============================================
#　HML市場ボリューム
# ============================================
def hml_bubblesize_list():
    """
    ピポットテーブルを使用
    行ラベル：HML
    値：ID
    HMLごとのIDの個数を算出
    ラベルテキストとバブルサイズを作成
    """
    df = read_csv_df_add_hq1_HML()
    hml_pt = pd.pivot_table(df, index="HML", values="ID", aggfunc="count")
    # hml_ptの値　H:165 M:460 L:375

    # わかりやすいようにIDをsizeにrename
    hml_pt = hml_pt.rename(columns={'ID': 'size'})
    # HMLの順に入れるため、並び替え
    hml_pt = hml_pt.reindex(index=['H', 'M', 'L'])

    # hml_ptのラベルテキスト作成
    hml_text_list = []

    HML_list = ['Heavy', 'Middle', 'Light']

    # ラベル用のサイズに変換
    hml_pt_text_size = (hml_pt / 10)

    for (HML_list, hml_pt_item) in zip(HML_list, hml_pt_text_size['size']):
        i = str(HML_list) + '<br>' + str(hml_pt_item) + '%'
        hml_text_list.append(i)

    # hml_ptのバブル作成
    # 表示のため大きさを３倍にする
    hml_pt_size = (hml_pt / 10) * 3

    # リスト化
    # [49.5, 138.0, 112.5]
    hml_bubblesize_list = [i for i in hml_pt_size['size']]

    result = {'hml_text_list': hml_text_list,
              'hml_bubblesize_list': hml_bubblesize_list}
    return result


# ============================================
#　缶ビール重視点
# ============================================

#　重視点の割合を算出する関数
# ============================================
def q7c_beer_importance():

    df = read_csv_df_add_hq1_HML()

    q7c_list_item = create_q7c_list_item()

    q7c_df = pd.DataFrame(index=[], columns=[])
    for i in q7c_list_item:
        i_pt = pd.pivot_table(df, index=i, values="ID", aggfunc="count")
        q7c_df = pd.concat([q7c_df, i_pt], axis=1)

    # rate算出
    q7c_df_rate = round(q7c_df.apply(lambda x: x / sum(x), axis=0) * 100, 1)
    q7c_df_rate.columns = q7c_list_item

    # ソートを行番号1、行方向、降順で指定
    result = q7c_df_rate.sort_values(by=1, axis=1, ascending=False)

    return result


#　q7c_hmlを作成する関数
# ============================================
def q7c_hml_beer_importance():
    df = read_csv_df_add_hq1_HML()

    q7c_list_item = create_q7c_list_item()

    q7c_hml_df = pd.DataFrame(index=[], columns=[])
    for i in q7c_list_item:
        hml_i_pt = pd.pivot_table(
            df, index=i, columns="HML", values="ID", aggfunc="count")
        q7c_hml_df = pd.concat([q7c_hml_df, hml_i_pt], axis=1)

    # rate算出
    result = round(q7c_hml_df.apply(lambda x: x / sum(x), axis=0) * 100, 1)

    return result


#　q7c_hmlを作成する関数
# ============================================
def q7c_hml_beer_importance_H():
    # HML別ビール重視点を取得
    q7c_hml_rate = q7c_hml_beer_importance()

    # Hを抽出
    hml_q7_rate_h = q7c_hml_rate['H']
    # カラムがHになっているので、重視点の質問番号順に振り直す
    hml_q7_rate_h.columns = create_q7c_list_item()
    # 重視点の値の大きい降順の順番にするため、順番を入れ替える
    hml_q7_rate_h_reindex = hml_q7_rate_h.reindex(
        columns=q7c_beer_importance().columns)
    result = hml_q7_rate_h_reindex

    return result


#　q7c_hmlを作成する関数
# ============================================
def q7c_hml_beer_importance_M():
    # HML別ビール重視点を取得
    q7c_hml_rate = q7c_hml_beer_importance()

    # Mを抽出
    hml_q7_rate_m = q7c_hml_rate['M']
    # カラムがHになっているので、重視点の質問番号順に振り直す
    hml_q7_rate_m.columns = create_q7c_list_item()
    # 重視点の値の大きい降順の順番にするため、順番を入れ替える
    hml_q7_rate_m_reindex = hml_q7_rate_m.reindex(
        columns=q7c_beer_importance().columns)

    result = hml_q7_rate_m_reindex
    return result


#　q7c_hmlを作成する関数
# ============================================
def q7c_hml_beer_importance_L():
    # HML別ビール重視点を取得
    q7c_hml_rate = q7c_hml_beer_importance()

    # Lを抽出
    hml_q7_rate_l = q7c_hml_rate['L']
    # カラムがHになっているので、重視点の質問番号順に振り直す
    hml_q7_rate_l.columns = create_q7c_list_item()
    # 重視点の値の大きい降順の順番にするため、順番を入れ替える
    hml_q7_rate_l_reindex = hml_q7_rate_l.reindex(
        columns=q7c_beer_importance().columns)

    result = hml_q7_rate_l_reindex
    return result


#　缶ビール重視点グラフ作成用に関数をまとめる
# ============================================
def q7c_hml_beer_importance_list():
    # 棒グラフ＞ビール重視点リスト化
    beer_importance = [str(i) + "%" for i in q7c_beer_importance().loc[1]]

    H_list = [i for i in q7c_hml_beer_importance_H().loc[1]]
    M_list = [i for i in q7c_hml_beer_importance_M().loc[1]]
    L_list = [i for i in q7c_hml_beer_importance_L().loc[1]]

    result = {'beer_importance': beer_importance,
              'H_list': H_list,
              'M_list': M_list,
              'L_list': L_list}
    return result


# ============================================
#　マーケット浸透率
# ============================================
def market_penetration_rate():
    q8_list = c_q8_list()
    q10_list = c_q10_list()
    q12_list = c_q12_list()
    q13_list = c_q13_list()

    # 認知率から主購入を連結
    market_penetration_rate = pd.concat(
        [q8_list, q10_list, q12_list, q13_list], axis=1)
    # カラムを変更
    market_penetration_rate.columns = ['認知率', '購入経験率', '3ヶ月以内購入率', '主購入']
    # グラフでは、主購入〜認知率の順で値が表示されるのでreindexさせる

    market_penetration_rate_reindex = market_penetration_rate.reindex(
        columns=['主購入', '3ヶ月以内購入率', '購入経験率', '認知率']
    )

    mpr_honkirin_list = [
        str(i) + '%' for i in market_penetration_rate_reindex.loc['1 キリン「本麒麟」']
    ]
    mpr_kinmugi_list = [
        str(i) + '%' for i in market_penetration_rate_reindex.loc['2 サントリー「金麦」']
    ]
    mpr_asahi_list = [
        str(i) + '%' for i in market_penetration_rate_reindex.loc['3 アサヒ「クリアアサヒ」']
    ]

    result = {'1 キリン「本麒麟」': mpr_honkirin_list,
              '2 サントリー「金麦」': mpr_kinmugi_list,
              '3 アサヒ「クリアアサヒ」': mpr_asahi_list,
              }

    return result


# ============================================
#　歩留まり
# ============================================
def budomari():
    q8_list = c_q8_list()
    q10_list = c_q10_list()
    q12_list = c_q12_list()
    q13_list = c_q13_list()

    # 認知率から主購入を連結
    market_penetration_rate = pd.concat(
        [q8_list, q10_list, q12_list, q13_list], axis=1)
    # カラムを変更
    market_penetration_rate.columns = ['認知率', '購入経験率', '3ヶ月以内購入率', '主購入']

    # rename
    mpr_table = market_penetration_rate

    mpr_table['認知率→購入経験率'] = round(
        mpr_table['購入経験率'] / mpr_table['認知率'] * 100, 1)
    mpr_table['購入経験率→3ヶ月以内購入率'] = round(
        mpr_table['3ヶ月以内購入率'] / mpr_table['購入経験率'] * 100, 1)
    mpr_table['3ヶ月以内購入率→主購入'] = round(
        mpr_table['主購入'] / mpr_table['3ヶ月以内購入率'] * 100, 1)

    budomari_table = mpr_table.reindex(columns=[
                                       '3ヶ月以内購入率→主購入', '購入経験率→3ヶ月以内購入率', '認知率→購入経験率', '主購入', '3ヶ月以内購入率', '購入経験率', '認知率'])

    # 必要な列のみ取得
    budomari_table = budomari_table[[
        '3ヶ月以内購入率→主購入', '購入経験率→3ヶ月以内購入率', '認知率→購入経験率']
    ]

    budomari_honkirin_list = [
        str(i) + '%' for i in budomari_table.loc['1 キリン「本麒麟」']
    ]
    budomari_kinmugi_list = [
        str(i) + '%' for i in budomari_table.loc['2 サントリー「金麦」']
    ]
    budomari_asahi_list = [
        str(i) + '%' for i in budomari_table.loc['3 アサヒ「クリアアサヒ」']
    ]

    result = {'1 キリン「本麒麟」': budomari_honkirin_list,
              '2 サントリー「金麦」': budomari_kinmugi_list,
              '3 アサヒ「クリアアサヒ」': budomari_asahi_list, }

    return result


# ============================================
#　HML別マーケット浸透率
# ============================================
def hml_market_penetration_rate():
    df = read_csv_df_add_hq1_HML_fill_na_0()
    # 認知率
    q8_1_HML_pt = pd.pivot_table(df, index=["q8c1"], columns=[
                                 "HML"], values="ID", aggfunc="count")
    q8_2_HML_pt = pd.pivot_table(df, index=["q8c2"], columns=[
                                 "HML"], values="ID", aggfunc="count")
    q8_3_HML_pt = pd.pivot_table(df, index=["q8c3"], columns=[
                                 "HML"], values="ID", aggfunc="count")
    q8_HML_table = pd.concat([q8_1_HML_pt, q8_2_HML_pt, q8_3_HML_pt], axis=1)
    q8_HML_table_rate = round(q8_HML_table.apply(
        lambda x: x / sum(x), axis=0) * 100, 1)
    q8_HML_table_rate.columns = ['1 キリン「本麒麟」_H', '1 キリン「本麒麟」_L', '1 キリン「本麒麟」_M',
                                 '2 サントリー「金麦」_H', '2 サントリー「金麦」_L', '2 サントリー「金麦」_M',
                                 '3 アサヒ「クリアアサヒ」_H', '3 アサヒ「クリアアサヒ」_L', '3 アサヒ「クリアアサヒ」_M', ]
    q8_HML_table_rate_1 = q8_HML_table_rate.loc[1]

    # 購入経験率
    q10_1_HML_pt = pd.pivot_table(df, index=["q10c1"], columns=[
                                  "HML"], values="ID", aggfunc="count")
    q10_2_HML_pt = pd.pivot_table(df, index=["q10c2"], columns=[
                                  "HML"], values="ID", aggfunc="count")
    q10_3_HML_pt = pd.pivot_table(df, index=["q10c3"], columns=[
                                  "HML"], values="ID", aggfunc="count")
    q10_HML_table = pd.concat(
        [q10_1_HML_pt, q10_2_HML_pt, q10_3_HML_pt], axis=1)
    q10_HML_table_rate = round(q10_HML_table.apply(
        lambda x: x / sum(x), axis=0) * 100, 1)
    q10_HML_table_rate.columns = ['1 キリン「本麒麟」_H', '1 キリン「本麒麟」_L', '1 キリン「本麒麟」_M',
                                  '2 サントリー「金麦」_H', '2 サントリー「金麦」_L', '2 サントリー「金麦」_M',
                                  '3 アサヒ「クリアアサヒ」_H', '3 アサヒ「クリアアサヒ」_L', '3 アサヒ「クリアアサヒ」_M', ]
    q10_HML_table_rate_1 = q10_HML_table_rate.loc[1]

    # 3ヶ月以内購入率
    q12_1_HML_pt = pd.pivot_table(df, index=["q12c1"], columns=[
                                  "HML"], values="ID", aggfunc="count")
    q12_2_HML_pt = pd.pivot_table(df, index=["q12c2"], columns=[
                                  "HML"], values="ID", aggfunc="count")
    q12_3_HML_pt = pd.pivot_table(df, index=["q12c3"], columns=[
                                  "HML"], values="ID", aggfunc="count")
    q12_HML_table = pd.concat(
        [q12_1_HML_pt, q12_2_HML_pt, q12_3_HML_pt], axis=1)
    q12_HML_table_rate = round(q12_HML_table.apply(
        lambda x: x / sum(x), axis=0) * 100, 1)
    q12_HML_table_rate.columns = ['1 キリン「本麒麟」_H', '1 キリン「本麒麟」_L', '1 キリン「本麒麟」_M',
                                  '2 サントリー「金麦」_H', '2 サントリー「金麦」_L', '2 サントリー「金麦」_M',
                                  '3 アサヒ「クリアアサヒ」_H', '3 アサヒ「クリアアサヒ」_L', '3 アサヒ「クリアアサヒ」_M', ]
    q12_HML_table_rate_1 = q12_HML_table_rate.loc[1]

    # 主購入
    df = pd.get_dummies(df, columns=['q13'])
    q13_1_HML_pt = pd.pivot_table(df, index=["q13_1.0"], columns=[
                                  "HML"], values="ID", aggfunc="count")
    q13_2_HML_pt = pd.pivot_table(df, index=["q13_2.0"], columns=[
                                  "HML"], values="ID", aggfunc="count")
    q13_3_HML_pt = pd.pivot_table(df, index=["q13_3.0"], columns=[
                                  "HML"], values="ID", aggfunc="count")
    q13_HML_table = pd.concat(
        [q13_1_HML_pt, q13_2_HML_pt, q13_3_HML_pt], axis=1)
    q13_HML_table_rate = round(q13_HML_table.apply(
        lambda x: x / sum(x), axis=0) * 100, 1)
    q13_HML_table_rate.columns = ['1 キリン「本麒麟」_H', '1 キリン「本麒麟」_L', '1 キリン「本麒麟」_M',
                                  '2 サントリー「金麦」_H', '2 サントリー「金麦」_L', '2 サントリー「金麦」_M',
                                  '3 アサヒ「クリアアサヒ」_H', '3 アサヒ「クリアアサヒ」_L', '3 アサヒ「クリアアサヒ」_M', ]
    q13_HML_table_rate_1 = q13_HML_table_rate.loc[1]

    hml_market_penetration_rate = pd.concat(
        [q8_HML_table_rate_1, q10_HML_table_rate_1, q12_HML_table_rate_1, q13_HML_table_rate_1], axis=1)

    hml_market_penetration_rate.columns = ['認知率', '購入経験率', '3ヶ月以内購入率', '主購入']

    # 本麒麟
    # H
    honkirin_h_list = [
        i for i in hml_market_penetration_rate.loc['1 キリン「本麒麟」_H']]

    # M
    honkirin_m_list = [
        i for i in hml_market_penetration_rate.loc['1 キリン「本麒麟」_M']]

    # L
    honkirin_l_list = [
        i for i in hml_market_penetration_rate.loc['1 キリン「本麒麟」_L']]

    # 金麦
    # H
    kinmugi_h_list = [
        i for i in hml_market_penetration_rate.loc['2 サントリー「金麦」_H']]

    # M
    kinmugi_m_list = [
        i for i in hml_market_penetration_rate.loc['2 サントリー「金麦」_M']]

    # L
    kinmugi_l_list = [
        i for i in hml_market_penetration_rate.loc['2 サントリー「金麦」_L']]

    # クリアアサヒ
    # H
    clear_asahi_h_list = [
        i for i in hml_market_penetration_rate.loc['3 アサヒ「クリアアサヒ」_H']]

    # M
    clear_asahi_m_list = [
        i for i in hml_market_penetration_rate.loc['3 アサヒ「クリアアサヒ」_M']]

    # L
    clear_asahi_l_list = [
        i for i in hml_market_penetration_rate.loc['3 アサヒ「クリアアサヒ」_L']]

    result = {'1 キリン「本麒麟」H': honkirin_h_list,
              '1 キリン「本麒麟」M': honkirin_m_list,
              '1 キリン「本麒麟」L': honkirin_l_list,

              '2 サントリー「金麦」H': kinmugi_h_list,
              '2 サントリー「金麦」M': kinmugi_m_list,
              '2 サントリー「金麦」L': kinmugi_l_list,

              '3 アサヒ「クリアアサヒ」H': clear_asahi_h_list,
              '3 アサヒ「クリアアサヒ」M': clear_asahi_m_list,
              '3 アサヒ「クリアアサヒ」L': clear_asahi_l_list, }

    return result


# ============================================
#　商品イメージ Base：各銘柄認知者
# ============================================
def product_image():
    df = read_csv_df_add_hq1_HML()
    # 本麒麟
    ##################
    q9s1c1_pt = pd.pivot_table(
        df, index=["q9s1c1"], values="ID", aggfunc="count")
    q9s1c2_pt = pd.pivot_table(
        df, index=["q9s1c2"], values="ID", aggfunc="count")
    q9s1c3_pt = pd.pivot_table(
        df, index=["q9s1c3"], values="ID", aggfunc="count")
    q9s1c4_pt = pd.pivot_table(
        df, index=["q9s1c4"], values="ID", aggfunc="count")
    q9s1c5_pt = pd.pivot_table(
        df, index=["q9s1c5"], values="ID", aggfunc="count")
    q9s1c6_pt = pd.pivot_table(
        df, index=["q9s1c6"], values="ID", aggfunc="count")
    q9s1c7_pt = pd.pivot_table(
        df, index=["q9s1c7"], values="ID", aggfunc="count")
    q9s1c8_pt = pd.pivot_table(
        df, index=["q9s1c8"], values="ID", aggfunc="count")
    q9s1c9_pt = pd.pivot_table(
        df, index=["q9s1c9"], values="ID", aggfunc="count")
    q9s1c10_pt = pd.pivot_table(
        df, index=["q9s1c10"], values="ID", aggfunc="count")
    q9s1c11_pt = pd.pivot_table(
        df, index=["q9s1c11"], values="ID", aggfunc="count")
    q9s1c12_pt = pd.pivot_table(
        df, index=["q9s1c12"], values="ID", aggfunc="count")
    q9s1c13_pt = pd.pivot_table(
        df, index=["q9s1c13"], values="ID", aggfunc="count")
    q9s1c14_pt = pd.pivot_table(
        df, index=["q9s1c14"], values="ID", aggfunc="count")
    q9s1c15_pt = pd.pivot_table(
        df, index=["q9s1c15"], values="ID", aggfunc="count")
    q9s1c16_pt = pd.pivot_table(
        df, index=["q9s1c16"], values="ID", aggfunc="count")
    q9s1c17_pt = pd.pivot_table(
        df, index=["q9s1c17"], values="ID", aggfunc="count")
    q9s1c18_pt = pd.pivot_table(
        df, index=["q9s1c18"], values="ID", aggfunc="count")
    q9s1c19_pt = pd.pivot_table(
        df, index=["q9s1c19"], values="ID", aggfunc="count")

    # １つのテーブルにまとめる
    q9s1_table = pd.concat([q9s1c1_pt, q9s1c2_pt, q9s1c3_pt, q9s1c4_pt, q9s1c5_pt, q9s1c6_pt, q9s1c7_pt, q9s1c8_pt,
                            q9s1c9_pt, q9s1c10_pt, q9s1c11_pt, q9s1c12_pt, q9s1c13_pt, q9s1c14_pt, q9s1c15_pt, q9s1c16_pt,
                            q9s1c17_pt, q9s1c18_pt, q9s1c19_pt], axis=1)

    # rate算出
    q9s1_table = round(q9s1_table.apply(lambda x: x / sum(x), axis=0) * 100, 1)
    q9s1_table.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                          '11', '12', '13', '14', '15', '16', '17', '18', '19']

    q9s1_table = q9s1_table.rename(index={0: 'honkirin_0', 1: 'honkirin_1'})

    q9s1_table = q9s1_table.transpose()

    q9s1_table = q9s1_table['honkirin_1']

    # 金麦
    ##################
    q9s2c1_pt = pd.pivot_table(
        df, index=["q9s2c1"], values="ID", aggfunc="count")
    q9s2c2_pt = pd.pivot_table(
        df, index=["q9s2c2"], values="ID", aggfunc="count")
    q9s2c3_pt = pd.pivot_table(
        df, index=["q9s2c3"], values="ID", aggfunc="count")
    q9s2c4_pt = pd.pivot_table(
        df, index=["q9s2c4"], values="ID", aggfunc="count")
    q9s2c5_pt = pd.pivot_table(
        df, index=["q9s2c5"], values="ID", aggfunc="count")
    q9s2c6_pt = pd.pivot_table(
        df, index=["q9s2c6"], values="ID", aggfunc="count")
    q9s2c7_pt = pd.pivot_table(
        df, index=["q9s2c7"], values="ID", aggfunc="count")
    q9s2c8_pt = pd.pivot_table(
        df, index=["q9s2c8"], values="ID", aggfunc="count")
    q9s2c9_pt = pd.pivot_table(
        df, index=["q9s2c9"], values="ID", aggfunc="count")
    q9s2c10_pt = pd.pivot_table(
        df, index=["q9s2c10"], values="ID", aggfunc="count")
    q9s2c11_pt = pd.pivot_table(
        df, index=["q9s2c11"], values="ID", aggfunc="count")
    q9s2c12_pt = pd.pivot_table(
        df, index=["q9s2c12"], values="ID", aggfunc="count")
    q9s2c13_pt = pd.pivot_table(
        df, index=["q9s2c13"], values="ID", aggfunc="count")
    q9s2c14_pt = pd.pivot_table(
        df, index=["q9s2c14"], values="ID", aggfunc="count")
    q9s2c15_pt = pd.pivot_table(
        df, index=["q9s2c15"], values="ID", aggfunc="count")
    q9s2c16_pt = pd.pivot_table(
        df, index=["q9s2c16"], values="ID", aggfunc="count")
    q9s2c17_pt = pd.pivot_table(
        df, index=["q9s2c17"], values="ID", aggfunc="count")
    q9s2c18_pt = pd.pivot_table(
        df, index=["q9s2c18"], values="ID", aggfunc="count")
    q9s2c19_pt = pd.pivot_table(
        df, index=["q9s2c19"], values="ID", aggfunc="count")

    # １つのテーブルにまとめる
    q9s2_table = pd.concat([q9s2c1_pt, q9s2c2_pt, q9s2c3_pt, q9s2c4_pt, q9s2c5_pt, q9s2c6_pt, q9s2c7_pt, q9s2c8_pt,
                            q9s2c9_pt, q9s2c10_pt, q9s2c11_pt, q9s2c12_pt, q9s2c13_pt, q9s2c14_pt, q9s2c15_pt, q9s2c16_pt,
                            q9s2c17_pt, q9s2c18_pt, q9s2c19_pt], axis=1)

    # rate算出
    q9s2_table = round(q9s2_table.apply(lambda x: x / sum(x), axis=0) * 100, 1)

    q9s2_table.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                          '11', '12', '13', '14', '15', '16', '17', '18', '19']

    q9s2_table = q9s2_table.rename(index={0: 'kinmugi_0', 1: 'kinmugi_1'})
    q9s2_table = q9s2_table.transpose()

    q9s2_table = q9s2_table['kinmugi_1']

    # クリアアサヒ
    ##################
    q9s3c1_pt = pd.pivot_table(
        df, index=["q9s3c1"], values="ID", aggfunc="count")
    q9s3c2_pt = pd.pivot_table(
        df, index=["q9s3c2"], values="ID", aggfunc="count")
    q9s3c3_pt = pd.pivot_table(
        df, index=["q9s3c3"], values="ID", aggfunc="count")
    q9s3c4_pt = pd.pivot_table(
        df, index=["q9s3c4"], values="ID", aggfunc="count")
    q9s3c5_pt = pd.pivot_table(
        df, index=["q9s3c5"], values="ID", aggfunc="count")
    q9s3c6_pt = pd.pivot_table(
        df, index=["q9s3c6"], values="ID", aggfunc="count")
    q9s3c7_pt = pd.pivot_table(
        df, index=["q9s3c7"], values="ID", aggfunc="count")
    q9s3c8_pt = pd.pivot_table(
        df, index=["q9s3c8"], values="ID", aggfunc="count")
    q9s3c9_pt = pd.pivot_table(
        df, index=["q9s3c9"], values="ID", aggfunc="count")
    q9s3c10_pt = pd.pivot_table(
        df, index=["q9s3c10"], values="ID", aggfunc="count")
    q9s3c11_pt = pd.pivot_table(
        df, index=["q9s3c11"], values="ID", aggfunc="count")
    q9s3c12_pt = pd.pivot_table(
        df, index=["q9s3c12"], values="ID", aggfunc="count")
    q9s3c13_pt = pd.pivot_table(
        df, index=["q9s3c13"], values="ID", aggfunc="count")
    q9s3c14_pt = pd.pivot_table(
        df, index=["q9s3c14"], values="ID", aggfunc="count")
    q9s3c15_pt = pd.pivot_table(
        df, index=["q9s3c15"], values="ID", aggfunc="count")
    q9s3c16_pt = pd.pivot_table(
        df, index=["q9s3c16"], values="ID", aggfunc="count")
    q9s3c17_pt = pd.pivot_table(
        df, index=["q9s3c17"], values="ID", aggfunc="count")
    q9s3c18_pt = pd.pivot_table(
        df, index=["q9s3c18"], values="ID", aggfunc="count")
    q9s3c19_pt = pd.pivot_table(
        df, index=["q9s3c19"], values="ID", aggfunc="count")

    # １つのテーブルにまとめる
    q9s3_table = pd.concat([q9s3c1_pt, q9s3c2_pt, q9s3c3_pt, q9s3c4_pt, q9s3c5_pt, q9s3c6_pt, q9s3c7_pt, q9s3c8_pt,
                            q9s3c9_pt, q9s3c10_pt, q9s3c11_pt, q9s3c12_pt, q9s3c13_pt, q9s3c14_pt, q9s3c15_pt, q9s3c16_pt,
                            q9s3c17_pt, q9s3c18_pt, q9s3c19_pt], axis=1)
    # rate算出
    q9s3_table = round(q9s3_table.apply(lambda x: x / sum(x), axis=0) * 100, 1)

    q9s3_table.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                          '11', '12', '13', '14', '15', '16', '17', '18', '19']

    q9s3_table = q9s3_table.rename(index={0: 'asahi_0', 1: 'asahi_1'})
    q9s3_table = q9s3_table.transpose()

    q9s3_table = q9s3_table['asahi_1']

    # のどごし＜生＞
    ##################
    q9s4c1_pt = pd.pivot_table(
        df, index=["q9s4c1"], values="ID", aggfunc="count")
    q9s4c2_pt = pd.pivot_table(
        df, index=["q9s4c2"], values="ID", aggfunc="count")
    q9s4c3_pt = pd.pivot_table(
        df, index=["q9s4c3"], values="ID", aggfunc="count")
    q9s4c4_pt = pd.pivot_table(
        df, index=["q9s4c4"], values="ID", aggfunc="count")
    q9s4c5_pt = pd.pivot_table(
        df, index=["q9s4c5"], values="ID", aggfunc="count")
    q9s4c6_pt = pd.pivot_table(
        df, index=["q9s4c6"], values="ID", aggfunc="count")
    q9s4c7_pt = pd.pivot_table(
        df, index=["q9s4c7"], values="ID", aggfunc="count")
    q9s4c8_pt = pd.pivot_table(
        df, index=["q9s4c8"], values="ID", aggfunc="count")
    q9s4c9_pt = pd.pivot_table(
        df, index=["q9s4c9"], values="ID", aggfunc="count")
    q9s4c10_pt = pd.pivot_table(
        df, index=["q9s4c10"], values="ID", aggfunc="count")
    q9s4c11_pt = pd.pivot_table(
        df, index=["q9s4c11"], values="ID", aggfunc="count")
    q9s4c12_pt = pd.pivot_table(
        df, index=["q9s4c12"], values="ID", aggfunc="count")
    q9s4c13_pt = pd.pivot_table(
        df, index=["q9s4c13"], values="ID", aggfunc="count")
    q9s4c14_pt = pd.pivot_table(
        df, index=["q9s4c14"], values="ID", aggfunc="count")
    q9s4c15_pt = pd.pivot_table(
        df, index=["q9s4c15"], values="ID", aggfunc="count")
    q9s4c16_pt = pd.pivot_table(
        df, index=["q9s4c16"], values="ID", aggfunc="count")
    q9s4c17_pt = pd.pivot_table(
        df, index=["q9s4c17"], values="ID", aggfunc="count")
    q9s4c18_pt = pd.pivot_table(
        df, index=["q9s4c18"], values="ID", aggfunc="count")
    q9s4c19_pt = pd.pivot_table(
        df, index=["q9s4c19"], values="ID", aggfunc="count")

    # １つのテーブルにまとめる
    q9s4_table = pd.concat([q9s4c1_pt, q9s4c2_pt, q9s4c3_pt, q9s4c4_pt, q9s4c5_pt, q9s4c6_pt, q9s4c7_pt, q9s4c8_pt,
                            q9s4c9_pt, q9s4c10_pt, q9s4c11_pt, q9s4c12_pt, q9s4c13_pt, q9s4c14_pt, q9s4c15_pt, q9s4c16_pt,
                            q9s4c17_pt, q9s4c18_pt, q9s4c19_pt], axis=1)
    # rate算出
    q9s4_table = round(q9s4_table.apply(lambda x: x / sum(x), axis=0) * 100, 1)
    q9s4_table.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                          '11', '12', '13', '14', '15', '16', '17', '18', '19']

    q9s4_table = q9s4_table.rename(index={0: 'nodogoshi_0', 1: 'nodogoshi_1'})
    q9s4_table = q9s4_table.transpose()

    q9s4_table = q9s4_table['nodogoshi_1']

    # 淡麗グリーンラベル
    ##################
    q9s5c1_pt = pd.pivot_table(
        df, index=["q9s5c1"], values="ID", aggfunc="count")
    q9s5c2_pt = pd.pivot_table(
        df, index=["q9s5c2"], values="ID", aggfunc="count")
    q9s5c3_pt = pd.pivot_table(
        df, index=["q9s5c3"], values="ID", aggfunc="count")
    q9s5c4_pt = pd.pivot_table(
        df, index=["q9s5c4"], values="ID", aggfunc="count")
    q9s5c5_pt = pd.pivot_table(
        df, index=["q9s5c5"], values="ID", aggfunc="count")
    q9s5c6_pt = pd.pivot_table(
        df, index=["q9s5c6"], values="ID", aggfunc="count")
    q9s5c7_pt = pd.pivot_table(
        df, index=["q9s5c7"], values="ID", aggfunc="count")
    q9s5c8_pt = pd.pivot_table(
        df, index=["q9s5c8"], values="ID", aggfunc="count")
    q9s5c9_pt = pd.pivot_table(
        df, index=["q9s5c9"], values="ID", aggfunc="count")
    q9s5c10_pt = pd.pivot_table(
        df, index=["q9s5c10"], values="ID", aggfunc="count")
    q9s5c11_pt = pd.pivot_table(
        df, index=["q9s5c11"], values="ID", aggfunc="count")
    q9s5c12_pt = pd.pivot_table(
        df, index=["q9s5c12"], values="ID", aggfunc="count")
    q9s5c13_pt = pd.pivot_table(
        df, index=["q9s5c13"], values="ID", aggfunc="count")
    q9s5c14_pt = pd.pivot_table(
        df, index=["q9s5c14"], values="ID", aggfunc="count")
    q9s5c15_pt = pd.pivot_table(
        df, index=["q9s5c15"], values="ID", aggfunc="count")
    q9s5c16_pt = pd.pivot_table(
        df, index=["q9s5c16"], values="ID", aggfunc="count")
    q9s5c17_pt = pd.pivot_table(
        df, index=["q9s5c17"], values="ID", aggfunc="count")
    q9s5c18_pt = pd.pivot_table(
        df, index=["q9s5c18"], values="ID", aggfunc="count")
    q9s5c19_pt = pd.pivot_table(
        df, index=["q9s5c19"], values="ID", aggfunc="count")

    # １つのテーブルにまとめる
    q9s5_table = pd.concat([q9s5c1_pt, q9s5c2_pt, q9s5c3_pt, q9s5c4_pt, q9s5c5_pt, q9s5c6_pt, q9s5c7_pt, q9s5c8_pt,
                            q9s5c9_pt, q9s5c10_pt, q9s5c11_pt, q9s5c12_pt, q9s5c13_pt, q9s5c14_pt, q9s5c15_pt, q9s5c16_pt,
                            q9s5c17_pt, q9s5c18_pt, q9s5c19_pt], axis=1)
    # rate算出
    q9s5_table = round(q9s5_table.apply(lambda x: x / sum(x), axis=0) * 100, 1)

    q9s5_table.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                          '11', '12', '13', '14', '15', '16', '17', '18', '19']
    q9s5_table = q9s5_table.rename(index={0: 'tanrei_0', 1: 'tanrei_1'})
    q9s5_table = q9s5_table.transpose()
    q9s5_table = q9s5_table['tanrei_1']

    # 5つのテーブルをマージ　後の処理は5つのテーブルをマージしたテーブル「q9_merge_table」にて行う
    # 5つのテーブルをマージして、一行ごとに平均値を算出　平均値が高い上位10項目を選出する
    ##################
    q9_merge_table = pd.concat(
        [q9s1_table, q9s2_table, q9s3_table, q9s4_table, q9s5_table], axis=1)

    # １９番　「あてはまるものはない」を除外
    q9_merge_table = q9_merge_table.drop(index='19')

    # 行ごとの平均を求める
    q9_merge_table['mean_column'] = q9_merge_table.mean(axis='columns')

    # 平均の列「mean_column」で降順にする
    q9_merge_table_2 = q9_merge_table.sort_values(
        'mean_column', ascending=False)

    # 平均の列「mean_column」で降順にする
    honkirin_1_list = []
    kinmugi_1_list = []
    asahi_1_list = []
    #nodogoshi_1_list = []
    #tanrei_1_list = []

    # 各銘柄の項目のスコアを取得してリストにする
    for index, row in q9_merge_table_2.iloc[:10].iterrows():
        honkirin_i = row['honkirin_1']
        kinmugi_i = row['kinmugi_1']
        asahi_i = row['asahi_1']
        #nodogoshi_e = row['nodogoshi_1']
        #tanrei_e = row['tanrei_1']

        honkirin_1_list.append(honkirin_i)
        kinmugi_1_list.append(kinmugi_i)
        asahi_1_list.append(asahi_i)
        # nodogoshi_1_list.append(nodogoshi_e)
        # tanrei_1_list.append(tanrei_e)

    result = {'キリン「本麒麟」': honkirin_1_list,
              'サントリー「金麦」': kinmugi_1_list,
              'アサヒ「クリアアサヒ」': asahi_1_list
              }

    return result
