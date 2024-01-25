
def paper_info(paper,k):
    x_start, y_start, length, height = map(int,input().split())
    for i in range(length):
        for j in range(height):
            paper[(x_start+i)*1001+y_start+j] = k
            
    return paper

def paper_count(paper,k):
    count = 0
    for i in range(1001):
        for j in range(1001):
            if paper[1001*i+j] == k:
                count += 1
    return count   

def main():
    # 1001*1001 판을 만든다.
    paper = [-1 for i in range(1001*1001)]
    
    # 색종이 수를 입력받고 색종이 정보를 입력한다.
    number = int(input())
    for i in range(number):
        paper = paper_info(paper,i)

    #종이 면적 카운트
    for i in  range(number):
        print(paper_count(paper,i))


if __name__ == "__main__":
    main()