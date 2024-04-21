"""  
Input:
3
3 5
4 9
5 8
Output:
2


Input:
3
1 1000
2 3
5 6
Output:
2
"""

movies_qty = int(input())
movies = []
count = 0

for _ in range(movies_qty):
    start, finish = map(int, input().split())
    movies.append((start, finish))

sorted_movies = sorted(movies, key=lambda x: x[1])
cursor_finish_time = 0

for movie in sorted_movies:
    movie_start = movie[0]
    movie_end = movie[1]

    if movie_start >= cursor_finish_time:
        cursor_finish_time = movie_end
        count += 1

print(count)