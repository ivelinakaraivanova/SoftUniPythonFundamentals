population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

is_not_possible = False
for i, p in enumerate(population):
    if p < minimum_wealth:
        maxi = max(population)
        distribution = minimum_wealth - p
        if maxi - distribution >= minimum_wealth:
            population[population.index(maxi)] -= distribution
            population[i] += distribution
        else:
            print("No equal distribution possible")
            is_not_possible = True
            break

if not is_not_possible:
    print(population)