global trg
trg=0
def start_astar():
  #Check illegal moves
  def valid(x,y,z,ex,ey,ez):
      if(x<0 or x>ex or y<0 or y>ey or z<0 or z>ez):
        trg=1
        outfile = open("output.txt", "w+")
        outfile.write("FAIL")
        outfile.close()

        return False
      return True

  moves={}
  moves[0]=(1,0,0,10)
  moves[1]=(-1,0,0,10)
  moves[2]=(0,1,0,10)
  moves[3]=(0,-1,0,10)
  moves[4]=(0,0,1,10)
  moves[5]=(0,0,-1,10)
  moves[6]=(1,1,0,14)
  moves[7]=(1,-1,0,14)
  moves[8]=(-1,1,0,14)
  moves[9]=(-1,-1,0,14)
  moves[10]=(1,0,1,14)
  moves[11]=(1,0,-1,14)
  moves[12]=(-1,0,1,14)
  moves[13]=(-1,0,-1,14)
  moves[14]=(0,1,1,14)
  moves[15]=(0,1,-1,14)
  moves[16]=(0,-1,1,14)
  moves[17]=(0,-1,-1,14)

  with open ("input.txt","r") as file:
      alg=file.readline().strip()
      ex,ey,ez=list(map(int,file.readline().strip().split()))
      x,y,z=list(map(int,file.readline().strip().split()))
      dx,dy,dz=list(map(int,file.readline().strip().split()))
      # Fetched the algorithm, max domain values, entry and exit coordinates.
      n=int(file.readline().strip())
      dic={}
      
      thislst=[]
      #Assigning xn,yn and zn the coordinates of the nodes
      for _ in range(n):
          #print(file.readline().strip().split())
          thislst=[]
          line_items = list(map(int, file.readline().strip().split()))
          #print(line_items)
          xn = line_items.pop(0)
          #print(line_items)
          yn = line_items.pop(0)
          #print(line_items)
          zn = line_items.pop(0)
          for nxt_mv in line_items:
              #print(nxt_mv)
              #moves are not getting added corretly
              ##print(moves[nxt_mv-1][0])
              ##print(moves[nxt_mv-1][1])
              ##print(moves[nxt_mv-1][2])
              
              a=moves.keys()
              d=list(a)
              #print(d)
              #b=moves.keys()
              #c=moves.keys()
              
              if valid(xn + moves[nxt_mv-1][0],yn + moves[nxt_mv-1][1],zn + moves[nxt_mv-1][2],ex,ey,ez):  
                  thislst.append( ((xn + int(moves[nxt_mv-1][0]), yn + int(moves[nxt_mv-1][1]), zn + int(moves[nxt_mv-1][2])), int(moves[nxt_mv-1][3])))
              
              #print(thislst)

              dic[(xn,yn,zn)] = thislst


  from queue import PriorityQueue
  import math
  def astar():
      myQueue = PriorityQueue()
      queue1=[]
      pathfound=0
      #Appending the eucladian distance.
      queue1.append((math.sqrt(math.pow(x-dx,2)+math.pow(y-dy,2)+math.pow(z-dz,2)),0,(x,y,z)))
      #Creating a set for already visited nodes.
      visited=set()
      visited.add((x,y,z))
      Costmap={
          (x,y,z):0
      }
      Parentmap={

      # visited={ (x,y,z) : True
      (x,y,z):None
      }
      # print("parentmap",Parentmap)
      # print("visited",visited)
      pathisavail = False
      costtrace=[]
    # Loop till queue is not empty
      while len(queue1)!=0:
          if trg==1:
              break
          estimated,cost,current_node=queue1.pop(0)
          
          if         current_node == (dx,dy,dz):
              
              pathisavail=True
              break

          
          
          for child, current_cost in dic[current_node]:
              child= tuple(child)
              
              #If child is not been visited then append it
              
              
              if child not in visited:
                  
                  dis_hst=math.sqrt(math.pow(child[0]-dx,2)+math.pow(child[1]-dy,2)+math.pow(child[2]-dz,2))
                  queue1.append((dis_hst+current_cost+cost,current_cost+cost,child))
                  Parentmap[child]=(current_node)
                  Costmap[child]=(current_cost)
                  visited.add(child)

          
      # Parentmap[(x,y,z)]=None
      
      pathtrace=[]

      i=0 
      tracknode= (dx,dy,dz)
      #This is not working
      k=0
      costing1=0
      # print(visited)
      
      if pathisavail:
          
          
          pathtrace.append((dx,dy,dz))
          
          while Parentmap[tracknode] is not None:

              
              pathtrace.insert(0,Parentmap[tracknode])
              costtrace.insert(0,Costmap[tracknode])
              tracknode= Parentmap[tracknode]

              # cost=cost+1
              # if k==0:
              #     costing1=0
              # else:
              #     if ((pathtrace[k-1][0]!=pathtrace[k][0] and pathtrace[k-1][1]!=pathtrace[k][1]) or (pathtrace[k-1][1]!=pathtrace[k][1] and pathtrace[k-1][2]!=pathtrace[k][2]) or (pathtrace[k-1][0]!=pathtrace[k][0] and pathtrace[k-1][2]!=pathtrace[k][2]) ):
              #         costing1=1
              #     else:
              #         costing1=1
              # k=k+1
          # pathtrace.reverse()
      
      '''if len(pathtrace) ==0:
          print("FAIL")
      else:
          print(cost)
          print(k)
          print(pathtrace)'''

      outfile = open("output.txt", "w+")
      if(len(pathtrace)==0 or trg==1):
          #print('FAIL')
          outfile.write("FAIL")
          outfile.close()
      else:
          outfile.write(str(cost))
          outfile.write("\n")
          outfile.write(str(len(pathtrace)))
          outfile.write("\n")
          #print(best_dis)
          #print(best_dis+1)


          strf=''
          previousi= pathtrace[0]
          costing1 = 0
          #Print the output in the file
          strf+=str(x)+" "+str(y)+" "+str(z)+" 0\n"
          
          
          for i in range(1,len(pathtrace)):
              strf+=str(pathtrace[i][0])+" "+str(pathtrace[i][1])+" "+str(pathtrace[i][2])+" "+str(costtrace[i-1])
              # if i!=previousi:
              #     if ((previousi[0]!=i[0] and previousi[1]!=i[1]) or (previousi[1]!=i[1] and previousi[2]!=i[2]) or (previousi[0]!=i[0] and previousi[2]!=i[2]) ):
              #         costing1=1
              #     else:
              #         costing1=1
              # k=k+1
              
              # strf+=str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str(costing1)
              
              strf+="\n"
              # previousi = i
          outfile.write(strf.rstrip())
          outfile.close()
  astar()




