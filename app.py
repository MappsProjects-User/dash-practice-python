# Import required libraries
import collections
import pathlib
import random

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd

import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# 自作モジュールのインポート
import data_processing as dp

# ============================================
# ダッシュボードの設定
# ============================================
# config
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server


# Create global chart template
mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"

# Layout
layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=30, r=30, b=20, t=40),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Satellite Overview",
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="light",
        center=dict(lon=-78.05, lat=42.54),
        zoom=7,
    ),
)


# ============================================
#　飲用頻度・飲用量の性年代別分布
# ============================================

# 飲用頻度・飲用量の性年代別分布 ▶︎
# データの入力、データの表示を制御する場所
# ============================================
x_axis_list = dp.gender_age_bubble_chart()['x_axis_list']
y_axis_list = dp.gender_age_bubble_chart()['y_axis_list']
bubble_size_list = dp.gender_age_bubble_chart()['bubble_size_list']
text_list = dp.gender_age_bubble_chart()['text_list']

gender_and_age_distribution = go.Figure()

gender_and_age_distribution_data = go.Scatter(
    x=x_axis_list, y=y_axis_list,
    mode='markers+text',

    text=text_list,
    textposition=['top center', 'middle center', 'top center', 'middle center', 'middle center',
                  'middle center', 'middle center', 'middle center', 'middle center', 'bottom center', ],
    marker=dict(
        color=['#3371a0', '#3371a0', '#3371a0', '#3371a0', '#3371a0',
               '#b24644', '#b24644', '#b24644', '#b24644', '#b24644'],
        opacity=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
        # 元のサイズは、16.5, 46.0, 37.5 *3
        size=[bubble_size_list[0], bubble_size_list[1], bubble_size_list[2], bubble_size_list[3], bubble_size_list[4], bubble_size_list[5],
              bubble_size_list[6], bubble_size_list[7], bubble_size_list[8], bubble_size_list[9]],
    )
)

# 飲用頻度・飲用量の性年代別分布 ▶︎
# レイアウトを決める場所
# ============================================
layout = go.Layout(
    title=dict(
        text='飲用頻度・飲用量の性年代別分布<br><br>・円の大きさ：3ヵ月以内缶ビール購入率を表す※使用データはスクリーニングデータ<br>'
        '→サンプル数は性年代ごとに異なり322～608s<br>'
        '・飲用量/飲用頻度：性年代ごとに平均値を算出※使用データは本調査データ<br>'
        '→サンプル数は性年代ごとに異なり40～153s',
        y=0.91,
        yanchor="top"
    ),
    height=650,
    width=1185,
    xaxis=dict(
        title_text="飲用頻度(回/月)",
        range=[4, 15],
        dtick=1
    ),
    yaxis=dict(
        title_text="飲用量(ml/日)",
        range=[350, 700]
    ),
    margin=dict(t=200, r=0, b=0)
)

# 飲用頻度・飲用量の性年代別分布 ▶︎
# データとレイアウトをまとめ場所
# ============================================
gender_and_age_distribution = go.Figure(
    data=gender_and_age_distribution_data, layout=layout)


# ============================================
#　HMLの市場ボリューム
# ============================================

# HMLの市場ボリューム ▶︎
# 関数から戻り値を取得
# ============================================

hml_text_list = dp.hml_bubblesize_list()['hml_text_list']
hml_bubblesize_list = dp.hml_bubblesize_list()['hml_bubblesize_list']

# HMLの市場ボリューム ▶︎
# データの入力、データの表示を制御する場所
# ============================================
HML_bubble_data = go.Scatter(
    x=[1, 2, 3], y=[1, 1, 1],
    mode='markers+text',
    text=['Heavy<br>16.5%', 'Middle<br>46.0%', 'Light<br>37.5%'],
    textposition='middle center',
    marker=dict(
        color=['#df5f6a', '#94d736', '#d5c72c'],
        opacity=[0.6, 0.6, 0.6],
        # 元のサイズは、16.5, 46.0, 37.5 *3
        size=hml_bubblesize_list,
    )
)

# HMLの市場ボリューム ▶︎
# レイアウトを決める場所
# ============================================
layout = go.Layout(
    title='HMLの市場ボリューム<br>Base:3ヶ月以内缶ビール購入者（n=1,000)',
    height=350,
    width=895
)

# HMLの市場ボリューム ▶︎
# データとレイアウトをまとめ場所
# ============================================
HML_bubble = go.Figure(data=HML_bubble_data, layout=layout)


# ============================================
#　缶ビール重視点
# ============================================

#　缶ビール重視点 ▶︎
# 空のgraph.objects作成
# ============================================
beer_important_points = go.Figure()


