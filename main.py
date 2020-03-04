import matplotlib as mpl
import matplotlib.pyplot as plt
import math

x = [345280000.0, 344910000.0, 340800000.0, 335950000.0, 336490000.0, 338990000.0, 343690000.0, 346170000.0, 348870000.0, 353950000.0, 364460000.0, 
     370780000.0, 365640000.0, 361720000.0, 359050000.0, 357620000.0, 355230000.0, 353020000.0, 355510000.0, 359320000.0, 360650000.0, 361860000.0, 
     358730000.0, 355060000.0, 354280000.0, 356740000.0, 363780000.0, 371720000.0, 376440000.0, 374870000.0, 377550000.0, 386530000.0, 390380000.0, 
     394040000.0, 397640000.0, 400830000.0, 410700000.0, 414880000.0, 417260000.0, 419850000.0] # Кількість Робочих

y = [21875.946, 21858.888, 21702.091,	22116.623, 22833.864, 23392.174, 23941.167, 24288.566, 25043.371, 25765.860, 26728.077, 
     27707.890, 28056.398, 27629.360, 28220.956, 28599.312,	28776.123, 29275.549,	29890.019, 30462.464, 31333.982, 31839.544,	
     31751.748,	31538.462, 31948.734, 32228.752, 33525.493,	34600.134, 35032.935, 33153.234, 34625.895, 35985.076, 36071.071,
     36127.668, 36775.383, 37093.549,	37615.886, 38399.535,	38868.792, 39049.118] # ВВП на душу населення

y1 = []

def moda():
  popular_table = {}
  for i in x:
    try:
      data = popular_table[str(i)]
      popular_table[str(i)] += 1
    except:
      popular_table[str(i)] = 1

  max_key = None
  newkey = None
  for key, value in popular_table.items(): 
    if max_key == None:
      newkey = key
      max_key = {key: value}
    else:
      if value > max_key[newkey]:
        newkey = key
        max_key = {key: value}
  if max_key[newkey] == 1:
    return None
  else:
    return float(newkey)


def avg_result(arr):
  sm = 0
  for i in arr:
    sm += i
  return sm / len(arr)



def cor():
  z = 0
  k = 0
  for i in range(len(x)):
    z += ((x[i] - avg_result(x)) * (y[i] - avg_result(y)))
    k += (((x[i] - avg_result(x))**2) * ((y[i] - avg_result(y))**2))

  return (z / len(x)) / math.sqrt(k)


def b():
  x_avg = avg_result(x)
  y_avg = avg_result(y)

  result = 0
  var = 0

  for i in range(len(x)):
    result += (x[i] - x_avg)*(y[i] - y_avg)
    var += (x[i] - x_avg)**2

  return result / var

def a():
  a = avg_result(y) - (b()*avg_result(x))
  return a

def formula(x):
  result = a() + (b() * x)
  return result

for i in range(len(x)):
  y1.append(formula(x[i]))


def determ():
  ssr = 0
  sst = 0
  sse = 0

  for i in range(len(y)):
    ssr += (y1[i] - avg_result(y))**2
    sst += (y[i] - avg_result(y))**2
    sse += (y[i] - y1[i])**2

  sse = sse / len(y)
  sst = sst / len(y)
  
  return sse / sst

def sd():
  sd_y = 0
  sd_y1 = 0
  for i in range(len(y)):
    sd_y += (y[i] - avg_result(y))**2
    sd_y1 += (y1[i] - avg_result(y1))**2
  
  sd_y = sd_y / len(y)
  sd_y1 = sd_y1 / len(y)

  return {    
      "mr_y1": sd_y1 / len(y),
      "mr_y": sd_y / len(y),
  }

def f_crit():
  d = determ()
  result = (d / (1 - d)) / ((len(x) - 1 - 1) / 1)
  
  k = sd()
  
  s = (avg_result(y1) - avg_result(y)) / math.sqrt(k["mr_y1"] + k["mr_y"])

  print("Критерій Стюдента: {}".format(s))
  print("Коефіцієнт детермінації: {}".format(d))
  print("Критерій фішера {}".format(result))
  print("Кореляція {}".format(cor()))
 
 
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (840 / dpi, 480 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.xlabel('Кількість робочих')
plt.ylabel('ВВП на душу населення в Deutsche mark(DEM)')


plt.scatter(x, y, color='blue', s=40, marker='o')

 
plt.plot(x, y1, color = 'red', linestyle = 'solid',
         label = 'y = {0} + {1}x'.format(round(a(), 4), round(b(), 4)))

plt.plot([avg_result(x), avg_result(x)], [min(y), max(y)], color = 'green', linestyle = 'solid',
         label = 'Середнє значення X')

plt.plot([max(x), max(x)], [min(y), max(y)], color = 'black', linestyle = 'solid',
         label = 'Максимальне значення Y')

plt.plot([min(x), min(x)], [min(y), max(y)], color = 'yellow', linestyle = 'solid',
         label = 'Мінімальне значення X')

plt.plot([min(x), max(x)], [avg_result(y), avg_result(y)], color = 'brown', linestyle = 'solid',
         label = 'Середнє значення Y')



plt.legend(loc = 'upper right')
fig.savefig('trigan.png')

if moda() == None:
  print("Всі данні унікальні, мода не знайдена")
else:
  plt.plot([moda(), moda()], [min(y), max(y)], color = 'black', linestyle = 'solid',
         label = 'Мода')
f_crit()
