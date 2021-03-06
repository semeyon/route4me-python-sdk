from route4me import Route4Me

KEY = "11111111111111111111111111111111"


def main():
    route4me = Route4Me(KEY)
    optimization = route4me.optimization
    response = optimization.get_optimizations(limit=10, Offset=5)
    if hasattr(response, 'errors'):
        print('. '.join(response.errors))
    else:
        optimizations = response.optimizations
        optimization_problem_id = optimizations[0].optimization_problem_id
        response = optimization.get_optimization(
            optimization_problem_id=optimization_problem_id)
        if hasattr(response, 'errors'):
            print('. '.join(response.errors))
        else:
            optimization_problem_id = response.optimization_problem_id
            print('\tOptimization ID: {}'.format(optimization_problem_id))


if __name__ == '__main__':
    main()