# 缶ビール重視点 ▶︎
# 項目
# ============================================
beer_important_points_koumoku = ['のど越しが良いこと',
                                 '飲みやすいこと',
                                 'キレがあること',
                                 '飲みごたえがあること',
                                 '気軽に飲めること',
                                 'コクがあること',
                                 '後味が良いこと',
                                 '食事に合うこと',
                                 '品質が良いこと',
                                 '本格的なこと',
                                 '香りが良いこと',
                                 '味が濃いこと',
                                 '泡がきめ細かいこと',
                                 '素材にこだわっていること',
                                 '苦味があること',
                                 '健康にこだわっていること',
                                 '高級感があること',
                                 '話題性があること',
                                 'あてはまるものはない']

# 缶ビール重視点 ▶︎
# 棒グラフ
# ============================================
beer_importance_list = dp.q7c_hml_beer_importance_list()['beer_importance']
# q7c_array = ['45.4%', '41.8%', '31.9%', '29.5%', '29.0%', '28.6%', '27.2%', '26.9%', '25.4%', '19.8%',
#             '16.9%', '14.5%', '14.1%', '13.3%', '13.1%', '9.4%', '7.0%', '4.0%', '2.2%']

beer_important_points.add_trace(
    go.Bar(
        x=beer_important_points_koumoku,
        y=beer_importance_list,
        name="全体(n=1,000)",
        text=beer_importance_list,
        textposition="auto",
        marker=dict(
            color='#c0c4c7',
            line=dict(
                color='#c0c4c7',
                width=1
            )
        )
    )
)

# 缶ビール重視点 ▶︎
# Heavy 折れ線グラフ
# ============================================
H_list = dp.q7c_hml_beer_importance_list()['H_list']

# q7cs_H_array = ['47.9%', '38.2%', '46.7%', '38.8%', '29.7%', '30.9%', '29.1%', '29.1%',
#                 '28.5%', '21.8%', '21.2%', '21.8%', '17.6%', '20.6%', '24.2%', '16.4%',
#                 '12.7%', '9.1%', '0.6%']
beer_important_points.add_trace(
    go.Scatter(
        x=beer_important_points_koumoku,
        y=H_list,
        name="Heavy(n=165)",
        marker=dict(
            color='#b24644',
            size=8,
            line=dict(
                color='#b24644',
                width=1
            )
        )
    ))

# 缶ビール重視点 ▶︎
# Middle 折れ線グラフ
# ============================================
M_list = dp.q7c_hml_beer_importance_list()['M_list']

# q7cs_M_array = ['47.8%', '43.3%', '32.8%', '33.5%', '32.2%', '32.4%', '30.0%', '29.1%', '25.2%',
#                '21.3%', '17.6%', '16.7%', '15.2%', '13.5%', '14.3%', '8.7%', '7.6%', '2.4%', '1.3%']
beer_important_points.add_trace(
    go.Scatter(
        x=beer_important_points_koumoku,
        y=M_list,
        name="Middle(n=460)",
        marker=dict(
            symbol='cross',
            color='#669636',
            size=8,
            line=dict(
                color='#669636',
                width=1
            )
        )
    ))

# 缶ビール重視点 ▶︎
# Light 折れ線グラフ
# ============================================
L_list = dp.q7c_hml_beer_importance_list()['L_list']

# q7cs_L_array = ['41.3%', '41.6%', '24.3%', '20.5%', '24.8%', '22.9%', '22.9%', '23.2%', '24.3%', '17.1%',
#                 '14.1%', '8.5%', '11.2%', '9.9%', '6.7%', '7.2%', '3.7%', '3.7%', '4.0%']
beer_important_points.add_trace(
    go.Scatter(
        x=beer_important_points_koumoku,
        y=L_list,
        name="Light(n=375)",
        marker=dict(
            color='#d09356',
            size=8,
            line=dict(
                color='#d09356',
                width=1
            )
        )
    ))


beer_important_points.update_layout(height=400, width=1180, showlegend=True,
                                    autosize=False, title_text='缶ビール重視点<br>Base:3ヶ月以内缶ビール購入者')


# ============================================
#　マーケット浸透率 Base:3ヶ月以内缶ビール購入者
# ============================================

# マーケット浸透率 ▶︎
# 本麒麟
# ============================================
mpr_honkirin_list = dp.market_penetration_rate()['1 キリン「本麒麟」']

