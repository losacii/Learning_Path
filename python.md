### open file mode

  r   :read(只读)
  w   :write(覆盖原有内容)
  a   :append(追加)
  w+b
  r+b
  fp.flush()   (不退出，强制写入)

### eval(expression) | exec | execfile

  exp = "8****8"
  print(eval(exp))

### import string module (反射)

  mod = 'os'
  __import__(mod)
  print mod.path

  反射：以字符串的方式，導入摸快、執行函數
  （用於快速切換數據庫）

### random

  random.random()         0.0~1.0
  random.randint(3,5)     3~5
  random.randrange(3,5)   3~4

  生成隨機字母：
      (用chr函數將數字轉化爲英文字符)
      c = chr(random.randint(65, 90))

### MD5 加密

  import hashlib
  hash = hashlib.md5()
  hash.update('passcode')

  print( hash.hexdigest() )
  print( hash.digest()    )

### 序列化：把對象存儲爲字符串

  import pickle

  objx = ['x', 'y', 'z']
  obj_str = pickle.dumps(objx) " 把對象序列化爲字符串
  objy = pickle.loads(obj_str) “ 把字符串還原(反序列化)

  pickle.dump(objx, open("./obj.pk", "w"))
  objy = pickle.load(open("./obj.pk", "r"))

  * pickle 只在python中使用，json可以在各種場景使用
  * json 序列化的格式可讀，pickle不可讀

### 正則表達式

  res = re.match( pattern, str) # 匹配
  if res:
    print res.group()

  res = re.search(pattern, str) # 尋找
  if res:
    print res.group()

  * match     從頭開始”匹配“
  * search    只爲尋找1個
  * findall   全部尋找， 返回列表

  rp = re.compile('\d+')
  res = rp.findall(str)

  ?  *  +   {m}  {m,}  {m,n}

  \d{3,5}   3到5個數字

### time.localtime

  time.time()  -> seconds

  localtime(...)
    localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                              tm_sec,tm_wday,tm_yday,tm_isdst)

  In [5]: time.localtime(time.time()).tm_year
  Out[5]: 2018

  time.strftime("%Y-%m-%d %H:%M:%S")

### python: datetime module

  from datetime import timedelta

  t1 = timedelta(hours=7, minutes=36)
  t2 = timedelta(hours=11, minutes=32)
  t3 = timedelta(hours=13, minutes=37)
  t4 = timedelta(hours=21, minutes=0)

  arrival = t2 - t1
  lunch = (t3 - t2 - timedelta(hours=1))
  departure = t4 - t3

  print(arrival, lunch, departure)

### map, reduce, filter

### chr(n)   ord(c)

### lambda

~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~40~~~~~~~~50~~~~~~~~60~~~~~~~~70~~~~~~~~80|

http://www.cnblogs.com/wupeiqi/articles/4276448.html

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor inci
didunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exe
rcitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur 
sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim 
id est laborum.
