## Search Algorithm

탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 알고리즘

그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 자주 다룬다.

대표적인 탐색 알고리즘으로는 `DFS / BFS가` 있다.

<br>

### 자료구조

자료구조란 '데이터를 표현하고 관리하고 처리하기 위한 구조'

**Stack**
* Last In First Out(후입 선출)의 특징을 가지고 있는 자료구조
* 파이썬에서는 기존 리스트에서 `append()`와 `pop()` 메소드를 이용해서 스택 자료구조와 동일하게 작동시킬 수 있다.

**Queue**
* First In First Out(선입선출)의 특징을 가지고 있는 자료구조
* 파이썬에서 큐를 구현할 때는 collection 모듈에서 제공하는 deque 자료구조를 활용할 수 있다.

**Graph**
* Node와 Edge로 표현되는 자료구조
* 두 Node가 Edge로 연결되어 있을 때 '인접하다'라고 표현한다.
* 그래프는 인접 행렬 방식과 인접 리스트 방식으로 표현할 수 있다.
* 인접 행렬 방식 : 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식. <br>
  모든 관계를 저장하므로 노드 개수가 많을수록 메모리 사용이 많아짐. <br>
  특정 노드의 연결 정보를 조회하는 속도는 빠름
* 인접 리스트 방식 : 리스트로 그래프의 연결 관계를 표현하는 방식 <br>
  연결된 관계만을 저장하기 때문에 메모리 효율이 좋다. <br>
  특정 노드의 연결 정보를 확인하기 위해서는 순차적으로 확인해야함.



<br>

### 재귀함수
* 자기 자신을 다시 호출하는 함수이다.
* 수학 시간에 언급되는 개념인 프랙털 구조와 유사하다. 프랙털 이미지를 출력하는 프로그램을 작성할 때도 <br>
  재귀 함수가 사용된다.
* 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 사용한다.
* 연속해서 호출되는 함수는 메인 메모리의 스택 공간에 적재되는 원리

<br>

### DFS
* Depth-First Search, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
* 동작 과정 
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
  2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
  3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
* 데이터의 개수가 N개인 경우 O(N)의 시간 복잡도를 갖는다.

### BFS
* Breadth First Search, 그래프에서 가까운 노드부터 탐색하는 알고리즘
* 동작과정 
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
  2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
  3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
* 데이터의 개수가 N개인 경우 O(N)의 시간 복잡도를 갖는다.
* 일반적인 경우 실제 수행 시간은 DFS보다 좋은 편이다.