# x = ['19.8%', '31.7%', '51.3%', '76.4%']
y = ['主購入', '3ヶ月以内購入率', '購入経験率', '認知率']
honkirin_mp = go.Figure(data=[go.Bar(
    x=mpr_honkirin_list,
    y=y,
    text=mpr_honkirin_list,
    orientation='h',
    textposition='auto',
    marker=dict(
                color='#b24644',
                # color = 'rgba(201, 54, 0, 1.0)',
                line=dict(
                    color='#b24644',
                    width=1
                )
    )
)])

honkirin_mp.update_xaxes(range=[0, 100], dtick=25)
honkirin_mp.update_layout(height=200, width=360,
                          showlegend=False, margin=dict(t=10, r=0))

# マーケット浸透率 ▶︎
# 金麦
# ============================================
mpr_kinmugi_list = dp.market_penetration_rate()['2 サントリー「金麦」']
# x = ['16.7%', '32.0%', '59.6%', '84.2%']
y = ['主購入', '3ヶ月以内購入率', '購入経験率', '認知率']
meigara2_mp = go.Figure(data=[go.Bar(
    x=mpr_kinmugi_list,
    y=y,
    text=mpr_kinmugi_list,
    orientation='h',
    textposition='auto',
    marker=dict(
                color='#006fbe',
                line=dict(
                    color='#006fbe',
                    width=1
                )
    ),

)])
meigara2_mp.update_xaxes(range=[0, 100], dtick=25)
meigara2_mp.update_layout(height=200, width=360,
                          showlegend=False, margin=dict(t=10, r=0))

# マーケット浸透率 ▶︎
# クリアアサヒ
# ============================================
mpr_asahi_list = dp.market_penetration_rate()['3 アサヒ「クリアアサヒ」']

# x = ['10.5%', '24.3%', '53.2%', '79.8%']
y = ['主購入', '3ヶ月以内購入率', '購入経験率', '認知率']
meigara3_mp = go.Figure(data=[go.Bar(
    x=mpr_asahi_list,
    y=y,
    text=mpr_asahi_list,
    orientation='h',
    textposition='auto',
    marker=dict(
                color='#e0d666',
                line=dict(
                    color='#e0d666',
                    width=1
                )
    )
)])

meigara3_mp.update_xaxes(range=[0, 100], dtick=25)
meigara3_mp.update_layout(height=200, width=360, margin=dict(t=10, r=0))


# ============================================
#　歩留まり
# ============================================

# 歩留まり ▶︎
# 本麒麟
# ============================================
budomari_honkirin_list = dp.budomari()['1 キリン「本麒麟」']

# x = ['62.5%', '61.8%', '67.1%']
y = ['3ヶ月以内購入率→主購入', '購入経験率→3ヶ月以内購入率', '認知率→購入経験率']
honkirin_budomari = go.Figure(data=[go.Bar(
    x=budomari_honkirin_list,
    y=y,
    text=budomari_honkirin_list,
    orientation='h',
    textposition='auto',
    marker=dict(
                color='#b24644',
                line=dict(
                    color='#b24644',
                    width=1
                )
    )
)])

honkirin_budomari.update_xaxes(range=[0, 100], dtick=25)
honkirin_budomari.update_layout(
    height=200, width=360, showlegend=False, margin=dict(t=10, r=0))

# meigara2
budomari_kinmugi_list = dp.budomari()['2 サントリー「金麦」']

# x = ['52.2%', '53.7%', '70.8%']
y = ['3ヶ月以内購入率→主購入', '購入経験率→3ヶ月以内購入率', '認知率→購入経験率']
meigara2_budomari = go.Figure(data=[go.Bar(
    x=budomari_kinmugi_list,
    y=y,
    text=budomari_kinmugi_list,
    orientation='h',
    textposition='auto',
    marker=dict(
                color='#006fbe',
                line=dict(
                    color='#006fbe',
                    width=1
                )
    ),

)])
meigara2_budomari.update_xaxes(range=[0, 100], dtick=25)
meigara2_budomari.update_layout(
    height=200, width=360, showlegend=False, margin=dict(t=10, r=0))


budomari_asahi_list = dp.budomari()['3 アサヒ「クリアアサヒ」']
# x = ['43.2%', '45.7%', '66.7%']
y = ['3ヶ月以内購入率→主購入', '購入経験率→3ヶ月以内購入率', '認知率→購入経験率']
meigara3_budomari = go.Figure(data=[go.Bar(
    x=budomari_asahi_list,
    y=y,
    text=budomari_asahi_list,
    orientation='h',
    textposition='auto',
    marker=dict(
                color='#e0d666',
                line=dict(
                    color='#e0d666',
                    width=1
                )
    )
)])
meigara3_budomari.update_xaxes(range=[0, 100], dtick=25)
meigara3_budomari.update_layout(height=200, width=360, margin=dict(t=10, r=0))


