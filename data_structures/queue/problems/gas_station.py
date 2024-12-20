from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    num_of_gas_stations = len(gas)

    # if we only have one gas station
    if num_of_gas_stations == 1:
        # check if the gas station has gas more than or equal to cost of that gas station.
        # if not we cannot reach that gas station.
        if gas[0] < cost[0]:
            return -1
        else:
            return 0

    start, end = 0, 1

    curr_gas = gas[start] - cost[start]
    while start != end or curr_gas < 0:
        while curr_gas < 0:
            curr_gas = curr_gas - (gas[start] - cost[start])
            start = (start + 1) % num_of_gas_stations

            if start == 0:
                return -1
        curr_gas = curr_gas + (gas[end] - cost[end])
        end = (end + 1) % num_of_gas_stations
    return start


def main():
    # gas = [1, 2, 3, 4, 5]
    # cost = [3, 4, 5, 1, 2]

    # or curr_gas < 0
    # gas = [2, 3, 4]
    # cost = [3, 4, 3]

    gas = [1, 2, 3, 4, 5, 5, 70]
    cost = [2, 3, 4, 3, 9, 6, 2]
    i = can_complete_circuit(gas, cost)
    print(i)


if __name__ == "__main__":
    main()
