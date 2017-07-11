# -*-coding:utf-8 -*-
import plotly.offline as pyoff
import plotly.graph_objs as go
import plotly as py
from app.models import Kjhm, Weather


def count_of_ball():
    numbers = []
    cols = ['num1', 'num2', 'num3', 'num4', 'num5', 'num6']
    for ball in range(1, 34):
        count = 0
        for col in cols:
            temp = Kjhm.get_count_by_col(col, ball)
            count += temp
        numbers.append(count)

    trace2 = go.Bar(x=[x for x in range(1, 34)], y=[num/max(numbers) for num in numbers])
    data = [trace2]
    pyoff.plot(data, filename="../templates/tables/count_of_ball.html", auto_open=True)


def get_kjhm_and_weather_by_count():
    numbers1, numbers2, numbers3, numbers4, numbers5, numbers6, numbers7, numbers8 = [], [], [], [], [], [], [], []
    numbers = [numbers1, numbers2, numbers3, numbers4, numbers5, numbers6, numbers7, numbers8]
    # end = Kjhm.get_count_by_col()
    # results = Kjhm.get_kjhm_and_weather_by_count(end=993)
    cols = ['num1', 'num2', 'num3', 'num4', 'num5', 'num6']
    weathers = ['阴', '晴', '小雨', '阵雨', '中雨', '雾', '小雪', '鬼天气']

    index = 0
    for desc in weathers:
        for ball in range(1, 34):
            count2 = 0
            for col in cols:
                temp = Kjhm.get_kjhm_and_weather_by_col(col, ball, desc)
                count2 += temp
            numbers[index].append(count2)
        index += 1

    trace1 = go.Scatter(x=[x for x in range(1, 34)], y=[x/Weather.get_desc_count_by_desc(weathers[0]) for x in numbers1], name=weathers[0])
    trace2 = go.Scatter(x=[x for x in range(1, 34)], y=[x/Weather.get_desc_count_by_desc(weathers[1]) for x in numbers2], name=weathers[1])
    trace3 = go.Scatter(x=[x for x in range(1, 34)], y=[x/Weather.get_desc_count_by_desc(weathers[2]) for x in numbers3], name=weathers[2])
    trace4 = go.Scatter(x=[x for x in range(1, 34)], y=[x/Weather.get_desc_count_by_desc(weathers[3]) for x in numbers4], name=weathers[3])
    trace5 = go.Scatter(x=[x for x in range(1, 34)], y=[x/Weather.get_desc_count_by_desc(weathers[4]) for x in numbers5], name=weathers[4])
    trace6 = go.Scatter(x=[x for x in range(1, 34)], y=[x/Weather.get_desc_count_by_desc(weathers[5]) for x in numbers6], name=weathers[5])
    trace7 = go.Scatter(x=[x for x in range(1, 34)], y=[x/Weather.get_desc_count_by_desc(weathers[6]) for x in numbers7], name=weathers[6])
    trace8 = go.Scatter(x=[x for x in range(1, 34)], y=[x/Weather.get_desc_count_by_desc(weathers[7]) for x in numbers8], name=weathers[7])
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]
    pyoff.plot(data, auto_open=True, filename="../templates/tables/weather_and_ball.html")


def blue_pic_bar():
    numbers = []
    for ball in range(1, 17):
        temp = Kjhm.get_count_by_col('num7', ball)
        numbers.append(temp)

    trace2 = go.Bar(x=[x for x in range(1, 17)], y=[num / max(numbers) for num in numbers])
    data = [trace2]
    pyoff.plot(data, filename="../templates/tables/blue_Pic_bar.html", auto_open=True)


def blue_pic_scatter():
    weathers = ['阴', '晴', '小雨', '阵雨', '中雨', '雾', '小雪', '鬼天气']
    numbers1, numbers2, numbers3, numbers4, numbers5, numbers6, numbers7, numbers8 = [], [], [], [], [], [], [], []
    numbers = [numbers1, numbers2, numbers3, numbers4, numbers5, numbers6, numbers7, numbers8]
    index = 0
    for desc in weathers:
        for ball in range(1, 17):
            temp = Kjhm.get_kjhm_and_weather_by_col('num7', ball, desc)
            numbers[index].append(temp)
        index += 1

    trace1 = go.Scatter(x=[x for x in range(1, 17)],
                        y=[x / Weather.get_desc_count_by_desc(weathers[0]) for x in numbers1], name=weathers[0])
    trace2 = go.Scatter(x=[x for x in range(1, 17)],
                        y=[x / Weather.get_desc_count_by_desc(weathers[1]) for x in numbers2], name=weathers[1])
    trace3 = go.Scatter(x=[x for x in range(1, 17)],
                        y=[x / Weather.get_desc_count_by_desc(weathers[2]) for x in numbers3], name=weathers[2])
    trace4 = go.Scatter(x=[x for x in range(1, 17)],
                        y=[x / Weather.get_desc_count_by_desc(weathers[3]) for x in numbers4], name=weathers[3])
    trace5 = go.Scatter(x=[x for x in range(1, 17)],
                        y=[x / Weather.get_desc_count_by_desc(weathers[4]) for x in numbers5], name=weathers[4])
    trace6 = go.Scatter(x=[x for x in range(1, 17)],
                        y=[x / Weather.get_desc_count_by_desc(weathers[5]) for x in numbers6], name=weathers[5])
    trace7 = go.Scatter(x=[x for x in range(1, 17)],
                        y=[x / Weather.get_desc_count_by_desc(weathers[6]) for x in numbers7], name=weathers[6])
    trace8 = go.Scatter(x=[x for x in range(1, 17)],
                        y=[x / Weather.get_desc_count_by_desc(weathers[7]) for x in numbers8], name=weathers[7])
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]
    pyoff.plot(data, auto_open=True, filename="../templates/tables/blue_pic_scatter.html")


if __name__ == '__main__':
    blue_pic_scatter()

