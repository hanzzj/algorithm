class goods:
    def __init__(self, name, benefit, weight):
        self.name = name
        self.weight = weight
        self.benefit = benefit
        
def sort_benefit(capacity=0, goods_set=[]):
    #以效益为第一排序元素
  goods_set.sort(key=lambda obj:obj.weight, reverse=True)
  goods_set.sort(key=lambda obj:obj.benefit, reverse=True)
  result = []
  all_benefit=0
  for a_goods in goods_set:
    if capacity < a_goods.weight:
      break
    result.append(a_goods)
    capacity -= a_goods.weight
    all_benefit += a_goods.benefit
  print("按效益值:"+str(all_benefit))
  return result

def sort_weight(capacity=0, goods_set=[]):
  #以重量为第一排序元素
  goods_set.sort(key=lambda obj:obj.benefit, reverse=False)
  goods_set.sort(key=lambda obj:obj.weight, reverse=False)
  result = []
  all_benefit=0
  for a_goods in goods_set:
    if capacity < a_goods.weight:
      break
    result.append(a_goods)
    capacity -= a_goods.weight
    all_benefit += a_goods.benefit
  print("按重量:"+str(all_benefit))
  '''for obj in result:
    print('物品编号:' + str(obj.name) + ' ,放入重量:' + str(obj.weight) + ',放入的价值:' + str(obj.benefit), end=',')'''
  return result

def sort_unit(capacity=0, goods=[]):
  # 按单位价值量排序
  goods.sort(key=lambda obj: obj.benefit / obj.weight, reverse=True)
  result = []
  all_benefit=0
  for a_goods in goods:
    if capacity < a_goods.weight:
      break
    result.append(a_goods)
    capacity -= a_goods.weight
    all_benefit += a_goods.benefit
  print("按单位价值量:"+str(all_benefit))
  return result


some_goods = [goods('A', 10, 35), goods('B', 40, 30), goods('C', 30, 60), goods('D', 50, 50), goods('E', 35, 40),goods('F',40,10), goods('G',30,25)]
res1 = sort_benefit(150, some_goods)
res2 = sort_weight(150, some_goods)
res3 = sort_unit(150, some_goods)

          