# ============================================
#　HML別マーケット浸透率 Base:3ヶ月以内缶ビール購入者
# ============================================

# HML別マーケット浸透率 ▶︎
# 空のgraph.objects作成
# ============================================
hml_mpr = go.Figure()

# HML別マーケット浸透率 ▶︎
# 関数でそれぞれの値を取得
# ============================================
honkirin_h_list = dp.hml_market_penetration_rate()['1 キリン「本麒麟」H']
honkirin_m_list = dp.hml_market_penetration_rate()['1 キリン「本麒麟」M']
honkirin_l_list = dp.hml_market_penetration_rate()['1 キリン「本麒麟」L']

kinmugi_h_list = dp.hml_market_penetration_rate()['2 サントリー「金麦」H']
kinmugi_m_list = dp.hml_market_penetration_rate()['2 サントリー「金麦」M']
kinmugi_l_list = dp.hml_market_penetration_rate()['2 サントリー「金麦」L']

clear_asahi_h_list = dp.hml_market_penetration_rate()['3 アサヒ「クリアアサヒ」H']
clear_asahi_m_list = dp.hml_market_penetration_rate()['3 アサヒ「クリアアサヒ」M']
clear_asahi_l_list = dp.hml_market_penetration_rate()['3 アサヒ「クリアアサヒ」L']


# HML別マーケット浸透率 ▶︎
# make_subplots作成
# ============================================
hml_mpr = make_subplots(rows=1, cols=3, shared_yaxes=True,
                        subplot_titles=("Heavy(n=165)", "Middle(n=460)", "Light(n=375)"))

# HML別マーケット浸透率 ▶︎
# Heavy層
# ============================================

# y=[82.4, 66.1, 44.2, 20.6]
hml_mpr.add_trace(go.Scatter(x=["認知", "購入", "3ヶ月以内購入率", "主購入"], y=honkirin_h_list, marker_color='#b24644', name='本麒麟'),
                  row=1, col=1)

# [88.5, 70.3, 44.8, 18.2]
hml_mpr.add_trace(go.Scatter(x=["認知", "購入", "3ヶ月以内購入率", "主購入"], y=kinmugi_h_list, marker_color='#3371a0', name="金麦"),
                  row=1, col=1)

# y=[83, 70.3, 40, 15.8]
hml_mpr.add_trace(go.Scatter(x=["認知", "購入", "3ヶ月以内購入率", "主購入"], y=clear_asahi_h_list, marker_color='#978b00', name="クリアアサヒ"),
                  row=1, col=1)


# HML別マーケット浸透率 ▶︎
# Middle層
# ============================================
# y=[74.8, 56.7, 36.7, 24.3]
hml_mpr.add_trace(go.Scatter(x=["認知", "購入", "3ヶ月以内購入率", "主購入"], y=honkirin_m_list, marker_color='#b24644', name="本麒麟"),
                  row=1, col=2)

# y=[82.4, 62.8, 36.1, 17.6]
hml_mpr.add_trace(go.Scatter(x=["認知", "購入", "3ヶ月以内購入率", "主購入"], y=kinmugi_m_list, marker_color='#3371a0', name="金麦"),
                  row=1, col=2)

# y=[80, 57, 28.3, 12]
hml_mpr.add_trace(go.Scatter(x=["認知", "購入", "3ヶ月以内購入率", "主購入"], y=clear_asahi_m_list, marker_color='#978b00', name="クリアアサヒ"),
                  row=1, col=2)


# HML別マーケット浸透率 ▶︎
# Light層
# ============================================
# y=[75.7, 38.1, 20, 13.9]
hml_mpr.add_trace(go.Scatter(x=["認知", "購入", "3ヶ月以内購入率", "主購入"], y=honkirin_l_list, marker_color='#b24644', name="本麒麟"),
                  row=1, col=3)

# y=[84.5, 50.9, 21.3, 14.9]
hml_mpr.add_trace(go.Scatter(x=["認知", "購入", "3ヶ月以内購入率", "主購入"], y=kinmugi_l_list, marker_color='#3371a0', name="金麦"),
                  row=1, col=3)

# y=[78.1, 41.1, 12.5, 6.4]
hml_mpr.add_trace(go.Scatter(x=["認知", "購入", "3ヶ月以内購入率", "主購入"], y=clear_asahi_l_list, marker_color='#978b00', name="クリアアサヒ"),
                  row=1, col=3)

hml_mpr.add_layout_image(
    dict(
        source=app.get_asset_url("HML_market_hanrei_2.png"),
        xref="paper", yref="paper",
        x=1.07, y=1.06,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
    ),
)

