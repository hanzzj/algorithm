from random import randint
import time

#普通快排
def quick_sort(list): 
	if not list:  #当list为空时返回
		return []
	else:
		div=list[0]
		left=quick_sort([l for l in list[1:] if l<=div])
		right=quick_sort([r for r in list[1:] if r>div])
		return left+[div]+right

#随机化快排
def randomized_quicksort(list):
       if not list:
                return []
       else:
                div = list[randint(0,len(list)-1)]
                list[0], list[div]=list[div], list[0]
                div=list[0]
                left=quick_sort([l for l in list[1:] if l<=div])
                right=quick_sort([r for r in list[1:] if r>div])
                return left+[div]+right



if __name__ == '__main__':
  #list_demo = [randint(1,50) for i in range(10000)] #随机序列
  list_demo=[i for i in range(500)] #有序序列
  i, sum=0,0
  while i<10:
    start = time.time()
    quick_sort(list_demo)
    end=time.time()
    sum=sum+float(end-start)
    i+=1
  print("普通快排平均所需要时间为："+str(sum/10))

  i, sum=0,0
  while i<10:
    start = time.time()
    randomized_quicksort(list_demo)
    end=time.time()
    sum=sum+float(end-start)
    i+=1
  print("快排随机化平均所需时间为："+str(sum/10))