def start_bfs():
  def valid(x,y,z,ex,ey,ez):
      if(x<0 or x>ex or y<0 or y>ey or z<0 or z>ez):
        trg=1
        outfile = open("output.txt", "w+")
        outfile.write("FAIL")
        outfile.close()
        return False
      return True
  # Moves in the domain for bfs
  moves={}
  moves[0]=(1,0,0)
  moves[1]=(-1,0,0)
  moves[2]=(0,1,0)
  moves[3]=(0,-1,0)
  moves[4]=(0,0,1)
  moves[5]=(0,0,-1)
  moves[6]=(1,1,0)
  moves[7]=(1,-1,0)
  moves[8]=(-1,1,0)
  moves[9]=(-1,-1,0)
  moves[10]=(1,0,1)
  moves[11]=(1,0,-1)
  moves[12]=(-1,0,1)
  moves[13]=(-1,0,-1)
  moves[14]=(0,1,1)
  moves[15]=(0,1,-1)
  moves[16]=(0,-1,1)
  moves[17]=(0,-1,-1)

  with open ("input.txt","r") as file:
      alg=file.readline().strip()
      ex,ey,ez=list(map(int,file.readline().strip().split()))
      x,y,z=list(map(int,file.readline().strip().split()))
      dx,dy,dz=list(map(int,file.readline().strip().split()))
      # visited1=[[[0 for i in range(ez)]for j in range(ey)]for z in range(ex)]
      n=int(file.readline().strip())
      dic={}
      thislst=[]
      # Getting x,y and z coordinates and their moves and adding the cost in thislst
      for _ in range(n):
          #print(file.readline().strip().split())
          thislst=[]
          line_items = list(map(int, file.readline().strip().split()))
          #print(line_items)
          '''print(xn)
          print(yn)
          print(zn)'''
          xn = line_items.pop(0)
          #print(line_items)
          yn = line_items.pop(0)
          #print(line_items)
          zn = line_items.pop(0)
          #print(line_items)
          #m=len(line_items)
          #print(m)
          for nxt_mv in line_items:
              #print(nxt_mv)
              #moves are not getting added corretly
              ##print(moves[nxt_mv-1][0])
              ##print(moves[nxt_mv-1][1])
              ##print(moves[nxt_mv-1][2])
              
              a=moves.keys()
              d=list(a)
              #print(d)
              #b=moves.keys()
              #c=moves.keys()
              
              if valid(xn + moves[nxt_mv-1][0],yn + moves[nxt_mv-1][1],zn + moves[nxt_mv-1][2],ex,ey,ez):  
                  thislst.append([ xn + int(moves[nxt_mv-1][0]), yn + int(moves[nxt_mv-1][1]), zn + int(moves[nxt_mv-1][2]) ])
              
              #print(thislst)

              dic[(xn,yn,zn)] = thislst

  def bfs():
      cost=0
      queue1=[]
      pathfound=0
      queue1.append((x,y,z))
      visited=set()
      visited.add((x,y,z))
      Parentmap={

      # visited={ (x,y,z) : True
      (x,y,z):None
      }
      # Path avail is false when there is no path
      pathisavail = False
      # Loop till there are vales in queue1

      while len(queue1)!=0:
          if trg==1:
              break
          current_node=queue1.pop(0)
          
          if         current_node == (dx,dy,dz):
              
              pathisavail=True
              
              break

          
          
          for child in dic[current_node]:
              child= tuple(child)
              
              
              
              
              if child not in visited:
                  
                  queue1.append(child)
                  Parentmap[child]=current_node
                  
                  visited.add(child)

          
      # Parentmap[(x,y,z)]=None
      
      pathtrace=[]
      i=0 
      tracknode= (dx,dy,dz)
      #This is not working
      k=0
      costing1=0
      # print(visited)
      
      if pathisavail:
          
          
          pathtrace.append((dx,dy,dz))
          while Parentmap[tracknode] is not None:

              
              pathtrace.insert(0,Parentmap[tracknode])
              tracknode= Parentmap[tracknode]

              # cost=cost+1
              # if k==0:
              #     costing1=0
              # else:
              #     if ((pathtrace[k-1][0]!=pathtrace[k][0] and pathtrace[k-1][1]!=pathtrace[k][1]) or (pathtrace[k-1][1]!=pathtrace[k][1] and pathtrace[k-1][2]!=pathtrace[k][2]) or (pathtrace[k-1][0]!=pathtrace[k][0] and pathtrace[k-1][2]!=pathtrace[k][2]) ):
              #         costing1=1
              #     else:
              #         costing1=1
              # k=k+1
          # pathtrace.reverse()
      
      '''if len(pathtrace) ==0:
          print("FAIL")
      else:
          print(cost)
          print(k)
          print(pathtrace)'''
      #Outputing the path with their cost
      outfile = open("output.txt", "w+")
      if(len(pathtrace)==0 or trg==1):
          #print('FAIL')
          outfile.write("FAIL")
          outfile.close()
      else:
          outfile.write(str(len(pathtrace)-1))
          outfile.write("\n")
          outfile.write(str(len(pathtrace)))
          outfile.write("\n")
          #print(best_dis)
          #print(best_dis+1)
          strf=''
          previousi= pathtrace[0]
          costing1 = 0
          strf+=str(x)+" "+str(y)+" "+str(z)+" 0\n"
          for i in pathtrace[1:]:
              strf+=str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str("1")
              # if i!=previousi:
              #     if ((previousi[0]!=i[0] and previousi[1]!=i[1]) or (previousi[1]!=i[1] and previousi[2]!=i[2]) or (previousi[0]!=i[0] and previousi[2]!=i[2]) ):
              #         costing1=1
              #     else:
              #         costing1=1
              # k=k+1
              
              # strf+=str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str(costing1)
              
              strf+="\n"
              # previousi = i
          outfile.write(strf.rstrip())
          outfile.close()
  bfs()



