def calculate_route_risk(stops, distance_miles, driver_hours_remaining):

    risk_score = 0

    # Stop count risk
    if stops > 8:
        risk_score += 3
    elif stops > 5:
        risk_score += 2
    else:
        risk_score += 1

    # Distance risk
    if distance_miles > 400:
        risk_score += 3
    elif distance_miles > 250:
        risk_score += 2
    else:
        risk_score += 1

    # Driver hours risk
    if driver_hours_remaining < 3:
        risk_score += 3
    elif driver_hours_remaining < 6:
        risk_score += 2
    else:
        risk_score += 1

    if risk_score >= 7:
        risk = "HIGH"
    elif risk_score >= 5:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return risk


# Example simulation
route = calculate_route_risk(
    stops=9,
    distance_miles=320,
    driver_hours_remaining=4
)

print("Route Risk Level:", route)
