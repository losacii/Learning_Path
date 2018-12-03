### open file mode

  r   :read(只读)
  w   :write(覆盖原有内容)
  a   :append(追加)
  w+b
  r+b
  fp.flush()   (不退出，强制写入)

### eval(expression)

  exp = "8****8"
  print(eval(exp))

### py code

  mod = 'os'
  __import__(mod)
  print mod.path
