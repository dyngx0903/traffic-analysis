from math import floor
from numpy import mean, std, percentile

def data_analyzing(trafficData):
    time_labels = [f"{hour}:00 - {hour + 1}:00" for hour in range(6, 21)]
    outputStr = "ANALYSIS\n\n"
    name = ['Car', 'Giant', 'Motor']

    # Count total vehicles for each type and overall
    vehicle_totals = [sum(vehicle_counts) for vehicle_counts in trafficData]
    total_vehicles = sum(vehicle_totals)

    # Calculate total traffic per interval
    total_traffic = [sum(x) for x in zip(*trafficData)]

    # Statistical metrics
    meanVal = floor(mean(total_traffic))
    stdVal = floor(std(total_traffic))

    # Categorize time intervals
    p10 = percentile(total_traffic, 10)  # Low traffic threshold
    p75 = percentile(total_traffic, 75)  # High traffic threshold
    p90 = percentile(total_traffic, 90)  # Rush hour threshold

    rush_hours = [
        time_labels[i]
        for i, count in enumerate(total_traffic)
        if count >= p90
    ]
    high_traffic_hours = [
        time_labels[i]
        for i, count in enumerate(total_traffic)
        if p75 <= count < p90
    ]
    low_traffic_hours = [
        time_labels[i]
        for i, count in enumerate(total_traffic)
        if count < p10
    ]

    # Convert lists to strings
    rush_hours_str = ", ".join(rush_hours)
    high_traffic_hours_str = ", ".join(high_traffic_hours)
    low_traffic_hours_str = ", ".join(low_traffic_hours)

    # Build output string
    outputStr += f"Total Vehicles Counted: {total_vehicles}\n"
    outputStr += f"Mean: {meanVal}\n"
    outputStr += f"Standard Deviation: {stdVal}\n\n"

    # Add vehicle totals
    for i, count in enumerate(vehicle_totals):
        outputStr += f"{name[i]}s Counted: {count}\n"

    outputStr += f"\nRush Hours: \n{rush_hours_str}\n"
    outputStr += f"High Traffic Hours: \n{high_traffic_hours_str}\n"
    outputStr += f"Low Traffic Hours: \n{low_traffic_hours_str}"

    return outputStr