hml_mpr.update_yaxes(range=[0, 100], dtick=25)
hml_mpr.update_layout(height=500, width=1180, margin=dict(b=10),
                      title_text="HML別マーケット浸透率<br>Base:3ヶ月以内缶ビール購入者", showlegend=False)


# ============================================
#　商品イメージ Base：各銘柄認知者
# ============================================

# 商品イメージ Base：各銘柄認知者 ▶︎
# 共通のラベル
# ============================================
categories = ['飲みやすい', '気軽に飲める', 'のど越しが良い', '食事に合う', 'キレがある', '品質が良い',
              '飲みごたえがある', 'コクがある', '後味が良い', '本格的']

# 商品イメージ Base：各銘柄認知者 ▶︎
# 本麒麟
# ============================================
radar = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "pie"}, {}]],
)

honkirin_1_list = dp.product_image()['キリン「本麒麟」']
radar.add_trace(go.Scatterpolar(
    #    r=[23.7, 18.5, 19.0, 15.3, 16.5, 20.4, 23.6, 23.2, 11.5, 25.0],
    r=honkirin_1_list,
    theta=categories,
    fill='toself',
    name='本麒麟'
))

radar.update_layout(
    height=300, width=358, title_text="",  margin=dict(r=0, l=10, t=60, b=30),
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 40]
        )),
    showlegend=False
)

# 商品イメージ Base：各銘柄認知者 ▶︎
# 金麦
# ============================================
radar_2 = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "pie"}, {}]],
)

kinmugi_1_list = dp.product_image()['サントリー「金麦」']
radar_2.add_trace(go.Scatterpolar(
    # r=[35.0, 27.6, 19.4, 19.4, 12.7, 16.3, 14.3, 13.4, 14.4, 11.2],
    r=kinmugi_1_list,
    theta=categories,
    fill='toself',
    name='金麦',
))


radar_2.update_layout(
    height=300, width=358, title_text="",  margin=dict(r=0, l=10, t=60, b=30),
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 40]
        )),
    showlegend=False
)

# 商品イメージ Base：各銘柄認知者 ▶︎
# クリアアサヒ
# ============================================
radar_3 = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "pie"}, {}]],
)

asahi_1_list = dp.product_image()['アサヒ「クリアアサヒ」']
radar_3.add_trace(go.Scatterpolar(
    # r=[37.5, 28.2, 23.7, 18.2, 18.8, 12.0, 10.2, 10.4, 14.3, 7.0],
    r=asahi_1_list,
    theta=categories,
    fill='toself',
    name='クリアアサヒ'
))


radar_3.update_layout(
    height=300, width=358, title_text="",  margin=dict(r=0, l=10, t=60, b=30),
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 40]
        )),
    showlegend=False
)


# ============================================
#　重視点と銘柄別イメージの比較
# ============================================

# 重視点と銘柄別イメージの比較
# 重視点
# ============================================
beer_important_points_koumoku = ['のど越しが良いこと',
                                 '飲みやすいこと',
                                 'キレがあること',
                                 '飲みごたえがあること',
                                 '気軽に飲めること',
                                 'コクがあること',
                                 '後味が良いこと',
                                 '食事に合うこと',
                                 '品質が良いこと',
                                 '本格的なこと',
                                 '香りが良いこと',
                                 '味が濃いこと',
                                 '泡がきめ細かいこと',
                                 '素材にこだわっていること',
                                 '苦味があること',
                                 '健康にこだわっていること',
                                 '高級感があること',
                                 '話題性があること',
                                 'あてはまるものはない']

# 重視点と銘柄別イメージの比較
# 本麒麟
# ============================================
q9s1_honkirin_array = ['19.0%', '23.7%', '16.5%', '23.6%', '18.5%', '23.2%', '11.5%', '15.3%', '20.4%',
                       '25.0%', '10.3%', '15.8%', '7.9%', '13.7%', '12.0%', '4.6%', '10.1%', '14.3%', '15.7%']
y = q9s1_honkirin_array,
m_fig3 = go.Figure()
m_fig3.add_trace(
    go.Scatter(
        x=beer_important_points_koumoku,
        y=q9s1_honkirin_array,
        name="本麒麟(n=764)",
        marker=dict(
            color='#b24644',
            size=12,
            line=dict(
                color='#b24644',
                width=1
            )
        )
    ))


# 重視点と銘柄別イメージの比較
# 金麦
# ============================================
q9s2_kinmugi_array = ['19.4%', '35.0%', '12.7%', '14.3%', '27.6%', '13.4%', '14.4%', '19.4%',
                      '16.3%', '11.2%', '12.5%', '7.5%', '8.9%', '10.1%', '7.0%', '5.1%', '6.7%', '7.4%', '19.1%']
