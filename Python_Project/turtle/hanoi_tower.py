"""
하노이의 탑 문제를 풀기 위해서는 재귀적인 방법으로 풀 수 있습니다.



일반적으로 사용하는 용어에 관해 정의하겠습니다.



T(N, Beg, Aux, End)

T: 풀이 절차의 단계를 나타내는 수

N: 원판의 수

Beg: 시작 기둥

Aux: 임시 기둥

End: 목표 기둥



풀이 절차

1. T(N-1, Beg, End, Aux)

2. T(1, Beg, Aux, End)

3. T(N-1, Aux, Beg, End)



1단계에서는 가장 위의 (N-1) 원판을 시작 기둥에서 임시 기둥으로 옮깁니다.



2단계에서는 1 원판을 시작 기둥에서 목표 기둥으로 옮깁니다.



3단계에서는 가장 위의 (N-1) 원판을 임시 기둥에서 목표 기둥으로 옮깁니다.



N이 1일 때는 Beg에서 End로 원판을 옮깁니다.



하노이의 탑 가장 쉬운 문제인 원판 세 개 부터 시작합시다.



N = 3 이므로



T(3, A, B, C)



부터 시작합니다(시작 기둥: A, 임시 기둥: B, 목표 기둥: C).



재귀적 문제 풀이 방법인 아래의 풀이 절차를 따라가겠습니다.



1단계: T(N-1, Beg, End, Aux)

2단계: T(1, Beg, Aux, End)

3단계: T(N-1, Aux, Beg, End)



T(3, A, B, C)



N = 3

Beg = A

Aux = B

End = C

이므로



1단계 T(N-1, Beg, End, Aux)에 T(3, A, B, C)를 적용하면,

T(2, A, C, B)를 얻습니다.



2단계 T(1, Beg, Aux, End)에 T(3, A, B, C)를 적용하면,

T(1, A, B, C)를 얻습니다. 이는 A에서 C로 옮겨라는 의미입니다(A -> C).



3단계 T(N-1, Aux, Beg, End)에 다시 T(3, A, B, C)를 적용하면

T(2, B, A, C)를 얻습니다.



1단계에서 얻은 T(2, A, C, B)에서 다시 위 1, 2, 3단계를 적용합니다.

1단계 T(N-1, Beg, End, Aux)에 T(2, A, C, B)를 적용하면,

T(1, A, B, C)를 얻습니다. 이는 A에서 C로 옮겨라는 의미입니다(A -> B).



2단계 T(1, Beg, Aux, End)에 T(2, A, C, B)를 적용하면,

T(1, A, C, B)를 얻습니다. 이는 A에서 B로 옮겨라는 의미입니다(A -> B).



3단계 T(N-1, Aux, Beg, End)에 T(2, A, C, B)를 적용하면,

T(1, C, A, B)를 얻습니다. 이는 C를 B로 옮겨라는 의미입니다(C -> B).



가장 처음에 얻은 2단계에서 N = 1이므로 건너뜁니다.



가장 처음 3단계에서 얻은 결과인 T(2, B, A, C)로 다시 갑니다.



1단계 T(N-1, Beg, End, Aux)에 T(2, B, A, C)를 적용하면,

T(1, B, C, A)를 얻습니다. 이는 B를 A로 옮겨라는 의미입니다.



2단계 T(1, Beg, Aux, End)에 T(2, B, A, C)를 적용하면,

T(1, B, A, C)를 얻습니다. 이는 B를 C로 옮겨라는 의미입니다(B -> C).



3단계 T(N-1, Aux, Beg, End)에 T(2, B, A, C)를 적용하면,

T(1, A, B, C)를 얻습니다. 이는 A를 C로 옮겨라는 의미입니다(A -> C).



출처: https://woongheelee.com/entry/하노이-타워-알고리즘 [노트정리]

"""

def T(N, Beg, Aux, End):
    if N == 1:
        print(Beg, '->', End)
    else:
        T(N-1, Beg, End, Aux)
        T(1, Beg, Aux, End)
        T(N-1, Aux, Beg, End)
#print(T(3, 'A', 'B', 'C'))
#print(T(7, 'A', 'B', 'C'))