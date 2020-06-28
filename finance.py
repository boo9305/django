import pandas as pd 

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
 # 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해줌 
 
# code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
  # 우리가 필요한 것은 회사명과 종목코드이기 때문에 필요없는 column들은 제외해준다. 

code_df.to_csv("code.txt")

def get_url(item_name , code_df):
    code = code_df.query("회사명=='{}'".format(item_name))['종목코드'].to_string(index=False)
    code = code.strip()
    print(code)
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code) 
    return url

# 신라젠의 일자데이터 url 가져오기 
item_name='신라젠' 
url = get_url(item_name, code_df) #
print(url)


df = pd.DataFrame() 
# 1페이지에서 20페이지의 데이터만 가져오기
for page in range(1, 21): 
    pg_url = '{url}&page={page}'.format(url=url, page=page) 
    df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)

df = df.dropna()
print(df.head())


for i in range(10000):
    str = "board%s" % i
    board = Board(name=str)
    board.save()
    