m_fig3.add_trace(
    go.Scatter(
        x=beer_important_points_koumoku,
        y=q9s2_kinmugi_array,
        name="金麦(n=842)",
        marker=dict(
            symbol='cross',
            color='#3371a0',
            size=8,
            line=dict(
                color='#3371a0',
                width=1
            )
        )
    ))


# 重視点と銘柄別イメージの比較
# クリアアサヒ
# ============================================
q7cs_asahi_array = ['23.7%', '37.5%', '18.8%', '10.2%', '28.2%', '10.4%', '14.3%', '18.2%',
                    '12.0%', '7.0%', '8.5%', '5.0%', '16.3%', '7.6%', '6.8%', '6.0%', '4.5%', '5.8%', '17.5%']
m_fig3.add_trace(
    go.Scatter(
        x=beer_important_points_koumoku,
        y=q7cs_asahi_array,
        name="クリアアサヒ(n=798)",
        marker=dict(
            symbol='diamond',
            color='#978b00',
            size=8,
            line=dict(
                color='#978b00',
                width=1
            )
        )
    ))


q7c_array = ['45.4%', '41.8%', '31.9%', '29.5%', '29.0%', '28.6%', '27.2%', '26.9%', '25.4%', '19.8%',
             '16.9%', '14.5%', '14.1%', '13.3%', '13.1%', '9.4%', '7.0%', '4.0%', '2.2%']

m_fig3.add_trace(
    go.Bar(
        x=beer_important_points_koumoku,
        y=q7c_array,
        name="全体(n=1,000)",
        text=q7c_array,
        textposition="auto",
        marker=dict(
            color='#c0c4c7',
            line=dict(
                color='#c0c4c7',
                width=1
            )
        )
    )
)

m_fig3.update_layout(height=400, width=1180, showlegend=True,
                     autosize=False, title_text='重視点と銘柄別イメージの比較<br>Base:　重視点→3ヶ月以内缶ビール購入者<br>イメージ→各銘柄認知者')


# ============================================
#　各銘柄のワードクラウド
# ============================================

# 各銘柄のワードクラウド ▶︎
# 本麒麟
# ============================================
honkirin_wc = pd.read_csv("data/honkirin_wc3.csv")

honkirin_words = honkirin_wc['word']
colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(
    1, 10)] for i in range(150)]
honkirin_weights = honkirin_wc['count'] * 3

data = go.Scatter(x=[random.random() for i in range(30)],
                  y=[random.random() for i in range(1200)],
                  mode='text',
                  text=honkirin_words,
                  marker={'opacity': 0.3},
                  textfont={'size': honkirin_weights,
                            'color': colors})
layout = go.Layout({'title_text': '本麒麟 購入理由(n=198)<br>(頻出語の内、出現回数5回以上の単語を抽出)',
                    'height': 450,
                    'width': 1180,
                    'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                    'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}},
                   margin=dict(r=0, l=0, t=80, b=30))
honkirin_wc = go.Figure(data=[data], layout=layout)

# 各銘柄のワードクラウド ▶︎
# 金麦
# ============================================
kinmugi_wc = pd.read_csv("data/kinmugi_wc2.csv")

kinmugi_words = kinmugi_wc['word']
colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(
    1, 10)] for i in range(150)]
kinmugi_weights = kinmugi_wc['count'] * 3

data = go.Scatter(x=[random.random() for i in range(30)],
                  y=[random.random() for i in range(1200)],
                  mode='text',
                  text=kinmugi_words,
                  marker={'opacity': 0.3},
                  textfont={'size': kinmugi_weights,
                            'color': colors})
layout = go.Layout({'title_text': '金麦 購入理由(n=167)<br>(頻出語の内、出現回数5回以上の単語を抽出)',
                    'height': 450,
                    'width': 1180,
                    'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                    'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}},
                   margin=dict(r=0, l=0, t=80, b=30))
kinmugi_wc = go.Figure(data=[data], layout=layout)

# 各銘柄のワードクラウド ▶︎
# クリアアサヒ
# ============================================
asahi_wc = pd.read_csv("data/asahi_wc2.csv")

asahi_words = asahi_wc['word']
colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(
    1, 10)] for i in range(150)]
asahi_weights = asahi_wc['count'] * 3

data = go.Scatter(x=[random.random() for i in range(30)],
                  y=[random.random() for i in range(1200)],
                  mode='text',
                  text=asahi_words,
                  marker={'opacity': 0.3},
                  textfont={'size': asahi_weights,
                            'color': colors})
