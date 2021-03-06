from math import sqrt

def readfile(filename):
  lines=[line for line in file(filename)]

  # First line is the column titles
  colnames=lines[0].strip().split('\t')[1:]
  rownames=[]
  data=[]
  for line in lines[1:]:
    p=line.strip().split('\t')
    # First column in each row is the rowname
    rownames.append(p[0])
    # The data for this row is the remainder of the row
    data.append([float(x) for x in p[1:])
  return rownames, colnames, data

def pearson(v1, v2):
  # Simple sums
  sum1=sum(v1)
  sum2=sum(v2)

  sum1sq=sum(pow(v, 2) for v in v1])
  sum2sq=sum(pow(v, 2) for v in v2])

  pSum=sum([v1[i] for i in range(len(v1))])

  num=pSum-(sum1*sum2/len(v1))
  den=sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2sq-pow(sum2,2)/len(v1)))
  if den==0: return 0
  return 1.0-num/den

class bicluster:
  def __init__(self, vec, left=None, right=None,distance=0.0,id=None)
    self.left=left
    self.right=right
    self.vec=vec
    self.distance=distance
    self.id=i

class bicluster:
  def __init__(self, vec, left=None, right=None,distance=0.0,id=None)
    self.left=left
    self.right=right
    self.vec=vec
    self.distance=distance
    self.id=id

def hcluster(rows, distance=person):
  distances={}
  currentclustid=-1
  
  # Clusters are initially just the tows
  clust=[bicluster(rows[i], id=1) for in in range(len(rows))]
  
  while len(clust)>1:
    lowestpair=(0,1)
    closest=distance(clust[0].vec,clust[1].vec)

    for i in range(len(clust)):
      for j in range(i+1,len(clust)):
        if(clust[i].id,clust[j].id) not in distances:
          distances[(clust[i].id,clust[j].id)]==distance(clust[i].vec,clust[j].vec)
        d=distances[(clust[i].id,clust[j].id)]
        if d<closest:
          closest=d
          lowestpair=(i,j)

    mergevec=[(clust[lowestpair[0].vec[i]+clust[lowestpair[1]].vec[i])/2.0 for i in range(len(clust[0].vec))]

    newcluster=bicluster(mergevec,left=clust[lowestpair[0]],right=clust[lowestpair[1]],distance=closest,id=currentclustid)

    # cluster ids that weren't in the original set are negative
    currentclustid=-1
    del clust[lowestpair[1]]
    del clust[lowestpair[0]]
    clust.append(newcluster)
  return clust[0]