def start_ucs():
  def valid(x,y,z,ex,ey,ez):
      if(x<0 or x>ex or y<0 or y>ey or z<0 or z>ez):
          trg=1
          outfile = open("output.txt", "w+")
          outfile.write("FAIL")
          outfile.close()
          return False
      return True
  #Possible moves with its cost for priority queue
  moves={}
  moves[0]=(1,0,0,10)
  moves[1]=(-1,0,0,10)
  moves[2]=(0,1,0,10)
  moves[3]=(0,-1,0,10)
  moves[4]=(0,0,1,10)
  moves[5]=(0,0,-1,10)
  moves[6]=(1,1,0,14)
  moves[7]=(1,-1,0,14)
  moves[8]=(-1,1,0,14)
  moves[9]=(-1,-1,0,14)
  moves[10]=(1,0,1,14)
  moves[11]=(1,0,-1,14)
  moves[12]=(-1,0,1,14)
  moves[13]=(-1,0,-1,14)
  moves[14]=(0,1,1,14)
  moves[15]=(0,1,-1,14)
  moves[16]=(0,-1,1,14)
  moves[17]=(0,-1,-1,14)
  
  with open ("input.txt","r") as file:
      alg=file.readline().strip()
      ex,ey,ez=list(map(int,file.readline().strip().split()))
      x,y,z=list(map(int,file.readline().strip().split()))
      dx,dy,dz=list(map(int,file.readline().strip().split()))
      # visited1=[[[0 for i in range(ez)]for j in range(ey)]for z in range(ex)]
      n=int(file.readline().strip())
      dic={}
      thislst=[]
      # Getting x,y and z coordinates and their moves and adding the cost in thislst
      for _ in range(n):
          #print(file.readline().strip().split())
          thislst=[]
          line_items = list(map(int, file.readline().strip().split()))
          #print(line_items)
          '''print(xn)
          print(yn)
          print(zn)'''
          xn = line_items.pop(0)
          #print(line_items)
          yn = line_items.pop(0)
          #print(line_items)
          zn = line_items.pop(0)
          #print(line_items)
          #m=len(line_items)
          #print(m)
          for nxt_mv in line_items:
              #print(nxt_mv)
              #moves are not getting added corretly
              ##print(moves[nxt_mv-1][0])
              ##print(moves[nxt_mv-1][1])
              ##print(moves[nxt_mv-1][2])
              
              a=moves.keys()
              d=list(a)
              #print(d)
              #b=moves.keys()
              #c=moves.keys()
              
              if valid(xn + moves[nxt_mv-1][0],yn + moves[nxt_mv-1][1],zn + moves[nxt_mv-1][2],ex,ey,ez):  
                  thislst.append( ((xn + int(moves[nxt_mv-1][0]), yn + int(moves[nxt_mv-1][1]), zn + int(moves[nxt_mv-1][2])), int(moves[nxt_mv-1][3])))
              
              #print(thislst)

              dic[(xn,yn,zn)] = thislst




  from queue import PriorityQueue
  def ucs1():
      myQueue = PriorityQueue()
      queue1=[]
      pathfound=0
      queue1.append((0,(x,y,z)))
      visited=set()
      visited.add((x,y,z))
      Costmap={
          (x,y,z):0
      }
      Parentmap={

      # visited={ (x,y,z) : True
      (x,y,z):None
      }
      pathisavail = False
      costtrace=[]
      # Loop till not empty
      while len(queue1)!=0:
          cost,current_node=queue1.pop(0)
          
          if         current_node == (dx,dy,dz):
              
              pathisavail=True
              break

          
          
          for child, current_cost in dic[current_node]:
              child= tuple(child)
              
              #This is not working and parent map is not printing
              
              
              if child not in visited:
                  
                  queue1.append((current_cost+cost,child))
                  Parentmap[child]=(current_node)
                  Costmap[child]=(current_cost)
                  visited.add(child)

          
      # Parentmap[(x,y,z)]=None
      
      pathtrace=[]

      i=0 
      tracknode= (dx,dy,dz)
      #This is not working
      k=0
      costing1=0
      # print(visited)
      
      if pathisavail:
          
          
          pathtrace.append((dx,dy,dz))
          
          while Parentmap[tracknode] is not None:

              
              pathtrace.insert(0,Parentmap[tracknode])
              costtrace.insert(0,Costmap[tracknode])
              tracknode= Parentmap[tracknode]

              # cost=cost+1
              # if k==0:
              #     costing1=0
              # else:
              #     if ((pathtrace[k-1][0]!=pathtrace[k][0] and pathtrace[k-1][1]!=pathtrace[k][1]) or (pathtrace[k-1][1]!=pathtrace[k][1] and pathtrace[k-1][2]!=pathtrace[k][2]) or (pathtrace[k-1][0]!=pathtrace[k][0] and pathtrace[k-1][2]!=pathtrace[k][2]) ):
              #         costing1=1
              #     else:
              #         costing1=1
              # k=k+1
          # pathtrace.reverse()
      
      '''if len(pathtrace) ==0:
          print("FAIL")
      else:
          print(cost)
          print(k)
          print(pathtrace)'''

      outfile = open("output.txt", "w+")
      if(len(pathtrace)==0 or trg==1):
          #print('FAIL')
          outfile.write("FAIL")
          outfile.close()
      else:
          outfile.write(str(cost))
          outfile.write("\n")
          outfile.write(str(len(pathtrace)))
          outfile.write("\n")
          #print(best_dis)
          #print(best_dis+1)

          '''mx,my,mz=dx,dy,dz
          ans=[]
          while((mx,my,mz)!=(x,y,z)):
              ans.append([mx,my,mz,1])
              nxt=pathtrace
              mx,my,mz=nxt[0],nxt[1],nxt[2]
          ans.append([x,y,z,0])
          ans=ans[::-1]'''
          strf=''
          previousi= pathtrace[0]
          costing1 = 0
          strf+=str(x)+" "+str(y)+" "+str(z)+" 0\n"
          for i in range(1,len(pathtrace)):
              strf+=str(pathtrace[i][0])+" "+str(pathtrace[i][1])+" "+str(pathtrace[i][2])+" "+str(costtrace[i-1])
              # if i!=previousi:
              #     if ((previousi[0]!=i[0] and previousi[1]!=i[1]) or (previousi[1]!=i[1] and previousi[2]!=i[2]) or (previousi[0]!=i[0] and previousi[2]!=i[2]) ):
              #         costing1=1
              #     else:
              #         costing1=1
              # k=k+1
              
              # strf+=str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str(costing1)
              
              strf+="\n"
              # previousi = i
          outfile.write(strf.rstrip())
          outfile.close()
  ucs1()

with open ("input.txt","r") as file:
  alg=file.readline().strip()
  if alg == "UCS":
    start_ucs()
  elif alg == "A*":
    start_astar()
  elif alg == "BFS":
    start_bfs()