layout = go.Layout({'title_text': 'クリアアサヒ 購入理由(n=105)<br>(頻出語の内、出現回数5回以上の単語を抽出)',
                    'height': 450,
                    'width': 1180,
                    'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                    'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}},
                   margin=dict(r=0, l=0, t=80, b=30))
asahi_wc = go.Figure(data=[data], layout=layout)


# ============================================
#　アプリの表示部分
# ============================================
app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url("MApps-logo.png"),
                            id="",
                            style={
                                "height": "60px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "MApps Dashbord",
                                    style={"margin-bottom": "0px",
                                           "text-align": "center"},
                                ),
                                html.H5(
                                    "ヒット商品分析", style={"margin-top": "0px", "text-align": "center"}
                                ),
                            ]
                        )
                    ],
                    className="one-third column",
                    id="",
                ),
                html.Div(
                    [
                    ],
                    className="one-third column",
                    id="",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dcc.Graph(
                                            id="",
                                            figure=gender_and_age_distribution
                                        ),
                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px 0px 0px 5px', 'height': '700px',
                                              'margin': '10px 0px 10px 10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey',
                                              }

                                ),
                            ],
                            id="",
                            className="row container-display",
                        ),
                    ],
                    id="",
                    className="",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dcc.Graph(
                                            id="",
                                            figure=HML_bubble
                                        ),
                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px 0px 0px 5px', 'height': '350px',
                                              'margin': '10px 0px 10px 10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey',
                                              }
                                ),
                                html.Div(
                                    [
                                        html.Span(
                                            ['缶ビールの月間飲用量で分類。', html.Br()]),
                                        html.Span(
                                            ['Heavy　 ：10L以上/月', html.Br()]),
                                        html.Span(
                                            ['Middle　 ：2L～10L未満/月', html.Br()]),
                                        html.Span(
                                            ['Light　　：2L未満/月', html.Br(), html.Br()]),

                                        html.Span(
                                            '※缶ビールの飲用頻度及び1回あたりの飲用量の回答結果から月間飲用量を推定しています。'),
                                    ], style={'background-color': '#ffffff', 'text-align': 'left', 'border-radius': '0px 5px 5px 0px', 'height': '315px', 'width': '260px',
                                              'margin': '10px 0px 10px 0px', 'padding': '50px 15px 15px 15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey',
                                              }
                                ),
                            ],
                            id="",
                            className="row container-display",
                        ),
                    ],
                    id="",
                    className="",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=beer_important_points

                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'width': '1500px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }


                                ),

                            ],
                            id="info-container-multiple",
                            className="row container-display",
                        ),
                    ],
                    id="right-column-multiple",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.H6(
                    ['マーケット浸透率', html.Br(), 'Base:3ヶ月以内缶ビール購入者(n=1,000)'],
                    className="subtitle padded",
                ),
            ]

        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "honkirin.jpeg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=honkirin_mp,

                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }
                                ),
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "kinmugi.jpg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=meigara2_mp,
                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }
                                ),
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "clear-asahi.jpg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=meigara3_mp,
                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }
                                ),
                            ],
                            id="",
                            className="row container-display",
                        ),
                    ],
                    id="",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.H6(
                    "歩留まり",
                    className="subtitle padded",
                ),
            ]

        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "honkirin.jpeg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=honkirin_budomari,

                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }
                                ),
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "kinmugi.jpg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=meigara2_budomari,
                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }
                                ),
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "clear-asahi.jpg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=meigara3_budomari,
                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }
                                ),
                            ],
                            id="",
                            className="row container-display",
                        ),
                    ],
                    id="",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=hml_mpr

                                        ),

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey',
                                              }
                                )
                            ],
                            id="splom info-container-multiple",
                            className="row container-display",
                        ),
                    ],
                    id="splom right-column-multiple",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.H6(
                    "商品イメージ Base：各銘柄認知者",
                    className="subtitle padded",
                ),
                html.P(
                    ['本麒麟(n=764)、金麦(n=842)、クリアアサヒ(n=798)'],
                ),
            ],

        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "honkirin.jpeg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=radar,

                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }
                                ),
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "kinmugi.jpg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=radar_2,
                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }

                                ),
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "clear-asahi.jpg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=radar_3,
                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }

                                ),
                            ],
                            id="",
                            className="row container-display",
                        ),
                    ],
                    id="",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=m_fig3

                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'width': '1500px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }

                                ),

                            ],
                            id="",
                            className="row container-display",
                        ),
                    ],
                    id="",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.H6(
                    ['各銘柄のNPS（推奨度）', html.Br(), 'Base:各銘柄3ヶ月以内購入者'],
                    className="subtitle padded",
                ),
                html.P(
                    "「推奨度を0-10の11段階で聴取、「推奨者（9,10選択者）の割合」と「批判者（0-6選択者）の割合」の差分でスコア化。",
                    className="",
                ),
            ]

        ),

        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "honkirin.jpeg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),



                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'height': '200px', 'width': '358px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }

                                ),
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "kinmugi.jpg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'height': '200px', 'width': '358px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }
                                ),
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "clear-asahi.jpg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),
                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'height': '200px', 'width': '358px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }
                                ),
                            ],
                            id="",
                            className="row container-display",
                        ),
                    ],
                    id="",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Div(
                                            [
                                                html.Span(
                                                    ['全体（３ヶ月以内購入者）n=317', html.Br()]
                                                ),
                                                html.Span(
                                                    '7.26', style={'font-size': 'xx-large', 'font-weight': 'bold'}
                                                )
                                            ],
                                        ),
                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'height': '50px', 'width': '358px',
                                              'margin': '10px', 'padding': '0px 0px 30px 0px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }

                                ),
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Div(
                                            [
                                                html.Span(
                                                    ['全体（３ヶ月以内購入者) n=320',
                                                        html.Br()]
                                                ),
                                                html.Span(
                                                    '10.3', style={'font-size': 'xx-large', 'font-weight': 'bold'}
                                                )
                                            ],

                                        ),

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'height': '50px', 'width': '358px',
                                              'margin': '10px', 'padding': '0px 0px 30px 0px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }

                                ),
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Div(
                                            [
                                                html.Span(
                                                    ['全体（３ヶ月以内購入者) n=243',
                                                        html.Br()]
                                                ),

                                                html.Span(
                                                    '-3.7', style={'font-size': 'xx-large', 'font-weight': 'bold'}
                                                )
                                            ]

                                        ),
                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'height': '50px', 'width': '358px',
                                              'margin': '10px', 'padding': '0px 0px 30px 0px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }

                                ),
                            ],
                            id="",
                            className="row container-display",
                        ),
                    ],
                    id="",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.H6(
                    "各銘柄のワードクラウド",
                    className="subtitle padded",
                ),
            ],

        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=honkirin_wc

                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'width': '1500px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }
                                ),

                            ],
                            id="",
                            className="row container-display",
                        ),
                    ],
                    id="",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=kinmugi_wc

                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'width': '1500px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }

                                ),

                            ],
                            id="",
                            className="row container-display",
                        ),
                    ],
                    id="",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        dcc.Graph(
                                            id="",
                                            figure=asahi_wc

                                        )

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'width': '1500px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }
                                ),

                            ],
                            id="",
                            className="row container-display",
                        ),
                    ],
                    id="",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.H6(
                    "各銘柄の共起ネットワーク",
                    className="subtitle padded",
                ),
                html.P(
                    ['本麒麟(n=198)、金麦(n=167)、クリアアサヒ(n=105)'],
                ),
            ],

        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "honkirin.jpeg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "honkirin_co_network3.png"),
                                            id="",
                                            style={
                                                "height": "450px",
                                                "width": "563px",
                                                "margin-bottom": "0px",
                                            },
                                        ),

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }

                                ),
                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "kinmugi.jpg"),
                                            id="",
                                            style={
                                                "height": "150px",
                                                "width": "150px",
                                                "margin-bottom": "0px",
                                            },
                                        ),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "kinmugi_co_network3.png"),
                                            id="",
                                            style={
                                                "height": "450px",
                                                "width": "563px",
                                                "margin-bottom": "0px",
                                            },
                                        ),

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }

                                ),

                            ],
                            id="",
                            className="row container-display",
                        ),
                    ],
                    id="",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [

                                html.Div(
                                    [

                                        html.H6(
                                            id=""
                                            ""
                                        ),
                                        html.Div(
                                            [
                                                html.Img(
                                                    src=app.get_asset_url(
                                                        "clear-asahi.jpg"),
                                                    id="",
                                                    style={
                                                        "height": "150px",
                                                        "width": "150px",
                                                        "margin-bottom": "0px",
                                                    },
                                                ),
                                            ]),
                                        html.Img(
                                            src=app.get_asset_url(
                                                "asahi_co_network3.png"),
                                            id="",
                                            style={
                                                "height": "450px",
                                                "width": "563px",
                                                "margin-bottom": "0px",
                                            },
                                        ),

                                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px',
                                              'margin': '10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                                              }

                                ),
                            ],
                            id="",
                            className="row container-display",
                        ),
                    ],
                    id="",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
    ],
    id="mainContainerhoge",
    style={"display": "flex", "flex-direction": "column"},
)

# ============================================
#　アプリの起動
# ============================================
if __name__ == "__main__":
    app.run_server(debug=True)
