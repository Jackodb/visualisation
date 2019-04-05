import webview
import threading
import pandas as pd
import json

class Api:

    def getData(self,params):
        fields = ['Price','Mountain_neutral_view','Current']
        df = pd.read_csv('test.csv',usecols=fields)
        price_list = [round(i,3) for i in list(df.Price)]
        mountain = [round(i,3) for i in list(df.Mountain_neutral_view)]
        x = {
            'price': price_list,
            'mountain': mountain,
            'current': list(df.Current),
            'title': 'BTS/USD' # this will be a dynamic variable
        }
        y = json.dumps(x)
        return y


def create_app():
    # with open('sample.html', 'r') as x, open('style.css', 'r') as y:
    #     html = x.read() #css = y.read()
    #     webview.load_html(html)
    webview.evaluate_js('showChart();')
    # webview.load_css(css)


if __name__ == '__main__':
     t = threading.Thread(target=create_app)
     t.start()

     api = Api()
     webview.create_window('<Strategy> visualisation', 'sample.html', js_api=api, width=900, height=650, debug=True)
