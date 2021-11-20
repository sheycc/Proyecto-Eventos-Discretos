from airport_sim import sim

if __name__ == "__main__":
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~> Please enter simulation time(seconds).')
    t = int(input('~~> Simulaton time = ')) # 10080(1 week)
    A, D = sim(t, rnd=True)

    result = {}
    for i in range(5):
        c = 0
        a = A[i]
        d = D[i]
        for j in range(1, len(A[i])):
            c += a[j] - d[j - 1]
        c += a[0]
        result[i] = c

    print('~~> Results:')
    print('############################################')
    for i, j in result.items():
        print(f"# Landingtrack {i + 1} - Time: {j}")
    print('###########################################')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')